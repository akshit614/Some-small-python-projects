
# ******** This is a program if you shutdown, Restart, Restart in some time using python ***********


from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="skyblue")

shut_button = Button(st,text="Restart", font=("Time New Roman","30","bold"),relief=RAISED, cursor="plus",command=restart,)
shut_button.place(x=180,y=60,height=40,width=150)

rt_button = Button(st,text="Restart Time", font=("Time New Roman","10","bold"),relief=RAISED, cursor="plus",command=restart_time)
rt_button.place(x=180,y=170,height=40,width=150)

lg_button = Button(st,text="Log Out", font=("Italic","20","bold"),relief=RAISED, cursor="plus",command=logout)
lg_button.place(x=180,y=270,height=40,width=150)

st_button = Button(st,text="Shut Down", font=("Italic","15","bold"),relief=RAISED, cursor="plus",command=shutdown)
st_button.place(x=180,y=370,height=40,width=150)


st.mainloop()