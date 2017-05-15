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

    def __repr__(self):
        return "<User user_id=%s email=%s>" % (self.user_id, self.email)


# class Oauth(db.Model):
#     """ Oauth credentials for given user. """

#     __tablename__ = "oauth"

#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)


#     user = db.relationship("User", backref=db.backref("oauth",
#                                                     order_by=user_id))

#     def __repr__(self):
#         return "<Oauth oauth_token=%s oauth_expiry=%s for user_id=%s>" % (self.oauth_token, 
#                                                             self.oauth_expiry, self.user_id)


class Contact(db.Model):
    """ User contacts. """

    __tablename__ = "contacts"

    contact_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=True)
    nickname = db.Column(db.String(15), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    relationship = db.Column(db.String(5), db.ForeignKey('relationships.rel_id'),
                            nullable=False, default="other")
    contact_period = db.Column(db.Integer, nullable=False, default=90)
    phone = db.Column(db.String(16), nullable=True)
    whatsapp = db.Column(db.String(16), nullable=True)


    user = db.relationship("User", backref=db.backref("contacts",
                                                    order_by=user_id))
    relationship_fk = db.relationship("Relationship", backref=db.backref("contacts"))
    # period = db.relationship("ContactPeriod", 
    #                                 backref=db.backref("contacts", order_by=contact_id))

    def __repr__(self):
        return "<Contact contact_id=%s email=%s belonging to user_id=%s>" % (self.contact_id, self.email, self.user_id)



class Relationship(db.Model):
    """ Contact relationship to user. """

    __tablename__ = "relationships" 

    rel_id = db.Column(db.String(5), primary_key=True) # frnd, fmly, prof, other
    rel_type = db.Column(db.String(15), nullable=False) 

    def __repr__(self):
        return "<Relationship rel_id=%s rel_type=%s>" % (self.rel_id, self.rel_type)


# class ContactPeriod(db.Model):
#     """ How frequently the user wishes to contact a given contact. """

#     __tablename__ = "contact_periods"

#     period_id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(20), nullable=False)

#     def __repr__(self):
#         return "<ContactPeriod period_id=%s (days) description=%s>" % (self.period_id, self.description)


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


# class ScheduledMessage(db.Model): # this would be a queue


###############################################################################

# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///contacts'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ????
    # or app.config['SQLALCHEMY_ECHO'] = True ???
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

