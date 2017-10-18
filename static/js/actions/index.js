// defines 'action creators', or what reducers listen to

import 'whatwg-fetch'
var userIdSpan = document.getElementById('user-id');
export const userId = parseInt(userIdSpan.getAttribute('value'))
console.log("User", userId, "logged in.");

export const setCurrentView = (index) => ({
    type: 'SET_CURRENT_VIEW',
    payload: {
        index: index
    }
})

export const setContacts = (contacts) => ({
    type: 'SET_CONTACTS',
    payload: {
        contacts: contacts,
        userId: userId
    }
})

export const getUserContacts = (dispatch) => { 
  return (dispatch) => {
    var contacts = [
      {
        contact_id: 1,
        email: 'example1@gmail.com',
        first_name: 'Some',
        last_name: 'Person'
      },
      {
        contact_id: 2,
        email: 'example2@gmail.com',
        first_name: 'Some',
        last_name: 'OtherPerson'
      },
    ]
    dispatch(setContacts(contacts))
  }
}


export const displayMessages = (messages) => ({
  type: 'DISPLAY_MESSAGES',
  payload: {
    messages: messages
  }
})

// this is also a thunk
export const getMessages = (dispatch) => {
  return (dispatch) => {
    var messages = [
      {
        created_by: 1,
        msg_id: 1,
        msg_text: "Hey, sorry I've been so out of the loop but I'd love to chat sometime soon."
      }
    ]
    dispatch(displayMessages(messages))
  }
}

export const addMessage = (msg) => ({
  type: 'ADD_MESSAGE',
  payload: {
    msg: msg
  }
})

