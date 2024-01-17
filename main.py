import funzioni as fn

if __name__ == '__main__':
    driver = fn.attiva()
    punti = fn.ottieni_nodi(driver)
    if not punti:
        print('panico')
    includi_seggiovie = False
    while 1:
        print('Benvenuto nell\'app degli sciatori')
        print('1} Trova il percorso più facile tra due punti')
        print('2} Trova il percorso più rapido tra due punti')
        print(f'    Seggiovie incluse:{includi_seggiovie}, 9 per cambiare')
        print('3} Vedi difficoltà piste')
        print('4} Vedi stato piste')
        print('0} Esci')
        num = ''
        while 1:
            num = input('')
            try:
                num = int(num)
                break
            except:
                print('Valore inserito non valido, per favore inserisci un altro valore')
        if num == 0:
            fn.spegni(driver)
            quit()
        if num == 1:
            fine, inizio = '', ''
            for num, nodo in enumerate(punti):
                print(f'{num + 1}){nodo}')
            resta = True
            while resta:
                inizio = input('Scegli il numero del punto in cui ti trovi: ')
                try:
                    inizio = int(inizio) - 1
                    if inizio > len(punti) - 1:
                        print('Valore inserito non valido, per favore inserisci un altro valore')
                        continue
                    resta = False
                except:
                    print('Valore inserito non valido, per favore inserisci un altro valore')
            resta = True
            while resta:
                fine = input('Scegli il numero del punto in cui vuoi arrivare: ')
                try:
                    fine = int(fine) - 1
                    if fine > len(punti):
                        print('Valore inserito non valido, per favore inserisci un altro valore')
                        continue
                    resta = False
                except:
                    print('Valore inserito non valido, per favore inserisci un altro valore')
            if inizio == fine:
                print('Sei arrivato')
            else:
                nodi, archi, dif_tot = fn.ottieni_percorso_facile(partenza=punti[inizio], arrivo=punti[fine],
                                                                  seggiovie=includi_seggiovie, driver=driver)
                if nodi:
                    print('partendo ', end='')
                    arrivo = len(nodi)
                    for num, _ in enumerate(nodi):
                        if num < arrivo - 1:
                            print(f"da {nodi[num]}, prendi il percorso {archi[num]} per arrivare a {nodi[num + 1]}")
                    print(f'sei arrivato, la difficoltà totale è di: {dif_tot}')
                else:
                    print('percorso non disponibile')
        if num == 2:
            fine, inizio = '', ''
            for num, nodo in enumerate(punti):
                print(f'{num + 1}){nodo}')
            resta = True
            while resta:
                inizio = input('Scegli il numero del punto in cui ti trovi: ')
                try:
                    inizio = int(inizio) - 1
                    if inizio > len(punti) - 1:
                        print('Valore inserito non valido, per favore inserisci un altro valore')
                        continue
                    resta = False
                except:
                    print('Valore inserito non valido, per favore inserisci un altro valore')
            resta = True
            while resta:
                fine = input('Scegli il numero del punto in cui vuoi arrivare: ')
                try:
                    fine = int(fine) - 1
                    if fine > len(punti):
                        print('Valore inserito non valido, per favore inserisci un altro valore')
                        continue
                    resta = False
                except:
                    print('Valore inserito non valido, per favore inserisci un altro valore')
            if inizio == fine:
                print('Sei arrivato')
            else:
                nodi, archi, tempo_tot = fn.ottieni_percorso_breve(partenza=punti[inizio], arrivo=punti[fine],
                                                                   seggiovie=includi_seggiovie, driver=driver)
                if nodi:
                    print('partendo ', end='')
                    arrivo = len(nodi)
                    for num, _ in enumerate(nodi):
                        if num < arrivo - 1:
                            print(f"da {nodi[num]}, prendi il percorso {archi[num]} per arrivare a {nodi[num + 1]}")
                    print(f'sei arrivato, il tempo totale stimato è di: {tempo_tot} minuti')
                else:
                    print('percorso non disponibile')
        if num == 3:
            difficolta = fn.ottieni_piste_difficolta(driver)
            for pista in difficolta:
                print(f'{pista[0]}: difficoltà {pista[1] - 1}')
        if num == 4:
            stato = fn.ottieni_piste_aperte(driver)
            for pista in stato:
                print(pista)
        if num == 9:
            includi_seggiovie = not includi_seggiovie
## usa il path
