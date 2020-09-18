import tkinter as tk
from tkinter import Frame
from data import convert_data

root = tk.Tk()
root.title('DMFC')
root.geometry('{}x{}'.format(500, 350))
root.maxsize(500, 350)

top = Frame(root, bg='lightgrey', width=500, height=100)

top.grid(row=0)

label_1 = tk.Label(top, pady=10, text="Cell Temperature Anode", bg='lightgrey')
label_2 = tk.Label(top, pady=10, text="Molarity", bg='lightgrey')
label_3 = tk.Label(top, pady=10, text="Flowrate Anode", bg='lightgrey')
label_4 = tk.Label(top, pady=10, text="Channel Width", bg='lightgrey')
label_5 = tk.Label(top, pady=10, text="Channel Height", bg='lightgrey')
label_6 = tk.Label(top, pady=10, text="Channel Length", bg='lightgrey')
label_7 = tk.Label(top, pady=10, text="Number of Channels", bg='lightgrey')

label_1_unit = tk.Label(top, pady=10, text="°C", bg='lightgrey')
label_2_unit = tk.Label(top, pady=10, text="mol/l", bg='lightgrey')
label_3_unit = tk.Label(top, pady=10, text="ml/min", bg='lightgrey')
label_4_unit = tk.Label(top, pady=10, text="mm", bg='lightgrey')
label_5_unit = tk.Label(top, pady=10, text="mm", bg='lightgrey')
label_6_unit = tk.Label(top, pady=10, text="mm", bg='lightgrey')
label_7_unit = tk.Label(top, pady=10, text="", bg='lightgrey')


label_1.grid(row=1, column=0, padx=20, sticky="w")
label_2.grid(row=2, column=0, padx=20, sticky="w")
label_3.grid(row=3, column=0, padx=20, sticky="w")
label_4.grid(row=4, column=0, padx=20, sticky="w")
label_5.grid(row=5, column=0, padx=20, sticky="w")
label_6.grid(row=6, column=0, padx=20, sticky="w")
label_7.grid(row=7, column=0, padx=20, sticky="w")

label_1_unit.grid(row=1, column=2, padx=20, sticky="w")
label_2_unit.grid(row=2, column=2, padx=20, sticky="w")
label_3_unit.grid(row=3, column=2, padx=20, sticky="w")
label_4_unit.grid(row=4, column=2, padx=20, sticky="w")
label_5_unit.grid(row=5, column=2, padx=20, sticky="w")
label_6_unit.grid(row=6, column=2, padx=20, sticky="w")
label_7_unit.grid(row=7, column=2, padx=20, sticky="w")

cta = tk.DoubleVar()
cta.set(65)
entry_1 = tk.Entry(top, width=30, bd=5, textvariable=cta)
mol = tk.DoubleVar()
mol.set(1)
entry_2 = tk.Entry(top, width=30, bd=5, textvariable=mol)
fra = tk.DoubleVar()
fra.set(5)
entry_3 = tk.Entry(top, width=30, bd=5, textvariable=fra)
chw = tk.DoubleVar()
chw.set(1)
entry_4 = tk.Entry(top, width=30, bd=5, textvariable=chw)
chh = tk.DoubleVar()
chh.set(1)
entry_5 = tk.Entry(top, width=30, bd=5, textvariable=chh)
chl = tk.DoubleVar()
chl.set(1000)
entry_6 = tk.Entry(top, width=30, bd=5, textvariable=chl)
chn = tk.DoubleVar()
chn.set(1)
entry_7 = tk.Entry(top, width=30, bd=5, textvariable=chn)

entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
entry_3.grid(row=3, column=1)
entry_4.grid(row=4, column=1)
entry_5.grid(row=5, column=1)
entry_6.grid(row=6, column=1)
entry_7.grid(row=7, column=1)

button_1 = \
        tk.Button(top, text='OK', width=20, bd=5,
                  command=lambda: convert_data(entry_1.get(), entry_2.get(),
                                               entry_3.get(), entry_4.get(),
                                               entry_5.get(), entry_6.get(),
                                               entry_7.get()))

button_1.grid(row=8, column=1)

root.mainloop()