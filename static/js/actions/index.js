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

// export const beginFetchingContacts = (userId) => ({
//     type: 'BEGIN_FETCHING_CONTACTS',
//     payload: {
//         userId: userId
//     }
// })

// export const finishFetchingContacts = (userId) => ({
//     type: 'FINISH_FETCHING_CONTACTS',
//     payload: {
//         userId: userId,
//         data: data
//     }
// })

export const setContacts = (contacts) => ({
    type: 'SET_CONTACTS',
    payload: {
        contacts: contacts,
        userId: userId
    }
})

// this is a thunk
export const getUserContacts = (dispatch) => { // did not need to pass userId because it's already in function
  return (dispatch) => {
    console.log('sending contacts request')
    fetch('/user/' + userId + '/contacts')
    .then((resp) => resp.json()) 
    .then((data) => {
      console.log('contacts received')
      var contacts = data
      dispatch(setContacts(contacts))
    })
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
    fetch('/user/' + userId + '/messages')
    .then((resp) => resp.json())
    .then((data) => {
      var messages = data
      dispatch(displayMessages(messages))
    })
  }
}

export const addMessage = (msg) => ({
  type: 'ADD_MESSAGE',
  payload: {
    msg: msg
  }
})

// export const contactPeriodSuccess = () => ({
//   type: 'POST_CONTACT_PERIOD_SUCCESS',
//   payload: {

//   }
// })

// export const postContactPeriod = (dispatch) => {
//   return (dispatch) => {
//     fetch('/set_period', {
//     method: 'POST',
//     headers: {
//       'Accept': 'application/json',
//       'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({
//       contact_id: 206, // example data
//       period: 30,
//       })
//     })
//   }
// }
