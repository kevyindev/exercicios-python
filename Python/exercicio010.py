##Converter reais em dolares
real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real/4.94
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))

##Converter dolares em reais
dolar = float(input('Quantos dolares você tem na carteira? U$'))
real = dolar/0.20
print('Com U${:.2f} você pode comprar R${:.2f}'.format(dolar, real))