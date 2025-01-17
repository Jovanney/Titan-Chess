import pygame as pg 
import utils.constants as constants
import utils.matrix_transformations as mt
import sprite_mananger.sprite_mananger as sm
import random


clock = pg.time.Clock()
display = pg.display.set_mode(constants.WINDOW_SIZE, 0, 32)

tile_sheet_image = pg.image.load('./resources/atlas/iso_tileset1.png')
tile_sheet = sm.SpriteManganger(tile_sheet_image)

block_black_floor = tile_sheet.get_image(0, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))
block_white_floor = tile_sheet.get_image(1, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))
orbe = tile_sheet.get_image(2, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 1, (0, 0, 0))
torre_img = tile_sheet.get_image(3, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 2, (0, 0, 0))

#CRIANDO BORDAS IMAGINARIAS
border_TopLeft = []
border_TopRight = []
border_DownLeft = []
border_DownRight = []

for i in range(8):
    VariavelX=(mt.mudanca_base(1, i, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][0]
    VariavelY=(mt.mudanca_base(1, i, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][1]
    
    border_TopLeft.append((int(VariavelX)-30,int(VariavelY)-32, 20))
for i in range(8):
    VariavelX=(mt.mudanca_base(i+1, 0, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][0]
    VariavelY=(mt.mudanca_base(i+1, 0, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][1]
        
    border_TopRight.append((int(VariavelX)+30,int(VariavelY)-32, 20))
        
for i in range(8):
    VariavelX=(mt.mudanca_base(8, i, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][0]
    VariavelY=(mt.mudanca_base(8, i, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][1]

    border_DownRight.append((int(VariavelX)+30,int(VariavelY)+32, 20))
        
for i in range(8):
    VariavelX=(mt.mudanca_base(i, 7, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][0]
    VariavelY=(mt.mudanca_base(i, 7, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE),284,10,10)[0][1]

    border_DownLeft.append((int(VariavelX)+30,int(VariavelY)+62, 20))


tile_sheet_image = pg.image.load('./resources/atlas/iso_tileset1.png')
tile_sheet = sm.SpriteManganger(tile_sheet_image)
personagem_sheet = pg.image.load('./resources/atlas/personagem.png')
perso = sm.SpriteManganger(personagem_sheet)


block_black_floor = tile_sheet.get_image(0, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))
block_white_floor = tile_sheet.get_image(1, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 4, (0, 0, 0))
orbe = tile_sheet.get_image(2, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 1, (0, 0, 0))
torre_img = tile_sheet.get_image(3, 0, constants.FLOOR_SIZE, constants.FLOOR_SIZE, 2, (0, 0, 0))

#ANIMAÇÃO SPRITE PLAYER

lista_animacao = []
animacao_linha = 4
animacao_coluna = 9
ultima_atualizarcao = pg.time.get_ticks()
velocidade_animacao = 150
animacao_passo = []

frame_direita = 27
frame_esquerda = 9
frame_cima = 0
frame_baixo = 18

for y in range(animacao_linha):
    for x in range(animacao_coluna):
        lista_animacao.append(perso.get_image(x,y+8, 64, 64, 1, (0, 0, 0)))

#CORES USADAS:
AzulMarinho = (0,0,123) #Player
AzulClaroFosco = (153,153,255) #Imunidade
Ciano = (0,238,238)  #Velocidade

def calcularDistanciaPontos(xA,xB,yA,yB):
    return (((xB-xA)**2)+((yB-yA)**2))**(1/2)

def tela_inicial():
    global run
    while not run:
        display.blit(begin, (0,0))
        pg.display.update()

        for event in pg.event.get(): 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()

                elif event.key == 13:
                    run = True

def jogar_novamente():
    global run
    cont_frames = 1
    i = 0
    #SE O PLAYER MORREU, MOSTRA GAME OVER E PERGUNTA SE QUER JOGAR NOVAMENTE
    if Dama.morto:
        while Dama.morto or i <= 661:
            i += 1
            if cont_frames <= 480 :
                if cont_frames <= 40:
                    display.blit(game_over[0], (0,0)) 

                elif cont_frames <= 280:
                    display.blit(game_over[1], (0,0))    

                elif cont_frames <= 480:
                    display.blit(game_over[2], (0,0))    

                pg.display.update()
                cont_frames += 1
                for event in pg.event.get():

                    if event.type == pg.QUIT:
                        pg.quit()

                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            pg.quit()
                        
                        else:
                            Dama.vida = 1
                            Dama.ammo = 1
                            run = True
                            Dama.morto = False
                            Dama.posicao_x = 1200
                            Dama.posicao_y = 500 
                            torre.vida = 200
                            torre.bossX = constants.WINDOW_SIZE[0] // 2
                            torre.bossY = constants.WINDOW_SIZE[1] // 2    
                            sombra.posicao_X = constants.WINDOW_SIZE[0] // 2
                            sombra.posicao_Y = constants.WINDOW_SIZE[1] // 2
                            
                            item_vida_coletada = False
                            static_timer = None
                            last_item_time = None

                            
                    
            else:
                cont_frames = 41
    #SE O BOSS MORREU, MOSTRA WIN E PERGUNTA SE QUER JOGAR NOVAMENTE
    if torre.morto:
        while torre.morto or i <= 661:
            i += 1
            if cont_frames <= 480 :
                if cont_frames <= 40:
                    display.blit(win[0], (0,0)) 

                elif cont_frames <= 280:
                    display.blit(win[1], (0,0))    

                elif cont_frames <= 480:
                    display.blit(win[2], (0,0))    

                pg.display.update()
                cont_frames += 1
                for event in pg.event.get():

                    if event.type == pg.QUIT:
                        pg.quit()

                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            pg.quit()
                        
                        else:
                            Dama.vida = 1
                            Dama.ammo = 1
                            
                            run = True
                            torre.morto = False
                            torre.vida = 200
                            Dama.posicao_x = 1200
                            Dama.posicao_y = 500 
                            torre.bossX = constants.WINDOW_SIZE[0] // 2
                            torre.bossY = constants.WINDOW_SIZE[1] // 2    
                            sombra.posicao_X = constants.WINDOW_SIZE[0] // 2
                            sombra.posicao_Y = constants.WINDOW_SIZE[1] // 2


                            item_vida_coletada = False
                            static_timer = None
                            last_item_time = None
                        
            else:
                cont_frames = 41

#CONTADORES DE TEMPO SPAWN ITENS

static_timer = None
last_item_time = None

#CONTADORES DE TEMPO DE DANO AO PLAYER
static_timer_player = None
last_hit_time = None
tempo_imune = 3000 #milisegundos
hits = 0


class Player(object):
    def __init__(self, posicao_x, posicao_y) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = 3
        self.raio = 20
        self.cor = (0,0,123)
        self.hitbox = (self.posicao_x, self.posicao_y, self.raio)
        self.ammo = 1
        self.vida = 1
        self.imune = False
        self.morto = False

        self.canMove={'cima' : True,
                      'direita' : True,
                      'esquerda': True,
                      'baixo' : True}

        self.cima = True
        self.direita = False
        self.esquerda = False
        self.baixo = False
        
    def desenhar(self):
        if self.direita:
            display.blit(lista_animacao[frame_direita], (Dama.posicao_x - 29, Dama.posicao_y - 32))
        if self.esquerda:
            display.blit(lista_animacao[frame_esquerda], (Dama.posicao_x - 29, Dama.posicao_y - 32))
        if self.cima:
            display.blit(lista_animacao[frame_cima], (Dama.posicao_x - 29, Dama.posicao_y - 32))
        if self.baixo:
            display.blit(lista_animacao[frame_baixo], (Dama.posicao_x - 29, Dama.posicao_y - 32))
        
    def andar(self):
        keys = pg.key.get_pressed()
    
        if keys[pg.K_LEFT]: #and self.posicao_x >= 490:
            if Dama.canMove['esquerda']:
                self.posicao_x -= self.velocidade

            Dama.esquerda = True
            Dama.cima = False
            Dama.direita = False
            Dama.baixo = False

        if keys[pg.K_RIGHT]: #and self.posicao_x <= 1440:
            if Dama.canMove['direita']:
                self.posicao_x += self.velocidade

            Dama.direita = True
            Dama.cima = False
            Dama.esquerda = False
            Dama.baixo = False


        if keys[pg.K_UP]: #and self.posicao_y >= 275:
            if Dama.canMove['cima']:
                self.posicao_y -= self.velocidade

            Dama.cima = True
            Dama.direita = False
            Dama.esquerda = False
            Dama.baixo = False

        if keys[pg.K_DOWN]: #and self.posicao_y <= 735:
            if Dama.canMove['baixo']:
                self.posicao_y += self.velocidade

            Dama.baixo = True
            Dama.cima = False
            Dama.direita = False
            Dama.esquerda = False
    
    def barra_de_vida(self):      
        coracao_sprite = pg.image.load('./resources/atlas/heart pixel art 48x48.png')

        if self.vida >= 1:           
            display.blit(coracao_sprite,(220,120))
        if self.vida >= 2:           
            display.blit(coracao_sprite,(275,120))  
        if self.vida >= 3:
            display.blit(coracao_sprite,(330,120))


#BOSS

class Boss(object):
    def __init__(self, bossX, bossY):
        self.bossX = bossX
        self.bossY = bossY
        self.velI = 32
        self.raio = 20
        self.cor = (255,0,0)
        self.walkCount = 2
        self.jump_count = 10
        self.is_jump = True
        self.largura = 0
        self.altura = 0
        self.vida = 200
        self.tamanho_da_barra_vida = 400
        self.morto = False

    def tomar_dano(self,dano_do_player):
        if self.vida > 0:
            self.vida -= dano_do_player       
        if self.vida <= 0:
            self.vida = 0

    def barra_De_vida(self):
        pg.draw.rect(display, (255, 0, 0), (1300, 110, self.vida, 15))
        pg.draw.rect(display, (0,255,0), (1300,110, self.vida, 15))
        pg.draw.rect(display, (0,0,0), (1300, 110, self.tamanho_da_barra_vida, 15),4)

#Clase específica, recebe os parâmetros do boss, mas prioriza o que for dado dentro dela

class Torre(Boss):
    def andar(self):
        if self.walkCount <= 0: # o Boss anda "2" vezes antes de parar
                if self.bossX <= Dama.posicao_x and distanciaX >= 0: # Direita
                    self.bossX += (self.velI + 32)
                    sombra.posicao_X += (self.velI + 32)
                    self.is_jump = True
            
                elif self.bossX > Dama.posicao_x and distanciaX < 0: # Esquerda
                    self.bossX -= (self.velI + 32)
                    sombra.posicao_X -= (self.velI + 32)
                    self.is_jump = True
                    
                if self.bossY <= Dama.posicao_y and distanciaY >= 0: # Baixo
                    self.bossY += self.velI
                    sombra.posicao_Y += self.velI
                    self.is_jump = True
                
                elif self.bossY > Dama.posicao_y and distanciaY < 0: # Cima
                    self.bossY -= self.velI
                    sombra.posicao_Y -= self.velI
                    self.is_jump = True

    def pular(self):
        self.is_jump = True
        if self.jump_count >= -10:
            self.bossY -= (self.jump_count ** 3) / 25
            self.jump_count -= 1

        else:
            self.is_jump = False
            self.jump_count = 10


class Sombra(object): 
    def __init__(self):
        self.raio = torre.raio
        self.posicao_X = torre.bossX - (self.raio // 2) + (torre.raio // 2)
        self.posicao_Y = torre.bossY - (self.raio // 2) + (torre.raio // 2)

    def desenhar(self):
        if torre.is_jump:
            pg.draw.circle(display, (54,54,54), (self.posicao_X, self.posicao_Y,), self.raio)

Dama = Player(1200,500)
torre = Torre(constants.WINDOW_SIZE[0] // 2, constants.WINDOW_SIZE[1] // 2) 
sombra = Sombra()          

#PROJÉTIL
#imgs dos projéteis


class projetil(object):
    def __init__(self):
        self.color = (238,173,14)
        self.tamanho = 10
        self.dano = 50
        self.posicao_projetil_x = 0
        self.posicao_projetil_y = 0
        self.range = 300
        self.destino = None
        self.movimentando = False
        self.hitbox = (self.posicao_projetil_x, self.posicao_projetil_y, self.tamanho)
    

Espada = projetil()

#COLETÁVEIS

class coletaveis(object):
    def __init__(self, color, tamanho, posicao_coletavel_x, posicao_coletavel_y) -> None:
        self.color = color
        self.tamanho = tamanho
        self.posicao_coletavel_x = posicao_coletavel_x
        self.posicao_coletavel_y = posicao_coletavel_y
        self.hitbox = (self.posicao_coletavel_x, self.posicao_coletavel_y, self.tamanho)

cords_item_Verde = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
item_Verde = coletaveis((61,145,64), 10, cords_item_Verde[0], cords_item_Verde[1])

cords_item_vida_drop = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
Vida_item = coletaveis((255,0,226), 10, cords_item_vida_drop[0], cords_item_vida_drop[1])

posicao_da_bala_chao = [0,0]
arma_no_chao = coletaveis((238,173,14), 10, posicao_da_bala_chao[0], posicao_da_bala_chao[1])


item_Verde_coletado = False

item_vida_coletada = False

#ARRUMAR ESSA PARTE

game_over = (pg.image.load('./resources/atlas/game_over.jpg'), pg.image.load('./resources/atlas/game_over_branco.jpg'), pg.image.load('./resources/atlas/game_over_vermelho.jpg'))
begin = pg.image.load('./resources/atlas/tela_inicial.png')
win = (pg.image.load('./resources/atlas/win_base.png'), pg.image.load('./resources/atlas/win_branco.png'), pg.image.load('./resources/atlas/win_vermelho.png'))


#MAIN LOOP
run = False
tela_inicial()
while run:   
    display.fill((146, 244, 255))

#SAIR DO JOGO        
    for event in pg.event.get():
        if event.type == pg.QUIT:            
            run = False

#CONSTRUÇÂO DO TABULEIRO           
    for row in range(8):
        for col in range(8):
            block_coords = mt.mudanca_base(row, col, constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                display.blit(block_white_floor, block_coords)
            else:
                display.blit(block_black_floor, block_coords)
#DESENHO E ANIMACAO DO PLAYER

    current_time = pg.time.get_ticks()  
    
    if Dama.direita:
        if current_time - ultima_atualizarcao >= velocidade_animacao:
            frame_direita += 1
            ultima_atualizarcao = current_time
            if frame_direita >= 35:
                frame_direita = 27
    if Dama.esquerda:
        if current_time - ultima_atualizarcao >= velocidade_animacao:
            frame_esquerda += 1
            ultima_atualizarcao = current_time
            if frame_esquerda >= 17:
                frame_esquerda = 9
    if Dama.cima:
        if current_time - ultima_atualizarcao >= velocidade_animacao:
            frame_cima += 1
            ultima_atualizarcao = current_time
            if frame_cima >= 8:
                frame_cima = 0
    if Dama.baixo:
        if current_time - ultima_atualizarcao >= velocidade_animacao:
            frame_baixo += 1
            ultima_atualizarcao = current_time
            if frame_baixo >= 26:
                frame_baixo = 18


#DESENHO DO COLETÁVEL MAIS ATRIBUTO
    item_vida_sprite = pg.image.load('./resources/atlas/heart_full_32x32.png')
    item_velocidade_Sprite = pg.image.load('./resources/atlas/Emerald.png')
    
    display.blit(item_vida_sprite, (Vida_item.posicao_coletavel_x - 10, Vida_item.posicao_coletavel_y - 20))
    display.blit(item_velocidade_Sprite, (item_Verde.posicao_coletavel_x-20, item_Verde.posicao_coletavel_y-30))
   
    torre.barra_De_vida()

    
#DESENHO DO PLAYER E MOVIMENTAÇÂO COM OOP
 
    Dama.desenhar()
    Dama.andar()
    Dama.barra_de_vida()

#BALA

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE] and Dama.posicao_y <= 735:
        if Dama.ammo > 0:
            if Dama.cima == True:
                Espada.destino = (Dama.posicao_x, Dama.posicao_y-Espada.range)
                posicao_da_bala_chao = Espada.destino
                
            if Dama.direita == True:
                Espada.destino = (Dama.posicao_x+Espada.range, Dama.posicao_y)
                posicao_da_bala_chao = Espada.destino

            if Dama.esquerda == True:
                Espada.destino = (Dama.posicao_x-Espada.range, Dama.posicao_y)
                posicao_da_bala_chao = Espada.destino

            if Dama.baixo == True:
                Espada.destino = (Dama.posicao_x, Dama.posicao_y+Espada.range)
                posicao_da_bala_chao = Espada.destino
        
#BLOCO DE VERIFICAÇÃO SE O TEMPO DA IMUNIDADE DO PLAYER JÁ PASSOU
    if hits > 0:
        last_hit_time = pg.time.get_ticks() - static_timer_player
        if last_hit_time > tempo_imune:
            Dama.imune = False
            if Dama.cor == AzulClaroFosco: #VERIFICA SE O PLAYER ESTÁ COM A COR FOSCA DA IMUNIDADE
                Dama.cor = (0,0,123)
            
#DESENHO DO BOOS E MOVIMENTAÇÃO COM OOP
    if torre.vida > 0: # Se a vida da torre for < 0, a torre morre
        display.blit(torre_img, (torre.bossX-30, torre.bossY-50))
    
        distanciaX = Dama.posicao_x - torre.bossX # Distancia entre o player e o boss na posição X
        distanciaY = Dama.posicao_y - torre.bossY # Distancia entre o player e o boss na posição Y

        if not torre.is_jump: #Caso não esteja pulando, anda
            torre.andar()

        else: #Pula e desenha a sombra
            torre.pular()
            sombra.desenhar()

        torre.walkCount += 1
        if torre.walkCount >= 40: #Velocidade do boss
            torre.walkCount = 0

        if not torre.is_jump: #Para ele não bater no player em cima no meio do pulo
            if calcularDistanciaPontos(Dama.posicao_x, torre.bossX, Dama.posicao_y, torre.bossY) <= 40:
                if Dama.imune == False: # Verifica se o player está imune aos hits ainda (Variável)
                    Dama.vida -= 1
                    Dama.imune = True
                    static_timer_player = pg.time.get_ticks()
                    hits+=1
                if Dama.imune == True: # Caso o player não esteja mais imune
                    Dama.cor = (153,153,255)
                    
            if calcularDistanciaPontos(Espada.posicao_projetil_x, torre.bossX, Espada.posicao_projetil_y, torre.bossY) <= 30 and Espada.movimentando:
                torre.tomar_dano(Espada.dano)
                Espada.destino = (Espada.posicao_projetil_x, Espada.posicao_projetil_y)              
                Espada.dano = 0      
                posicao_da_bala_chao = Espada.destino   
    #VERIFICANDO SE O PLAYER VENCER (YOU WIN)
    elif torre.vida <= 0:
        torre.morto = True

        while torre.morto and run:                       
            jogar_novamente()
                        
    #VERIFICANDO SE PLAYER PERDEU (GAME OVER)
    if Dama.vida == 0:
        Dama.morto = True
        
        while Dama.morto and run:                       
            jogar_novamente()
                    

#MUDANÇA DE LUGAR DO ITEM / IDENTIFICAÇÃO SE ITEM FOI COLETADO
    
    if item_Verde_coletado:
        
        if last_item_time > 3000:          
            cords_item_Verde = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            item_Verde = coletaveis((61,145,64), 10, cords_item_Verde[0], cords_item_Verde[1])
            item_Verde_coletado = False
            Dama.velocidade -= 2
            Dama.cor  = (0,0,255)
    
    if item_vida_coletada:

        if last_item_time > 15000:

            cords_item_vida_drop = mt.mudanca_base(random.randint(1,8), random.randint(0,7), constants.FLOOR_SIZE*4, constants.MATRIZ_MUDA_BASE)
            Vida_item = coletaveis((255,0,226), 10, cords_item_vida_drop[0], cords_item_vida_drop[1])
            item_vida_coletada = False
            

            
#IDENTIFICAÇÃO DE COLISÃO COM O ITEM e CD para SPAWN
        
    distanciaPlayerObjeto = calcularDistanciaPontos(Dama.posicao_x, item_Verde.posicao_coletavel_x, Dama.posicao_y, item_Verde.posicao_coletavel_y)
    
    if distanciaPlayerObjeto <= 20:       
       
        Dama.velocidade += 2
        Dama.cor = (0,238,238)           
        item_Verde.posicao_coletavel_x = -30
        item_Verde.posicao_coletavel_y = -30
        item_Verde.color = (146, 244, 255)
        item_Verde.tamanho = 0
        static_timer = pg.time.get_ticks()
    
        item_Verde_coletado = True

    distanciaPlayerObjeto_2 = calcularDistanciaPontos(Dama.posicao_x, Vida_item.posicao_coletavel_x, Dama.posicao_y, Vida_item.posicao_coletavel_y)

    if distanciaPlayerObjeto_2 <= 20:
        if Dama.vida <= 3:
            Dama.vida += 1

        Vida_item.posicao_coletavel_x = -30
        Vida_item.posicao_coletavel_y = -30
        Vida_item.tamanho = 0
        static_timer = pg.time.get_ticks()
    
        item_vida_coletada = True
    
    distacia_da_bala_chao = calcularDistanciaPontos(Dama.posicao_x, posicao_da_bala_chao[0], Dama.posicao_y, posicao_da_bala_chao[1])

    if distacia_da_bala_chao <= 20:
        Dama.ammo = 1
        Espada.destino = None
        Espada.dano = 30


    if static_timer:
        last_item_time = pg.time.get_ticks() - static_timer

#MOVIMENTAÇÃO DO PROJÉTIL
    if Dama.ammo > 0:
        if Dama.cima:
            Espada.posicao_projetil_x = Dama.posicao_x
            Espada.posicao_projetil_y = Dama.posicao_y-20
            
        elif Dama.direita:
            Espada.posicao_projetil_x = Dama.posicao_x+20
            Espada.posicao_projetil_y = Dama.posicao_y
            
        elif Dama.esquerda:
            Espada.posicao_projetil_x = Dama.posicao_x-20
            Espada.posicao_projetil_y = Dama.posicao_y
            
        elif Dama.baixo:
            Espada.posicao_projetil_x = Dama.posicao_x
            Espada.posicao_projetil_y = Dama.posicao_y+20

#
            
    if Espada.destino != None:
        if not Espada.destino == (Espada.posicao_projetil_x, Espada.posicao_projetil_y):
            Espada.movimentando = True
            Dama.ammo = 0
            #
            if Espada.destino[0]>Espada.posicao_projetil_x:
                if (Espada.destino[0] - Espada.posicao_projetil_x)<5:
                    
                    Espada.posicao_projetil_x = Espada.destino[0]
                    
                else:
                    Espada.posicao_projetil_x += 8
                    
            if Espada.destino[0]<Espada.posicao_projetil_x:
                if (Espada.posicao_projetil_x - Espada.destino[0])<5:
                    
                    Espada.posicao_projetil_x = Espada.destino[0]
                    
                else:
                    Espada.posicao_projetil_x -= 8
            #
            if Espada.destino[1]>Espada.posicao_projetil_y:
                if (Espada.destino[1] - Espada.posicao_projetil_y)<5:
                    
                    Espada.posicao_projetil_y = Espada.destino[1]
                    
                else:
                    Espada.posicao_projetil_y += 8
                    
            if Espada.destino[1]<Espada.posicao_projetil_y:
                if (Espada.posicao_projetil_y - Espada.destino[1])<5:
                    
                    Espada.posicao_projetil_y = Espada.destino[1]
                    
                else:
                    Espada.posicao_projetil_y -= 8
                    
        else:
            Espada.destino = None #Caso tenha chegado no destino, volta a ser destino = None
    else:
        Espada.movimentando = False #Já que o destino virou None no tick passado, ele deixa de estar em movimento

    if Dama.ammo > 0:   

        if Dama.esquerda:
            chao = orbe
        if Dama.direita:
            chao = orbe
        if Dama.cima:
            chao = orbe
        if Dama.baixo:
            chao = orbe

    else:
        display.blit(chao, (Espada.posicao_projetil_x-20, Espada.posicao_projetil_y-20))


        
    #
    Dama.canMove['cima'] = True
    Dama.canMove['direita'] = True
    Dama.canMove['esquerda'] = True
    Dama.canMove['baixo'] = True
    
    for i in border_TopLeft:
        if calcularDistanciaPontos(Dama.posicao_x, i[0], Dama.posicao_y, i[1])<40:
            Dama.canMove['cima'] = False
            Dama.canMove['esquerda'] = False
        if Dama.ammo == 0:
            if calcularDistanciaPontos(Espada.posicao_projetil_x, i[0], Espada.posicao_projetil_y, i[1])<40:
                Espada.posicao_projetil_x = Espada.posicao_projetil_x + 20
                Espada.posicao_projetil_y = Espada.posicao_projetil_y + 20
                Espada.destino = (Espada.posicao_projetil_x + 20, Espada.posicao_projetil_y + 20)
                posicao_da_bala_chao = Espada.destino

    for i in border_TopRight:
        if calcularDistanciaPontos(Dama.posicao_x, i[0], Dama.posicao_y, i[1])<40:
            Dama.canMove['cima'] = False
            Dama.canMove['direita'] = False
        if Dama.ammo == 0:
            if calcularDistanciaPontos(Espada.posicao_projetil_x, i[0], Espada.posicao_projetil_y, i[1])<40:
                Espada.posicao_projetil_x = Espada.posicao_projetil_x - 20
                Espada.posicao_projetil_y = Espada.posicao_projetil_y + 20
                Espada.destino = (Espada.posicao_projetil_x - 20, Espada.posicao_projetil_y + 20)
                posicao_da_bala_chao = Espada.destino

    for i in border_DownLeft:
        if calcularDistanciaPontos(Dama.posicao_x, i[0], Dama.posicao_y, i[1])<40:
            Dama.canMove['baixo'] = False
            Dama.canMove['esquerda'] = False
        if Dama.ammo == 0:
            if calcularDistanciaPontos(Espada.posicao_projetil_x, i[0], Espada.posicao_projetil_y, i[1])<40:
                Espada.posicao_projetil_x = Espada.posicao_projetil_x + 20
                Espada.posicao_projetil_y = Espada.posicao_projetil_y - 20
                Espada.destino = (Espada.posicao_projetil_x + 20, Espada.posicao_projetil_y - 20)
                posicao_da_bala_chao = Espada.destino

    for i in border_DownRight:
        if calcularDistanciaPontos(Dama.posicao_x, i[0], Dama.posicao_y, i[1])<40:
            Dama.canMove['baixo'] = False
            Dama.canMove['direita'] = False
        if Dama.ammo == 0:
            if calcularDistanciaPontos(Espada.posicao_projetil_x, i[0], Espada.posicao_projetil_y, i[1])<40:
                Espada.posicao_projetil_x = Espada.posicao_projetil_x - 20
                Espada.posicao_projetil_y = Espada.posicao_projetil_y - 20
                Espada.destino = (Espada.posicao_projetil_x - 20, Espada.posicao_projetil_y - 20)
                posicao_da_bala_chao = Espada.destino
    #
    pg.display.update()
    clock.tick(60)
    
