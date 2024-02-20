from plyer import notification
import datetime, threading
import Database, Sessions_Control

reminders = {}

def load_rem_data_from_db():
    global reminders
    reminders = Database.load_reminders_data()

def upload_rem_data_to_db():
    global reminders
    Database.add_reminders_data(reminders)

def notify(name):
    notification.notify(app_name = 'Reminder',
        title = 'Revise today:', 
        message = name,
        timeout = 10)

def set_reminder(name, interval):
    if name in reminders:
        tdelta = datetime.timedelta(days=interval+1)
        reminders[name] = reminders[name] + tdelta
        print(reminders)
    else:
        tday = datetime.date.today()
        tdelta = datetime.timedelta(days=interval+1)
        reminder_date = tday + tdelta
        reminders[name] = reminder_date
        print(reminders)

def sort_reminder_dates():
    global reminders
    if len(reminders) > 0:
        sorted_values = sorted(reminders.items(), key=lambda x: x[1])
        reminders = dict(sorted_values)

def show_specific_reminder_next_date(name):
    if len(reminders) > 0:
        return reminders[name]

def show_all_reminders_next_date():
    if len(reminders) > 0:
        return reminders

def check_any_reminder_today(dummyDate): #remove parameter
#def check_any_reminder_today():
    global reminders
    load_rem_data_from_db()
    sort_reminder_dates()
    tday = datetime.date.today()
    tday = datetime.date.today() + datetime.timedelta(days=dummyDate) #remove
    print(f"\nToday: {tday.strftime('%d-%m-%Y')}") #remove dummy
    sessions_to_remind = []
    if len(reminders) > 0:
        for session, date in reminders.items():
            if date == tday:
                sessions_to_remind.append(session)
    return sessions_to_remind

def revised_today(sess_name, confi_score):
    for i in range(len(Sessions_Control.all_Sessions)):
        if Sessions_Control.all_Sessions[i].name == sess_name:
            Sessions_Control.all_Sessions[i].get_user_confidence_score(confi_score)
            Sessions_Control.all_Sessions[i].set_next_interval_reminder()
            break
    Database.update_data(Sessions_Control.all_Sessions)
    Sessions_Control.load_all_sess_from_db()
    upload_rem_data_to_db()

def get_10_days_revisions():
    sort_reminder_dates()
    tday = datetime.date.today()
    nxt_10_dates = []
    nxt_10_dates.append(tday)
    for i in range(10):
        nxt_10_dates.append(tday + datetime.timedelta(days=i+1))
    temp = []
    if len(reminders) > 0:
        for session, date in reminders.items():
            if date in nxt_10_dates:
                temp.append((session + '. Next Revision date: ' + date.strftime('%d-%m-%Y')))
    return temp


dummyDate = 0
def dummy():
    global dummyDate
    while True:
        temp = int(input('Skip a date: '))
        if temp == 1:
            dummyDate += 1

x = threading.Thread(target=dummy)
x.start()
