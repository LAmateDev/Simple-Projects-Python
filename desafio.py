class Jogo():
    def __init__(self, titulo, preco, classificacao, genero):
        self.genero = genero
        self.preco = preco
        self.titulo = titulo
        self.classificcao = classificacao

    def exibir_detalhes(self):
        print(f"Título do jogo: {self.titulo}\nPreço: R${self.preco}\nGênero: {self.genero}\nClassificação: {self.classificcao}")

    
class Jogador():
    def __init__(self, nickname, id, saldo):
        self.nickname = nickname
        self.id = id
        self.saldo = saldo
        self.biblioteca_jogos = []

    def ver_perfil(self):
        print(f"Perfil {self.nickname} - ID: {self.id}\nSeu saldo: {self.saldo}")
        if self.biblioteca_jogos == []:
            print("Sem jogos na biblioteca")
        else:
            print("Seus Jogos:")
            for i in self.biblioteca_jogos:
                print(f"{i.titulo}")

    def adicionar_jogo(self, jogo):
        if isinstance(jogo, Jogo):
            self.biblioteca_jogos.append(jogo)
            print(f"O jogo {jogo.titulo} foi adicionado na biblioteca com sucesso!")
        else:
            print("Erro, passe um objeto como parametro")

    def debitar_saldo(self, debitar):
        self.debitar = debitar
        if self.saldo > self.debitar:
            self.saldo -= self.debitar
            print(f"Valor debitado com sucesso\nNovo saldo {self.saldo}")
        else: 
            print(f"Saldo Insuficiente! O valor a ser debitado é maior que o saldo disponível\nSaldo disponível: {self.saldo}")

    
    def comprar_jogo(self, jogo):
        if isinstance(jogo, Jogo):
            if self.saldo > jogo.preco:
                print(f"O Jogo {jogo.titulo} foi comprado com sucesso")
                self.adicionar_jogo(jogo)
                self.debitar_saldo(jogo.preco)
            else:
                print(f"Saldo Insufuciente\nSeu saldo: {self.saldo}\nPreço do Jogo: {jogo.preco}")
        else:
            print(f"Erro, passe um objeto como parametro")

    
    def adicionar_saldo(self, deposito):
        self.deposito = deposito
        self.saldo += self.deposito
        print(f"Valor depositado com sucesso!\nNovo saldo: {self.saldo}")

class Plataforma():
    def __init__(self, nome):
        self.nome = nome
        self.catalago_jogos = []
        self.jogadores_cadastrados = []

    def adicionar_jogo_catalogo(self, jogo):
        if isinstance (jogo, Jogo):
            self.catalago_jogos.append(jogo)
            print(f"{jogo.titulo} adicionado ao catalogo com sucesso")
        else:
            print("ERRO, passe um objeto jogo como parametro")

    def adicionar_jogador(self, jogador):
        if isinstance(jogador, Jogador):
            self.jogadores_cadastrados.append(jogador)
            print(f"{jogador.nickname} cadastrado com sucesso")
        else:
            print("ERRO, passe um objeto jogo como parametro")

    def buscar_jogo(self, titulo_jogo):
        self.titulo_jogo = titulo_jogo
        for j in self.catalago_jogos:
            if j.titulo == self.titulo_jogo:
                return j
                j.exibir_detalhes()
            
                



   
jogo1 = Jogo("Dead cells", 50, "10+", "Rogue Like")  #Criando objeto

jogo1.exibir_detalhes()   #Exibe detalhes do jogo

jogador1 = Jogador("SarahGames", "3473473", 200)  # Criando objeto jogador/usuario
jogador1.ver_perfil()    # Mostra o perfil do jogador
jogador1.comprar_jogo(jogo1)   #Compramos um jogo, o adicionamos na biblioteca e debitamos o valor do jogo do saldo atual do usuario
jogador1.ver_perfil()  # Mostra o perfil com as atualizações feitas
jogador1.adicionar_saldo(1000)   #adiciona saldo na carteira
jogador1.ver_perfil()     # Mostra o perfil com as atualizaçẽos feitas

steam = Plataforma("steam")
steam.adicionar_jogo_catalogo(jogo1)


