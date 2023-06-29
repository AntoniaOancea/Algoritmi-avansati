def incrucisare(lungime_cromozom, cromozom1, cromozom2, punct_rupere):
    segment1_cromozom1 = cromozom1[:punct_rupere]
    segment2_cromozom1 = cromozom1[punct_rupere:]

    segment1_cromozom2 = cromozom2[:punct_rupere]
    segment2_cromozom2 = cromozom2[punct_rupere:]

    cromozom_rezultat1 = segment1_cromozom1 + segment2_cromozom2
    cromozom_rezultat2 = segment1_cromozom2 + segment2_cromozom1

    return cromozom_rezultat1, cromozom_rezultat2


# Citirea datelor de intrare
lungime_cromozom = int(input())
cromozom1 = input()
cromozom2 = input()
punct_rupere = int(input())

# Aplicarea încrucișării
cromozom_rezultat1, cromozom_rezultat2 = incrucisare(lungime_cromozom, cromozom1, cromozom2, punct_rupere)

# Afișarea rezultatului
print(cromozom_rezultat1)
print(cromozom_rezultat2)
