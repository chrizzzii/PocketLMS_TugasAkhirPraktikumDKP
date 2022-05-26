#Import Module
from tkinter import *
from tkinter import messagebox as mb
from sistemLogin import sistemLogin
from PIL import ImageTk,Image

# Fungsi VerifikasiLogin untuk menverifikasi inputan user mengenai akunnya
def VerifikasiLogin():
    username = InputUsername.get()
    password = InputPassword.get()
    infologin = sistemLogin(username,password)
    loginsukses = infologin.ceklogin()
    panggilsambutan = infologin.sambutan()

 
    if(username == "" and password == "") :
        mb.showinfo("Peringatan", "Silahkan masukkan Username dan Password Anda!")
 
 
    elif(loginsukses):
 
        mb.showinfo("Login Berhasil","Halo " + panggilsambutan)
        HalamanLogin.destroy()
 
    else :
        mb.showinfo("Login Gagal","Username atau Password Salah!")


# Program Utama
# Set-up Library GUI
HalamanLogin = Tk()
HalamanLogin.title("Pocket LMS")
HalamanLogin.config(bg='#223441')
HalamanLogin.resizable(width=False, height=False)

# Set-up Window
LebarJendelaAplikasi = 300
TinggiJendelaAplikasi = 200

LebarLayarPerangkat = HalamanLogin.winfo_screenwidth()
TinggiLayarPerangkat = HalamanLogin.winfo_screenheight()

Tengah_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi / 2)
Tengah_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi / 2)
HalamanLogin.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{Tengah_x}+{Tengah_y}')




# Variabel global agar dapat diakses oleh function VerifikasiLogin()
global InputUsername
global InputPassword




# Menampilkan dan mengatur posisi text pada UI
Label(HalamanLogin, bg='#223441', fg='#F5F5F5', text="Silahkan Login!").place(x=110, y=0) 
Label(HalamanLogin, bg='#223441', fg='#F5F5F5', text="Username").place(x=25, y=30)
Label(HalamanLogin, bg='#223441', fg='#F5F5F5', text="Password").place(x=25, y=60)

# Menampilkan dan mengatur posisi textbox pada UI
InputUsername = Entry(HalamanLogin) #Textbox Username
InputUsername.place(x=140, y=30)
 
InputPassword = Entry(HalamanLogin) #Texbox Password
InputPassword.place(x=140, y=60)
InputPassword.config(show="*")
 
# Menampilkan dan mengatur posisi serta fungsi tombol pada UI 
Button(HalamanLogin, text="Login", command=VerifikasiLogin ,height = 1, width = 10).place(x=25, y=100)
 



# Program berjalan
HalamanLogin.mainloop()