# Máquina escolhe aleatoriamente um item da lista "filmes"
# e cabe ao usuário adivinhar o item escolhido pelo computador.
import random as rd

# Lista contendo todas as possibilidades 
filmes = ['Duna', 'Mad Max', 'Nosferatu', 'Bastardos Inglórios', 'Oppenheimer', 
'Batman', 'Vingadores', 'Homem Aranha', 'Indiana Jones', 'Transformers']

# Pega um filme aleatorio da lista e armezenar na variavel
filme_secreto = rd.choice(filmes)

# Usuário tenta adinhar o filme e o armazena na variavel    
chute_usuario = input(print('Qual o seu chute? '))

# Verifica se o usuário acertou o filme
while filme_secreto != chute_usuario:
    print('Errou, chute novamente! ')
    chute_usuario = input(print('Qual o seu chute? '))
   
    while filme_secreto == chute_usuario:
        print('Parabéns, você acertou!')
        break