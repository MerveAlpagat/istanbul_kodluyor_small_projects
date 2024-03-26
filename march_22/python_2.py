# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
fibonacci =[1,1]
for i in range(2,20):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)  
    
# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
sayi = int(input("Sayi Giriniz:"))
 
toplam=0
 
for i in range(1,sayi):
     if(sayi%i == 0):
         toplam +=i
        
if(sayi == toplam):
     print("Mükemmel Sayidir.")
else:
     print("Mükemmel Sayi Degildir")

# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))
 
if (birinciSayi > ikinciSayi):
     kucuksayi = ikinciSayi
else:
     kucuksayi = birinciSayi
for i in range(1,kucuksayi+1):
     if (birinciSayi % i==0) and (ikinciSayi%i ==0):
         ebob = i
         ekok = (birinciSayi*ikinciSayi)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Sayıyı Girin : "))
if sayi > 1:

 for i in range(2,sayi):
     if (sayi % i) == 0:
        print(sayi," Asal Sayı Değildir.")
        break
     else:
        print(sayi," Asal Sayıdır.")
 
else:
   print(sayi," Asal Sayı Değildir.")

# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
    
sayi = int(input("Bir sayı girin: "))
faktor = 2
print(sayi, "sayısının asal çarpanları:")
while faktor <= sayi:
    if sayi % faktor == 0:
        print(faktor)
        sayi //= faktor
    else:
        faktor += 1


