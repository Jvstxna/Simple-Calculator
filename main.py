from pystyle import Colorate, Colors, Center

# Pavadinimas

def Pavadinimas():
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("╔══════════════════════════════════════════════════════╗"))) #Pirma linija su raudonu ir geltonu persilejimu
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("║                       Skaičiuotuvas                  ║"))) #Antra linija "Skaičiuotuvas"
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter("╚══════════════════════════════════════════════════════╝"))) #

# Sudėtis

def Sudėtis(x, y):
    return x + y

# Atimtis

def Atimtis(x, y):
    return x - y

# Daugyba

def Daugyba(x, y):
    return x * y

# Dalyba

def Dalyba (x, y):
    return x / y


Pavadinimas()

while True:
    Pasirinkimas = input(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter('''Pasirinkite:
    + - Sudėtis
    - - Atimtis
    * - Daugyba
    / - Dalyba

    Pasirinkimas :''')))

    if Pasirinkimas in ('+', '-', '*', '/'):
        num1 = float(input("Pirmas skaitmuo: "))
        num2 = float(input("Antras skaitmuo: "))

        if Pasirinkimas == '+':
            print(num1, "+", num2, "=", Sudėtis(num1, num2))

        elif Pasirinkimas == '-':
            print(num1, "-", num2, "=", Atimtis(num1, num2))

        elif Pasirinkimas == '*':
            print(num1, "*", num2, "=", Daugyba(num1, num2))

        elif Pasirinkimas == '/':
            print(num1, "/", num2, "=", Dalyba(num1, num2))


        Kitas = input(("Ar norite atlikti kitą sprendimą? (T/N)"))

        if Kitas == "N":
            break

    else:
        print("Invalid input")
