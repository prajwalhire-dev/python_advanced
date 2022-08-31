from tkinter import Label, Tk
import time

#define title and size of application
app_window = Tk()
app_window.title("Digital clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

#define the font of the time, its color,its border width and the background color of the digital clock
text_font = ('Boulder',68,'bold')
background = '#f2e750'
foreground = '#363529'
border_width = 25

#will combine all the above elements to define the label of e clock application
label = Label(app_window, font=text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

#define main function of our digital clock
def digital_clock():
    time_live = time.strftime("%H:%M:%S") 
    label.config(text=time_live)
    label.after(200, digital_clock) #200 is milli seconds and a funtion is added beside it, such that to call the function after the 200 ms

#lets run and see the output
digital_clock() #calling the function
app_window.mainloop() # here mainloop means - tells the python to run the Tkinter event loop, like it will loop forever until the user exits the window
