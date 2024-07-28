import time
from tkinter import *
from tkinter import messagebox

clockWindow = Tk()
clockWindow.geometry("500x500")
clockWindow.title("Countdown Timer")
clockWindow.configure(background='red')

hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

hourString.set("00")
minuteString.set("00")
secondString.set("00")

hourTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=hourString)
minuteTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=minuteString)
secondTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=secondString)

hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)

def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    while(clockTime > -1):
        
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if(totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        clockWindow.update()
        time.sleep(1)

        if(clockTime == 0):
            messagebox.showinfo("", "Time Over!!")

        clockTime -= 1


setTimeButton = Button(clockWindow, text='Set Time', bd='5', command=runTimer)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

clockWindow.mainloop()