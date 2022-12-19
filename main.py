# ----------------------------------------------------- LANGUAGE CHOOSE / WYBÓR JĘZYKA -------------------------------------------------------------------------
def wybieranie_jezyka():
    print("Choose language:")
    print("Wybierz język")
    print("Do wyboru masz:")
    print("1) Polski / Polish")
    print("2) Angielski / English:")
    jezyk = input()
    if jezyk=="Polski" or jezyk=="Polish" or jezyk=="1" or jezyk=="polski" or jezyk=="polish" or jezyk=="pl" or jezyk=="PL":
        print("Możesz jeszcze wrócić do wyboru języka:")
        print("Wybierz 1 lub napisz Dalej, aby przejść dalej")
        print("Wybierz 2 lub napisz Powrót, aby wrócić")
        wyb=input()
        if wyb=="1" or wyb=="Dalej" or wyb=="dalej" or wyb=="d" or wyb=="D":
            poczatekprogramu()
        elif wyb=="2" or wyb=="Powrót" or wyb=="Powrot" or wyb=="p" or wyb=="P" or wyb=="powrot" or wyb=="powrót":
            wybieranie_jezyka()
        else:
            print("Nie rozumiem twojej komendy")
            print("Zostaneisz cofnięty do początu (wyboru języka)")
            wybieranie_jezyka()
    elif jezyk=="Angielski" or jezyk=="angielski" or jezyk=="2" or jezyk=="English" or jezyk=="english" or jezyk=="ENG" or jezyk=="eng":
        print("You can still go back to the language selection:")
        print("Select 1 or write Next to move on")
        print("Select 2 or write Back to return")
        wyb = input()
        if wyb == "1" or wyb == "Continue" or wyb == "continue" or wyb == "C" or wyb == "c":
            poczatekprogramu_eng()
        elif wyb == "2" or wyb == "Return" or wyb == "return" or wyb == "R" or wyb == "r":
            wybieranie_jezyka()
        else:
            print("I don't understand your command")
            print("You will be taken back to the beginning (language selection)")
            wybieranie_jezyka()
    else:
        wybieranie_jezyka()

#------------------------------------------------------------ PL part -----------------------------------------------------------------------------

