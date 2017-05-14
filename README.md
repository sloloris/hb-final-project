TO DO LIST:

model.py
- make password rules
- encrypt password field 
- write ScheduledMessage class 

server.py
- finish document docstring







CODE REVIEW QUESTIONS:

model.py
- the order_by in relationships is referring to which class? - the class in which it is declared if in regular format. however, it can refer to the related class so:
order_by='Other.variable'
- can I set created_by in Message class to default None? - yes

- check about oauth  variables in model.py. should they be in a separate table?

what are the relationship variables used for?


OTHER

