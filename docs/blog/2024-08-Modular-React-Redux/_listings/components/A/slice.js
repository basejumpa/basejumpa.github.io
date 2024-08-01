
import { createSlice } from '@reduxjs/toolkit';
import { registerReducer } from '../../App';

const initialState = {
  valueA: 19,
};

const componentASlice = createSlice({
  name: 'componentA',
  initialState,
  reducers: {
    incrementA(state) {
      state.valueA += 1;
    },
    resetA(state) {
      state.valueA = initialState.valueA;
    },
  },
});

export const { incrementA, resetA } = componentASlice.actions;

// Register the reducer when this module is loaded
registerReducer('componentA', componentASlice.reducer);

export default componentASlice.reducer;
