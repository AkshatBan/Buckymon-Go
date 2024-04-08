
import React from 'react';

const MockReactMapGL = ({ children }) => {
  return <div data-testid="mock-map">{children}</div>;
};

const MockMarker = ({ children }) => {
  return <div data-testid="mock-marker">{children}</div>;
};


export { MockReactMapGL as Map, MockMarker as Marker };
