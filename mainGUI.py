from select import select
from tkinter import *
from tkinter import messagebox
import Sessions_Control, Reminder_System, Database
import schedule, threading, datetime, time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk()
root.geometry("1440x1024")
root.configure(bg = "#d9e8f5")
root.iconbitmap('./assets/icon.ico')
root.title('Optimal Revision Recommender')

def load_view_all_sessions():
    learning_session(root)
def load_main_window():
    main_window(root)
def load_add_session():
    add_session(root)
def load_edit_session():
    edit_session(root)
def load_edit_name():
    edit_name(root)
def load_delete_session():
    delete_session(root)
def load_upcoming_sessions():
    upcoming_sessions(root)
def load_select_insight():
    select_insight(root)
def load_revisions_for_today():
    revisions_for_today(root)
def load_rate_effectiveness():
    rate_effectiveness(root)
def load_insight_window():
    insight_window(root)

def main_window(root_window):
    refresh_data()
    global background_img, btn_del_sess, btn_tdy_rev, btn_upco_revi, btn_add_sess, btn_view_all, btn_edit_sess, btn_get_insig
    canvas1 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas1.place(x = 0, y = 0)


    background_img = PhotoImage(file = f"./main_window/background.png")
    background = canvas1.create_image(
        330, 505,
        image=background_img)

    btn_del_sess = PhotoImage(file = f"./main_window/img0.png")
    b0 = Button(
        image = btn_del_sess,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_delete_session,
        relief = "flat")

    b0.place(
        x = 777, y = 710,
        width = 574,
        height = 95)

    btn_upco_revi = PhotoImage(file = f"./main_window/img1.png")
    b1 = Button(
        image = btn_upco_revi,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_upcoming_sessions,
        relief = "flat")

    b1.place(
        x = 779, y = 229,
        width = 574,
        height = 95)

    btn_view_all = PhotoImage(file = f"./main_window/img2.png")
    b2 = Button(
        image = btn_view_all,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_view_all_sessions,
        relief = "flat")

    b2.place(
        x = 779, y = 62,
        width = 574,
        height = 104)

    btn_edit_sess = PhotoImage(file = f"./main_window/img3.png")
    b3 = Button(
        image = btn_edit_sess,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_edit_session,
        relief = "flat")

    b3.place(
        x = 777, y = 552,
        width = 574,
        height = 95)

    btn_add_sess = PhotoImage(file = f"./main_window/img4.png")
    b4 = Button(
        image = btn_add_sess,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_add_session,
        relief = "flat")

    b4.place(
        x = 777, y = 387,
        width = 574,
        height = 101)

    btn_get_insig = PhotoImage(file = f"./main_window/img5.png")
    b5 = Button(
        image = btn_get_insig,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_select_insight,
        relief = "flat")

    b5.place(
        x = 779, y = 850,
        width = 574,
        height = 101)

    btn_tdy_rev = PhotoImage(file = f"./main_window/img6.png")
    b5 = Button(
        image = btn_tdy_rev,
        borderwidth = 0,
        highlightthickness = 0, bg='#304269', activebackground='#304269',
        command = load_revisions_for_today,
        relief = "flat")

    b5.place(
        x = 60, y = 850,
        width = 574,
        height = 101)
  
