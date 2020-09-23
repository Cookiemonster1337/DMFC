import tkinter as tk
from tkinter import Frame
from data import convert_data

root = tk.Tk()
root.title('DMFC')
root.geometry('{}x{}'.format(1000, 800))
#root.maxsize(1000, 800)

left = Frame(root, bg='lightgrey', width=500, height=800)
left.grid_propagate(0)
right = Frame(root, bg='lightgrey', width=500, height=800)
right.grid_propagate(0)

left.grid(row=0, column=0)
right.grid(row=0, column=1)

left.grid_rowconfigure(8, minsize=25)

# Labels
label_1 = tk.Label(left, pady=10, text="Cell Temperature Anode", bg='lightgrey')
label_2 = tk.Label(left, pady=10, text="Molarity", bg='lightgrey')
label_3 = tk.Label(left, pady=10, text="Flowrate Anode", bg='lightgrey')
label_4 = tk.Label(left, pady=10, text="Channel Width", bg='lightgrey')
label_5 = tk.Label(left, pady=10, text="Channel Height", bg='lightgrey')
label_6 = tk.Label(left, pady=10, text="Channel Length", bg='lightgrey')
label_7 = tk.Label(left, pady=10, text="Number of Channels", bg='lightgrey')

label_8 = tk.Label(left, pady=10, text="Current Density", bg='lightgrey')
label_9 = tk.Label(left, pady=10, text="Active Area", bg='lightgrey')

output_key = tk.StringVar()
output_label_key = tk.Label(right, pady=10, textvariable=output_key, bg='lightgrey', justify='left')
output_value = tk.StringVar()
output_label_value = tk.Label(right, pady=10, textvariable=output_value, bg='lightgrey', justify='right')
output_unit = tk.StringVar()
output_label_unit = tk.Label(right, pady=10, textvariable=output_unit, bg='lightgrey', justify='right')

label_1_unit = tk.Label(left, pady=10, text="°C", bg='lightgrey')
label_2_unit = tk.Label(left, pady=10, text="mol/l", bg='lightgrey')
label_3_unit = tk.Label(left, pady=10, text="ml/min", bg='lightgrey')
label_4_unit = tk.Label(left, pady=10, text="mm", bg='lightgrey')
label_5_unit = tk.Label(left, pady=10, text="mm", bg='lightgrey')
label_6_unit = tk.Label(left, pady=10, text="mm", bg='lightgrey')
label_7_unit = tk.Label(left, pady=10, text="", bg='lightgrey')

label_8_unit = tk.Label(left, pady=10, text="mA/cm2", bg='lightgrey')
label_9_unit = tk.Label(left, pady=10, text="cm2", bg='lightgrey')


label_1.grid(row=1, column=0, padx=20, sticky="w")
label_2.grid(row=2, column=0, padx=20, sticky="w")
label_3.grid(row=3, column=0, padx=20, sticky="w")
label_4.grid(row=4, column=0, padx=20, sticky="w")
label_5.grid(row=5, column=0, padx=20, sticky="w")
label_6.grid(row=6, column=0, padx=20, sticky="w")
label_7.grid(row=7, column=0, padx=20, sticky="w")

label_8.grid(row=9, column=0, padx=20, sticky="w")
label_9.grid(row=10, column=0, padx=20, sticky="w")

output_label_key.grid(row=1, column=0, padx=20, sticky="w")
output_label_value.grid(row=1, column=1, padx=20, sticky="w")
output_label_unit.grid(row=1, column=2, padx=20, sticky="w")

label_1_unit.grid(row=1, column=2, padx=20, sticky="w")
label_2_unit.grid(row=2, column=2, padx=20, sticky="w")
label_3_unit.grid(row=3, column=2, padx=20, sticky="w")
label_4_unit.grid(row=4, column=2, padx=20, sticky="w")
label_5_unit.grid(row=5, column=2, padx=20, sticky="w")
label_6_unit.grid(row=6, column=2, padx=20, sticky="w")
label_7_unit.grid(row=7, column=2, padx=20, sticky="w")

label_8_unit.grid(row=9, column=2, padx=20, sticky="w")
label_9_unit.grid(row=10, column=2, padx=20, sticky="w")

cta = tk.DoubleVar()
cta.set(65)
entry_1 = tk.Entry(left, width=30, bd=5, textvariable=cta)
mol = tk.DoubleVar()
mol.set(1)
entry_2 = tk.Entry(left, width=30, bd=5, textvariable=mol)
fra = tk.DoubleVar()
fra.set(5)
entry_3 = tk.Entry(left, width=30, bd=5, textvariable=fra)
chw = tk.DoubleVar()
chw.set(1)
entry_4 = tk.Entry(left, width=30, bd=5, textvariable=chw)
chh = tk.DoubleVar()
chh.set(1)
entry_5 = tk.Entry(left, width=30, bd=5, textvariable=chh)
chl = tk.DoubleVar()
chl.set(1000)
entry_6 = tk.Entry(left, width=30, bd=5, textvariable=chl)
chn = tk.DoubleVar()
chn.set(1)
entry_7 = tk.Entry(left, width=30, bd=5, textvariable=chn)
cd = tk.DoubleVar()
cd.set(10)
entry_8 = tk.Entry(left, width=30, bd=5, textvariable=cd)
aa = tk.DoubleVar()
aa.set(5)
entry_9 = tk.Entry(left, width=30, bd=5, textvariable=aa)

entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
entry_3.grid(row=3, column=1)
entry_4.grid(row=4, column=1)
entry_5.grid(row=5, column=1)
entry_6.grid(row=6, column=1)
entry_7.grid(row=7, column=1)

entry_8.grid(row=9, column=1)
entry_9.grid(row=10, column=1)

button_1 = \
        tk.Button(left, text='OK', width=20, bd=5,
                  command=lambda: convert_data(entry_1.get(), entry_2.get(),
                                               entry_3.get(), entry_4.get(),
                                               entry_5.get(), entry_6.get(),
                                               entry_7.get(), entry_8.get(),
                                               entry_9.get(), output_key,
                                               output_value, output_unit))

button_1.focus_set()

def onReturn(*event):
    convert_data(entry_1.get(), entry_2.get(),
                 entry_3.get(), entry_4.get(),
                 entry_5.get(), entry_6.get(),
                 entry_7.get(), entry_8.get(),
                 entry_9.get(), output_key,
                 output_value, output_unit)

root.bind('<Return>', onReturn)

button_1.grid(row=11, column=1)

root.mainloop()