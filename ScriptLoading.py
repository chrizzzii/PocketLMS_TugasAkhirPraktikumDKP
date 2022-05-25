# Import Library & Class
from tkinter import *

 
Loading = Tk()
Loading.config(bg='#223441')
Loading.overrideredirect(True)

LebarJendela = 320
TinggiJendela = 330

# get the screen dimension
LebarLayar = Loading.winfo_screenwidth()
TinggiLayar = Loading.winfo_screenheight()

# find the center point
center_x = int(LebarLayar/2 - LebarJendela / 2)
center_y = int(TinggiLayar/2 - TinggiJendela / 2)

# set the position of the window to the center of the screen
Loading.geometry(f'{LebarJendela}x{TinggiJendela}+{center_x}+{center_y}')

Judul=Label(Loading, bg='#223441', fg='#F5F5F5', text="Pocket LMS", font='Arial 17 bold')
Judul.place(relx=0.5, rely=0.5, anchor=CENTER)

Loading.after(10000, Loading.destroy)