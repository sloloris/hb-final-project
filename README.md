TO DO LIST:

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







- the order_by in relationships is referring to which class? - the class in which it is declared if in regular format. however, it can refer to the related class so:
order_by='Other.variable'
- can I set created_by in Message class to default None? - yes

CODE REVIEW QUESTIONS:

model.py
- check about oauth  variables in model.py. should they be in a separate table?

what are the relationship variables used for?

** CHECK MODEL.PY
should i store oauth credentials using gmail's thing?

OTHER

