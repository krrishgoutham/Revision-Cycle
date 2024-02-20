import pickle
from xml.dom import registerDOMImplementation

objs = []

def add_session_data(sess_obj):
    temp = load_sessions_data()
    temp.append(sess_obj)
    pickle_out = open('objs.pickle', 'wb')
    pickle.dump(temp, pickle_out)
    pickle_out.close()
    #objs.append(sess_obj)

def update_data(objs):
    pickle_out = open('objs.pickle', 'wb')
    pickle.dump(objs, pickle_out)
    pickle_out.close()

def add_reminders_data(remindersData):
    pickle_out = open('reminders.pickle', 'wb')
    pickle.dump(remindersData, pickle_out)
    pickle_out.close()

def delete_session_data(sess_obj):
    temp = load_sessions_data()
    for _ in temp:
        if sess_obj == _.name:
            temp.remove(_)
            pickle_out = open('objs.pickle', 'wb')
            pickle.dump(temp, pickle_out)
            pickle_out.close()
            return 1
    else:
        print('No such session to delete!')
        return 0

def load_sessions_data():
    #global objs
    #objs = []
    temp = []
    try:
        pickle_in = open('objs.pickle', 'rb')
        temp = pickle.load(pickle_in)
        #while True:
        #    try:
        #        temp.append(pickle.load(pickle_in))
        #   except EOFError:
        #        break
        pickle_in.close()
        return temp
    except:
        print("Load Failed. Objs file doesn't exist.")
        return temp

def load_reminders_data():
    temp = []
    try:
        pickle_in = open('reminders.pickle', 'rb')
        temp = pickle.load(pickle_in)
        pickle_in.close()
        return temp
    except:
        print("Load Failed. Reminders file doesn't exist.")
        return temp

def get_objs():
    return objs
