print('--------------------------------------------------------------------------------')
print('Bem vindo ao jogo Pedra, Papel e Tesoura!')
print('Esse jogo teremos dois jogadores, cada um deve escolher uma opção e ganhar.')
print('--------------------------------------------------------------------------------')

opcoes = ['pedra', 'papel', 'tesoura']

jogador1 = str(input('Escolha alguma opção: '))
jogador2 = str(input('Escolha alguma opção: '))

jogador1 = jogador1.lower().strip()
jogador2 = jogador2.lower().strip()

jogada1 = jogador1
jogada2 = jogador2

print(f'Jogador 1 escolheu: {jogador1}')
print(f'Jogador 2 escolheu: {jogador2}')

if jogada1 not in opcoes or jogada2 not in opcoes:
    print('Uma ou ambas as jogadas são inválidas.')

else:

    if jogada1 == jogada2:
        print('Empate!')
    elif jogada1 == 'pedra' and jogada2 == 'tesoura':
        print('Jogador 1 ganhou!')
    elif jogada1 == 'tesoura' and jogada2 == 'papel':
        print('Jogador 1 ganhou!')
    elif jogada1 == 'papel' and jogada2 == 'pedra':
        print('Jogador 1 ganhou!')
    else:
        print('Jogador 2 ganhou!')

print('='*40)