def learning_session(root_window):
    global canvas2, background_img, btn_go_back
    canvas2 = Canvas(
    root_window,
    bg = "#d9e8f5",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas2.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./learning_sessions/background.png")
    background = canvas2.create_image(
        720, 420,
        image=background_img)

    wrapper = LabelFrame(root_window, bg = '#ffffff', height=607, width=1266, border=10)
    wrapper.place(x=85, y=200)

    new_canvas = Canvas(wrapper, height=607, width=1266)#, bg='#304269')
    new_canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(wrapper, orient='vertical', command=new_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.config(yscrollcommand=yscrollbar.set, scrollregion=new_canvas.bbox('all'))
    new_canvas.bind('<Configure>', lambda e: new_canvas.configure(scrollregion = new_canvas.bbox('all')))

    myframe = Frame(new_canvas, height=607, width=1266)
    new_canvas.create_window((0,0), window=myframe, anchor='nw')

    refresh_data()
    learning_session.mySessions = Sessions_Control.all_Sessions

    for i in range(len(learning_session.mySessions)):
        Label(myframe, text=(learning_session.mySessions[i].name + '. Next Revision Date: ' + Reminder_System.show_specific_reminder_next_date(learning_session.mySessions[i].name).strftime('%d-%m-%Y')), 
            bg = "#ffffff", highlightthickness = 0, 
            font=('Lato', 25, 'bold'), 
            fg='#304269').pack(anchor='w')

    btn_go_back = PhotoImage(file = f"./learning_sessions/img0.png")
    b0 = Button(
        image = btn_go_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_main_window,
        relief = "flat")

    b0.place(
        x = 582, y = 855,#y=867
        width = 275,
        height = 104)

def add_session(root_window):
    global background_img, btn_add_x, btn_cancel_x, entry_img
    add_session.date_str = StringVar()
    canvas3 = Canvas(
    root_window,
    bg = "#d9e8f5",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas3.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./add_session/background.png")
    background = canvas3.create_image(
        670, 400,
        image=background_img)

    entry_img = PhotoImage(file = f"./add_session/img_textBox0.png")
    entry0_bg = canvas3.create_image(
        0.5, -189.0,
        image = entry_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 35, 'bold'), fg='#304269')

    entry0.place(
        x = 163, y = 272,
        width = 1075.0,
        height = 80)

    def session_add_successful():
        temp = entry0.get()
        if len(temp) > 0:
            d = Sessions_Control.add_session(temp)
            messagebox.showinfo('Add New Session', 'New Session added successfully!')
            add_session.date_str.set(d)
        else:
            messagebox.showinfo('Error', "Please enter a valid session name!")

    btn_add_x = PhotoImage(file = f"./add_session/img0.png")
    b0 = Button(
        image = btn_add_x,
        borderwidth = 0,
        highlightthickness = 0,
        command = session_add_successful,
        relief = "flat")

    b0.place(
        x = 630, y = 434,
        width = 180,
        height = 78)

    btn_cancel_x = PhotoImage(file = f"./add_session/img1.png")
    b1 = Button(
        image = btn_cancel_x,
        borderwidth = 0,
        highlightthickness = 0, bg = '#d9e8f5',
        command = load_main_window,
        relief = "flat")

    b1.place(
        x = 609, y = 842,
        width = 236,
        height = 89)

    label = Label(textvariable=add_session.date_str, bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')
    label.place(
        x = 750, y = 624,
        width = 486,
        height = 78)
    add_session.date_str.set('dd/mm/yyyy')

def edit_session(root_window):
    global background_img, btn_edit, btn_go_back
    canvas4 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas4.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./edit_session/background.png")
    background = canvas4.create_image(
        720, 420,
        image=background_img)

    wrapper = LabelFrame(root_window, bg = '#D9E8F5', height=607, width=1266, border=10)
    wrapper.place(x=85, y=200)

    new_canvas = Canvas(wrapper, height=607, width=1266, bg='#D9E8F5')
    new_canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(wrapper, orient='vertical', command=new_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.config(yscrollcommand=yscrollbar.set, scrollregion=new_canvas.bbox('all'))
    new_canvas.bind('<Configure>', lambda e: new_canvas.configure(scrollregion = new_canvas.bbox('all')))

    myframe = Frame(new_canvas, height=607, width=1266)
    new_canvas.create_window((0,0), window=myframe, anchor='nw')

    refresh_data()
    edit_session.mySessions = Sessions_Control.all_Sessions

    edit_session.var = IntVar()

    for i in range(len(edit_session.mySessions)):
        Radiobutton(myframe, text=edit_session.mySessions[i].name, variable=edit_session.var, value=i,
        bg = "#D9E8F5", highlightthickness = 0, font=('Lato', 25, 'bold'), 
        fg='#304269', indicatoron=0, background='#D9E8F5', bd=0).pack(fill=X, anchor='w')


    btn_edit = PhotoImage(file = f"./edit_session/img0.png")
    b0 = Button(
        image = btn_edit,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_edit_name,
        relief = "flat")

    b0.place(
        x = 304, y = 867,
        width = 275,
        height = 104)

    btn_go_back = PhotoImage(file = f"./edit_session/img1.png")
    b1 = Button(
        image = btn_go_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_main_window,
        relief = "flat")

    b1.place(
        x = 884, y = 869,
        width = 275,
        height = 104)


def edit_name(root_window):
    global background_img, btn_cancel, btn_edit_name
    canvas5 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas5.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./edit_name/background.png")
    background = canvas5.create_image(
        650, 350,
        image=background_img)

    btn_cancel = PhotoImage(file = f"./edit_name/img0.png")
    b0 = Button(
        image = btn_cancel,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_edit_session,
        relief = "flat")

    b0.place(
        x = 332, y = 844,
        width = 236,
        height = 89)

    def edit_name_successful():
        temp = entry0.get()
        if len(temp) > 0:
            Sessions_Control.edit_session_name(edit_session.mySessions[edit_session.var.get()].name, temp)
            messagebox.showinfo('Edit Session Name', 'New changed successfully!')
            load_edit_session()
        else:
            messagebox.showinfo('Error', "Please enter a valid name!")

    btn_edit_name = PhotoImage(file = f"./edit_name/img1.png")
    b1 = Button(
        image = btn_edit_name,
        borderwidth = 0,
        highlightthickness = 0,
        command = edit_name_successful,
        relief = "flat")

    b1.place(
        x = 903, y = 844,
        width = 236,
        height = 89)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')

    entry0.place(
        x = 570, y = 538,
        width = 701.0,
        height = 80)

    edit_name.old_name = StringVar()
    label = Label(textvariable=edit_name.old_name, bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')
    label.place(
        x = 547, y = 315,
        width = 745,
        height = 82)
    edit_name.old_name.set(edit_session.mySessions[edit_session.var.get()].name)

def delete_session(root_window):
    global background_img, btn_delete, btn_go_back
    canvas6 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas6.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./delete_session/background.png")
    background = canvas6.create_image(
        720, 420,
        image=background_img)

    wrapper = LabelFrame(root_window, bg = '#D9E8F5', height=607, width=1266, border=10)
    wrapper.place(x=85, y=200)

    new_canvas = Canvas(wrapper, height=607, width=1266, bg='#D9E8F5')
    new_canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(wrapper, orient='vertical', command=new_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.config(yscrollcommand=yscrollbar.set, scrollregion=new_canvas.bbox('all'))
    new_canvas.bind('<Configure>', lambda e: new_canvas.configure(scrollregion = new_canvas.bbox('all')))

    myframe = Frame(new_canvas, height=607, width=1266)
    new_canvas.create_window((0,0), window=myframe, anchor='nw')

    refresh_data()
    delete_session.mySessions = Sessions_Control.all_Sessions

    delete_session.var = IntVar()

    for i in range(len(delete_session.mySessions)):
        Radiobutton(myframe, text=delete_session.mySessions[i].name, variable=delete_session.var, value=i,
        bg = "#D9E8F5", highlightthickness = 0, font=('Lato', 25, 'bold'), 
        fg='#304269', indicatoron=0, background='#D9E8F5', bd=0).pack(fill=X, anchor='w')
    
    def delete_session_successful():
        user_choice = messagebox.askquestion('Confirmation', f'Are you sure you want to delete the session {delete_session.mySessions[delete_session.var.get()].name}?')
        if(user_choice == 'yes'):
            Sessions_Control.delete_session(delete_session.mySessions[delete_session.var.get()])
            messagebox.showinfo('Delete Session', 'Session deleted successfully!')
            refresh_data()
            load_main_window()

    btn_go_back = PhotoImage(file = f"./delete_session/img0.png")
    b0 = Button(
        image = btn_go_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_main_window,
        relief = "flat")

    b0.place(
        x = 878, y = 867,
        width = 275,
        height = 104)

    btn_delete = PhotoImage(file = f"./delete_session/img1.png")
    b1 = Button(
        image = btn_delete,
        borderwidth = 0,
        highlightthickness = 0,
        command = delete_session_successful,
        relief = "flat")

    b1.place(
        x = 303, y = 867,
        width = 275,
        height = 104)

def upcoming_sessions(root_window):
    global background_img, btn_ok
    canvas7 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas7.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./upcoming_revisions/background.png")
    background = canvas7.create_image(
        720, 420,
        image=background_img)

    wrapper = LabelFrame(root_window, bg = '#ffffff', height=607, width=1266, border=10)
    wrapper.place(x=85, y=200)

    new_canvas = Canvas(wrapper, height=607, width=1266)#, bg='#304269')
    new_canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(wrapper, orient='vertical', command=new_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.config(yscrollcommand=yscrollbar.set, scrollregion=new_canvas.bbox('all'))
    new_canvas.bind('<Configure>', lambda e: new_canvas.configure(scrollregion = new_canvas.bbox('all')))

    myframe = Frame(new_canvas, height=607, width=1266)
    new_canvas.create_window((0,0), window=myframe, anchor='nw')

    refresh_data()
    upcoming_sessions.mySessions = Reminder_System.get_10_days_revisions()

    for i in range(len(upcoming_sessions.mySessions)):
        Label(myframe, text= upcoming_sessions.mySessions[i], bg = "#ffffff", highlightthickness = 0, 
            font=('Lato', 25, 'bold'), 
            fg='#304269').pack(anchor='w')


    btn_ok = PhotoImage(file = f"./upcoming_revisions/img0.png")
    b0 = Button(
        image = btn_ok,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_main_window,
        relief = "flat")

    b0.place(
        x = 595, y = 864,
        width = 250,
        height = 104)

def select_insight(root_window):
    global background_img, btn_go_back, btn_get_insig
    canvas8 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas8.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./select_insight/background.png")
    background = canvas8.create_image(
        720, 420,
        image=background_img)

    wrapper = LabelFrame(root_window, bg = '#D9E8F5', height=607, width=1266, border=10)
    wrapper.place(x=85, y=200)

    new_canvas = Canvas(wrapper, height=607, width=1266, bg='#D9E8F5')
    new_canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(wrapper, orient='vertical', command=new_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.config(yscrollcommand=yscrollbar.set, scrollregion=new_canvas.bbox('all'))
    new_canvas.bind('<Configure>', lambda e: new_canvas.configure(scrollregion = new_canvas.bbox('all')))

    myframe = Frame(new_canvas, height=607, width=1266)
    new_canvas.create_window((0,0), window=myframe, anchor='nw')

    refresh_data()
    select_insight.mySessions = Sessions_Control.all_Sessions

    select_insight.var = IntVar()

    for i in range(len(select_insight.mySessions)):
        Radiobutton(myframe, text=select_insight.mySessions[i].name, variable=select_insight.var, value=i+1,
        bg = "#D9E8F5", highlightthickness = 0, font=('Lato', 25, 'bold'), 
        fg='#304269', indicatoron=0, background='#D9E8F5', bd=0).pack(fill=X, anchor='w')

    btn_go_back = PhotoImage(file = f"./select_insight/img0.png")
    b0 = Button(
        image = btn_go_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_main_window,
        relief = "flat")

    b0.place(
        x = 878, y = 850,
        width = 275,
        height = 124)

    def insight_window_loader():
        if select_insight.var.get() > 0:
            load_insight_window()
        else:
            pass

    btn_get_insig = PhotoImage(file = f"./select_insight/img1.png")
    b1 = Button(
        image = btn_get_insig,
        borderwidth = 0,
        highlightthickness = 0,
        command = insight_window_loader,
        relief = "flat")

    b1.place(
        x = 303, y = 850,
        width = 275,
        height = 124)

def insight_window(root_window):
    global background_img, btn_ok
    refresh_data()
    canvas = Canvas(
    root_window,
    bg = "#d9e8f5",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./insight_window/background.png")
    background = canvas.create_image(
        655, 450,
        image=background_img)

    intervals = select_insight.mySessions[select_insight.var.get()-1].intervals
    confi_scores = select_insight.mySessions[select_insight.var.get()-1].confidence_scores
    #intervals = [1, 3, 6, 15, 43]
    #confi_scores = [3, 4, 4, 4]
    intervals.insert(0, 0)
    confi_scores.insert(0, 0)
    def draw_graph():
        draw_graph.f = Figure(figsize=(7,5), dpi = 100)
        a = draw_graph.f.add_subplot(111)
        a.plot(intervals[0:len(confi_scores)], color='#304269', label='Interval between revisions')
        a.plot(confi_scores, color='#F26101', label='Effectiveness score for each revision')
        #a.set_title('Progress', fontdict={'fontname': 'Lato', 'fontsize': 15}, color='#1a1a1a')
        a.set_xlabel('Revisions ->')
        #a.set_ylabel('Interval b/w revisions & Effectiveness score ->')
        a.set_ylim(bottom=0)
        a.set_xlim(left=0)
        a.yaxis.get_major_locator().set_params(integer=True)
        a.xaxis.get_major_locator().set_params(integer=True)
        a.legend()
        mycanvas = FigureCanvasTkAgg(draw_graph.f, root_window)
        mycanvas.draw()
        mycanvas.get_tk_widget().place(x=450, y =225)

    draw_graph()

    insight_window.s_name = StringVar()
    label = Label(textvariable=insight_window.s_name, bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')
    label.place(
        x = 373, y = 63,
        width = 870,
        height = 82)
    insight_window.s_name.set(select_insight.mySessions[select_insight.var.get()-1].name)

    insight_window.no_of_rev = StringVar()
    label = Label(textvariable=insight_window.no_of_rev, bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')
    label.place(
        x = 156, y = 394,
        width = 100,
        height = 80)
    insight_window.no_of_rev.set(select_insight.mySessions[select_insight.var.get()-1].no_of_revisions-1)
    #insight_window.no_of_rev.set(4) #dummy

    insight_window.rev_date = StringVar()
    label = Label(textvariable=insight_window.rev_date, bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')
    label.place(
        x = 59, y = 770,
        width = 300,
        height = 80)
    insight_window.rev_date.set((Reminder_System.show_specific_reminder_next_date(select_insight.mySessions[select_insight.var.get()-1].name)).strftime('%d-%m-%Y'))
    #insight_window.rev_date.set('08-12-2022') #dummy


    def clear_and_go_back():
        draw_graph.f.clear()
        plt.close(draw_graph.f)
        load_select_insight()

    btn_ok = PhotoImage(file = f"./insight_window/img0.png")
    b0 = Button(
        image = btn_ok,
        borderwidth = 0,
        highlightthickness = 0, bg='#d9e8f5',
        command = clear_and_go_back,
        relief = "flat")

    b0.place(
        x = 602, y = 880,
        width = 236,
        height = 89)


def revisions_for_today(root_window):
    global background_img, btn_go_back, btn_revise
    canvas9 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas9.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./revisions_for_today/background.png")
    background = canvas9.create_image(
        720, 420,
        image=background_img)

    wrapper = LabelFrame(root_window, bg = '#D9E8F5', height=607, width=1266, border=10)
    wrapper.place(x=85, y=200)

    new_canvas = Canvas(wrapper, height=607, width=1266, bg='#D9E8F5')
    new_canvas.pack(side=LEFT)

    yscrollbar = Scrollbar(wrapper, orient='vertical', command=new_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    new_canvas.config(yscrollcommand=yscrollbar.set, scrollregion=new_canvas.bbox('all'))
    new_canvas.bind('<Configure>', lambda e: new_canvas.configure(scrollregion = new_canvas.bbox('all')))

    myframe = Frame(new_canvas, height=607, width=1266, bg='#D9E8F5')
    new_canvas.create_window((0,0), window=myframe, anchor='nw')

    refresh_data()
    revisions_for_today.todaySessions = Reminder_System.check_any_reminder_today(Reminder_System.dummyDate)
    #revisions_for_today.todaySessions = Reminder_System.check_any_reminder_today()


    revisions_for_today.var = IntVar()

    for i in range(len(revisions_for_today.todaySessions)):
        Radiobutton(myframe, text=revisions_for_today.todaySessions[i], variable=revisions_for_today.var, value=i+1,
        bg = "#D9E8F5", highlightthickness = 0, font=('Lato', 27, 'bold'), 
        fg='#304269', indicatoron=0, background='#D9E8F5', bd=0).pack(anchor='w')

    btn_go_back = PhotoImage(file = f"./revisions_for_today/img0.png")
    b0 = Button(
        image = btn_go_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_main_window,
        relief = "flat")

    b0.place(
        x = 878, y = 862,
        width = 275,
        height = 104)

    def rate_effectiveness_loader():
        if revisions_for_today.var.get() > 0:
            load_rate_effectiveness()
        else:
            pass

    btn_revise = PhotoImage(file = f"./revisions_for_today/img1.png")
    b1 = Button(
        image = btn_revise,
        borderwidth = 0,
        highlightthickness = 0,
        command = rate_effectiveness_loader,
        relief = "flat")

    b1.place(
        x = 303, y = 862,
        width = 275,
        height = 104)

def rate_effectiveness(root_window):
    global background_img, btn_done, btn_go_back, img2, img3, img4, img5, img6, img7, img8
    rate_effectiveness.var = IntVar()
    canvas10 = Canvas(
        root_window,
        bg = "#d9e8f5",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas10.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./rate_effectiveness/background.png")
    background = canvas10.create_image(
        720, 300,
        image=background_img)

    session_name = StringVar()
    label = Label(textvariable=session_name, bd = 0,
        bg = "#ffffff",
        highlightthickness = 0, font=('Lato', 30, 'bold'), fg='#304269')
    label.place(
        x = 525, y = 95,
        width = 810,
        height = 82)
    session_name.set(revisions_for_today.todaySessions[revisions_for_today.var.get()-1])

    btn_go_back = PhotoImage(file = f"./rate_effectiveness/img0.png")
    b0 = Button(
        image = btn_go_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = load_revisions_for_today,
        relief = "flat")

    b0.place(
        x = 903, y = 844,
        width = 236,
        height = 89)

    def revised_session_successful(): 
        confi_score = rate_effectiveness.var.get()
        if confi_score in [1,2,3,4,5]:
            print(confi_score)
            Reminder_System.revised_today(revisions_for_today.todaySessions[revisions_for_today.var.get()-1], confi_score)
            messagebox.showinfo('Revision Details', 'Updated revision details successfully!')
            load_revisions_for_today()
        else:
            messagebox.showinfo('Error', 'Please select your revision effectiveness level!')

    btn_done = PhotoImage(file = f"./rate_effectiveness/img1.png")
    b1 = Button(
        image = btn_done,
        borderwidth = 0,
        highlightthickness = 0,
        command = revised_session_successful,
        relief = "flat")

    b1.place(
        x = 332, y = 844,
        width = 236,
        height = 84)

    img2 = PhotoImage(file = f"./rate_effectiveness/img2.png")
    img3 = PhotoImage(file = f"./rate_effectiveness/img3.png")

    global is_on
    is_on = False

    def toggle_command():
        global is_on
        if is_on:
            toggle.config(image=img2)
            r1.configure(state=DISABLED, selectcolor='#D9E8F5')
            r2.configure(state=DISABLED, selectcolor='#D9E8F5')
            r3.configure(state=DISABLED, selectcolor='#D9E8F5')
            r4.configure(state=DISABLED, selectcolor='#D9E8F5')
            r5.configure(state=DISABLED, selectcolor='#D9E8F5')
            is_on = False
        else:
            toggle.config(image=img3)
            r1.configure(state=NORMAL, selectcolor='#304269')
            r2.configure(state=NORMAL, selectcolor='#304269')
            r3.configure(state=NORMAL, selectcolor='#304269')
            r4.configure(state=NORMAL, selectcolor='#304269')
            r5.configure(state=NORMAL, selectcolor='#304269')
            is_on = True

    toggle = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        activebackground = '#D9E8F5',
        command = toggle_command,
        relief = "flat", bg='#D9E8F5')

    toggle.place(
        x = 704, y = 255,
        width = 128,
        height = 128)

    frame = Frame(canvas10, height= 125, width=895, bg='#D9E8F5')
    frame.place(x=320, y=598)

    img4 = PhotoImage(file = f"./rate_effectiveness/1.png")
    img5 = PhotoImage(file = f"./rate_effectiveness/2.png")
    img6 = PhotoImage(file = f"./rate_effectiveness/3.png")
    img7 = PhotoImage(file = f"./rate_effectiveness/4.png")
    img8 = PhotoImage(file = f"./rate_effectiveness/5.png")


    r1 = Radiobutton(frame, image=img4,variable=rate_effectiveness.var, value=1, state=DISABLED,
        highlightthickness = 0, selectcolor='#304269',activebackground='#D9E8F5', 
        indicatoron=0, background='#D9E8F5', bd=0)
    r1.pack(padx=10, side=LEFT)
    r2 = Radiobutton(frame, image=img5, variable=rate_effectiveness.var, value=2, state=DISABLED,
        highlightthickness = 0, selectcolor='#304269',activebackground='#D9E8F5',
        indicatoron=0, background='#D9E8F5', bd=0)
    r2.pack(padx=10, side=LEFT)
    r3 = Radiobutton(frame, image=img6, variable=rate_effectiveness.var, value=3, state=DISABLED,
        highlightthickness = 0, selectcolor='#304269',activebackground='#D9E8F5',
        indicatoron=0, background='#D9E8F5', bd=0)
    r3.pack(padx=10, side=LEFT)
    r4 = Radiobutton(frame, image=img7, variable=rate_effectiveness.var, value=4, state=DISABLED,
        highlightthickness = 0, selectcolor='#304269',activebackground='#D9E8F5',
        indicatoron=0, background='#D9E8F5', bd=0)
    r4.pack(padx=10, side=LEFT)
    r5 = Radiobutton(frame, image=img8, variable=rate_effectiveness.var, value=5, state=DISABLED,
        highlightthickness = 0, selectcolor='#304269',activebackground='#D9E8F5',
        indicatoron=0, background='#D9E8F5', bd=0)
    r5.pack(padx=10, side=LEFT) 

def refresh_data():
    Sessions_Control.load_all_sess_from_db()
    Reminder_System.load_rem_data_from_db()

def check_for_today():
    sess = Reminder_System.check_any_reminder_today()
    if len(sess) > 0:
        for i in range(len(sess)):
            Reminder_System.notify(sess[i])

#schedule.every(5).hours.do(check_for_today)
schedule.every().day.at('05:00').do(check_for_today)
schedule.every().day.at('06:00').do(check_for_today)
schedule.every().day.at('07:00').do(check_for_today)
schedule.every().day.at('08:00').do(check_for_today)
schedule.every().day.at('09:00').do(check_for_today)
schedule.every().day.at('10:00').do(check_for_today)
schedule.every().day.at('11:00').do(check_for_today)
schedule.every().day.at('12:00').do(check_for_today)
schedule.every().day.at('13:00').do(check_for_today)
schedule.every().day.at('14:00').do(check_for_today)
schedule.every().day.at('15:00').do(check_for_today)
schedule.every().day.at('16:00').do(check_for_today)
schedule.every().day.at('17:00').do(check_for_today)
schedule.every().day.at('18:00').do(check_for_today)
schedule.every().day.at('19:00').do(check_for_today)
schedule.every().day.at('20:00').do(check_for_today)
schedule.every().day.at('21:00').do(check_for_today)
schedule.every().day.at('22:00').do(check_for_today)
#schedule.every(5).seconds.do(check_for_today)

def start():
    while True:
        schedule.run_pending()
        time.sleep(1)

th = threading.Thread(target=start)
th.start()

main_window(root)

root.resizable(False, False)
root.mainloop()
