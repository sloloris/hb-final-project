// defines 'action creators', or what reducers listen to
var userIdSpan = document.getElementById('user-id');
var userId = userIdSpan.getAttribute('value');


export const setCurrentView = (index) => ({
    type: 'SET_CURRENT_VIEW',
    payload: {
        index: index
    }
})

export const beginFetchingContacts = (userId) => ({
    type: 'BEGIN_FETCHING_CONTACTS',
    payload: {
        userId: user_id
    }
})

export const finishFetchingContacts = (userId) => ({
    type: 'FINISH_FETCHING_CONTACTS',
    payload: {
        userId: user_id
    }
})