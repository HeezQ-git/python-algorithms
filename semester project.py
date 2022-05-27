oddzialy = []
pracownicy = []
liczbaPracownikow = -1

n = int(input())

def zmiana(index, ilosc, oddzial):
    osoby = []
    last = None
    for _ in range(int(ilosc)+1):
        if index >= len(oddzial['pracownicy']):
            index = 0
        else:
            if oddzial['pracownicy'][index] not in osoby:
                osoby.append(oddzial['pracownicy'][index])
            else:
                last = oddzial['pracownicy'][index]

            if index+1 < len(oddzial['pracownicy']):
                last = oddzial['pracownicy'][index+1]
            else:
                # last = None
                last = oddzial['pracownicy'][0]
            index += 1
    return osoby, last

for x in range(n):
    cmd = input()
    if cmd.startswith('a w'):
        cmd = cmd.split('a w ')[1]
        if len(cmd.split(' ')) > 1:
            nazwaOddzialu = cmd.split(' ')[0]
            wielkoscZmiany = int(cmd.split(' ')[1])
            oddzialy.append({
                "nazwa": nazwaOddzialu,
                "wielkosc": wielkoscZmiany,
                "pracownicy": [],       # lista id pracowników
                "kierownik": None       # id pracownika
            })
    elif cmd.startswith('a e'):
        cmd = cmd.split('a e ')[1]
        if len(cmd.split(' ')) > 1:
            nazwaPracownika = cmd.split(' ')[0]
            nazwaOddzialu = cmd.split(' ')[1]

            for oddzial in oddzialy:
                if oddzial['nazwa'] == nazwaOddzialu:
                    liczbaPracownikow += 1
                    pracownicy.append({
                        "id": liczbaPracownikow,
                        "nazwa": nazwaPracownika
                    })
                    # (ileZmian*wielkoscZmiany) % iloscPracownikow   -- następny kierownik zmiany
                    if len(oddzial['pracownicy']) > 0:
                        oddzial['pracownicy'].insert(oddzial['pracownicy'].index(oddzial['kierownik']), liczbaPracownikow)
                    else:
                        oddzial['pracownicy'].append(liczbaPracownikow)
                        oddzial['kierownik'] = liczbaPracownikow
                    break
    elif cmd.startswith('d w'):
        cmd = cmd.split('d w ')[1]
        nazwaOddzialu = cmd
        for oddzial in oddzialy:
            if oddzial['nazwa'] == nazwaOddzialu:
                oddzialy.remove(oddzial)
                break
    elif cmd.startswith('m '):
        cmd = cmd.split('m ')[1]
        idPracownika = int(cmd.split(' ')[0])
        nazwaOddzialu = cmd.split(' ')[1]

        for oddzial in oddzialy:
            if idPracownika in oddzial['pracownicy']:
                i = oddzial['pracownicy'].index(idPracownika)
                oddzial['pracownicy'].remove(idPracownika)
                if oddzial['kierownik'] == idPracownika:
                    if i >= len(oddzial['pracownicy']):
                        i = 0
                    if len(oddzial['pracownicy']) > 0:
                        if oddzial['pracownicy'][i]:
                            oddzial['kierownik'] = oddzial['pracownicy'][i]
                        elif oddzial['pracownicy'][i-1]:
                            oddzial['kierownik'] = oddzial['pracownicy'][i-1]
            if oddzial['nazwa'] == nazwaOddzialu:
                if len(oddzial['pracownicy']) > 0:
                    oddzial['pracownicy'].insert(oddzial['pracownicy'].index(oddzial['kierownik']), idPracownika)
                else:
                    oddzial['pracownicy'].append(idPracownika)
                    oddzial['kierownik'] = idPracownika
    elif cmd.startswith('e w '):
        cmd = cmd.split('e w ')[1]
        nazwaOddzialu = cmd.split(' ')[0]
        nowaNazwaOddzialu = cmd.split(' ')[1]
        nowaWielkoscZmiany = cmd.split(' ')[2]

        for oddzial in oddzialy:
            if oddzial['nazwa'] == nazwaOddzialu:
                oddzial['nazwa'] = nowaNazwaOddzialu
                oddzial['wielkosc'] = nowaWielkoscZmiany
    elif cmd.startswith('e e '):
        cmd = cmd.split('e e ')[1]
        idPracownika = int(cmd.split(' ')[0])
        nazwaPracownika = cmd.split(' ')[1]

        for pracownik in pracownicy:
            if pracownik['id'] == idPracownika:
                pracownik['nazwa'] = nazwaPracownika
    elif cmd.startswith('s '):
        cmd = cmd.split('s ')[1]
        iloscZmian = int(cmd.split(' ')[0])

        zmianaKierownika = True
        if iloscZmian == 0:
            zmianaKierownika = False

        for oddzial in oddzialy:
            if len(oddzial['pracownicy']) > 0:
                ilosc = oddzial['wielkosc']
                index = oddzial['pracownicy'].index(oddzial['kierownik'])
                title = ""
                osoby = []
                osobyFinal = []
                osoby2 = []

                for x in range(iloscZmian+1):
                    osoby, last = zmiana(index, ilosc, oddzial)
                    osobyFinal.append(osoby)
                    if last != None:
                        index = oddzial['pracownicy'].index(last)
                        if len(oddzial['pracownicy']) == len(osobyFinal[-1]):
                            title = "(niedobór pracowników)"
                
                if int(oddzial['wielkosc']) == len(oddzial['pracownicy']) or len(oddzial['pracownicy']) > int(oddzial['wielkosc']):
                    title = ""

                if zmianaKierownika == True:
                    pracownikID = oddzial['pracownicy'].index(oddzial['pracownicy'][(iloscZmian*ilosc) % len(oddzial['pracownicy'])-1])
                    oddzial['kierownik'] = oddzial['pracownicy'][pracownikID]

                for osoba in osobyFinal[-1]:
                    for pracownik in pracownicy:
                        if pracownik['id'] == osoba:
                            osoby2.append(pracownik['nazwa'])

                napis = ','.join(osoby2)
                print(f"{title}{oddzial['nazwa']}:{napis}.")
                    
            else:
                print(f"(niedobór pracowników){oddzial['nazwa']}:.")
        print('-')
