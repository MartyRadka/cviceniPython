from random import randrange

soucet = 0
while soucet < 21:
    print('Máš {} bodů'.format(soucet))
    odpoved = input('Otočit kartu? ')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        print('Otočila jsi: ', karta)
        soucet = soucet + karta
    elif odpoved == 'ne':
        break
    else:
        print('Nerozumím! Odpovídej "ano", nebo "ne"')

if soucet == 21:
    print('Gratuluji! Vyhrála jsi!')
elif soucet > 21:
    print('Smůla! {} bodů je moc!'.format(soucet))
else:
    print("Chybělo jen {} bodů!".format(21 - soucet))









