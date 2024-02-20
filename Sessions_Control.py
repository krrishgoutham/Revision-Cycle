import Learning_Session
import datetime
import Database
import Reminder_System

all_Sessions = []

def load_all_sess_from_db():
    global all_Sessions
    all_Sessions = []
    all_Sessions = Database.load_sessions_data()

def add_session(name):
    start_date = datetime.date.today()
    new_session = Learning_Session.Learning_Session(name, start_date)
    interval = new_session.set_next_interval_reminder()
    Database.add_session_data(new_session)
    load_all_sess_from_db()
    Reminder_System.upload_rem_data_to_db()
    return ((start_date + datetime.timedelta(days=2)).strftime('%d-%m-%Y'))

def delete_session(session_to_delete):
    success = Database.delete_session_data(session_to_delete.name)
    if success:
        del Reminder_System.reminders[session_to_delete.name]
        Reminder_System.upload_rem_data_to_db()
        load_all_sess_from_db()

def edit_session_name(old_session, new_name):
    global all_Sessions
    load_all_sess_from_db()
    for _ in all_Sessions:
        if old_session == _.name:
            _.name = new_name
            Reminder_System.reminders[new_name] = Reminder_System.reminders.pop(old_session)
            break
    Database.update_data(all_Sessions)
    Reminder_System.upload_rem_data_to_db()
    Reminder_System.load_rem_data_from_db()
    load_all_sess_from_db()
            
        
def list_all_sessions():
    load_all_sess_from_db()
    for i in range(len(all_Sessions)):
        print(all_Sessions[i].name)

def get_individual_session(sess_name):
    load_all_sess_from_db()
    for i in range(len(all_Sessions)):
        if all_Sessions[i].name == sess_name:
            return all_Sessions[i]
    else:
        print("No such session exists!")

def total_no_of_sessions():
    load_all_sess_from_db()
    return len(all_Sessions)