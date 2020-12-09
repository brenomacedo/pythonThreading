from threading import Thread
from time import sleep

def carro(velocidade, trajeto, piloto):
    posicao = 0
    while posicao < trajeto:
        print(f'carro {piloto}: {posicao} \n')
        posicao += velocidade
        sleep(0.3)


t_carro1 = Thread(target=carro, args=[5, 100, 'Breno'])
t_carro2 = Thread(target=carro, args=[10, 100, 'BrenoPvP'])

t_carro1.start()
t_carro2.start()