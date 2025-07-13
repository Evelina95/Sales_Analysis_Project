# Sukurti programą, kuri:
# • Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (data būtų nustatoma automatiškai,
# pagal dabartinę datą).
# • Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# • Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

from sqlalchemy.orm import sessionmaker
from alchemy_credentials import engine  # turi turėti DB prisijungimo nustatymus
from project import ManoProjektas
from datetime import datetime, date

Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("\n--- MENIU ---")
    print("1 - Įvesti naują darbuotoją")
    print("2 - Peržiūrėti visus darbuotojus")
    print("3 - Ištrinti darbuotoją")
    print("4 - Atnaujinti darbuotojo duomenis")
    print("0 - Išeiti")

    pasirinkimas = input("Pasirinkite veiksmą: ")

    if pasirinkimas == "1":
        name = input("Vardas: ")
        lastname = input("Pavardė: ")
        while True:
            ivestis = input("Gimimo data (YYYY-MM-DD): ")
            try:
                birthdate = datetime.strptime(ivestis, "%Y-%m-%d")
                break
            except ValueError:
                print("Blogas formatas!")
        occupation = input("Pareigos: ")
        salary = float(input("Atlyginimas (€): "))
        startdate = datetime.today()

        naujas_darbuotojas = ManoProjektas(
            name=name,
            lastname=lastname,
            birthdate=birthdate,
            occupation=occupation,
            salary=salary,
            startdate=startdate
        )
        session.add(naujas_darbuotojas)
        session.commit()
        print("Darbuotojas įrašytas")

    elif pasirinkimas == "2":
        visi = session.query(ManoProjektas).all()
        for d in visi:
            print(d)

    elif pasirinkimas == "3":
        visi = session.query(ManoProjektas).all()
        for d in visi:
            print(d)
        id_istrinti = int(input("Įveskite darbuotojo ID, kurį norite ištrinti: "))
        darbuotojas = session.query(ManoProjektas).get(id_istrinti)
        if darbuotojas:
            session.delete(darbuotojas)
            session.commit()
            print("Darbuotojas ištrintas.")
        else:
            print("Toks ID nerastas.")

    elif pasirinkimas == "4":
        visi = session.query(ManoProjektas).all()
        for d in visi:
            print(d)
        id_atnaujinti = int(input("Įveskite ID darbuotojo, kurį norite keisti: "))
        d = session.query(ManoProjektas).get(id_atnaujinti)
        if not d:
            print("Toks darbuotojas nerastas.")
            continue

        print("1 - Vardas")
        print("2 - Pavardė")
        print("3 - Gimimo data")
        print("4 - Pareigos")
        print("5 - Atlyginimas")
        print("6 - Įsidarbinimo data")
        laukas = input("Ką norite keisti: ")

        if laukas == "1":
            d.name = input("Naujas vardas: ")
        elif laukas == "2":
            d.lastname = input("Nauja pavardė: ")
        elif laukas == "3":
            while True:
                nauja_data = input("Nauja gimimo data (YYYY-MM-DD): ")
                try:
                    d.birthdate = date.strptime(nauja_data, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Blogas formatas.")
        elif laukas == "4":
            d.occupation = input("Naujos pareigos: ")
        elif laukas == "5":
            d.salary = float(input("Naujas atlyginimas (€): "))
        elif laukas == "6":
            while True:
                nauja_data = input("Nauja įsidarbinimo data (YYYY-MM-DD): ")
                try:
                    d.startdate = datetime.strptime(nauja_data, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Blogas formatas.")

        session.commit()
        print("Darbuotojas atnaujintas.")

    elif pasirinkimas == "0":
        print("Programa baigta.")
        break

    else:
        print("Netinkamas pasirinkimas.")

