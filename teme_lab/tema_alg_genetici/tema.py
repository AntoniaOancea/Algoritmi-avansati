import math
import random


def mutatie (cromozom,prob):
    #cromozom = list(cromozom)
    cromozom_nou=[]
    for gena in range(len(cromozom)):
        u = random.uniform(0,1)
        if u<prob:
            if cromozom[gena] == '1':
                cromozom_nou.append('0')
            else:
                cromozom_nou.append('1')
        else:
            cromozom_nou.append(cromozom[gena])
    return "".join(cromozom_nou)


def codificare(numar, a, b, p):
    l = int(math.log((b-a)*(10**p),2)) + 1
    interval_size = (b - a) / (2 ** l)
    index = int((float(numar) - a) // interval_size)
    binar = format(index,f'0{l}b' )
    return binar

def decodificare(binar, a, b):
    p = len(binar)
    interval_size = (b - a) / (2 ** p)
    index = int(binar, 2)
    numar = a + index * interval_size
    return "{:.4f}".format(numar)


# def selectie(coeficienti, dimensiune_populatie, cromozomi):
#     a, b, c = coeficienti
#     suma_fitness = 0.0
#     sume_partiale_fitness = []
#
#     # Calculăm suma totală a fitness-urilor și sumele parțiale ale fitness-urilor
#     for cromozom in cromozomi:
#         fitness = a * cromozom ** 2 + b * cromozom + c
#         suma_fitness += fitness
#         sume_partiale_fitness.append(suma_fitness)
#
#     capete_intervale = []
#
#     # Calculăm capetele intervalelor de selecție
#     for suma_partiala in sume_partiale_fitness:
#         capat_interval = suma_partiala / suma_fitness
#         capete_intervale.append(capat_interval)
#
#     return capete_intervale


def incrucisare(lungime_cromozom, cromozom1, cromozom2, punct_rupere):
    segment1_cromozom1 = cromozom1[:punct_rupere]
    segment2_cromozom1 = cromozom1[punct_rupere:]

    segment1_cromozom2 = cromozom2[:punct_rupere]
    segment2_cromozom2 = cromozom2[punct_rupere:]

    cromozom_rezultat1 = segment1_cromozom1 + segment2_cromozom2
    cromozom_rezultat2 = segment1_cromozom2 + segment2_cromozom1

    return cromozom_rezultat1, cromozom_rezultat2

def incrucisare3(lungime_cromozom, cromozom1,cromozom2,cromozom3,punct_rupere):
    segment1_cromozom1 = cromozom1[:punct_rupere]
    segment2_cromozom1 = cromozom1[punct_rupere:]

    segment1_cromozom2 = cromozom2[:punct_rupere]
    segment2_cromozom2 = cromozom2[punct_rupere:]

    segment1_cromozom3 = cromozom3[:punct_rupere]
    segment2_cromozom3 = cromozom3[punct_rupere:]

    cromozom_rezultat1 = segment1_cromozom1 + segment2_cromozom2
    cromozom_rezultat2 = segment1_cromozom2 + segment2_cromozom3
    cromozom_rezultat3 = segment1_cromozom3 + segment2_cromozom1

    return cromozom_rezultat1, cromozom_rezultat2, cromozom_rezultat3

def functie (x, a, b, c):
    x = float(x)
    return x ** 3 + 2 *x**2 -x + 1

def cautare_binara(lista, element):
    stanga = 0
    dreapta = len(lista) - 1

    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2

        if lista[mijloc] <= element and lista[mijloc+1] >= element:
            return mijloc+1
        elif lista[mijloc] < element:
            stanga = mijloc + 1
        else:
            dreapta = mijloc - 1
    return -1

# nr_cromozomi = int(input()) #numarul de cromozomi  === 20
# x, y = map(int, input().split()) #capetele intervalului  === [-1,2]
# a, b, c = map(int,input().split()) #coeficientii polinomului de grad 2  === [-1,1,2]
# p = int(input()) #precizia === 6
# prob_combinare = int(input()) #probabilitatea de recombinare == 25
# prob_mutatie = int(input()) #probabilitatea de mutatie == 1
# nr_etape = int(input()) #numarul de etape al algoritmului == 50

nr_cromozomi = 20
x = -2
y = 1
a = 2
b = -4
c = 3

p = 6
prob_combinare = 25/100
prob_mutatie = 1/100
nr_etape = 50

populatie = [0]
populatie_codificata = [0]
functie_rezultat = [0]

fisier = open("evolutie.txt", "w")

#generam prima populatie
fisier.write("Populatie initiala\n")
for i in range(1,nr_cromozomi+1):
    z = random.uniform(x,y)
    fisier.write(f"{i} : {codificare(z,x,y,p)}  x = {'{:.6f}'.format(z)}   f(x) = {functie(z,a,b,c)}\n")
    populatie.append(z)
    functie_rezultat.append(functie(z,a,b,c))

#calculam f(x)/sum(f(x_i))
fisier.write("\nProbabilitati selectie\n")
prob_etapa1 = [0]
for i in range(1,nr_cromozomi+1):
    prob = functie_rezultat[i]/sum(functie_rezultat,0)
    fisier.write(f"cromozom   {i} :   probabilitate   {prob}\n")
    prob_etapa1.append(prob)

#calculam intervalele
fisier.write("\nIntervale probabilitati selectie\n")
q = [0]
for i in range(1,nr_cromozomi+1):
    q.append(sum(prob_etapa1[:i+1]))
sorted(q)

fisier.write(f"{' '.join(map(str, q))}\n")

#verificam in ce interval se afla un numar random si selectam cromozomul i+1 unde i+1 este pozitia capatului din dreapta in intervalul calculat
cromozomi_selectati = [0]
for i in range(len(q)):
    u = random.uniform(0,1)
    i_cromozom = cautare_binara(q,u)
    fisier.write(f"u = {u}  selectam cromozomul  {i_cromozom}\n")
    cromozomi_selectati.append(i_cromozom)

#noua populatie contine cromozomii selectati mai sus
populatie1 = [0]

fisier.write("\nDupa selectie\n")
for i in range(1,nr_cromozomi+1):
    fisier.write(f"{i} : {codificare(populatie[cromozomi_selectati[i]],x,y,p)}  x= {populatie[cromozomi_selectati[i]]}  f= {functie(populatie[cromozomi_selectati[i]],a,b,c)}\n")
    populatie1.append(populatie[cromozomi_selectati[i]])

#combinarea se realizeaza intre cromozomii pentru care numarul generat aleator a fost mai mic decat probabilitatea de combinare
i_participa_combinare = []
fisier.write(f"\nProbabilitatea de incrucisare {prob_combinare}\n")
for i in range(1,nr_cromozomi+1):
    u = random.uniform(0,1)
    if u < prob_combinare:
        fisier.write(f"{i}: {codificare(populatie1[i],x,y,p)}  u= {u} < {prob_combinare} participa\n")
        i_participa_combinare.append(i)
    else:
        fisier.write(f"{i}: {codificare(populatie1[i], x, y, p)}  u= {u}\n")
if(len(i_participa_combinare)>=2):  #daca nu sunt cel putin 2 cromozomi selectati pentru combinare , aceasta nu se realizeaza
    if len(i_participa_combinare) % 2 == 0: #numar par de cromozomi selectati
        for i in range(0,len(i_participa_combinare),2):
            cromozom1 = codificare(populatie1[i_participa_combinare[i]],x,y,p)
            cromozom2 = codificare(populatie1[i_participa_combinare[i+1]],x,y,p)
            punct_rupere = int(random.uniform(1, len(cromozom1)))
            fisier.write(f"Recombinarea dintre cromozomul {i_participa_combinare[i]} cu cromozomul {i_participa_combinare[i + 1]}:\n")
            fisier.write(f"{cromozom1} , {cromozom2} punct de rupere {punct_rupere}\n")
            populatie1[i_participa_combinare[i]],populatie1[i_participa_combinare[i+1]] = incrucisare(len(cromozom1),cromozom1,cromozom2,punct_rupere)
            fisier.write(f"Rezultat {populatie1[i_participa_combinare[i]]} , {populatie1[i_participa_combinare[i+1]]}\n")
            populatie1[i_participa_combinare[i]] = decodificare(populatie1[i_participa_combinare[i]],x,y)
            populatie1[i_participa_combinare[i+1]] = decodificare(populatie1[i_participa_combinare[i+1]], x, y)

    else:#numar impar de cromozomi selectati
        n = len(i_participa_combinare)
        for i in range(0,len(i_participa_combinare)-3,2):
            cromozom1 = codificare(populatie1[i_participa_combinare[i]],x,y,p)
            cromozom2 = codificare(populatie1[i_participa_combinare[i+1]],x,y,p)
            punct_rupere = int(random.uniform(1, len(cromozom1)))
            fisier.write(f"Recombinarea dintre cromozomul {i_participa_combinare[i]} cu cromozomul {i_participa_combinare[i+1]}:\n")
            fisier.write(f"{cromozom1}  , {cromozom2} punct de rupere {punct_rupere}\n")
            populatie1[i_participa_combinare[i]],populatie1[i_participa_combinare[i+1]] = incrucisare(len(cromozom1),cromozom1,cromozom2,punct_rupere)
            fisier.write(f"Rezultat {populatie1[i_participa_combinare[i]]}  , {populatie1[i_participa_combinare[i + 1]]}\n")
            populatie1[i_participa_combinare[i]] = decodificare(populatie1[i_participa_combinare[i]],x,y)
            populatie1[i_participa_combinare[i+1]] = decodificare(populatie1[i_participa_combinare[i+1]], x, y)
        #ultima pereche de combinari e formata din 3 cromozomi pe care ii combinam circular
        cromozom1 = codificare(populatie1[i_participa_combinare[n-3]],x,y,p)
        cromozom2 = codificare(populatie1[i_participa_combinare[n -2]],x,y,p)
        cromozom3 = codificare(populatie1[i_participa_combinare[n -1]],x,y,p)
        punct_rupere = int(random.uniform(1, len(cromozom1)))
        fisier.write(f"Recombinare dinre cromozomii {i_participa_combinare[n-3]},{i_participa_combinare[n-2]} si {i_participa_combinare[n-1]}\n")
        fisier.write(f"{cromozom1} ,  {cromozom2}  , {cromozom3} punct de rupere {punct_rupere}\n")
        populatie1[i_participa_combinare[n-3]],populatie1[i_participa_combinare[n-2]],populatie1[i_participa_combinare[n-1]] = incrucisare3(len(cromozom1),cromozom1,cromozom2,cromozom3,punct_rupere)
        fisier.write(f"Rezultat {populatie1[i_participa_combinare[n-3]]} ,  {populatie1[i_participa_combinare[n-2]]}  , {populatie1[i_participa_combinare[n-1]]}\n")
        populatie1[i_participa_combinare[n-3]] = decodificare(populatie1[i_participa_combinare[n-3]], x, y)
        populatie1[i_participa_combinare[n-2]] = decodificare(populatie1[i_participa_combinare[n-2]], x, y)
        populatie1[i_participa_combinare[n - 1]] = decodificare(populatie1[i_participa_combinare[n - 1]], x, y)

#cromozomii rezultati dupa recombinare
fisier.write("\nDupa recombinare:\n")
for i in range(1,nr_cromozomi+1):
    fisier.write(f"{i}: {codificare(populatie1[i],x,y,p)} x={'{:.6f}'.format(float(populatie1[i]))} f(x)={functie(populatie1[i],a,b,c)}\n")

#selectam cromozomii pentru mutatie
fisier.write(f"\nProbabilitatea de mutatie pentru fiecare gena {prob_mutatie}\n")
fisier.write("Au fost modificati cromozomii:\n")

i_mutatie = []
for i in range(1,nr_cromozomi+1):
    #u = random.uniform(0,1)
    #if u < prob_mutatie:
        i_mutatie.append(i)
        fisier.write(f"{i}\n")
        populatie1[i] = mutatie(codificare(float(populatie1[i]),x,y,p),prob_mutatie)
        populatie1[i] = decodificare(populatie1[i],x,y)

fisier.write(f"Au fost selectati {len(i_mutatie)} cromozomi pentru mutatie\n")
#afisam populatia dupa mutatie
for i in range(1,nr_cromozomi+1):
    fisier.write(f"{i}: {codificare(populatie1[i], x, y, p)} x={'{:.6f}'.format(float(populatie1[i]))} f(x)={functie(populatie1[i], a, b, c)}\n")

#calculam rezultatul functiei pentru fiecare cromozom
functie_rezultat=[0]
for i in range(1,nr_cromozomi+1):
    functie_rezultat.append(functie(populatie1[i],a,b,c))

#afisam rezultatul maxim
maxim = -999999
for i in range(1,nr_cromozomi+1):
    f1 = functie(float(populatie1[i]),a,b,c)
    if f1 > maxim:
        maxim = f1

maxime=[maxim]
fisier.write(f"Maxim={maxim} Media={sum(functie_rezultat,0)/len(functie_rezultat)}\n")

for _ in range(1,nr_etape):
    prob_etapa1 = [0]
    for i in range(1, nr_cromozomi + 1):
        prob = functie_rezultat[i] / sum(functie_rezultat, 0)
        prob_etapa1.append(prob)

    populatie = populatie1
    q = [0]
    for i in range(1, nr_cromozomi + 1):
        q.append(sum(prob_etapa1[:i + 1]))

    cromozomi_selectati = [0]
    for i in range(len(q)):
        u = random.uniform(0, 1)
        i_cromozom = cautare_binara(q, u)
        cromozomi_selectati.append(i_cromozom)

    populatie1 = [0]

    for i in range(1, nr_cromozomi + 1):
        populatie1.append(populatie[cromozomi_selectati[i]])

    i_participa_combinare = []
    for i in range(1, nr_cromozomi + 1):
        u = random.uniform(0, 1)
        if u < prob_combinare:
            i_participa_combinare.append(i)
    if len(i_participa_combinare) >2:
        if len(i_participa_combinare) % 2 == 0:
            for i in range(0, len(i_participa_combinare), 2):
                cromozom1 = codificare(populatie1[i_participa_combinare[i]], x, y, p)
                cromozom2 = codificare(populatie1[i_participa_combinare[i + 1]], x, y, p)
                punct_rupere = int(random.uniform(1, len(cromozom1)))
                populatie1[i_participa_combinare[i]], populatie1[i_participa_combinare[i + 1]] = incrucisare(len(cromozom1),cromozom1,cromozom2,punct_rupere)
                populatie1[i_participa_combinare[i]] = float(decodificare(populatie1[i_participa_combinare[i]], x, y))
                populatie1[i_participa_combinare[i + 1]] = float(decodificare(populatie1[i_participa_combinare[i + 1]], x, y))

        else:
            n = len(i_participa_combinare)
            for i in range(0, len(i_participa_combinare) - 3, 2):
                cromozom1 = codificare(populatie1[i_participa_combinare[i]], x, y, p)
                cromozom2 = codificare(populatie1[i_participa_combinare[i + 1]], x, y, p)
                punct_rupere = int(random.uniform(1, len(cromozom1)))
                populatie1[i_participa_combinare[i]], populatie1[i_participa_combinare[i + 1]] = incrucisare(len(cromozom1),cromozom1,cromozom2,punct_rupere)
                populatie1[i_participa_combinare[i]] = float(decodificare(populatie1[i_participa_combinare[i]], x, y))
                populatie1[i_participa_combinare[i + 1]] = float(decodificare(populatie1[i_participa_combinare[i + 1]], x, y))

            cromozom1 = codificare(populatie1[i_participa_combinare[n - 3]], x, y, p)
            cromozom2 = codificare(populatie1[i_participa_combinare[n - 2]], x, y, p)
            cromozom3 = codificare(populatie1[i_participa_combinare[n - 1]], x, y, p)
            punct_rupere = int(random.uniform(1, len(cromozom1)))
            populatie1[i_participa_combinare[n - 3]], populatie1[i_participa_combinare[n - 2]], populatie1[i_participa_combinare[n - 1]] = incrucisare3(len(cromozom1), cromozom1, cromozom2, cromozom3, punct_rupere)
            populatie1[i_participa_combinare[n - 3]] = float(decodificare(populatie1[i_participa_combinare[n - 3]], x, y))
            populatie1[i_participa_combinare[n - 2]] = float(decodificare(populatie1[i_participa_combinare[n - 2]], x, y))
            populatie1[i_participa_combinare[n - 1]] = float(decodificare(populatie1[i_participa_combinare[n - 1]], x, y))

    i_mutatie = []
    for i in range(1, nr_cromozomi + 1):
        #u = random.uniform(0, 1)
        #if u < prob_mutatie:
            i_mutatie.append(i)
            populatie1[i] = mutatie(codificare(float(populatie1[i]), x, y, p), prob_mutatie)
            populatie1[i] = decodificare(populatie1[i], x, y)
    functie_rezultat = [0]
    for i in range(1, nr_cromozomi + 1):
        functie_rezultat.append(functie(populatie1[i], a, b, c))

    maxim = -999999
    for i in range(1,nr_cromozomi+1):
        f1 = functie(float(populatie1[i]),a,b,c)
        if f1 > maxim:
            maxim = f1

    fisier.write(f"Maxim={maxim} Media={sum(functie_rezultat,0)/len(functie_rezultat)}\n")
    maxime.append(maxim)

fisier.write(f"\nMedia maximelor = {sum(maxime,0)/len(maxime)} ")