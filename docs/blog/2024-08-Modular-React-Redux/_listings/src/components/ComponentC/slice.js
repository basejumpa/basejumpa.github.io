import { createSlice } from '@reduxjs/toolkit';
import { registerReducer } from '../../store';

const initialState = {};

const componentCSlice = createSlice({
  name: 'componentC',
  initialState,
  reducers: {},
});

registerReducer('componentC', componentCSlice.reducer);

export default componentCSlice.reducer;
