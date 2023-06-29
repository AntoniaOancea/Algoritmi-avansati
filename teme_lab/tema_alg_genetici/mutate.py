
def mutatie (cromozom, pozitii):
    for gena in pozitii:
            cromozom[gena] = 1 - cromozom[gena]
    return cromozom

lungime_cromozom, numar_mutatii = map(int, input().split())
cromozom = list(map(int,input().strip()))
pozitii = list(map(int, input().split()))

rezultat = mutatie(cromozom,pozitii)

print(''.join(str(gena) for gena in rezultat))