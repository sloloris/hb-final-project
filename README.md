TO DO LIST:

- create & style contacts list
- create scheduling mechanism:
https://github.com/dbader/schedule
https://schedule.readthedocs.io/en/stable/

SUNDAY
- create server-side chron job
- autofill for schedule template
- appearing schedule button on selected contacts
- change contact sort on click (not prioritized for demo night)




TopNav.js
- make user name appear


store contains the state
state changes in response to actions as defined by reducers
components display parts of the UI based on the state, which is passed to them via their containers

... is the spread operator - it flattens the obj1 in obj2 = {...obj1, key: value} into obj2

thunk is a function that returns another function containing "dispatch" as input 
dispatch sends action to store

reducer is like a key in state where the next state value is what the reducer returns

SEND THUNK (AJAX) GET REQUEST:
1. create server route, return jsonify
2. create action to receive & parse json
3. create reducer
4. add reducer to reducer index.js (make sure to import first!)
5. feed function through relevant container (import, map data to state, map function to dispatch)
6. create component to render data on page
7. if component is in another component, make sure to add an instance of it to the latter's render & the relevant data & functions to the latter's props

SEND THUNK POST REQUEST WITH FORM:
1. create form component with a callback for submit (javascript)
    callback creates JSON out of form input 
    export JSON and import into body of post request in actions/index.js
2. put component in parent component where you want form to render


CREATE ACTION:
return JSON from server route
call action addMessage on reducer 






model.py
- write ScheduledMessage class 

server.py
- finish document docstring
- parse landing page function

registration.html
- add hover to explain nickname
- add hover to explain phone number format
- restrict phone number format?
- add "i already have an account" button

-figure out whatsapp thing


landing.html


account_home
- add user photo
- add update for user photo

preferences.html
- actually add current preferences
- javascript make form appear or disappear

contacts.html 
- figure out how to get the contacts back (authorize)

server_functions.py
- in get_google_contacts, extract phone numbers







- the order_by in relationships is referring to which class? - the class in which it is declared if in regular format. however, it can refer to the related class so:
order_by='Other.variable'


* RESEARCH PAGINATION

to fix button
-webkit-appearance: button; is commented out in node_modules/normalize/normalize.css



