from fractions import Fraction

def grupiraj(lista, *operandi):
    i = 0
    grupe = []
    curr_grupa = []
    for element in lista:
        if element in operandi:
            grupe.append(curr_grupa)
            grupe.append(element)
            curr_grupa = []
        else:
            curr_grupa.append(element)
    
    if len(curr_grupa) != 0:
        grupe.append(curr_grupa)
    return grupe


def obradi_zagrade(i):
    #vraca dvije vrijednosti:
    #listu tokena bez_zagrada i indeks nakon desne zagrade
    global tokeni
    L = []
    #provjera postojanja unarnog operatora
    if tokeni[i] in ("+", "-"):
        L.append(0)
        
    while i < len(tokeni):
        if tokeni[i] == "(":
            t, i = obradi_zagrade(i+1)
            L.append(t)
        elif tokeni[i] == ")":
            return (obradi_pm(L), i+1)
        else:
            L.append(tokeni[i])
            i += 1
    return L, i+1
        

def obradi_pm(pribrojnici):
    #grupiranje pribrojnika
    pribrojnici_grupe = grupiraj(pribrojnici, "+", "-")
    lijevo = obradi_pp(pribrojnici_grupe[0])
    i = 1
    while i < len(pribrojnici_grupe):
        if pribrojnici_grupe[i] == "+":
            desno = obradi_pp(pribrojnici_grupe[i+1])
            lijevo += desno
            i += 2
        elif pribrojnici_grupe[i] == "-":
            desno = obradi_pp(pribrojnici_grupe[i+1])
            lijevo -= desno
            i += 2
        else:
            i += 1
    return lijevo
        
    
def obradi_pp(faktori):
    #grupiranje faktora
    faktori_grupe = grupiraj(faktori, "*", "/")
    lijevo = obradi_pot(faktori_grupe[0])
    i = 1
    while i < len(faktori_grupe):
        if faktori_grupe[i] == "*":
            desno = obradi_pot(faktori_grupe[i+1])
            lijevo *= desno
            i += 2
        elif faktori_grupe[i] == "/":
            desno = obradi_pot(faktori_grupe[i+1])
            lijevo /= desno
            i += 2
        else:
            i += 1
    return lijevo
    
    
def obradi_pot(operandi):
    #operator potenciranja je desno asocijativan
    desno = Fraction(operandi[-1])
    i = len(operandi) - 2
    while i >= 0:
        if operandi[i] == "^":
            lijevo = Fraction(operandi[i-1])
            desno = lijevo ** desno
            i -= 2
        else:
            i -= 1
    return desno

ulaz = input()

tokeni = []

broj = None
for c in ulaz:
    if broj is not None:
        if c.isnumeric():
            broj = broj*10 + int(c)
        else:
            tokeni.append(broj)
            broj = None
            tokeni.append(c)
    else:
        if c.isnumeric():
            broj = int(c)
        else:
            tokeni.append(c)
if broj is not None:
    tokeni.append(broj)

bez_zagrada, end = obradi_zagrade(0)
sol = obradi_pm(bez_zagrada)

print(sol.numerator, sol.denominator)
