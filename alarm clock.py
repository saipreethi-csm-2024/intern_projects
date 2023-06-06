from tkinter.ttk import *
from tkinter import *
from pygame import mixer
from datetime import datetime
from time import sleep
from threading  import Thread

        
#colors
bg_color='#FF8000'
col='#0000CD'
co2='#FFFFFF'
        
#window
window=Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)
        
#frame up
frame_line=Frame(window,width=400,height=5,bg=col)
frame_line.grid(row=0,column=0)
        
frame_body=Frame(window,width=400,height=290,bg=co2)
frame_body.grid(row=1,column=0)
        
name=Label(frame_body,text="Alarm clock",height=1,font=('Ivy 18 bold'),bg=co2,fg=bg_color)
name.place(x=110,y=5)
        
hour=Label(frame_body,text="hour",height=1,font=('Ivy 10 bold'),bg=co2,fg=col)
hour.place(x=10,y=40)
c_hour=Combobox(frame_body,width=2,font=('arial 10'))
c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=8,y=60)
        
min=Label(frame_body,text="min",height=1,font=('arial 10'),bg=co2,fg=col)
min.place(x=100,y=40)
c_min=Combobox(frame_body,width=2,font=('arial 10'))
c_min['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","57","58","55","56")
c_min.current(0)
c_min.place(x=100,y=60)
        
sec=Label(frame_body,text="sec",height=1,font=('arial 10'),bg=co2,fg=col)
sec.place(x=200,y=40)
c_sec=Combobox(frame_body,width=2,font=('arial 10'))
c_sec['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12",)
c_sec.current(0)
c_sec.place(x=200,y=60)
        
period=Label(frame_body,text="period",height=1,font=('arial 10'),bg=co2,fg=col)
period.place(x=300,y=40)
c_period=Combobox(frame_body,width=2,font=('arial 10'))
c_period['values']=("AM",'PM')
c_period.current(0)
c_period.place(x=300,y=60)
        
def activate_alarm():
    t=Thread(target=alarm)
    t.start()
def deactivate_alarm():
    print('deactivated alarm:',selected.get())
    mixer.music.stop()
selected=IntVar()
        
rad1=Radiobutton(frame_body,font=('airal 10 bold'),value=1,text="activate",bg=co2,fg=bg_color,command=activate_alarm,variable=selected)
rad1.place(x=70,y=95)
        
def sound_alarm():
    mixer.music.load('embrace-12278.mp3')
    mixer.music.play()
    selected.set(0)

    rad2=Radiobutton(frame_body,font=('airal 10 bold'),value=2,text="activate",bg=co2,fg=bg_color,command=deactivate_alarm,variable=selected)
    rad2.place(x=70,y=95)
def alarm():
    while True:
        control=1
        
        alarm_hour="12"
        alarm_min="07"
        alarm_sec="00"
        alarm_period="PM"
               
        now=datetime.now()
        
        hour=now.strftime("%H")
        minute=now.strftime("%M")
        second=now.strftime("%S")
        period=now.strftime("%p")
        
        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_min==minute:
                        if alarm_sec==second:
                            if alarm_period==period:
                                print("time to take a bresk")
                                sound_alarm()
        
                    
        sleep(1)
            
            
mixer.init()
sound_alarm()
        
        
window.mainloop()
        
        
        
        
    