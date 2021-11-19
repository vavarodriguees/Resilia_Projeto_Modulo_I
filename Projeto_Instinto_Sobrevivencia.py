# Função para fazer as escolhas dos personagens

def fazer_escolha(texto):
    escolha = input(texto)
    while True:
        if escolha == '1' or escolha == '2':
            break;
        escolha = input("Por favor, escolha 1 ou 2:\n")
    return int(escolha)

# --------------------- Contexto Ela ---------------------------------

def personagem_um_fase_quatro():
    print('''Isqueiro: Muito bem, agora Ela precisa queimar as cordas o mais rápido possível, enquanto os capangas estiver distraído. 
Ela tem que ser ágil, pois depende dos sequestradores não sentirem o cheiro da corda queimada. 
Ela precisa tomar mais uma decisão, ela não sabe onde está provavelmente num lugar afastado da cidade.\n''')
    texto_personagem_um = '''1 - Correr para um lugar seguro e escondido!
2 - Correr sem para, para que possa sair daquele lugar e encontrar ajuda! \n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        print('''--- VOCÊ VENCEU!!! ---
Ela conhece boa parte das matas e sabe se localizar sob as estrelas, quando escurece,
ela vai se guiando pela mata, apenas com o isqueiro acesso quando necessário para não 
chamar atenção. Consegue retornar a uma estrada, ficando atenta a todos que passem por ali.
Com fome e cede, chega o final da estrada, onde encontra uma casa pacata, onde pode procurar ajuda.\n''') 
    else:
        print('--- GAME OVER ---')   

def personagem_um_fase_tres():
    print('''Ela começa analisar como poderia sair daquela situação, sabe que quanto mais tempo passar nas mãos dos bandidos,
menos chance de sair viva ela terá. 
Ela verifica no senário, um isqueiro de um dos sequestradores e uma chave de fenda, qual a decisão mais sensata a se tomar?
A pergunta é: o que você faria?
''')
    texto_personagem_um = '''1 - Espera a distração deles e pega o isqueiro!
2 - Pegar a chave de fenda.\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        personagem_um_fase_quatro()
    else:
        print('--- GAME OVER ---')

def personagem_um_fase_dois():
    print('''
Ela entra no carro! Já tinha visto o sujeito se esgueirando pelo quarteirão algumas vezes. Após alguns metros... 
NADA... Tudo fica escuro. 
Ela acorda num lugar escuro, sombrio, amarrada, com três homens encapuzados na sua frente! Entra em pânico com a cena a sua frente, 
a pergunta é: o que você faria?\n''')
    texto_personagem_um = '''1-  Tenta se desvencilhar das amarras.
2-  Analisa toda situação em sua volta.
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        print('---GAME OVER---')
    else:
        personagem_um_fase_tres()

def personagem_um_fase_um():
    print('--- ELA ---')
    print('''Ela tem sua vida, um pouco pacata, é uma menina estudiosa com vários anseios pela vida. Sempre metódica, realiza as mesmas tarefas diariamente. 
Mora com a mãe e o seu padrasto, possui o Ted, seu cachorro de estimação. 
Em um sábado à noite, Ela aceita sair com sua melhor amiga, num café próximo a sua casa e decide ir caminhando...
Mas está atrasada, ela tem duas opções: 
''')
    texto_personagem_um = '''1 - Aceitar uma carona na rua. 
2 - Cortar caminho por um atalho. 
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        personagem_um_fase_dois()
    else:
        print(''' --- GAME OVER --- 
    Ela entra por um caminho estranho, um beco escuro onde consegue ver silhueta de uma pessoa ao final,
    com é um caminho dentro do condomínio ela continua.... Inesperadamente é surpreendida por um homem 
    a segura e o outro sai detrás da sua sombra levam tudo que podem e a deixam jogada sozinha naquele lugar.''')

# --------------------- Contexto Ela ---------------------------------

# --------------------- Contexto Iron ---------------------------------
def personagem_dois_fase_um():
    print()

def personagem_tres_fase_um():
    print("Personagem 3 escolhido")

def inicio():
    print(
'''Bem-vindo ao seu inferno de sobrevivência: 
Aqui você tomará decisões cruciais para sua existência e cada decisão implicará em uma eventualidade! 
Cuidado, tudo é muito frágil, inclusive sua vida!  
Muito bem, primeiro passo será tomado as cegas, cada personagem tem características diferentes. 
    ''')
    personagem = input('''Escolha qual personagem você quer ingressar: 
1 - Ela;
2 - Iron;
3 - Percy.\n''')
    while True:
        if personagem == '1' or personagem == '2' or personagem == '3':
            break;
        personagem = input("Por favor, escolha 1, 2 ou 3:\n")
    if personagem == '1':
        personagem_um_fase_um()
    elif personagem == '2':
        personagem_dois_fase_um()
    else:
        personagem_tres_fase_um()

inicio()
