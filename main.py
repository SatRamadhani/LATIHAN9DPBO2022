# Saya [Muhammad Satria Ramadhani - 2005128] mengerjakan evaluasi [Latihan
# Praktikum 09] dalam mata kuliah [Desain dan Pemrograman Berorientasi Objek]
# untuk keberkahan-Nya, maka saya tidak melakukan kecurangan seperti yang
# telah dispesifikasikan. Aamiin.

# Import library.
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# Residences as global variable of array.
hunians = []
hunians.append(Apartemen("Saul Goodman", 3, 3, 500))
hunians.append(Rumah("Gustavo Fring", 5, 2, 40))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 100))
hunians.append(Rumah("Mike Ehrmantraut", 1, 4, 60))
hunians.append(Indekos("Techi", "Aldian Hamard", 1000))

# Root document.
root = Tk()
root.title("Latihan Praktikum 9 - DPBO")

# Get details.
def details(index):
    # Create sub-frame.
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # Create internal frame(?).
    d_frame = LabelFrame(top, text = "Data Residen", padx = 10, pady = 10)
    d_frame.pack(padx = 10, pady = 10)

    # Generate summary.
    d_summary = Label(d_frame, text = "Summary\n\n" + "Nama pemilik : " + hunians[index].get_nama_pemilik() + ".\n" + hunians[index].get_summary() + "Dokumen\n" + hunians[index].get_dokumen(), anchor = "w").grid(row = 0, column = 0, sticky = "w")

    # Create internal exit button.
    b_d_exit = Button(d_frame, text = "Exit", command = top.destroy)
    b_d_exit.grid(row = 1, column = 0, pady = 10)

# Create main frame.
frame = LabelFrame(root, text = "Data Seluruh Residen", padx = 10, pady = 10)
frame.pack(padx = 10, pady = 10)

# Create internal frame(?).
opts = LabelFrame(root, padx = 10, pady = 10)
opts.pack(padx = 10, pady = 10)

# Add data button (currently disabled).
b_add = Button(opts, text = "Add Data", state = "disabled")
b_add.grid(row = 0, column = 0)

# Add exit button.
b_exit = Button(opts, text = "Exit", command = root.quit)
b_exit.grid(row = 0, column = 1)

# Generate column's name.
title_no = Label(frame, text = "No", width = 5, borderwidth = 1, relief = "solid")
title_no.grid(row = 0, column = 0)
title_type = Label(frame, text = "Jenis Hunian", width = 15, borderwidth = 1, relief = "solid")
title_type.grid(row = 0, column = 1)
title_name = Label(frame, text = "Nama Pemilik", width = 25, borderwidth = 1, relief = "solid")
title_name.grid(row = 0, column = 2)

# Generate every data from array to frame.
for index, h in enumerate(hunians):
    # Generate number in first column.
    idx = Label(frame, text = str(index + 1), width = 5, borderwidth = 1, relief = "solid")
    idx.grid(row = (index + 1), column = 0)

    # Generate residence type in second column.
    type = Label(frame, text = h.get_jenis(), width = 15, borderwidth = 1, relief = "solid")
    type.grid(row = (index + 1), column = 1)

    # Generate data.
    if h.get_jenis() != "Indekos": 
        # Owner's name if the residence is not "Indekos".
        name = Label(frame, text = " " + h.get_nama_pemilik(), width = 25, borderwidth = 1, relief = "solid", anchor = "w")
        name.grid(row = (index + 1), column = 2)
    else:
        # Resident's name if the residence is "Indekos".
        name = Label(frame, text = " " + h.get_nama_penghuni(), width = 25, borderwidth = 1, relief = "solid", anchor = "w")
        name.grid(row = (index + 1), column = 2)

    # Create detail button.
    b_detail = Button(frame, text = "Details ", command = lambda index = index: details(index))
    b_detail.grid(row = (index + 1), column = 3)

# Execute main program(?).
root.mainloop()
