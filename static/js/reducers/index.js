// exports all reducers for store creation in app.js

import { combineReducers } from 'redux'
import currentView from './currentView'
import contacts from './contacts'
import messages from './messagesDisplay'

const contactManager = combineReducers({
    currentView,
    contacts,
    messages
})

export default contactManager