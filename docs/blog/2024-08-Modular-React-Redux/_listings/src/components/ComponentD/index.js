import React from 'react';
import { useDispatch } from 'react-redux';
import { resetA } from '../ComponentA/slice';
import { resetB } from '../ComponentB/slice';

const ComponentD = () => {
  const dispatch = useDispatch();

  const resetValues = () => {
    dispatch(resetA());
    dispatch(resetB());
  };

  return (
    <button onClick={resetValues}>
      Reset Values
    </button>
  );
};

export default ComponentD;
