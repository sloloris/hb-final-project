TO DO LIST:

model.py
- make password rules
- encrypt password field 

server.py
- finish document docstring







CODE REVIEW QUESTIONS:

model.py
- are my sqlalchemy relationships good? (can there be a relationship that's the same name as another column? see freq_of_contact in Contact & created_by in Message)
- do relationships have to be in the class that specifies the foreign key?
- the order_by in relationships is referring to which class?
- can I set created_by in Message class to default None?
- ask about connect to app function
- __repr__ % next page?

server.py
- new line on imports?
- secret key for flask on github? 


popup: A plugin (SublimeLinter) may be making Sublime Text unresponsive by taking too long (0.034545s) in its on_selection_modified callback.

This message can be disabled via the detect_slow_plugins setting
