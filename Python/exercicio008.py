medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
m = medida
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('O valor de {} em milimetros é {}'.format(medida, mm))
print('O valor de {} em centimetros é {}'.format(medida, cm))
print('O valor de {} em decimetros é {}'.format(medida, dm))
print('O valor em metros é {}'.format(m))
print('O valor de {} em decametros é {}'.format(medida, dam))
print('O valor de {} em hectares é {}'.format(medida, hm))
print('O valor de {} em quilometros é {}'.format(medida, km))

