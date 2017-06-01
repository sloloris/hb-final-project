const messages = (state = [], action) => {
    switch(action.type) {

        case 'DISPLAY_MESSAGES':
            return action.payload.messages 

        case 'ADD_MESSAGE':
            return state.push(action.payload.msg)

        default:
            return state
    }
}

export default messages