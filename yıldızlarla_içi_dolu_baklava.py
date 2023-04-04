#sadece while kullanarak yıldızlarla içi dolu baklava dilimi 
#baklava şeklinin yarısnın boyu kullanıcdan alınacak
i = 1
yildiz = '*'
bosluk = ' '
kullanici_deger = int(input("Bir deger girin:")) #kullanıcıdan baklava şeklinin yarısının boyunu alma
while(i <= kullanici_deger):  #baklava şeklinin üst kısmı
    print(bosluk*(kullanici_deger-i),yildiz*(i+(i-1)))
    i+= 1

i = 1
while(i<= kullanici_deger-1):  #baklava şeklinin alt kısmı
    print(bosluk*i,yildiz*((kullanici_deger-i)+kullanici_deger-(i+1)))
    i+= 1