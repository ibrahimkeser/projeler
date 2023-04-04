#sadece while kullanarak yıldızlarla içi dolu baklava dilimi
#baklava şeklinin yarısnın boyu kullanıcdan alınacak
i = 1
yıldız = '*'
bosluk = ' '
kullanıc_deger = int(input("Bir deger girin: ")) #kullanıcıdan baklava diliminin yarısının boyunu alma
while(i <= kullanıc_deger):  #baklava şeklinin üst kısmı
    print(bosluk*(kullanıc_deger-i),yıldız*(i+(i-1)))
    i+= 1

i = 1
while(i<= kullanıc_deger-1):  #baklava şeklinin alt kısmı
    print(bosluk*i,yıldız*((kullanıc_deger-i)+kullanıc_deger-(i+1)))
    i+= 1