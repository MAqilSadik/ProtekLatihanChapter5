#latihan1 no 2

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
