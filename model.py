""" Table models and functions for database 'contacts'. """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Model definitions

class User(db.Model):
    """ Application user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(15), nullable=True) # for clarity: defaults to True
    email = db.Column(db.String(50), nullable=False, unique=True) # also user login
    phone = db.Column(db.String(16), nullable=True)
    whatsapp = db.Column(db.String(16), nullable=True)

    oauth_token = db.Column(db.String(200), nullable=True)
    oauth_expiry = db.Column(db.DateTime, nullable=True)
    refresh_token = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return "<User user_id=%s email=%s>" % (self.user_id, self.email)


class Contact(db.Model):
    """ User contacts. """

    __tablename__ = "contacts"

    contact_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    nickname = db.Column(db.String(15), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    relationship = db.Column(db.String(5), db.ForeignKey('relationships.rel_id'), nullable=False, default="other")
    contact_period = db.Column(db.Integer, nullable=False, default=90)
    phone = db.Column(db.String(16), nullable=True)
    whatsapp = db.Column(db.String(16), nullable=True)


    user = db.relationship("User", backref=db.backref("contacts",
                                                    order_by=user_id))
    relationship_fk = db.relationship("Relationship", backref=db.backref("contacts"))

    def __repr__(self):
        return "<Contact contact_id=%s email=%s belonging to user_id=%s>" % (self.contact_id, self.email, self.user_id)



class Relationship(db.Model):
    """ Contact relationship to user. """

    __tablename__ = "relationships" 

    rel_id = db.Column(db.String(5), primary_key=True) # frnd, fmly, prof, other
    rel_type = db.Column(db.String(15), nullable=False) 

    def __repr__(self):
        return "<Relationship rel_id=%s rel_type=%s>" % (self.rel_id, self.rel_type)


class Message(db.Model):
    """ Message templates to choose from. """

    __tablename__ = "messages"

    msg_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), default=None)
    msg_text = db.Column(db.String(700), nullable=False)

    user = db.relationship("User", backref=db.backref("messages", 
                                                            order_by=msg_id))

    def __repr__(self):
        return "<Message msg_id=%s created_by=%s>" % (self.msg_id, self.created_by)


class ScheduledMessage(db.Model): # this would be a queue
    """ Messages scheduled by users. """

    __tablename__ = "scheduled_messages"
    schedule_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False, default=None)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.contact_id'), nullable=False)
    send_date = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean, nullable=False, default=False)

    user = db.relationship("User", backref=db.backref("scheduled_messages", 
                                                        order_by=user_id))
    contact = db.relationship("Contact", backref=db.backref("scheduled_messages",
                                                            order_by=contact_id))




###############################################################################

# Test Data

def test_data():
    """ Create fake data to seed test database with. """

    test_user = User(first_name='Test', 
                    last_name='User', 
                    email='contactmanager.tests@gmail.com')

    db.session.add(test_user)
    db.session.commit()

    contact1 = Contact(user_id=1,
                    first_name='Ari', 
                    last_name='Zona', 
                    email='ari.zona3875@gmail.com')

    contact2 = Contact(user_id=1,
                    first_name='Cali', 
                    last_name='Fornia', 
                    email='cali.fornia1209@gmail.com')

    contact3 = Contact(user_id=1,
                    first_name='George', 
                    last_name='Gia', 
                    email='georgia0876@gmail.com')

    contact4 = Contact(user_id=1,
                    first_name='Ken', 
                    last_name='Tucky', 
                    email='ken.tucky0965@gmail.com')

    contact5 = Contact(user_id=1,
                    first_name='Mary', 
                    last_name='Land', 
                    email='mary.land5866@gmail.com')



    db.session.add_all([contact1, contact2, contact3, contact4, contact5])
    db.session.commit()




###############################################################################

# Helper functions

def connect_to_db(app, db_uri='postgresql:///contacts'):
    """Connect the database to our Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ????
    # or app.config['SQLALCHEMY_ECHO'] = True ???
    db.app = app
    db.init_app(app)
    db.create_all()

def create_user1():
    user1 = User(first_name="Default",
                last_name="User",
                email="contactmanager.tests@gmail.com")

    db.session.add(user1)
    db.session.commit()

def fill_relationships_table():
    friend = Relationship(rel_id='frnd', rel_type='friend')
    family = Relationship(rel_id='fmly', rel_type='family')
    professional = Relationship(rel_id='prof', rel_type='professional')
    other = Relationship(rel_id='other', rel_type='other')

    db.session.add_all([friend, family, professional, other])
    db.session.commit()

def add_msg_samples_to_messages_table():
    skype_sometime = Message(created_by=1, msg_text="Hey you, \n\nI was just thinking of you the other day and that it's been a while! What do you say we set up a Skype call sometime soon to catch up?")
    long_time_no_see = Message(created_by=1, msg_text="Hey, \nLong time no see! What are you up to these days?")
    catch_up_sometime = Message(created_by=1, msg_text="Hi friend, It's been a while since we caught up. Do you have any time in the next couple of weeks to chat?")


    db.session.add_all([skype_sometime, long_time_no_see, catch_up_sometime])
    db.session.commit()

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    create_user1()
    fill_relationships_table()
    add_msg_samples_to_messages_table()
    print "Connected to DB."

