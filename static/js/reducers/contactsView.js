const contactsView = (state = {}, action) => {
    switch(action.type) {
        case 'BEGIN_FETCHING_CONTACTS':
            return {
                ...state,
                [action.payload.userId]: {
                    isFetching: true,
                    data: []
                }
            }

        case 'FINISH_FETCHING_CONTACTS':
            return {
                ...state,
                [action.payload.userId]: {
                    isFetching: false,
                    data: action.payload.data
            }

        default:
            return
    }
}

export default contactsView