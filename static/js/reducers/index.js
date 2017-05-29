// exports all reducers for store creation in app.js

import { combineReducers } from 'redux'
import currentView from './currentView'

const contactManager = combineReducers({
    currentView
})

export default contactManager