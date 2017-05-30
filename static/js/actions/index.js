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

export const setContacts = (contacts) => ({
    type: 'SET_CONTACTS',
    payload: {
        contacts: contacts
    }
})

export const getUserContacts = (dispatch, userId) => {
  return (dispatch) => {
    fetch('/user/' + userId + '/contacts')
    .then((resp) => resp.json())
    .then((data) => {
        var contacts = data
        dispatch(setContacts(contacts))
    })
  }
}