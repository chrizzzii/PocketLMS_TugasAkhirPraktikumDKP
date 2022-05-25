from tkinter import *
from tkinter import messagebox as mb

#Program Utama
#Mendefinisikan window dan ukuran layar

ToDoList = Tk()
ToDoList.title("Pocket LMS")
ToDoList.config(bg='#223441')
ToDoList.resizable(width=False, height=False)

LebarJendelaAplikasi = 500
TinggiJendelaAplikasi = 450

LebarLayarPerangkat = ToDoList.winfo_screenwidth()
TinggiLayarPerangkat = ToDoList.winfo_screenheight()
#----------------------------------------------------------------------------------------------------#

#Mencari titik tengah pada layar dan Menset window program di tengah layar user
center_x = int(LebarLayarPerangkat/2 - LebarJendelaAplikasi / 2)
center_y = int(TinggiLayarPerangkat/2 - TinggiJendelaAplikasi / 2)
ToDoList.geometry(f'{LebarJendelaAplikasi}x{TinggiJendelaAplikasi}+{center_x}+{center_y}')
#----------------------------------------------------------------------------------------------------#

# Pembuatan frame sebagai tempat untuk box daftar tugas
frame = Frame(ToDoList)
frame.pack(pady=10)

# Pembuatan box daftar tugas di dalam frame
BoxDaftar = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
BoxDaftar.pack(side=LEFT, fill=BOTH)

DummyDaftarTugas = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas',
    ]


for DaftarTugas in DummyDaftarTugas:
    BoxDaftar.insert(END, DaftarTugas)

# Pembuatan scrollbar di sebelah box daftar tugas
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

BoxDaftar.config(yscrollcommand=sb.set)
sb.config(command=BoxDaftar.yview)

# Pembuatan box inputan pengguna
MasukkanPengguna = Entry(
    ToDoList,
    font=('times', 24)
    )
MasukkanPengguna.pack(pady=20)

# TOMBOL
# Pembuatan frame
FrameTombol = Frame(ToDoList)
FrameTombol.pack(pady=20)

# Pembuatan fungsi dan pemosisian
def newTask():
    task = MasukkanPengguna.get()
    if task != "":
        BoxDaftar.insert(END, task)
        MasukkanPengguna.delete(0, "end")
    else:
        mb.showwarning("warning", "Please enter some task.")

def deleteTask():
    BoxDaftar.delete(ANCHOR)

addTask_btn = Button(
    FrameTombol,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    FrameTombol,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Menjalankan program
ToDoList.mainloop()
# SELESAI