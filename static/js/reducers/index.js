import { combineReducers } from 'redux'
import currentView from './currentView'

const contactManager = combineReducers({
    currentView
})

export default contactManager