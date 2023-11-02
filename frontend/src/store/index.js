import { cashReducer } from './cashReducer';
import { combineReducers, createStore } from 'redux';
import { costumerReducer } from './costumerReducer';

const rootReducer = combineReducers({
    cash: cashReducer, costumer: costumerReducer
})

export const store = createStore(
    rootReducer,
    + window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
    )


