# Import Library & Class
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import random
from PIL import ImageTk,Image
from ScriptLoading import *
from ScriptLogin import *

# Pembuatan Program

# Set-up Library GUI Aplikasi Pocket LMS
PocketLMS = Tk()
PocketLMS.title("Pocket LMS")
PocketLMS.config(bg='#223441')
PocketLMS.resizable(width=False, height=False)

# Set-up Window Aplikasi Pocket LMS
LebarJendelaAplikasi = 320
TinggiJendelaAplikasi = 330

LebarLayarPerangkat = PocketLMS.winfo_screenwidth()
TinggiLayarPerangkat = PocketLMS.winfo_screenheight()

Tengah_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi/2)
Tengah_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi/2)
PocketLMS.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{Tengah_x}+{Tengah_y}')




# Fungsi Pemanggilan Halaman Aplikasi

    

def PanggilJadwal():
    class TabelJadwal:
    # Set-up Constructor
        def __init__(self, Jadwal):
            # Set-up Tabel
            for i in range(TotalBaris):
                for j in range(TotalKolom):
                    if i == 0:
                        self.entry = Entry(Jadwal, width=21, bg='#223441',fg='white',
                                        font=('Times New Roman', 16, 'bold'))
                    else:
                        self.entry = Entry(Jadwal, width=21, bg='#223441', fg='white',
                                font=('Calibri', 16))

                    self.entry.grid(row=i, column=j)
                    self.entry.insert(END, DaftarJadwal[i][j])


    # Data Tabel Jadwal
    DaftarJadwal = [('No', 'Mata Kuliah', 'Kelas', 'SKS'),
            (1, 'Algortima & Pemrograman', 'B', 2),
        (2, 'Praktikum Fisika Dasar I', 'A', 1),
        (3, 'Elektronika Dasar', 'B', 3),
        (4, 'Aljabar Linier', 'B', 4),
        (5, 'Internet of Things', 'B', 2),
        (6, 'Kimia', 'A', 4),
        (7, 'Fisika Dasar II', 'B', 3),
        (8, 'Matematika Teknik', 'B', 4),
        (9, 'Praktikum DKP', 'B', 1)]

    # Mencari total nomor Baris dan Kolom di dalam List
    TotalBaris = len(DaftarJadwal)
    TotalKolom = len(DaftarJadwal[0])

    # Program Jadwal Berjalan
    Jadwal = Tk()
    Jadwal.title("Pocket LMS")
    LebarJendelaAplikasi = 900
    TinggiJendelaAplikasi = 295

    LebarLayarPerangkat = Jadwal.winfo_screenwidth()
    TinggiLayarPerangkat = Jadwal.winfo_screenheight()

    Tengah_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi/2)
    Tengah_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi/2)
    Jadwal.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{Tengah_x}+{Tengah_y}')

    PanggilTabelJadwal = TabelJadwal(Jadwal)
    Jadwal.mainloop()

def PanggilAbsen():
        # Fungsi VerifikasiAbsen untuk menverifikasi inputan user mengenai kode absen
    def VerifikasiAbsen():
        VerifikasiKodeAbsen = InputKodeAbsen.get()

        if(VerifikasiKodeAbsen == KodeAbsenGenerator) :
            mb.showinfo("Absen Berhasil","Absen Telah Tercatat!")
            Absen.destroy()

        elif(VerifikasiKodeAbsen == "") :
            mb.showinfo("Peringatan", "Silahkan masukkan kode absen!")

        else :
            mb.showinfo("Absen Gagal","Kode absen salah!")



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
    KodeAbsenGenerator = str((random.randint(1, 9)))
    
     
     
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

