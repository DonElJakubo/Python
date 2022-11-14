# Program krótkiej rozmowy/gry wraz z pseudo sztuczną inteligencją
print("Podaj swoję imię")
# Prośba o podanie danej użytkownika (imienia)
a=input()
# Po podaniu imienia prośba o podanie ostatniej danej użytkownika
print("Podaj swoje nazwisko")
# Prośba o podanie danej użytkownika (nazwiska)
b=input()
# Po podaniu danych, program wita użytkownika jego imieniem i nazwiskiem oraz zaprasza do gry
print("Cześć", a, b)
print("Czy chcesz zagrać w grę?")
print("Prosze o odpowiedź tak lub nie")
# Użytkownik ma możliwość zagrania z pseudo sztuczną inteligencją w grę
c=input()

if c=="tak":
    print("Świetnie, gra polega na zgadnięciu o jakiej liczbie myślę")
    print("Liczby są w przedziale od 1 do 10")
    print("A i jeszcze jedno, żeby trochę utrudnić grę, masz tylko 3 podejścia")
    print("Podaj więc liczbę od 1 do 10:")
# Po zaakceptowaniu zaproszenia do gry wpisujemy losową liczbę w przedziale 1-10
    x=int(input())
    if x==5:
        print("Świetnie, zgadłeś za pierwszysm razem")
    elif x!=5:
        print("Masz jeszcze jedną szansę.")
        print("Ale masz ode mnie małą podpowiedź")
        if x > 5:
            print("Musisz podać mniejszą liczbę")
            print("Podaj jeszcze raz liczbę:")
        elif x < 5:
            print("Musisz podać większą liczbę")
            print("Podaj jeszcze raz liczbę:")
# Jeśli nie trafimy, dostajemy podpowiedź czy liczba jest za mała czy za duża
        x = int(input())
        if x==5:
            print("Udało ci się przy drugim podejściu, brawo")
        elif x != 5:
            print("Masz jeszcze ostatnią szansę.")
            print("Ale masz ode mnie małą podpowiedź")
            if x > 5:
                print("Musisz podać mniejszą liczbę")
                print("Podaj jeszcze raz liczbę:")
            elif x < 5:
                print("Musisz podać większą liczbę")
                print("Podaj jeszcze raz liczbę:")
# Podobnie jak w poprzednim etapie tylko jeśli tym razem nie trafimy to przegramy
            x = int(input())
            if x==5:
                print("Nie najgorzej, zgadłeś przy 3 podejściu")
            else:
                print("Przykro mi przegrałeś")
# Jeśli nie zaakceptujemy zaproszenia do gry to program się z nami pożegna
elif c=="nie":
    print("No nic to może następnym razem")
# W przypadku gry wpiszemy niepoprawne dane, to program rozpozna błąd i zakończy działanie
else:
    print("niestety nie podałeś odpowiedzi którą zrozumiałem")
    print("uruchom program jeszcze raz, pamiętając, że odpowiedź może być tylko tak lub nie")
    print("tak/nie pisz tylko małymi literami")
