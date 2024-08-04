import { createSlice } from '@reduxjs/toolkit';
import { registerReducer } from '../../store';

const initialState = {};

const componentDSlice = createSlice({
  name: 'ComponentD',
  initialState,
  reducers: {},
});

registerReducer('componentD', componentDSlice.reducer);

export default componentDSlice.reducer;
