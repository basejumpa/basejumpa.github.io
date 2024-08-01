
import { Provider } from 'react-redux';
import store from '../store/store';
import App from 'next/app';

const registerReducer = (key, reducer) => {
  store.reducerManager.add(key, reducer);
  store.replaceReducer(store.reducerManager.reduce);
};

export { registerReducer };

class MyApp extends App {
  render() {
    const { Component, pageProps } = this.props;
    return (
      <Provider store={store}>
        <Component {...pageProps} />
      </Provider>
    );
  }
}

export default MyApp;
