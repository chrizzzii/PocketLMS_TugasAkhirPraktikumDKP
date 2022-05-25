from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image
import random

# Fungsi VerifikasiAbsen untuk menverifikasi inputan user mengenai kode absen
def VerifikasiAbsen():
    VerifikasiKodeAbsen = int(InputKodeAbsen.get())
    
    if(VerifikasiKodeAbsen == KodeAbsenGenerator) :
        mb.showinfo("Berhasil","Absen Berhasil")
        Absen.destroy()

    elif(VerifikasiKodeAbsen == "") :
        mb.showinfo("Peringatan", "Silahkan masukkan kode absen!")

    else :
        mb.showinfo("Peringatan","Kode absen salah!")



# Set-up Library GUI
Absen = Tk()
Absen.title("Pocket LMS")
Absen.config(bg='#223441')
Absen.resizable(width=False, height=False)

# Set-up Window
LebarJendelaAplikasi = 320
TinggiJendelaAplikasi = 330

LebarLayarPerangkat = Absen.winfo_screenwidth()
TinggiLayarPerangkat = Absen.winfo_screenheight()

Tengah_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi / 2)
Tengah_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi / 2)
Absen.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{Tengah_x}+{Tengah_y}')




# Variabel global agar dapat diakses oleh function VerifikasiAbsen()
global InputKodeAbsen



# Generator random kode absen
KodeAbsenGenerator = (random.randint(1, 9))
    
     
     
# FrameContent sebagai tempat content absensi
FrameContent = Frame(Absen, bg="#223441")
FrameContent.pack(pady= 75)

Label(FrameContent, bg='#223441', fg='#F5F5F5', font = ('calibri', 14, 'bold'), text="Masukkan Kode Absen!").pack()
Label(FrameContent, bg='#223441', fg='#F5F5F5', font = ('calibri', 12), text=KodeAbsenGenerator).pack()
InputKodeAbsen = Entry(FrameContent)
InputKodeAbsen.pack()

Button(FrameContent, text="Absen", command=VerifikasiAbsen, width = 10).pack(pady=10)



# Program berjalan
Absen.mainloop()