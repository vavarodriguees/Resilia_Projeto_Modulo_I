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
    print('''-------------------- Fase Quatro --------------------
 Muito bem, agora Ela precisa queimar as cordas o mais rápido possível, enquanto os capangas estiver distraído. 
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
    print('''-------------------- Fase Três --------------------
Ela começa analisar como poderia sair daquela situação, sabe que quanto mais tempo passar nas mãos dos bandidos,
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
    print(''' -------------------- Fase Dois --------------------
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
def personagem_dois_fase_tres():
    print(''' -------------------- Fase Três --------------------
como Iron sabe como funciona o seu regime do seu governo, sabem que irão deixá-lo por dias 
na cela sem comida, ou com pouca. E sabendo que seu corpo precisa mais de água do que a comida, prioriza
a água e quando realmente precisar, comer o sanduíche. 

Dias se passam... e Iron está cada dia mais fraco.. Quando aparece um supervisor e o carrega para uma sala. 
Supervisor explica que com as habilidades de Iron ele poderá competir em um torneio mortal, cada pessoa tem 
uma habilidade diferente. 

Iron precisa tomar uma decisão: Qual decisão tomar?\n''')
    texto_personagem_um = '''1 - Ficar e esperar sua sentença. 
2 - Encarar o torneio. 
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        print(''' --- GAME OVER --- ''')
    else:
        print('''--- VOCÊ VENCEU!!! ---
Mesmo sabendo que é um torneio mortal, ele já estaria morto se continuasse na cadeia, pelo menos 
se vencer, estará livre e será respeitado pelo seu feito. ''') 

def personagem_dois_fase_dois():
    print('''-------------------- Fase Dois --------------------
Iron decide ficar, desta maneira enfrentar todas as consequências. 
Iron é preso e colocado em uma cela, contém uma garrafa d’agua, cerca de 1L e um sanduíche. 
Iron precisa tomar uma decisão: Qual decisão tomar?\n''')
    texto_personagem_um = '''1 - Comer o sanduíche e tomar água aos poucos. 
2 - Não comer o sanduíche agora e ir tomando pouca água. 
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        print(''' --- GAME OVER --- ''')
    else:
        personagem_dois_fase_tres()
        

def personagem_dois_fase_um():
    print('--- IRON ---')
    print('''Iron é um guerreiro, trabalha todos os dias para sobreviver, mas a condição de sua vida é extremamente precária. 
Então, por necessidade, ele resolver furtar pães de uma padaria. Ele tenta disfarçar e não ser reconhecido, mas está condenado. 
Iron precisa tomar uma decisão: Qual decisão tomar?\n''')
    texto_personagem_um = '''1 - Enfrentar as consequências. 
2 - Fugir daquela cidade. 
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        personagem_dois_fase_dois()
    else:
        print(''' --- GAME OVER --- 
Seria caçado e morto, sem chance de recorrer sua pena.''')

# --------------------- Contexto Iron ---------------------------------

# --------------------- Contexto Percy ---------------------------------

def personagem_tres_fase_tres():
    print(''' -------------------- Fase Três --------------------
Percy precisa revidar e se defender ao mesmo tempo, para Laura ele é um traidor.
Ela está descontando toda sua raiva, Laura possui os poderes elétricos e Percy, poder do fogo. 
No meio da batalha sangrenta, Percy precisa tomar uma decisão: Qual decisão tomar? 
\n''')
    texto_personagem_um = '''1 - Laura está sendo atacada por um prateado, que acredita estar 
ajudando Percy, ele tem que escolher entre deixar Laura morrer. 
2 - Expor seu lado sobre verdadeiro sobre sua opinião aos vermelhos e a Laura.  
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        print(''' --- GAME OVER --- ''')
    else:
        print('''--- VOCÊ VENCEU!!! ---
Pelos seus instintos, defende Laura, atacando o prateado. Percy consegue tirar Laura da batalha, 
a partir disso eles criam um laço para derrubar o Reinado do Rei.  ''') 

def personagem_tres_fase_dois():
    print(''' -------------------- Fase Dois --------------------
Deixando Laura, Percy pode trabalhar dentro da realeza, para planejar como poderá acabar 
com as castas e consegui igualdade do seu povo. 

Porém, em poucos dias, começa uma rebelião, contra os prateados, não é um povo vermelho comum, é um 
povo vermelho com habilidades prateadas. 

Está acontecendo um confronto, queima roupa, na praça principal da cidade. Tem sangue prateado e vermelho
para todos os lados e no meio de tudo isso está Laura, com olhos fixos em Percy pronto para atacá-lo. 
Percy precisa tomar uma decisão: Qual decisão tomar? ''')
    texto_personagem_um = '''1 - Revidar o ataque de Laura. 
2 - Apenas se defender. 
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        personagem_tres_fase_tres()
    else:
        print(''' --- GAME OVER --- ''')

def personagem_tres_fase_um():
    print('--- Percy ---')
    print('''Percy é herdeiro do trono prateado, jovem e forte! Seu pai é o rei de Montevidéu, um reino
onde pessoas de sangue prateado é soberano sobre as pessoas de sangue vermelho. 

Percy, não tem afeição por essas classes importas pelos prateados, quer o reinado para que o povo de Montevidéu,
seja um só. No meio de tanta turbulência, ele encontra Laura, a sangue vermelha rebelde. Desde então, mesmo com 
a diferença de classes eles começam a entender que possuem qualidades e as mesmas vontades com relação ao povo 
prateado e vermelho. 

Com o passar do tempo, o rei, começa a desconfiar de Percy, decide colocar seus homens para acabar com essa amizade. 
Percy precisa tomar uma decisão: Qual decisão tomar? \n''')
    texto_personagem_um = '''1 - Deixar Laura e aceitar a decisão de seu pai de separá-los e voltar para o meio das 
pessoas prateadas. 
2 - Ficar com ela e enfrentar seu pai.  
Qual opção seguir?\n'''
    escolha_usuario = fazer_escolha(texto_personagem_um)
    if escolha_usuario == 1:
        personagem_tres_fase_dois()
    else:
        print(''' --- GAME OVER --- ''')

# --------------------- Contexto Percy ---------------------------------

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
