#Import Module
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image
from sistemLogin import sistemLogin
import re  



# Fungsi VerifikasiLogin untuk menverifikasi inputan pengguna mengenai akunnya
def VerifikasiLogin():
    email = Inputemail.get()
    password = InputPassword.get()
    infologin = sistemLogin(email,password)
    loginsukses = infologin.ceklogin()

 
    if(email == "" and password == "") :
        mb.showinfo("Peringatan", "Silahkan masukkan Username dan Password Anda!")
 
 
    elif(loginsukses):
 
        mb.showinfo("Login Berhasil","Selamat Datang!")
        HalamanLogin.destroy()
 
    else :
        mb.showinfo("Login Gagal","Username atau Password Salah!")




# Fungsi ValidasiRegister & ValidasiRegister untuk menverifikasi inputan register pengguna baru
Katakunci = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
def ValidasiRegister(email):   
  
    if(re.search(Katakunci,email)):   
        return True   
    else:   
        return False  

def VerifikasiRegister():
    password = InputPassword.get()
    email = Inputemail.get()
    ValidasiRegisterSukses = ValidasiRegister(email) 
        
    if (ValidasiRegisterSukses):
        mb.showinfo("Register Berhasil","Klik Tombol OK!")
        HalamanLogin.destroy()
    else:
        mb.showinfo("Register Gagal","Email Kurang @!") 

        


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
global Inputemail
global InputPassword




# Menampilkan dan mengatur posisi text pada UI
Label(HalamanLogin, bg='#223441', fg='#F5F5F5', text="Silahkan Masuk!").place(x=110, y=0) 
Label(HalamanLogin, bg='#223441', fg='#F5F5F5', text="Email").place(x=25, y=30)
Label(HalamanLogin, bg='#223441', fg='#F5F5F5', text="Password").place(x=25, y=60)

# Menampilkan dan mengatur posisi textbox pada UI
Inputemail = Entry(HalamanLogin) #Textbox Username
Inputemail.place(x=140, y=30)
 
InputPassword = Entry(HalamanLogin) #Texbox Password
InputPassword.place(x=140, y=60)
InputPassword.config(show="*")
 
# Menampilkan dan mengatur posisi serta fungsi tombol pada UI 
Button(HalamanLogin, text="Login", command=VerifikasiLogin ,height = 1, width = 10).place(x=60, y=100)
Button(HalamanLogin, text="Register", command=VerifikasiRegister ,height = 1, width = 10).place(x=160, y=100)
 



# Program berjalan
HalamanLogin.mainloop()