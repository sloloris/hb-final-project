import React from 'react'
import ReactDOM from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import thunkMiddleware from 'redux-thunk' // ajax library
import { Provider } from 'react-redux'
import reducer from './js/reducers'
import Home from './js/components/Home'


// create store
const store = createStore(
    reducer,
    applyMiddleware(
        thunkMiddleware,
    )
)

const rootElement = document.getElementById('root')

const render = () => {
    ReactDOM.render(
        <Provider store={store}>
            <Home />
        </Provider>,
        rootElement
    )
}

render()
store.subscribe(render) // connects store to elements in render
