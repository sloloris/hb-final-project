TO DO LIST:

- ajax/thunk request to session.clear() for onClickLogout
- create & style contacts list
- create messages interface
- create scheduling mechanism:
https://github.com/dbader/schedule
https://schedule.readthedocs.io/en/stable/



TopNav.js
- make user name appear


store contains the state
state changes in response to actions as defined by reducers
components display parts of the UI based on the state, which is passed to them via their containers



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
- can I set created_by in Message class to default None? - yes

CODE REVIEW QUESTIONS:

secrets.sh imports the same as deets.py right?
function efficiency - esp. save_user_contacts_to_db
optimal refactorization?
what kind of tests to focus on? test function by function?
- test helper functions
- test database functions




* RESEARCH PAGINATION



