import model

def add_msg_samples_to_messages_table():
    skype_sometime = Message(created_by=1, msg_text="Hey you, \n\nI was just thinking of you the other day and that it's been a while! What do you say we set up a Skype call sometime soon to catch up?")
    long_time_no_see = Message(created_by=1, msg_text="Hey, \nLong time no see! What are you up to these days?")
    catch_up_sometime = Message(created_by=1, msg_text="Hi friend, It's been a while since we caught up. Do you have any time in the next couple of weeks to chat?")


    db.session.add_all([skype_sometime, long_time_no_see, catch_up_sometime])
    db.session.commit()

if __name__ == "__main__":
    add_msg_samples_to_messages_table()