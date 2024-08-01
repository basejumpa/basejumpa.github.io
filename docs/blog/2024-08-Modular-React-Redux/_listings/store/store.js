
import { configureStore } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';
import logger from 'redux-logger';
import { createReducerManager } from './reducerManager';

const initialReducers = {};

const reducerManager = createReducerManager(initialReducers);

const store = configureStore({
  reducer: reducerManager.reduce,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(thunk, logger),
});

store.reducerManager = reducerManager;

export default store;
