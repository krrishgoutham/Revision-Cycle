from datetime import date
import time
from Learning_Session import Learning_Session
import Sessions_Control, Reminder_System, Database



'''
my_session = Sessions_Control.get_individual_session("Economics - National Income")
for i in range(5):
    interval = my_session.set_next_interval_reminder()
    print(f'\nAfter {interval} days interval:')
    print(f"Date: {Reminder_System.show_specific_reminder_next_date('Economics - National Income').strftime('%d-%m-%Y')}")
    print(f'Revision {i+1}-----------')
    my_session.get_user_confidence_score()
start_date, revisions, intervals, confidence_scores = my_session.get_session_info()
print('\n')
print(f"\nSession start date = {start_date.strftime('%d-%m-%Y')}")
print(f'Session revisions = {revisions}')
print(f'Session intervals = {intervals}')
print(f'Session confidence_Scores = {confidence_scores}')
'''

#Sessions_Control.add_session('Economics')
#Sessions_Control.add_session('Geography')
#Sessions_Control.add_session('History')

#Database.load_sessions_data()
#Sessions_Control.load_all_sess_from_db()
#Reminder_System.load_rem_data_from_db()
'''
print('\n')

x = 0 #dummy
def daily_update(x): #remove param
    reminders = Reminder_System.check_any_reminder_today(x) #remove param
    print('Updating today..')
    if len(reminders) != 0:
        for _ in range(len(reminders)):
            my_session = Sessions_Control.get_individual_session(reminders.pop(0))
            Reminder_System.notify(my_session.name)
            print(f'Revise {my_session.name} today-----------')
            my_session.get_user_confidence_score()
            my_session.set_next_interval_reminder()
            Reminder_System.upload_rem_data_to_db()
            print(f"Next Revision date: {Reminder_System.show_specific_reminder_next_date(my_session.name).strftime('%d-%m-%Y')}\n")

while True:
    x += 1 #dummy
    daily_update(x)
    time.sleep(1)
'''