def PanggilTodoList():
    # Set-up Library GUI
    ToDoList = Tk()
    ToDoList.title("Pocket LMS")
    ToDoList.config(bg='#223441')
    ToDoList.resizable(width=False, height=False)

    # Set-up Window
    LebarJendelaAplikasi = 500
    TinggiJendelaAplikasi = 450

    LebarLayarPerangkat = ToDoList.winfo_screenwidth()
    TinggiLayarPerangkat = ToDoList.winfo_screenheight()

    Tengah_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi / 2)
    Tengah_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi / 2)
    ToDoList.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{Tengah_x}+{Tengah_y}')




    # Frame sebagai tempat untuk box daftar tugas
    frame = Frame(ToDoList)
    frame.pack(pady=10)

    # Box daftar tugas di dalam frame
    BoxDaftar = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=3,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#223441',
        activestyle="none",
        
    )
    BoxDaftar.pack(side=LEFT, fill=BOTH)

    # Data Dummy ToDoList
    DummyDaftarTugas = [
        'Bermain tic tac toe',
        'Bermain puzzle',
        'Minum coklat panas',
        'Membaca buku',
        'Mengerjakan tugas',
        'Menyiram tanaman',
        'Belanja ke warung',
        'Belajar bersama',
        ]

    # Input Data Dummy ke BoxDaftar
    for DaftarTugas in DummyDaftarTugas:
        BoxDaftar.insert(END, DaftarTugas)



    # User Experience
    # Scrollbar di sebelah box daftar tugas
    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    BoxDaftar.config(yscrollcommand=sb.set)
    sb.config(command=BoxDaftar.yview)

    # Box inputan pengguna
    MasukkanPengguna = Entry(
        ToDoList,
        font=('times', 24)
        )
    MasukkanPengguna.pack(pady=20)

    # Frame Tombol
    FrameTombol = Frame(ToDoList, bg="#223441")
    FrameTombol.pack(pady=20)

    # Fungsi dan pemosisian
    def TambahTugas():
        Tugas = MasukkanPengguna.get()
        if Tugas != "":
            BoxDaftar.insert(END, Tugas) # END agar Tugas baru ditambahkan di baris bawah
            MasukkanPengguna.delete(0, "end")
        else:
            mb.showwarning("Peringatan", "Isian masih kosong!")

    def HapusTugas():
        BoxDaftar.delete(ANCHOR) # Akhir Fungsi

    TombolHapusTugas = Button(
        FrameTombol,
        text='Hapus Tugas',
        font=('calibri, 12'),
        bg='#ff4040',
        padx=20,
        pady=10,
        command = HapusTugas
    )
    TombolHapusTugas.pack(fill=BOTH, expand=True, side=LEFT, padx= 12) # pemosisian TombolHapusTugas

    TombolTambahTugas = Button(
        FrameTombol,
        text='Tambah Tugas',
        font=('calibri, 12'),
        bg='#5ca904',
        padx=20,
        pady=10,
        command = TambahTugas
    )
    TombolTambahTugas.pack(fill=BOTH, expand=True, side=LEFT, padx= 12) # pemosisian TombolTambahTugas




    # Menjalankan program
    ToDoList.mainloop()

def PanggilInfo():
    Info = Tk()
    Info.title("Pocket LMS")
    Info.config(bg='#223441')
    Info.resizable(width=False, height=False)

    LebarJendelaAplikasi = 320
    TinggiJendelaAplikasi = 330

    LebarLayarPerangkat = Info.winfo_screenwidth()
    TinggiLayarPerangkat = Info.winfo_screenheight()
    #----------------------------------------------------------------------------------------------------#

    #Mencari titik tengah pada layar dan Menset window program di tengah layar user
    center_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi / 2)
    center_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi / 2)
    Info.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{center_x}+{center_y}')



    # FrameContent sebagai tempat content absensi
    FrameContent = Frame(Info, bg="#223441")
    FrameContent.pack(pady= 100)

    Label(FrameContent, bg='#223441', fg='#F5F5F5', font = ('calibri', 14, 'bold'), text="Info Aplikasi").pack()
    Label(FrameContent, bg='#223441', fg='#F5F5F5', font = ('calibri', 12), text="Pocket LMS (Learning Management System)").pack()
    Label(FrameContent, bg='#223441', fg='#F5F5F5', font = ('calibri', 12), text="Versi : 1.0 Beta Version").pack()
    Label(FrameContent, bg='#223441', fg='#F5F5F5', font = ('calibri', 12), text="Desktop Mode").pack()
    



    Info.mainloop()




# Variabel Gambar
IconHeaderPocketLMS = ImageTk.PhotoImage(Image.open('HeaderPocketLMS.jpg'))
IconProfil = ImageTk.PhotoImage(Image.open('Info.png'))
IconTDL = ImageTk.PhotoImage(Image.open('ToDoList.png'))
IconJadwal = ImageTk.PhotoImage(Image.open('Jadwal.png'))
IconAbsen = ImageTk.PhotoImage(Image.open('Absen.png'))

# Frame Header Utama
FrameHeader = LabelFrame(PocketLMS, text="Pocket Learning Management System",bg="#0079fe",pady=5)
FrameHeader.pack(fill= BOTH)
HeaderPocketLMS = Label(FrameHeader, image = IconHeaderPocketLMS, height = 150, width = 300)
HeaderPocketLMS.pack(side=LEFT, padx= 10)

# Frame Icon Aplikasi
FrameAplikasi = Frame(PocketLMS,pady=45)
FrameAplikasi.pack(fill= BOTH)

# Icon Aplikasi
TombolJadwal = Button(FrameAplikasi, text="Jadwal", image = IconJadwal, height = 50, width = 50, command = PanggilJadwal) #Icon Jadwal
TombolJadwal.pack(side=LEFT, padx= 10)

TombolProfil = Button(FrameAplikasi, text="Absen", image = IconProfil, height = 50, width = 50, command = PanggilInfo) #Icon Profil
TombolProfil.pack(side=RIGHT, padx= 10)

TombolAbsen = Button(FrameAplikasi, text="ToDoList", image = IconAbsen, height = 50, width = 50, command = PanggilAbsen) #Icon Absen  
TombolAbsen.pack(side=LEFT, padx= 10)

TombolToDoList = Button(FrameAplikasi, text="Profil", image = IconTDL, height = 50, width = 50, command = PanggilTodoList) #Icon ToDoList
TombolToDoList.pack(side=RIGHT, padx= 10)


# Program Berjalan
HalamanLogin.mainloop()
if(VerifikasiLogin==True):
    HalamanLogin.destroy()
else:
    False
# Program Selesai