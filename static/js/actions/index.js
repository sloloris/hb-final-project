// defines 'action creators', or what reducers listen to

import 'whatwg-fetch'
var userIdSpan = document.getElementById('user-id');
var userId = parseInt(userIdSpan.getAttribute('value'));
console.log("User", userId, "logged in.");


export const setCurrentView = (index) => ({
    type: 'SET_CURRENT_VIEW',
    payload: {
        index: index
    }
})

export const beginFetchingContacts = (userId) => ({
    type: 'BEGIN_FETCHING_CONTACTS',
    payload: {
        userId: userId
    }
})

export const finishFetchingContacts = (userId) => ({
    type: 'FINISH_FETCHING_CONTACTS',
    payload: {
        userId: userId,
        data: data
    }
})

const setContacts = (contacts) => ({
    type: 'SET_CONTACTS',
    payload: {
        contacts: contacts
    }
})

const getUserContacts = (dispatch, userId) => {
        return (dispatch) => {
        fetch(userId + 'contacts')
        .then((response) => {
            var contacts = response.json().contacts
            dispatch(setContacts(contacts))
        })
    }
}