def calculate_sum_pl():
    print("Liczby zmienno przecinkowe wpisujemy za pomocą kropki")
    print("Np. 0.6")
    print("Zamiast używając przecinka")
    print("Np. 0,6")
    print("Ponieważ wpisując przecinek zamiast kropki zmieniasz typ danych z liczbowych na tekstowe,")
    print("Przez co program przestaje działać")
    print("Podaj liczby od -10 do 10")
    a = float(input("a: "))
    b = float(input("b: "))
    if a <= 10 and b <= 10 and a >= (-10) and b >= (-10):
        print("Wybierz działanie które chcesz wykonać")
        print("Do wyboru masz:")
        print("1) dodawanie")
        print("2) odejmowanie")
        print("3) mnożenie")
        print("4) dzielenie")
        print("5) potęga")
        print("6) dodawanie i odejmowanie")
        print("7) mnożenie i dzielenie")
        d=input()
        if d=="dodawanie" or d=="1":
            print("Suma:", a+b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d=="odejmowanie" or d=="2":
            print("Różnica:", a-b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d=="mnożenie" or d=="3" or d=="mnozenie":
            if a==0 or b==0:
                print("Mnożenie przez 0 daje wynik: 0")
                calculate_sum_pl()
            else:
                print("Mnożenie:", a*b)
                print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
                print("Wybierz:")
                print("1) Tak")
                print("2) Nie")
                print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d=="dzielenie" or d=="4":
            if a==0 or b==0:
                print("Nie można dzielić przez: 0")
                print("Zostajesz cofnięty so wyboru liczb")
                calculate_sum_pl()
            else:
                print("Dzielenie:", a/b)
                print("Liczba całkowita z dzielenia:", a//b)
                print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
                print("Wybierz:")
                print("1) Tak")
                print("2) Nie")
                print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d=="potęga" or d=="5" or d=="potega":
            print("Potęga:", a**b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d=="dodawanie i odejmowanie" or d=="6":
            print("Suma:", a+b)
            print("Różnica:", a-b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d=="mnożenie i dzielenie" or d=="7" or d=="mnozenie i dzielenie":
            if a==0 or b==0:
                print("Mnożenie przez 0 daje wynik: 0")
                print("Nie można dzielić przez: 0")
                print("Zostaniesz cofnięty do wyboru liczb")
                calculate_sum_pl()
            else:
                print("Mnożenie:", a * b)
                print("Dzielenie:", a / b)
                print("Liczba całkowita z dzielenia:", a // b)
                print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
                print("Wybierz:")
                print("1) Tak")
                print("2) Nie")
                print("Wybór:")
            wybor = input()
            if wybor=="1" or wybor=="Tak" or wybor=="tak" or wybor=="t":
                calculate_sum_pl()
            elif wybor=="2" or wybor=="Nie" or wybor=="nie" or wybor=="n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program został zakończony")
                zamkniecieprogrammu()
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        else:
            print("Nie rozumiem, wybierz jeszcze raz:")
            wybor_dzialan_kalkulator()
    elif (a>=10 and b<=10) or (a<=(-10) and b>=(-10)) :
        print("Podałeś za wysoką liczbę: (a)")
        print("Powrót do początku, wpisz: powrót")
        print("Zakończenie aplikacji wpisz: zakończ")
        x=input()
        if x=="powrot" or x=="powrót" or x=="Powrót" or x=="Powrot" or x=="POWRÓT" or x=="POWROT":
            print("Wróciłeś do początku")
            calculate_sum_pl()
        elif x == "zakoncz" or x == "zakończ" or x == "Zakończ" or x == "Zakoncz" or x == "ZAKONCZ or" or x == "ZAKOŃCZ" or x == 2 or x == "z" or x == "Z":
            zakonczenieprogramu()
        else:
            print("Nie rozumiem twojego wyboru")
            print("Zostajesz cofnięty do początku kalkulatora")
            calculate_sum_pl()
    elif b>=10 and a<=10 or b<=(-10) and a>=(-10):
        print("Podałeś za wysoką liczbę: (b)")
        print("Powrót do początku, wpisz: powrót")
        print("Zakończenie aplikacji wpisz: zakończ")
        x=input()
        if x=="powrot" or x=="powrót" or x=="Powrót" or x=="Powrot" or x=="POWRÓT" or x=="POWROT":
            print("wróciłeś do początku")
            calculate_sum_pl()
        elif x == "zakoncz" or x == "zakończ" or x == "Zakończ" or x == "Zakoncz" or x == "ZAKONCZ or" or x == "ZAKOŃCZ" or x == 2 or x == "z" or x == "Z":
            zakonczenieprogramu()
        else:
            print("Nie rozumiem twojego wyboru")
            print("Zostajesz cofnięty do początku kalkulatora")
            calculate_sum_pl()
    elif (b >= 10 and a >= 10) or (b <= (-10) and a <= (-10)):
        print("Podałeś za wysokie liczby: (a) oraz (b)")
        print("Powrót do początku, wpisz: powrót")
        print("Zakończenie aplikacji wpisz: zakończ")
        x=input()
        if x=="powrot" or x=="powrót" or x=="Powrót" or x=="Powrot" or x=="POWRÓT" or x=="POWROT":
            print("wróciłeś do początku")
            calculate_sum_pl()
        elif x=="zakoncz" or x=="zakończ" or x=="Zakończ" or x=="Zakoncz" or x=="ZAKONCZ or" or x=="ZAKOŃCZ" or x==2 or x=="z" or x=="Z":
            zakonczenieprogramu()
        else:
            poczatekprogramu()
    else:
            print("Nie rozumiem twojego wyboru")
            print("Zostajesz cofnięty do początku kalkulatora")
            calculate_sum_pl()

def poczatekprogramu():
    print("Imię:")
    n=input()
    print("Nazwisko:")
    i=input()
    print("Witaj:", i, n)
    print("Znajdujesz się na początku programu")
    print("Program w którym się znajdujesz to kalkulator")
    print("Prosty kalkulatory :)")
    print("Więc działania wykonuje tylko na dwóch liczbach w przedziale od 0 do 10")
    calculate_sum_pl()

def wybor_czy_chcesz_cos_jeszcze_wyliczyc():
    a = float(input("a: "))
    b = float(input("b: "))
    if a <= 10 and b <= 10 and a >= (-10) and b >= (-10):
        print("Wybierz działanie które chcesz wykonać")
        print("Do wyboru masz:")
        print("1) dodawanie")
        print("2) odejmowanie")
        print("3) mnożenie")
        print("4) dzielenie")
        print("5) potęga")
        print("6) dodawanie i odejmowanie")
        print("7) mnożenie i dzielenie")
    d = input()
    print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
    print("Wybierz:")
    print("1) Tak")
    print("2) Nie")
    print("Wybór:")
    wybor = input()
    if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
        calculate_sum_pl()
    elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
        print("Wybrałeś, że nie chcesz nic więcej policzyć")
        print("Program zostanie zakończony")
        import sys
        sys.exit("Koniec")
    else:
        print("Nie rozumiem twojego wyboru")
        print("Wybierz jeszcze raz:")
        wybor_czy_chcesz_cos_jeszcze_wyliczyc()

def wybor_dzialan_kalkulator():
    print("Liczby zmienno przecinkowe wpisujemy za pomocą kropki")
    print("Np. 0.6")
    print("Zamiast używając przecinka")
    print("Np. 0,6")
    print("Ponieważ wpisując przecinek zamiast kropki zmieniasz typ danych z liczbowych na tekstowe,")
    print("Przez co program przestaje działać")
    print("Podaj liczby od -10 do 10")
    a = float(input("a: "))
    b = float(input("b: "))
    if a <= 10 and b <= 10 and a >= (-10) and b >= (-10):
        print("Wybierz działanie które chcesz wykonać")
        print("Do wyboru masz:")
        print("1) dodawanie")
        print("2) odejmowanie")
        print("3) mnożenie")
        print("4) dzielenie")
        print("5) potęga")
        print("6) dodawanie i odejmowanie")
        print("7) mnożenie i dzielenie")
        d = input()
        if d == "dodawanie" or d == "1":
            print("Suma:", a + b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d == "odejmowanie" or d == "2":
            print("Różnica:", a - b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d == "mnożenie" or d == "3" or d == "mnozenie":
            if a == 0 or b == 0:
                print("Mnożenie przez 0 daje wynik: 0")
                calculate_sum_pl()
            else:
                print("Mnożenie:", a * b)
                print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
                print("Wybierz:")
                print("1) Tak")
                print("2) Nie")
                print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d == "dzielenie" or d == "4":
            if a == 0 or b == 0:
                print("Nie można dzielić przez: 0")
                print("Zostajesz cofnięty so wyboru liczb")
                calculate_sum_pl()
            else:
                print("Dzielenie:", a / b)
                print("Liczba całkowita z dzielenia:", a // b)
                print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
                print("Wybierz:")
                print("1) Tak")
                print("2) Nie")
                print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d == "potęga" or d == "5" or d == "potega":
            print("Potęga:", a ** b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d == "dodawanie i odejmowanie" or d == "6":
            print("Suma:", a + b)
            print("Różnica:", a - b)
            print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
            print("Wybierz:")
            print("1) Tak")
            print("2) Nie")
            print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        elif d == "mnożenie i dzielenie" or d == "7" or d == "mnozenie i dzielenie":
            if a == 0 or b == 0:
                print("Mnożenie przez 0 daje wynik: 0")
                print("Nie można dzielić przez: 0")
                print("Zostaniesz cofnięty do wyboru liczb")
                calculate_sum_pl()
            else:
                print("Mnożenie:", a * b)
                print("Dzielenie:", a / b)
                print("Liczba całkowita z dzielenia:", a // b)
                print("Czy chcesz wykonać jeszcze jakieś obliczenia?")
                print("Wybierz:")
                print("1) Tak")
                print("2) Nie")
                print("Wybór:")
            wybor = input()
            if wybor == "1" or wybor == "Tak" or wybor == "tak" or wybor == "t":
                calculate_sum_pl()
            elif wybor == "2" or wybor == "Nie" or wybor == "nie" or wybor == "n":
                print("Wybrałeś, że nie chcesz nic więcej policzyć")
                print("Program zostanie zakończony")
                import sys
                sys.exit("Koniec")
            else:
                print("Nie rozumiem twojego wyboru")
                print("Wybierz jeszcze raz:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc()
        else:
            print("Nie rozumiem, wybierz jeszcze raz:")
            wybor_dzialan_kalkulator()

def zakonczenieprogramu():
    print("Wybrałeś zakończenie programu")
    import sys
    sys.exit("Koniec")

def zamkniecieprogrammu():
    import sys
    sys.exit("Koniec")
    sys.exit(0)

#------------------------------------------------------------ ENG part -----------------------------------------------------------------------------

def zakonczenieprogramu_eng():
    print("You choose to end program")
    import sys
    sys.exit("End")

def zamkniecieprogrammu_eng():
    import sys
    sys.exit("End")
    sys.exit(0)

def poczatekprogramu_eng():
    print("Name:")
    n=input()
    print("Surrname:")
    i=input()
    print("Hello:", i, n)
    print("You are at the beginning of the program")
    print("The program you are in is a calculator")
    print("Simple calculators :)")
    print("So it only performs actions on two numbers between 0 and 10")
    calculate_sum_eng()

def calculate_sum_eng():
    print("We enter floating-point numbers using a period")
    print("E.g. 0.6")
    print("Instead of using a comma")
    print("E.g. 0.6")
    print("Because by entering a comma instead of a period, you change the data type from numeric to text,")
    print("By which the program stops working")
    print("Give numbers from -10 to 10")
    a = float(input("a: "))
    b = float(input("b: "))
    if a<=10 and b<=10 and a>=(-10) and b>=(-10):
        print("Select the action you want to perform")
        print("You can choose from:")
        print("1) adding")
        print("2) subtraction")
        print("3) multiplication")
        print("4) dzielenie")
        print("5) the power of")
        print("6) addition and subtraction")
        print("7) multiplication and dividing")
        d=input()
        if d=="adding" or d=="1":
            print("Total:", a+b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Your choice:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has ended")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Nie rozumiem twojego wyboru")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d=="subtraction" or d=="2":
            print("Difference:", a-b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Choose:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d=="multiplication" or d=="3" or d=="m":
            if a==0 or b==0:
                print("Multiplying by 0 gives the result: 0")
                calculate_sum_eng()
            else:
                print("Multiplication:", a*b)
                print("Do you want to do any more calculations?")
                print("Choose:")
                print("1) Yes")
                print("2) No")
                print("Choose:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d=="dividing" or d=="4":
            if a==0 or b==0:
                print("You cannot divide by: 0")
                print("You are taken back so the choice of numbers")
                calculate_sum_eng()
            else:
                print("Dividing:", a/b)
                print("Integer from division:", a//b)
                print("Do you want to do any more calculations?")
                print("Choose:")
                print("1) Yes")
                print("2) No")
                print("Choose:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d=="the power of" or d=="5" or d=="power":
            print("The power of:", a**b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Choose:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d=="addition and subtraction" or d=="6":
            print("Total:", a+b)
            print("Difference:", a-b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Choose:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d=="multiplication and dividing" or d=="7" or d=="multi and div":
            if a==0 or b==0:
                print("Multiplying by 0 gives the result: 0")
                print("You cannot divide by: 0")
                print("You will be taken back to the selection of numbers")
                calculate_sum_eng()
            else:
                print("Multiplication:", a * b)
                print("Dividing:", a / b)
                print("Integer from dividing:", a // b)
                print("Do you want to do any more calculations?")
                print("Choose:")
                print("1) Yes")
                print("2) No")
                print("Choose:")
            wybor = input()
            if wybor=="1" or wybor=="Yes" or wybor=="yes" or wybor=="y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        else:
            print("I don't understand, choose again:")
            wybor_dzialan_kalkulato_eng()
    elif (a>=10 and b<=10) or (a<=(-10) and b>=(-10)) :
        print("You have given too high a number: (a)")
        print("Back to the beginning, type: return")
        print("End the application type: end")
        x=input()
        if x=="return" or x=="Return" or x=="R" or x=="r" or x=="RETURN" :
            print("You're back to the beginning")
            calculate_sum_eng()
        elif x == "End" or x == "END" or x == "e" or x == "E" or x == 2:
            zakonczenieprogramu_eng()
        else:
            print("I don't understand your choice.")
            print("You are taken back to the beginning of the calculator")
            calculate_sum_eng()
    elif b>=10 and a<=10 or b<=(-10) and a>=(-10):
        print("You have given too high a number: (b)")
        print("Back to the beginning, type: return")
        print("End the application type: end")
        x=input()
        if x=="return" or x=="Return" or x=="R" or x=="r" or x=="RETURN" :
            print("You're back to the beginning")
            calculate_sum_eng()
        elif x == "End" or x == "END" or x == "e" or x == "E" or x == 2:
            zakonczenieprogramu_eng()
        else:
            print("I don't understand your choice.")
            print("You are taken back to the beginning of the calculator")
            calculate_sum_eng()
    elif (b >= 10 and a >= 10) or (b <= (-10) and a <= (-10)):
        print("You have given too high numbers: (a) and (b)")
        print("Back to the beginning, type: return")
        print("End the application type: end")
        x=input()
        if x=="return" or x=="Return" or x=="R" or x=="r" or x=="RETURN" :
            print("You're back to the beginning")
            calculate_sum_eng()
        elif x == "End" or x == "END" or x == "e" or x == "E" or x == 2:
            zakonczenieprogramu_eng()
        else:
            poczatekprogramu_eng()
    else:
            print("I don't understand your choice")
            print("You are taken back to the beginning of the calculator")
            calculate_sum_eng()

def wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng():
    a = float(input("a: "))
    b = float(input("b: "))
    if a <= 10 and b <= 10 and a >= (-10) and b >= (-10):
        print("Select the action you want to perform")
        print("You can choose from:")
        print("1) adding")
        print("2) subtraction")
        print("3) multiplication")
        print("4) dzielenie")
        print("5) the power of")
        print("6) addition and subtraction")
        print("7) multiplication and dividing")
    d = input()
    print("Do you want to do any more calculations?")
    print("Choose:")
    print("1) Yes")
    print("2) No")
    print("Your choice:")
    wybor = input()
    if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
        calculate_sum_eng()
    elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
        print("You chose not to count anything else")
        print("The program has ended")
        zamkniecieprogrammu_eng()
    else:
        print("I don't understand your choice")
        print("You are taken back to the beginning of the calculator")
        wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()

def wybor_dzialan_kalkulato_eng():
    print("We enter floating-point numbers using a period")
    print("E.g. 0.6")
    print("Instead of using a comma")
    print("E.g. 0.6")
    print("Because by entering a comma instead of a period, you change the data type from numeric to text,")
    print("By which the program stops working")
    print("Give numbers from -10 to 10")
    a = float(input("a: "))
    b = float(input("b: "))

    if a <= 10 and b <= 10 and a >= (-10) and b >= (-10):
        print("Select the action you want to perform")
        print("You can choose from:")
        print("1) adding")
        print("2) subtraction")
        print("3) multiplication")
        print("4) dzielenie")
        print("5) the power of")
        print("6) addition and subtraction")
        print("7) multiplication and dividing")
        d = input()
        if d == "adding" or d == "1":
            print("Total:", a + b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Your choice:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has ended")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("You are taken back to the beginning of the calculator")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d == "subtraction" or d == "2":
            print("Difference:", a - b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Choose:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d == "multiplication" or d == "3" or d == "m":
            if a == 0 or b == 0:
                print("Multiplying by 0 gives the result: 0")
                calculate_sum_eng()
            else:
                print("Multiplication:", a * b)
                print("Do you want to do any more calculations?")
                print("Choose:")
                print("1) Yes")
                print("2) No")
                print("Choose:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d == "dividing" or d == "4":
            if a == 0 or b == 0:
                print("You cannot divide by: 0")
                print("You are taken back so the choice of numbers")
                calculate_sum_eng()
            else:
                print("Dividing:", a / b)
                print("Integer from division:", a // b)
                print("Do you want to do any more calculations?")
                print("Choose:")
                print("1) Yes")
                print("2) No")
                print("Choose:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d == "the power of" or d == "5" or d == "power":
            print("The power of:", a ** b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Choose:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d == "addition and subtraction" or d == "6":
            print("Total:", a + b)
            print("Difference:", a - b)
            print("Do you want to do any more calculations?")
            print("Choose:")
            print("1) Yes")
            print("2) No")
            print("Choose:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        elif d == "multiplication and dividing" or d == "7" or d == "multi and div":
            if a == 0 or b == 0:
                print("Multiplying by 0 gives the result: 0")
                print("You cannot divide by: 0")
                print("You will be taken back to the selection of numbers")
                calculate_sum_eng()
            else:
                print("Multiplication:", a * b)
                print("Dividing:", a / b)
                print("Integer from dividing:", a // b)
                print("Do you want to do any more calculations?")
                print("Choose:")
                print("1) Yes")
                print("2) No")
                print("Choose:")
            wybor = input()
            if wybor == "1" or wybor == "Yes" or wybor == "yes" or wybor == "y":
                calculate_sum_eng()
            elif wybor == "2" or wybor == "No" or wybor == "no" or wybor == "n":
                print("You chose not to count anything else")
                print("The program has been completed")
                zamkniecieprogrammu_eng()
            else:
                print("I don't understand your choice")
                print("Choose again:")
                wybor_czy_chcesz_cos_jeszcze_wyliczyc_eng()
        else:
            print("I don't understand, choose again:")
            wybor_dzialan_kalkulato_eng()

# Uruchomienie programu:

if __name__ == '__main__':
    wybieranie_jezyka()

#------------------------------------------------ Program stworzony przez: Jakub Guth | Program created by: Jakub Guth ------------------------------------------------------------------