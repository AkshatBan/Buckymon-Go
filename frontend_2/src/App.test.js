import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';
import MyMap from './MyMap'
import MyMarker from './MyMarker'
import { Map } from 'react-map-gl';

jest.mock('react-map-gl');

//this tests that our map component loads, it used a mock for the react map gl
test('Map renders', () => {
  const {getByTestId} = render(<MyMap/>);
  expect(getByTestId('map')).toBeInTheDocument();
});

//This tests that the marker renders, a mock is used for the built in react map gl marker 
test('Marker renders', () => {
  const {getByTestId} = render(<MyMarker />)
  expect(getByTestId('marker')).toBeInTheDocument();
})


