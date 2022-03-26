quantidade = float(input('Digite o numero que deseja fazer a conversão: '))

x = int(input('''Digite o número da unidade de medida que deseja fazer a conversão: 
[ 1 ] Milhas
[ 2 ] Polegadas
[ 3 ] Pés
[ 4 ] Centímetros
[ 5 ] Metros
[ 6 ] Quilômetros

Digite aqui sua opção: '''))

if x == 1:
    milhas = quantidade
    polegadas = quantidade * 63360
    pes = quantidade * 5280
    cm = quantidade * 160934
    m = quantidade * 1609.34
    km = quantidade * 1.60934

    print('''A medida de {} Milhas corresponde a: 
    {} Milhas 
    {} Polegadas 
    {} Pes 
    {} Centímetros 
    {} Metros  
    {} Quilômetros'''.format(milhas, milhas, polegadas, pes, cm, m, km))

elif x == 2:
    milhas = quantidade / 63360
    polegadas = quantidade
    pes = quantidade / 12
    cm = quantidade * 2.54
    m = quantidade / 39.37
    km = quantidade / 39370

    print('''A medida de {} Polegadas corresponde a: 
    {} Milhas 
    {} Polegadas 
    {} Pes 
    {} Centímetros 
    {} Metros 
    {} Quilômetros'''.format(polegadas, milhas, polegadas, pes, cm, m, km))

elif x == 3:
    milhas = quantidade / 5280
    polegadas = quantidade * 12
    pes = quantidade
    cm = quantidade * 30.48
    m = quantidade / 3.281
    km = quantidade / 3281

    print('''A medida de {} Pes corresponde a: 
    {} Milhas 
    {} Polegadas 
    {} Pes 
    {} Centímetros 
    {} Metros 
    {} Quilômetros'''.format(pes, milhas, polegadas, pes, cm, m, km))

elif x == 4:
    milhas = quantidade / 160934
    polegadas = quantidade / 2.54
    pes = quantidade / 30.48
    cm = quantidade
    m = quantidade / 100
    km = quantidade / 100000

    print('''A medida de {} Centímetros corresponde a: 
    {} Milhas 
    {} Polegadas 
    {} Pes 
    {} Centímetros 
    {} Metros 
    {} Quilômetros'''.format(cm, milhas, polegadas, pes, cm, m, km))

elif x == 5:
    milhas = quantidade / 1609
    polegadas = quantidade * 39.37
    pes = quantidade * 3.281
    cm = quantidade * 100
    m = quantidade
    km = quantidade / 1000

    print('''A medida de {} Metros corresponde a: 
    {} Milhas 
    {} Polegadas 
    {} Pes 
    {} Centímetros 
    {} Metros 
    {} Quilômetros'''.format(m, milhas, polegadas, pes, cm, m, km))

elif x == 6:
    milhas = quantidade / 1.609
    polegadas = quantidade * 39370
    pes = quantidade * 3281
    cm = quantidade * 100000
    m = quantidade * 1000
    km = quantidade

    print('''A medida de {} Quilômetros corresponde a: 
    {} Milhas 
    {} Polegadas 
    {} Pes 
    {} Centímetros 
    {} Metros
    {} Quilômetros'''.format(km, milhas, polegadas, pes, cm, m, km))

else:
    print('Você digitou um valor errado, por favor digite novamente')
