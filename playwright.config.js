// Configuración de Playwright para las pruebas de MathUNAL. Ver tests/README.md.
const { defineConfig } = require('@playwright/test');

const PORT = process.env.MU_PORT || '4173';
// Se usa un host que NO sea localhost/127.0.0.1 para que el sitio no active su modo "local"
// (window.__SIM_LOCAL: panel dev, carga de *.dev.js) y se comporte como en producción.
const HOST = 'mathunal.test';

module.exports = defineConfig({
  testDir: 'tests/specs',
  timeout: 60000,
  workers: Number(process.env.MU_WORKERS || 4),
  retries: 0,
  fullyParallel: true,
  reporter: [['list']],
  use: {
    baseURL: `http://${HOST}:${PORT}`,
    viewport: { width: 1280, height: 800 },
    launchOptions: {
      args: ['--no-sandbox', `--host-resolver-rules=MAP ${HOST} 127.0.0.1`],
      ...(process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {}),
    },
  },
  webServer: {
    command: 'node tests/helpers/static-server.js',
    url: `http://127.0.0.1:${PORT}/index.html`,
    reuseExistingServer: true,
    env: { MU_PORT: PORT, MU_ROOT: process.env.MU_ROOT || '' },
  },
});
