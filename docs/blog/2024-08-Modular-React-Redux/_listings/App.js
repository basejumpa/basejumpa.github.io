
import React from 'react';
import { Provider } from 'react-redux';
import store from './store/store';
import ComponentA from './components/A/component';
import ComponentB from './components/B/component';
import ComponentC from './components/C/component';
import ComponentD from './components/D/component';

const registerReducer = (key, reducer) => {
  store.reducerManager.add(key, reducer);
  store.replaceReducer(store.reducerManager.reduce);
};

export { registerReducer };

const App = () => {
  return (
    <Provider store={store}>
      <div>
        <ComponentA />
        <ComponentB />
        <ComponentC />
        <ComponentD />
      </div>
    </Provider>
  );
};

export default App;
