import funzioni as fn


if __name__ == '__main__':
    print('Benvenuto nell\'app degli sciatori')
    print('1} Trova il percorso più facile tra due punti')
    print('2} Trova il percorso più rapido tra due punti')
    print('3} Vedi difficoltà piste')
    print('4} Vedi piste aperte')
    print('0} Esci')
    num = ''
    while 1:
        num = input('')
        try:
            num = int(num)
            break
        except:
            print('Valore inserito non valido, per favore inserici un altro valore')
    if num == 0:
        quit()

## usa il path