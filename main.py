import funzioni as fn

if __name__ == '__main__':
    driver = fn.attiva()
    punti = fn.ottieni_nodi(driver)
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
                percorso = fn.ottieni_percorso_facile(partenza=punti[inizio], arrivo=punti[fine],
                                                      seggiovie=includi_seggiovie, driver=driver)
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
                percorso = fn.ottieni_percorso_breve(partenza=punti[inizio], arrivo=punti[fine],
                                                     seggiovie=includi_seggiovie, driver=driver)

        if num == 9:
            includi_seggiovie = not includi_seggiovie
## usa il path
