#Inicialização:
print('[Calculadora Python Beta 0.1]\nBy: M4ttPizz4\n')
operação = int(input('Digite o número relacionado com a operação desejada:\n1.Somar.\n2.Subtrair.\n3.Multiplicar.\n4.Dividir.\n'))

#Condições:
#Soma:
if(operação == 1):
  soma1 = float(input('Insira o primeiro número e pressione ENTER:'))
  soma2 = float(input('Insira o segundo número e pressione ENTER:'))
  somar = soma1 + soma2
  print(somar)

#Subtração:
if(operação == 2):
  subt1 = float(input('Insira o primeiro número e pressione ENTER:'))
  subt2 = float(input('Insira o segundo número e pressione ENTER:'))
  subtr = subt1 - subt2
  print(subtr)

#Multiplicar:
if(operação == 3):
  mult1 = float(input('Insira o primeiro número e pressione ENTER:'))
  mult2 = float(input('Insira o segundo número e pressione ENTER:'))
  multr = mult1 * mult2
  print(multr)

#Dividir:
if(operação == 4):
  divi1 = float(input('Insira o primeiro número e pressione ENTER:'))
  divi2 = float(input('Insira o segundo número e pressione ENTER:'))
  divir = divi1 / divi2
  print(divir)
