const contacts = (state = [], action) => {
    switch(action.type) {
        // case 'BEGIN_FETCHING_CONTACTS':
        //     return {
        //         ...state,
        //         [action.payload.userId]: {
        //             isFetching: true,
        //             data: []
        //         }
        //     }

        // case 'FINISH_FETCHING_CONTACTS':
        //     return {
        //         ...state,
        //         [action.payload.userId]: {
        //             isFetching: false,
        //             data: action.payload.data
        //     }

        case 'SET_CONTACTS':
            return action.payload.contacts // next state

        default:
            return state
    }
}

export default contacts