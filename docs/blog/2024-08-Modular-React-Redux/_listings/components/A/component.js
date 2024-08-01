
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { incrementA } from './slice';

const ComponentA = () => {
  const valueA = useSelector(state => state.componentA.valueA);
  const dispatch = useDispatch();

  const incrementValueA = () => dispatch(incrementA());

  return (
    <button onClick={incrementValueA}>
      Increment Value A: {valueA}
    </button>
  );
};

export default ComponentA;
