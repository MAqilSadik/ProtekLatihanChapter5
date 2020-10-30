print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
bil=int(input('Tebakan Anda : '))
while True:
    if(bil<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        bil=int(input('Tebakan Anda : '))
    elif(bil>10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        bil=int(input('Tebakan Anda : '))
    elif(bil==10):
        print('yeeee...Bilangan tebakan anda benar')
        break
