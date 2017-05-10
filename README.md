TO DO LIST:

model.py
- make password rules
- encrypt password field 

server.py
- finish document docstring







CODE REVIEW QUESTIONS:

model.py
- the order_by in relationships is referring to which class? - the class in which it is declared if in regular format. however, it can refer to the related class so:
order_by='Other.variable'
- can I set created_by in Message class to default None? - yes

