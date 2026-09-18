-- ═══════════════════════════════════════════════════════════════════════════
-- MathUNAL · Simulacros Pro — esquema de Supabase
-- Rama simulacros-pro. NO APLICADO todavía. Luis lo corre en el proyecto
-- goxhxrdchfyphkenixng cuando decida abrir el pago.
--
-- Diseño anti-piratería:
--   · sim_entitlements  → quién compró qué, por cuánto tiempo (RLS: cada quien
--                          ve SOLO sus filas). Es la fuente de verdad de "es Pro".
--   · sim_purchases     → registro de cada compra (Wompi / manual).
--   · sim_solutions     → el CONTENIDO Pro (pasos, antibobo, widget) que NO
--                          puede vivir en index.html. RLS: solo lo devuelve a
--                          usuarios con un entitlement vigente de esa materia.
--   · sim_real_grades   → notas reales post-parcial, para calibrar la predicción
--                          (anónimas para el modelo agregado; el usuario también
--                          las tiene en localStorage).
--
-- Los ENUNCIADOS y OPCIONES siguen en index.html: son "capa gratis" y los
-- parciales viejos circulan igual. Lo que se vende es la solución trabajada +
-- el análisis por-usuario, que es lo difícil de copiar.
-- ═══════════════════════════════════════════════════════════════════════════

-- ── 1. Entitlements ──────────────────────────────────────────────────────────
create table if not exists public.sim_entitlements (
  id            bigint generated always as identity primary key,
  user_id       uuid not null references auth.users(id) on delete cascade,
  product_id    text not null,                    -- 'calcdif_pro' | 'calcdif_c2' ...
  course_id     text not null default '1000004',  -- código de materia
  exam_period_id text,                            -- '2026-2' (null = permanente)
  valid_until   timestamptz,                      -- null = sin vencimiento
  source        text default 'wompi',             -- 'wompi' | 'manual' | 'promo'
  created_at    timestamptz not null default now(),
  unique (user_id, product_id, exam_period_id)
);
create index if not exists sim_entitlements_user on public.sim_entitlements(user_id);

alter table public.sim_entitlements enable row level security;
-- cada usuario ve/gestiona SOLO sus entitlements; la escritura real la hace el
-- backend de pago con service_role (que ignora RLS).
create policy sim_ent_select_own on public.sim_entitlements
  for select using (auth.uid() = user_id);
revoke all on public.sim_entitlements from anon;

-- helper: ¿tiene el usuario actual un entitlement vigente para una materia?
create or replace function public.sim_has_pro(p_course text default '1000004')
returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.sim_entitlements e
    where e.user_id = auth.uid()
      and (e.course_id = p_course or e.product_id = 'all_pro')
      and (e.valid_until is null or e.valid_until > now())
  );
$$;
grant execute on function public.sim_has_pro(text) to authenticated;

-- ── 2. Compras (registro) ────────────────────────────────────────────────────
create table if not exists public.sim_purchases (
  id           bigint generated always as identity primary key,
  user_id      uuid references auth.users(id) on delete set null,
  product_id   text not null,
  amount_cop   integer,
  wompi_ref    text,
  status       text default 'pending',   -- pending | approved | declined
  raw          jsonb,
  created_at   timestamptz not null default now()
);
alter table public.sim_purchases enable row level security;
create policy sim_pur_select_own on public.sim_purchases
  for select using (auth.uid() = user_id);
revoke all on public.sim_purchases from anon;

-- ── 3. Contenido Pro: soluciones ─────────────────────────────────────────────
-- src = el mismo _src del cliente ('calcdif_p2_2', 'cd_c2_01', ...)
create table if not exists public.sim_solutions (
  src        text primary key,
  course_id  text not null default '1000004',
  corte      smallint,
  tema       text,
  body       jsonb not null,   -- { concepto, quePregunta, pasos[], resultado,
                               --   errorComun, comoReconocer, antibobo, rubrica[],
                               --   compruebalo }
  updated_at timestamptz not null default now()
);
alter table public.sim_solutions enable row level security;
-- SOLO usuarios con Pro vigente de esa materia pueden leer las soluciones.
create policy sim_sol_select_pro on public.sim_solutions
  for select to authenticated
  using ( public.sim_has_pro(course_id) );
revoke all on public.sim_solutions from anon;

-- ── 4. Notas reales post-parcial (para calibrar la predicción) ───────────────
create table if not exists public.sim_real_grades (
  id         bigint generated always as identity primary key,
  user_id    uuid references auth.users(id) on delete set null,
  course_id  text not null default '1000004',
  corte      smallint,
  sim_score  smallint,   -- preparación /100 al momento
  real_nota  numeric(2,1),
  created_at timestamptz not null default now()
);
alter table public.sim_real_grades enable row level security;
create policy sim_rg_insert_own on public.sim_real_grades
  for insert to authenticated with check (auth.uid() = user_id);
create policy sim_rg_select_own on public.sim_real_grades
  for select using (auth.uid() = user_id);
revoke all on public.sim_real_grades from anon;

-- vista agregada (para el modelo de calibración global; sin datos personales)
create or replace view public.sim_calib_agg as
  select course_id, corte,
         count(*) n,
         regr_slope(real_nota, sim_score/20.0)  as a,
         regr_intercept(real_nota, sim_score/20.0) as b,
         stddev_pop(real_nota) as sd
  from public.sim_real_grades
  where sim_score is not null and real_nota is not null
  group by course_id, corte
  having count(*) >= 15;
revoke all on public.sim_calib_agg from anon, authenticated;

-- ═══════════════════════════════════════════════════════════════════════════
-- Para poblar sim_solutions: exportar SIM_SOL + los pasos/antibobo de cada
-- pregunta de sim-calcdif.js a filas {src, body}. Script aparte cuando se
-- decida migrar (hoy el contenido sigue inline para el piloto gratis).
-- ═══════════════════════════════════════════════════════════════════════════
