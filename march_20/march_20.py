import math
# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Lutfen boyunuzu giriniz:"))
agirlik= float(input("Lütfen kilonuzu giriniz:"))

vki= agirlik/(boy*boy)
print("Vücut kitle endeksiniz:",vki)

# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("Lütfen maaşınızı giriniz:"))
zam_orani = float(input("Lütfen zam oranınızı giriniz: %"))
zamli_maas = maas + (maas * zam_orani/100)
print(zamli_maas)

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = int(input("Lütfen birinci sayıyı giriniz:"))
sayi2 = int (input("Lütfen ikinci sayıyı giriniz:"))
sayi3 = int (input("Lütfen üçüncü sayıyı giriniz:"))

en_buyuk = sayi1
if sayi2 > en_buyuk:
    en_buyuk = sayi2
if sayi3 > en_buyuk:
    en_buyuk = sayi3   
print("En büyük sayı:", en_buyuk)            

# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
yaricap = float(input("Dairenin yarıçapını girin:"))
alan = math.pi * yaricap **2 
cevre = 2 *math.pi * yaricap 
print("Dairenin alanı:", alan)
print("Dairenin çevresi", cevre)
               
# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi = input("Lütfen bir sayı girin:")
ters_sayi = sayi[::-1]
if sayi==ters_sayi:
    print("Girdiğiniz sayı palindromdur. ")
else:
    print("Girdiğiniz sayı palindrom değildir.")    



