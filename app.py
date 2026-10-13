numero = 67
palpite_atual = 0
jogadas_abaixo = 0
jogadas_acima = 0
total_tentativas = 0
menor_palpite = 100
maior_palpite = 0

print("===== JOGO DE ADIVINHAÇÃO =====")
print("\nEstou pensando em um número entre 0 e 100.")
print("Tente descobrir qual é!")

while  (palpite_atual != numero):
  palpite_atual = int(input("\nDigite seu palpite: "))

  if palpite_atual < numero:
   print("O número secreto é maior!")
   jogadas_abaixo += 1
   total_tentativas += 1

   if (palpite_atual < menor_palpite):
     menor_palpite = palpite_atual

  elif palpite_atual > numero:
     print("O número secreto é menor!")
     jogadas_acima += 1
     total_tentativas += 1

     if (palpite_atual > maior_palpite):
       maior_palpite = palpite_atual

  else:
    print("Parabéns! Você acertou!")
    total_tentativas += 1

if (total_tentativas <= 3):
  resultado = "\nExcelente! Sua intuição está afiada!"

elif (total_tentativas <= 6):
  resultado = "\nMuito bom! Foi por pouco... ou nem tanto!"

else:
  resultado = "\nConseguiu! Mas é hora de treinar essa intuição!"

if (menor_palpite == 101):
  menor_palpite = "nenhum"

if (maior_palpite == -0):
  maior_palpite = "nenhum"

print("\n===== RESUMO DO JOGO =====")
print("\nNúmero de tentativas: ", total_tentativas)
print("Chutes abaixo do número correto: ", jogadas_abaixo)
print("Chutes acima do número correto: ", jogadas_acima)
print("\nMenor palpite: ", menor_palpite)
print("Maior palpite: ", maior_palpite)
print(resultado)