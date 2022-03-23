#Projeto de que faz uma escolha para você, faça uma pergunta e o programa te dará uma resposta
import random

class DecidaPorMim:
    def __init__(self):
        # Possíveis respostas do programa
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei te responder, siga seu coração',
            'Não faça isso de jeito nenhum!',
            'Acho que está na hora certa!'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')                # Input para pergunta do usuário
        print(random.choice(self.respostas))        # Escolha randomica do programa

decisao = DecidaPorMim()
decisao.Iniciar()