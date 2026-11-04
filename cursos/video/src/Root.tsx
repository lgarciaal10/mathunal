import React from 'react';
import {Composition} from 'remotion';
import {Cadena, DURACION, FPS} from './Cadena';
export const Root: React.FC = () => (
  <>
    <Composition id="cadena-vertical" component={Cadena} durationInFrames={DURACION} fps={FPS} width={1080} height={1920} defaultProps={{formato:'vertical'}} />
    <Composition id="cadena-horizontal" component={Cadena} durationInFrames={DURACION} fps={FPS} width={1920} height={1080} defaultProps={{formato:'horizontal'}} />
  </>
);
