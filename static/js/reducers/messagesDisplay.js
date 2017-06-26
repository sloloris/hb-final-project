const messages = (state = [], action) => {
    switch(action.type) {

        case 'DISPLAY_MESSAGES':
            return action.payload.messages 

        case 'ADD_MESSAGE':
            // create new array so react recognizes changes to state
            state.push(action.payload.msg)
            var newState = Array.from(state)
            return newState
            // return state

        default:
            return state
    }
}

export default messages