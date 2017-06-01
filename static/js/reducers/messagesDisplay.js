const messages = (state = [], action) => {
    switch(action.type) {

        case 'DISPLAY_MESSAGES':
            return action.payload.messages 

        case 'ADD_MESSAGE':
            state.push(action.payload.msg)
            return state

        default:
            return state
    }
}

export default messages