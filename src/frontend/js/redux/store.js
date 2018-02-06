import Raven from 'raven-js';
import { createStore, applyMiddleware, compose } from 'redux';
import { persistCombineReducers, purgeStoredState } from 'redux-persist';
import createRavenMiddleware from 'raven-for-redux';
import storage from 'redux-persist/es/storage'; // default: localStorage if web, AsyncStorage if react-native
import Urls from 'util/urls';

/* eslint-disable no-underscore-dangle */
const buildStore = (key, reducers, initialState, client) => {
  const persistConfig = {
    key,
    storage,
    blacklist: ['ui', 'matchState'],
  };
  if (Urls.getParameterByName('purge')) {
    purgeStoredState(persistConfig);
  }
  const persistedReducers = persistCombineReducers(persistConfig, {
    ...reducers,
    apollo: client.reducer(),
  });
  return createStore(
    persistedReducers,
    initialState,
    compose(
      applyMiddleware(
        client.middleware(),
        createRavenMiddleware(Raven, {
          stateTransformer: state => ({
            ui: state.ui,
          }),
        }),
      ),
      typeof window.__REDUX_DEVTOOLS_EXTENSION__ !== 'undefined'
        ? window.__REDUX_DEVTOOLS_EXTENSION__()
        : f => f,
    ),
  );
};

/* eslint-enable no-underscore-dangle */
module.exports = buildStore;
