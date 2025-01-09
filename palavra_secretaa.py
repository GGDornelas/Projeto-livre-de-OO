import random
import os
import time
import json

class Faculdade:
    def __init__(self, nivel):
        self.nivel = nivel
        self.palavras_secretas = []
        self.palavra_secreta = ''
        self.letras_acertadas = ''
        self.letras_acertadas_2 = ''
        self.letra_digitada = ''
        self.letra_digitada_2 = ''
        self.contagem = 0
        self.contagem2 = 0
        self.dicas = 0

        if self.nivel == 1:
            self.palavras_secretas += 'aula', 'aluno', 'professor', 'prova', 'caderno', 'quadro', 'nota'
        elif self.nivel == 2:
            self.palavras_secretas += 'engenharia', 'fisica', 'calculo', 'matricula', 'quimica', 'notebook'
        elif self.nivel == 3:
            self.palavras_secretas += 'laboratorio', 'auditorio', 'lapiseira', 'compasso', 'carteira'
        elif self.nivel == 4:
            self.palavras_secretas += 'discente', 'obelisco', 'restaurante universitario', 'orientacao a objetos'
        else:
            print('Não era pra chegar aqui, digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
        

    def objetivo(self):
        print(
            'Olá, bem-vindo ao jogo PALAVRA SECRETA, o objetivo desse jogo é você conseguir acertar qual a palavra que está\nescondida na menor quantidade de tentativas possiveis'
            )

    def jogar_solo(self):
        self.player = input('Digite o nome do jogador: ')
        print(f'TEMA: {temadojogo}')
        print(f'Nível escolhido = {self.nivel}')
        print('SE VOCÊ SOUBER A PALAVRA DIGITE # e TENTA A SORTE!')

        tempo_inicio = time.time()
        
        while True:
            self.letra_digitada = input('Digite uma letra: ').lower()
            
            if self.letra_digitada == '#':
                palavra_digitada = input('Qual é a palavra? ').lower()
                if palavra_digitada == self.palavra_secreta:
                    self.contagem += 1
                    os.system('clear')
                    print('Parabéns, você ganhou!')
                    print(f'A palavra era "{self.palavra_secreta}"')
                    print(f'{self.contagem} tentativas')
                    print(f'Dicas usadas: {self.dicas}')
                    if minutos == 0:
                        print(f'Tempo gasto: {segundos:.2f} segundos')
                    else:
                        print(f'Tempo gasto: {minutos:.0f} minutos e {segundos:.2f} segundos')
                    break
                else:
                    self.contagem += 1
                    os.system('clear')
                    print('ERROUUUUU')
                    continue

            if len(self.letra_digitada) > 1 or len(self.letra_digitada) == 0 or self.letra_digitada.isdigit() or self.letra_digitada.isalnum() == False:
                print('Digite apenas uma letra')
                continue

            
            self.contagem += 1

            if ' ' in self.palavra_secreta:
                self.letras_acertadas += ' '

            if self.letra_digitada in self.palavra_secreta:
                self.letras_acertadas += self.letra_digitada

            if self.contagem == 10:
                for letra in self.palavra_secreta:
                    if letra not in self.letras_acertadas:
                        self.letras_acertadas += letra
                        break

            if self.contagem == 20:
                for letra in self.palavra_secreta:
                    if letra not in self.letras_acertadas:
                        self.letras_acertadas += letra
                        break

            if self.contagem == 30:
                for letra in self.palavra_secreta:
                    if letra not in self.letras_acertadas:
                        self.letras_acertadas += letra
                        break

            self.palavra_formada = ''
            for self.letra_secreta in self.palavra_secreta:
                if self.letra_secreta in self.letras_acertadas:
                    self.palavra_formada += self.letra_secreta
                else:
                    self.palavra_formada += '*'
                
    
            os.system('clear')
            if self.contagem == 10:
                self.dicas += 1
                print('Já se foram 10 tentativas, vou te ajudar!!') 
            if self.contagem == 20:
                self.dicas += 1
                print('Burro??? Já se foram 20 tentativas, vou te dar mais uma letra.') 
            if self.contagem == 30:
                self.dicas += 1
                print('30 tentativas, sério? Nunca mais joga isso, vou te dar a ultima letra.')
                                         
            tempo_decorrido = time.time() - tempo_inicio
            minutos = int(tempo_decorrido // 60)
            segundos = int(tempo_decorrido % 60)
            milissegundos = int((tempo_decorrido * 100) % 100)
            
            print(f'\rTempo: {minutos:02}:{segundos:02}.{milissegundos:02}\n', end='', flush=True)
            time.sleep(0.01)
            print(f'Palavra formada: {self.palavra_formada}')
        

            if self.palavra_formada == self.palavra_secreta:
                os.system('clear')
                
                print('Parabéns, você ganhou!')
                print(f'A palavra era "{self.palavra_secreta}"')
                print(f'{self.contagem} tentativas')
                print(f'Dicas usadas: {self.dicas}')
                if minutos == 0:
                    print(f'Tempo gasto: {segundos:.2f} segundos')
                else:
                    print(f'Tempo gasto: {minutos:.0f} minutos e {segundos:.2f} segundos')
                break

        desempenho_manager = Podio()
        desempenho_manager.registrar_desempenho(jogador=self.player, tema=temadojogo, nivel=self.nivel, tentativas=self.contagem, tempo_gasto=f'{tempo_decorrido:.2f}')
    

    def jogar_multiplayer(self):
        self.player_1 = input('Digite o nome do jogador 1: ')
        self.player_2 = input('Digite o nome do jogador 2: ')   

        print(f'Vez do {self.player_1}')
        print(f'Nível escolhido = {self.nivel}')
        print('SE VOCÊ SOUBER A PALAVRA DIGITE # e TENTA A SORTE!')

        tempo_inicio_1 = time.time()
        self.minutos_1 = 0
        self.segundos_1 = 0

        while True:
            self.letra_digitada = input('Digite uma letra: ').lower()
            
            if self.letra_digitada == '#':
                palavra_digitada = input('Qual é a palavra? ').lower()
                
                if palavra_digitada == self.palavra_secreta:
                    self.contagem += 1
                    os.system('clear')
                    tempo_final_1 = time.time()
                    self.tempo_gasto_1 = tempo_final_1 - tempo_inicio_1
                    self.minutos_1 = self.tempo_gasto_1 // 60
                    self.segundos_1 = self.tempo_gasto_1 % 60
                    print('Parabéns, você acertou!')
                    break
                else:
                    self.contagem += 1
                    os.system('clear')
                    print('ERROUUUUU')
                    continue

            if len(self.letra_digitada) > 1 or len(self.letra_digitada) == 0 or self.letra_digitada.isdigit() or self.letra_digitada.isalnum() == False:
                print('Digite apenas uma letra')
                continue
            
            self.contagem += 1

            if ' ' in self.palavra_secreta:
                self.letras_acertadas += ' '

            self.palavra_secreta_2 = self.palavra_secreta

            if self.letra_digitada in self.palavra_secreta:
                self.letras_acertadas += self.letra_digitada


            self.palavra_formada = ''
            for self.letra_secreta in self.palavra_secreta:
                if self.letra_secreta in self.letras_acertadas:
                    self.palavra_formada += self.letra_secreta
                else:
                    self.palavra_formada += '*'

            os.system('clear')
            print(f'Palavra formada: {self.palavra_formada}')

            if self.palavra_formada == self.palavra_secreta:
                os.system('clear')
                tempo_final_1 = time.time()
                self.tempo_gasto_1 = tempo_final_1 - tempo_inicio_1
                self.minutos_1 = self.tempo_gasto_1 // 60
                self.segundos_1 = self.tempo_gasto_1 % 60
                print('Parabéns, você acertou!')
                break
        
        print('-------------------------------------')
        print(f'Vez do {self.player_2}')
        print(f'Nível escolhido = {self.nivel}')
        print('SE VOCÊ SOUBER A PALAVRA DIGITE # e TENTA A SORTE!')

        tempo_inicio_2 = time.time()
        self.minutos_2 = 0
        self.segundos_2 = 0


        while True:
            self.letra_digitada_2 = input('Digite uma letra: ').lower()
            
            if self.letra_digitada_2 == '#':
                palavra_digitada_2 = input('Qual é a palavra? ').lower()
                
                if palavra_digitada_2 == self.palavra_secreta_2:
                    self.contagem2 += 1
                    os.system('clear')
                    tempo_final_2 = time.time()
                    self.tempo_gasto_2 = tempo_final_2 - tempo_inicio_2
                    self.minutos_2 = self.tempo_gasto_2 // 60
                    self.segundos_2 = self.tempo_gasto_2 % 60
                    print('Parabéns, você acertou!')
                    break
                else:
                    self.contagem2 += 1
                    os.system('clear')
                    print('ERROUUUUU')
                    continue

            if len(self.letra_digitada_2) > 1 or len(self.letra_digitada_2) == 0 or self.letra_digitada_2.isdigit() or self.letra_digitada_2.isalnum() == False:
                print('Digite apenas uma letra')
                continue
            
            self.contagem2 += 1

            if ' ' in self.palavra_secreta_2:
                self.letras_acertadas_2 += ' '

            if self.letra_digitada_2 in self.palavra_secreta_2:
                self.letras_acertadas_2 += self.letra_digitada_2

            self.palavra_formada_2 = ''
            for self.letra_secreta_2 in self.palavra_secreta_2:
                if self.letra_secreta_2 in self.letras_acertadas_2:
                    self.palavra_formada_2 += self.letra_secreta_2
                else:
                    self.palavra_formada_2 += '*'

            os.system('clear')
            print(f'Palavra formada: {self.palavra_formada_2}')

            if self.palavra_formada_2 == self.palavra_secreta_2:
                os.system('clear')
                tempo_final_2 = time.time()
                self.tempo_gasto_2 = tempo_final_2 - tempo_inicio_2
                self.minutos_2 = self.tempo_gasto_2 // 60
                self.segundos_2 = self.tempo_gasto_2 % 60
                print('Parabéns, você acertou!')
                break
            
        print('-------------------------`')
        print('RESULTADOS FINAIS')
        if self.minutos_1 == 0:
            print(f'{self.player_1} usou {self.contagem} tentativas e levou {self.segundos_1:.2f} segundos')
        else:
            print(f'{self.player_1} usou {self.contagem} tentativas e levou {self.minutos_1:.0f} minutos e {self.segundos_1:.2f} segundos')
        if self.minutos_2 == 0:
            print(f'{self.player_2} usou {self.contagem2} tentativas e levou {self.segundos_2:.2f} segundos')
        else:
            print(f'{self.player_2} usou {self.contagem2} tentativas e levou {self.minutos_2:.0f} minutos e {self.segundos_2:.2f} segundos')
        print('----------------------------------')
        print('PORTANTO...')
        if self.contagem > self.contagem2:
            print(f'{self.player_2} GANHOU A PARTIDA!!')
        elif self.contagem2 > self.contagem:
            print(f'{self.player_1} GANHOU A PARTIDA!!')
        elif self.contagem == self.contagem2:
            if self.tempo_gasto_1 > self.tempo_gasto_2:
                print(f'{self.player_2} GANHOU A PARTIDA!!')
            elif self.tempo_gasto_2 > self.tempo_gasto_1:
                print(f'{self.player_1} GANHOU A PARTIDA!!')
            else:
                print('DEu EMPATE!')
        else:
            print('DEU EMPATE!')
            
class Ingles(Faculdade):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.palavras_secretas = []
        if self.nivel == 1:
            self.palavras_secretas += 'hello', 'thank you', 'nice', 'good', 'bad', 'easy'
        elif self.nivel == 2:
            self.palavras_secretas += 'table', 'wood', 'maybe', 'because', 'beautiful', 'notebook', 'backpack'
        elif self.nivel == 3:
            self.palavras_secretas += 'weird', 'outside', 'church', 'health', 'noise'
        elif self.nivel == 4:
            self.palavras_secretas += 'throw', 'through', 'abroad', 'knowledge', 'environmental'
        else:
            print('digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
    
    def traducao(self):
        traducoes = {
            'hello': 'Olá',
            'thank you': 'Obrigado',
            'nice': 'Legal',
            'good': 'Bom',
            'bad': 'Ruim',
            'easy': 'Fácil',
            'table': 'Mesa',
            'wood': 'Madeira',
            'maybe': 'Talvez',
            'because': 'Porque',
            'beautiful': 'Bonito',
            'notebook': 'Caderno',
            'backpack': 'Mochila',
            'weird': 'Estranho',
            'outside': 'Fora',
            'church': 'Igreja',
            'health': 'Saúde',
            'noise': 'Barulho',
            'throw': 'Arremessar',
            'through': 'Através',
            'abroad': 'Exterior',
            'knowledge': 'Conhecimento',
            'environmental': 'Ambiental',
        }
        return traducoes.get(self.palavra_secreta, 'Não tem tradução')
    
    def objetivo(self):
        super().objetivo()
        print('Tema = INGLÊS')

    def jogar_solo(self):
        super().jogar_solo()  
        print(f'Tradução: {self.traducao()}')

    def jogar_multiplayer(self):
        super().jogar_multiplayer()
    

class Paises(Faculdade):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.palavras_secretas = []
        if self.nivel == 1:
            self.palavras_secretas += 'brasil', 'peru', 'china', 'argentina', 'estados unidos', 'franca', 'alemanha', 'canada'
        elif self.nivel == 2:
            self.palavras_secretas += 'china', 'japao', 'holanda', 'australia', 'grecia', 'turquia', 'egito', 'inglaterra', 'qatar'
        elif self.nivel == 3:
            self.palavras_secretas += 'singapura', 'irlanda do norte', 'argelia', 'tailandia', 'albania', 'marrocos', 'angola', 'nova zelandia', 'afeganistao'
        elif self.nivel == 4:
            self.palavras_secretas += 'chipre', 'etiopia', 'burkina faso', 'azerbaijao', 'sudao'
        else:
            print('digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
    
    
    def objetivo(self):
        super().objetivo()
        print('Tema = PAISES')

    def jogar_solo(self):
        super().jogar_solo()  

    def jogar_multiplayer(self):
        super().jogar_multiplayer()

class Podio:
    def __init__(self, arquivo='melhores_desempenhoss.json'):
        self.arquivo = arquivo
        self.desempenhos = self.carregar_desempenhos()

    def carregar_desempenhos(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        return []

    def salvar_desempenhos(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.desempenhos, f, indent=4)

    def registrar_desempenho(self, jogador, tema, nivel, tentativas, tempo_gasto):
        novo_desempenho = {
            "jogador": jogador,
            "tema": tema,
            "nivel": nivel,
            "tentativas": tentativas,
            "tempo_gasto": tempo_gasto
        }
           
        self.desempenhos.append(novo_desempenho)
        
        self.salvar_desempenhos()

    def exibir_desempenhos(self):
        if not self.desempenhos:
            print("Nenhum desempenho registrado ainda.")
        else:
            for desempenho in self.desempenhos:
                print(f"Jogador: {desempenho['jogador']}, Tema: {desempenho['tema']}, "
                      f"Nível: {desempenho['nivel']}, Tentativas: {desempenho['tentativas']}, "
                      f"Tempo Gasto: {desempenho['tempo_gasto']} segundos") 


    def podio_arrumado(self):
        melhores_por_nivel = {}

        for desempenho in self.desempenhos:
            nivel = desempenho['nivel']
            if nivel not in melhores_por_nivel:
                melhores_por_nivel[nivel] = desempenho
            else:
                melhor = melhores_por_nivel[nivel]
                if (desempenho['tentativas'] < melhor['tentativas'] or 
                    (desempenho['tentativas'] == melhor['tentativas'] and desempenho['tempo_gasto'] < melhor['tempo_gasto'])):
                    melhores_por_nivel[nivel] = desempenho

        print("Pódio de Melhores Jogadores:")
        for nivel, desempenho in sorted(melhores_por_nivel.items()):
            print(f"Nível {nivel}:")
            print(f"  Jogador: {desempenho['jogador']}")
            print(f"  Tema: {desempenho['tema']}")
            print(f"  Tentativas: {desempenho['tentativas']}")
            print(f"  Tempo Gasto: {desempenho['tempo_gasto']} segundos")
        
def selecionar_tema():
    print(
            'Olá, bem-vindo ao jogo PALAVRA SECRETA, o objetivo desse jogo é você conseguir acertar qual a palavra que está\nescondida na menor quantidade de tentativas possiveis'
            )
    print("Escolha o tema do jogo:")
    print("1 - Faculdade")
    print("2 - Inglês")
    print("3 - Países")

    while True:
        try:
            tema = int(input("Escolha o tema: "))
            if tema in [1, 2, 3]:
                os.system('clear')
                return tema
            else:
                print("Tema inválido. Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

def selecionar_nivel():
    print("Escolha o nível de dificuldade")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Muito Difícil")

    while True:
        try:
            nivel = int(input("Escolha o nível: "))
            if nivel in [1, 2, 3, 4]:
                os.system('clear')
                return nivel
            else:
                print("Nível inválido. Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

def selecionar_modo_de_jogo():
    print("Selecione o modo de jogo")
    print("1 - Solo")
    print("2 - Multijogador")

    while True:
        try:
            modo = int(input("Escolha o nível: "))
            if modo in [1, 2]:
                os.system('clear')
                return modo
            else:
                print("Nível inválido, Escolha entre 1 ou 2")
        except ValueError:
            print("Por favor, insira um número válido")


modo_de_jogo = selecionar_modo_de_jogo()
tema_jogo = selecionar_tema()
nivel_jogo = selecionar_nivel()

if tema_jogo == 1:
    jogo = Faculdade(nivel_jogo)
    temadojogo = 'Faculdade'
    if modo_de_jogo == 1:
        jogo.jogar_solo()
    elif modo_de_jogo == 2:
        jogo.jogar_multiplayer()
    else:
        print('Deu ruim')
elif tema_jogo == 2:
    jogo = Ingles(nivel_jogo)
    temadojogo = 'Inglês'
    if modo_de_jogo == 1:
        jogo.jogar_solo()
    elif modo_de_jogo == 2:
        jogo.jogar_multiplayer()
    else:
        print('Deu ruim')
elif tema_jogo == 3:
    jogo = Paises(nivel_jogo)
    temadojogo = 'Paises'
    if modo_de_jogo == 1:
        jogo.jogar_solo()
    elif modo_de_jogo == 2:
        jogo.jogar_multiplayer()
    else:
        print('Deu ruim')
else:
    print("Não era pra chegar aqui")
    exit()


def printar_podio():
    ver_podio = Podio()
    while True:
        deseja = input('Deseja ver o podio? s/n ----- ').lower()
        if deseja == 's':
            os.system('clear')
            ver_podio.podio_arrumado()
            break
        elif deseja == 'n':
            os.system('clear')
            print('Jogo encerrado!')
            break
        else:
            os.system('clear')
            print('Digite algo válido, "s" ou "n"')
            continue

if modo_de_jogo == 1:
    aparecer_podio = printar_podio()
else:
    None