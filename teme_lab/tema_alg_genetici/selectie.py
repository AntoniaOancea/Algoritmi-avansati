def selectie(coeficienti, dimensiune_populatie, cromozomi):
    a, b, c = coeficienti
    suma_fitness = 0.0
    sume_partiale_fitness = []

    # Calculăm suma totală a fitness-urilor și sumele parțiale ale fitness-urilor
    for cromozom in cromozomi:
        fitness = a * cromozom ** 2 + b * cromozom + c
        suma_fitness += fitness
        sume_partiale_fitness.append(suma_fitness)

    capete_intervale = []

    # Calculăm capetele intervalelor de selecție
    for suma_partiala in sume_partiale_fitness:
        capat_interval = suma_partiala / suma_fitness
        capete_intervale.append(capat_interval)

    return capete_intervale


# Citirea datelor de intrare
coeficienti = list(map(int, input().split()))
dimensiune_populatie = int(input())
cromozomi = list(map(float, input().split()))

# Calcularea capetelor intervalelor de selecție
intervale_selectie = selectie(coeficienti, dimensiune_populatie, cromozomi)

# Afișarea capetelor intervalelor de selecție
print("{:.6f}".format(0))
for capat_interval in intervale_selectie:
    print("{:.6f}".format(capat_interval))
