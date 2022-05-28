# Import Library
from tkinter import *

# Set-up Library GUI 
Loading = Tk()
Loading.config(bg='#223441')
Loading.overrideredirect(True)



# Set-up Window Aplikasi Pocket LMS
LebarJendela = 320
TinggiJendela = 330

LebarLayar = Loading.winfo_screenwidth()
TinggiLayar = Loading.winfo_screenheight()

Tengah_x = int(LebarLayar/2 - LebarJendela / 2)
Tengah_y = int(TinggiLayar/2 - TinggiJendela / 2)

Loading.geometry(f'{LebarJendela}x{TinggiJendela}+{Tengah_x}+{Tengah_y}')



# Set-up UI
Judul=Label(Loading, bg='#223441', fg='#F5F5F5', text="Pocket LMS", font='Arial 17 bold')
Judul.place(relx=0.5, rely=0.5, anchor=CENTER)

Loading.after(10000, Loading.destroy)