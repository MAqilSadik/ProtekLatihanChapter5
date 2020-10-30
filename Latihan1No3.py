#Latihan1 no 3

indo = int(input('Nilai Bahasa Indonesia:'))

ipa  = int(input('Nilai IPA:'))

mtk  = int(input('Nilai Matematika:'))

print('--------------------------')

if(indo < 0 or indo > 100):
    print('maaf input ada yang tidak valid')

elif(ipa < 0 or ipa > 100):
    print('maaf input ada yang tidak valid')

elif(mtk < 0 or mtk > 100):
    print('maaf input ada yang tidak valid')

elif(indo > 70 and ipa > 70 and mtk > 80):
    print('LULUS')

else:
    print('TIDAK LULUS')
    print('Sebab:')

    if(indo<60):
        print('Nilai Bahasa Indonesia kurang dari 60')

    if(mtk<70):
        print('Nilai MTK kurang dari 70')
