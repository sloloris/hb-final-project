// exports all reducers for store creation in app.js

import { combineReducers } from 'redux'
import currentView from './currentView'
import contacts from './contacts'

const contactManager = combineReducers({
    currentView,
    contacts
})

export default contactManager