# Perdaryti programą 1 užduotyje, kad ji:
# • Turėtų grafinę sąsają (su ikona ir pavadinimu). Sukurti per Tkinter
# • Leistų įvesti asmenis į duomenų bazę (jų vardą, pavardę, amžių, ...)
# • Parodytų visų į duomenų bazę įvestų asmenų sąrašą
# • Leistų ištrinti pasirinktą asmenį iš duomenų bazės
# • Leistų paredaguoti įvesto asmens duomenis ir įrašyti atnaujinimus į duomenų bazę



import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

from sqlalchemy.orm import sessionmaker
from alchemy_credentials import engine
from project import ManoProjektas

Session = sessionmaker(bind=engine)
session = Session()

root = tk.Tk()
root.title("Darbuotojų valdymas")

def atnaujinti_sarasa():
    darbuotojai = session.query(ManoProjektas).all()
    sarasas.delete(*sarasas.get_children())
    for d in darbuotojai:
        sarasas.insert("", "end", values=(d.ID, d.name, d.lastname, d.birthdate, d.occupation, d.salary, d.startdate))


def irasyti():
    try:
        gimimo_data = datetime.strptime(entry_gim_data.get(), "%Y-%m-%d").date()
        atlyginimas = float(entry_atlyginimas.get())
    except ValueError:
        messagebox.showerror("Klaida", "Patikrinkite datos arba atlyginimo formatą.")
        return

    naujas = ManoProjektas(
        name=entry_vardas.get(),
        lastname=entry_pavarde.get(),
        birthdate=gimimo_data,
        occupation=entry_pareigos.get(),
        salary=atlyginimas,
        startdate=datetime.today()
    )

    session.add(naujas)
    session.commit()
    messagebox.showinfo("OK", "Darbuotojas įrašytas")
    atnaujinti_sarasa()
    isvalyti_laukus()

def isvalyti_laukus():
    entry_vardas.delete(0, tk.END)
    entry_pavarde.delete(0, tk.END)
    entry_gim_data.delete(0, tk.END)
    entry_pareigos.delete(0, tk.END)
    entry_atlyginimas.delete(0, tk.END)

   

def istrinti():
    pasirinktas = sarasas.selection()
    if pasirinktas:
        item = sarasas.item(pasirinktas)
        darbuotojo_id = item['values'][0]
        darbuotojas = session.query(ManoProjektas).get(darbuotojo_id)
        if darbuotojas:
            session.delete(darbuotojas)
            session.commit()
            messagebox.showinfo("Ištrinta", "Darbuotojas pašalintas")
            atnaujinti_sarasa()


def redaguoti():
    pasirinktas = sarasas.selection()
    if pasirinktas:
        item = sarasas.item(pasirinktas)
        darbuotojo_id = item['values'][0]
        d = session.query(ManoProjektas).get(darbuotojo_id)

        entry_vardas.delete(0, tk.END)
        entry_pavarde.delete(0, tk.END)
        entry_gim_data.delete(0, tk.END)
        entry_pareigos.delete(0, tk.END)
        entry_atlyginimas.delete(0, tk.END)

        entry_vardas.insert(0, d.name)
        entry_pavarde.insert(0, d.lastname)
        entry_gim_data.insert(0, d.birthdate)
        entry_pareigos.insert(0, d.occupation)
        entry_atlyginimas.insert(0, d.salary)

        def issaugoti_redagavima():
            try:
                d.name = entry_vardas.get()
                d.lastname = entry_pavarde.get()
                d.birthdate = datetime.strptime(entry_gim_data.get(), "%Y-%m-%d").date()
                d.occupation = entry_pareigos.get()
                d.salary = float(entry_atlyginimas.get())
                session.commit()
                messagebox.showinfo("Atnaujinta", "Informacija atnaujinta")
                atnaujinti_sarasa()
                isvalyti_laukus()
            except Exception as e:
                messagebox.showerror("Klaida", str(e))

        btn_issaugoti.config(command=issaugoti_redagavima)
        
# Įvedimo laukai su mažais tarpais
label_padx = 3
entry_padx = 5
common_pady = 2

tk.Label(root, text="Vardas").grid(row=0, column=0, sticky="e", padx=label_padx, pady=common_pady)
entry_vardas = tk.Entry(root)
entry_vardas.grid(row=0, column=1, sticky="w", padx=entry_padx, pady=common_pady)

tk.Label(root, text="Pavardė").grid(row=1, column=0, sticky="e", padx=label_padx, pady=common_pady)
entry_pavarde = tk.Entry(root)
entry_pavarde.grid(row=1, column=1, sticky="w", padx=entry_padx, pady=common_pady)

tk.Label(root, text="Gimimo data (YYYY-MM-DD)").grid(row=2, column=0, sticky="e", padx=label_padx, pady=common_pady)
entry_gim_data = tk.Entry(root)
entry_gim_data.grid(row=2, column=1, sticky="w", padx=entry_padx, pady=common_pady)

tk.Label(root, text="Pareigos").grid(row=3, column=0, sticky="e", padx=label_padx, pady=common_pady)
entry_pareigos = tk.Entry(root)
entry_pareigos.grid(row=3, column=1, sticky="w", padx=entry_padx, pady=common_pady)

tk.Label(root, text="Atlyginimas").grid(row=4, column=0, sticky="e", padx=label_padx, pady=common_pady)
entry_atlyginimas = tk.Entry(root)
entry_atlyginimas.grid(row=4, column=1, sticky="w", padx=entry_padx, pady=common_pady)


# Mygtukų rėmelis (viena eilutė)
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=5, column=0, columnspan=2, pady=8)

btn_irasyti = tk.Button(frame_buttons, text="Įrašyti", command=irasyti)
btn_irasyti.pack(side="left", padx=4)

btn_issaugoti = tk.Button(frame_buttons, text="Išsaugoti redagavimą")
btn_issaugoti.pack(side="left", padx=4)

btn_istrinti = tk.Button(frame_buttons, text="Ištrinti", command=istrinti)
btn_istrinti.pack(side="left", padx=4)

btn_redaguoti = tk.Button(frame_buttons, text="Redaguoti", command=redaguoti)
btn_redaguoti.pack(side="left", padx=4)


# Duomenų lentelė
sarasas = ttk.Treeview(root, columns=("ID", "Vardas", "Pavardė", "Gimimo data", "Pareigos", "Atlyginimas", "Dirba nuo"), show="headings")
for col in sarasas["columns"]:
    sarasas.heading(col, text=col)
sarasas.grid(row=7, column=0, columnspan=2, pady=10)

atnaujinti_sarasa()

root.mainloop()
