import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { incrementB } from './slice';

const ComponentB = () => {
  const valueB = useSelector(state => state.ComponentB.valueB);
  const dispatch = useDispatch();

  const fetchValueAndUpdateB = async () => {
    const response = await fetch(`${window.location.origin.replace(/:\d+$/, '')}:8000/value`); // Use the current origin
    const data = await response.json();
    dispatch(incrementB(data.value));
  };

  return (
    <button onClick={fetchValueAndUpdateB}>
      Increment Value B: {valueB}
    </button>
  );
};

export default ComponentB;
