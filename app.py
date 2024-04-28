print('Boas vindas para o Jogo do número secreto')

numeroSecreto = int(5)
chute = input('Digite um numero de 1 a 10: ')
chute =int(chute)

if chute == numeroSecreto:
    print(f'Parabéns você acertou: {numeroSecreto} = {chute}')
# print(chute)
