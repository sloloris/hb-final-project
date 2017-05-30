const messages = (state = [], action) => {
    switch(action.type) {

        case 'DISPLAY_MESSAGES':
            return action.payload.messages 

        default:
            return state
    }
}

export default messages