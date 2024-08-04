import React from 'react';
import { useSelector } from 'react-redux';

const ComponentC = () => {
  const valueA = useSelector(state => state.ComponentA.valueA);
  const valueB = useSelector(state => state.ComponentB.valueB);

  return (
    <div>
      Sum of Values: {valueA + valueB}
    </div>
  );
};

export default ComponentC;
