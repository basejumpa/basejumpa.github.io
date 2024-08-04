import { createSlice } from '@reduxjs/toolkit';
import { registerReducer } from '../../store';

const initialState = {
  valueB: 76,
};

const componentBSlice = createSlice({
  name: 'ComponentB',
  initialState,
  reducers: {
    incrementB(state, action) {
      state.valueB += action.payload;
    },
    resetB(state) {
      state.valueB = initialState.valueB;
    },
  },
});

export const { incrementB, resetB } = componentBSlice.actions;

// Register the reducer when this module is loaded
registerReducer('ComponentB', componentBSlice.reducer);

export default componentBSlice.reducer;
