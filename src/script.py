tc = input("TC Numaranızı Yazınız: ")  # Python 3
tcstring = str(tc)

sliceobj = slice(10,11)
tcson = tcstring[sliceobj]
tcson = int(tcson)
tcsoncift = None # Son Rakamı Çift Olmalıdır
tcilk10toplamson11 = None # 1, 3, 5, 7 ve 9. rakamın toplamının 7 katı ile 2, 4, 6 ve 8. rakamın toplamının 9 katının toplamının birler basamağı 10. rakamı verir
digerozellik = None # 1, 3, 5, 7 ve 9. rakamın toplamının 8 katının birler basamağı 11. rakamı vermektedir.
onuncurakamtoplam = None # ilk 10 rakamın toplamının birler basamağı, 11. rakamı vermektedir.

ciftrakamlar = [0,2,4,6,8]

if tcson not in ciftrakamlar:
    print("TC Numarasının Sonu Çift Olmalı")
else:
    tcsoncift = True
sliceobj2 = slice(0,10)

tcilk10 = tcstring[sliceobj2]
i = 0
for tcrakam in tcilk10:
    i += int(tcrakam)
    
sliceobj3 = slice(1,2)
stri = str(i)

songerek = stri[sliceobj3]

if songerek == str(tcson):
    tcilk10toplamson11 = True
else:
    print("TC Numarasının ilk 10 hanesinin toplamının son rakamı TC Numarasının son rakamına eşit olmalıdır")

sliceobj4 = slice(0,10,2)
birucbesyedidokuz = tcstring[sliceobj4]
a = 0
for rakam in birucbesyedidokuz:
    a += int(rakam)
a = a * 7
sliceobj5 = slice(1,9,2)
ikidortaltisekiz = tcstring[sliceobj5]
h = 0
for rakam in ikidortaltisekiz:
    h += int(rakam)
h = h * 9
bothtektoplam = str(a+h)
sliceobj6 = slice(2,3)
son = bothtektoplam[sliceobj6]
sliceobj7 = slice(9,10)
onbirincihane = tcstring[sliceobj7]

if son == onbirincihane:
    onuncurakamtoplam = True
else:
    print("TC Numarası bir özelliğe takıldı, doğru değil.(1)")
lastbro = tcstring[sliceobj4]
asd = 0
for last in lastbro:
    asd += int(last)
asd = asd * 8
sliceobj9 = slice(2,3)
asd = str(asd)
asd = asd[len(asd) - 1]

sonhane = slice(10,11)
sonhane = tcstring[sonhane]
if sonhane == asd:
    digerozellik = True
else:
    print("TC Numarası bir özelliğe takıldı, doğru değil.(2)")
    
def sonucYaz():
    if tcsoncift == True:
        print("TC Numarasının Sonu Çift ✔️")
    if tcilk10toplamson11 == True:
        print("TC Numarasının ilk 10 toplamı sonu 11. Rakamı Veriyor ✔️")
    if onuncurakamtoplam == True:
        print("TC Numarasının Diğer Özellikleri Doğru (1) ✔️")
    if digerozellik == True:
        print("TC Numarasının Diğer Özellikleri Doğru (2) ✔️")
    if digerozellik == True and onuncurakamtoplam == True and tcilk10toplamson11 == True and tcsoncift == True:
        print("TC Numarası Doğru ✔️")
    else:
        print("TC Numarası Doğru Değil ❌")
sonucYaz()



#sonrakam = tc.slice(0,6)
#print(text[sonrakam])