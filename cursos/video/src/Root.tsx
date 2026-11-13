import React from 'react';
import {Composition} from 'remotion';
import {Cadena, DURACION, FPS} from './Cadena';
import {Resuelto, DURACION as DUR_R} from './Resuelto';
import {Reel, duracion} from './Reel';
import radicales from './guiones/radicales.json';
import notables from './guiones/notables.json';
import cuadraticas from './guiones/cuadraticas.json';
const REELS: [string, any][] = [['reel-radicales', radicales], ['reel-notables', notables], ['reel-cuadraticas', cuadraticas]];
export const Root: React.FC = () => (
  <>
    <Composition id="cadena-vertical" component={Cadena} durationInFrames={DURACION} fps={FPS} width={1080} height={1920} defaultProps={{formato:'vertical'}} />
    <Composition id="cadena-horizontal" component={Cadena} durationInFrames={DURACION} fps={FPS} width={1920} height={1080} defaultProps={{formato:'horizontal'}} />
    <Composition id="resuelto-fracciones" component={Resuelto} durationInFrames={DUR_R} fps={FPS} width={1080} height={1920} />
    {REELS.map(([id, g]) => <Composition key={id} id={id} component={Reel as any} durationInFrames={duracion(g)} fps={FPS} width={1080} height={1920} defaultProps={{g}} />)}
  </>
);
