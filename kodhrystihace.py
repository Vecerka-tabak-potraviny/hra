import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
import numpy.random as random
import pygame.sprite
import pygame.transform
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny
pozice = 470
zpozice = 0
Zlounpozice = 400
aaapozice = 0
Promena = 300
Munice = -1
class Player(pygame.sprite.Sprite):
    def __init__(self): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        rovne = pygame.image.load("electra2.png")
        dolu = pygame.image.load("electra4.png")
        nahoru = pygame.image.load("electra3.png")
        lansenrovne = pygame.image.load("lansen.png")
        ldolu = pygame.image.load("lansendolu.png")
        lhoru = pygame.image.load("lansenhoru.png")
        provne = pygame.image.load("p47.png")
        pdolu = pygame.image.load("p47dolu.png")
        phoru = pygame.image.load("p47na.png")
        self.letoun = 0
        self.kam = [dolu,rovne,nahoru,pdolu,provne,phoru,ldolu,lansenrovne,lhoru]
        self.image = self.kam[1]
        self.image = pygame.transform.scale(self.image, (220,112))
        self.rect = self.image.get_rect(midbottom = (Promena, pozice))
    def apply_gravity(self,poziceee,wwss):
            self.image = self.kam[wwss+3*(self.letoun)]
            if wwss == 0:
                if self.letoun==0:
                    self.image = pygame.transform.scale(self.image,(221,108))
                elif self.letoun==1:
                     self.image = pygame.transform.scale(self.image,(257,128))
                else:
                     self.image = pygame.transform.scale(self.image,(279,125))
            elif wwss == 2:
                if self.letoun==0:
                    self.image = pygame.transform.scale(self.image,(220,111))
                elif self.letoun == 1:
                     self.image = pygame.transform.scale(self.image,(250,120))
                else:
                    self.image = pygame.transform.scale(self.image,(278,119))
            else:
                if self.letoun==0:
                    self.image = pygame.transform.scale(self.image,(220,112))
                elif self.letoun == 1:
                    self.image = pygame.transform.scale(self.image,(255,114))
                else:
                    self.image = pygame.transform.scale(self.image,(280,120))
            self.rect.y = (poziceee)
    def apply_dopredudozadu(self, pozicex):
            self.rect.x = (pozicex)
    def update(self,pozicex,pozicey,wwss,typletounu):
        self.letoun = typletounu
        self.apply_gravity(pozicey,wwss)
        self.apply_dopredudozadu(pozicex)
class Nabito(pygame.sprite.Sprite):
    def __init__(self): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        nena1 = pygame.image.load("nenabito1.png")
        nena2 = pygame.image.load("nenabito2.png")
        nena3 = pygame.image.load("nenabito3.png")
        nena4 = pygame.image.load("nenabito4.png")
        nena5 = pygame.image.load("nenabito5.png")
        nena6 = pygame.image.load("nenabito6.png")
        nena7 = pygame.image.load("nenabito7.png")
        nena8 = pygame.image.load("nenabito8.png")
        nena9 = pygame.image.load("nenabito9.png")
        nena10 = pygame.image.load("nenabito10.png")
        nena11 = pygame.image.load("nenabito11.png")
        nena12 = pygame.image.load("nenabito12.png")
        nena13 = pygame.image.load("nenabito13.png")
        nena14 = pygame.image.load("nenabito14.png")
        nena15 = pygame.image.load("nenabito15.png")
        nena16 = pygame.image.load("nenabito16.png")
        na = pygame.image.load("nabito.png")
        self.kolecko=[nena1,nena9,nena2,nena10,nena3,nena11,nena4,nena12,nena5,nena13,nena6,nena14,nena7,nena15,nena8,nena16,na]
        self.fazor=0
        self.image = self.kolecko[self.fazor]
        self.image = pygame.transform.scale(self.image, (88,88))
        self.rect = self.image.get_rect(midbottom = (100, 1000))
    def update(self,k):
        if k == 1:
             self.fazor=0
        else:
            if self.fazor>16:
                self.fazor=0
            self.image = self.kolecko[self.fazor]
            self.image = pygame.transform.scale(self.image, (88,88))
            self.fazor=self.fazor+1
class Zloun(pygame.sprite.Sprite):
    def __init__(self): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("blackwidow3.png")
        self.image = pygame.transform.scale(self.image, (422,222))
        self.rect = self.image.get_rect(midbottom = (1700, (pozice-70)))
    def apply_gravity(self,poziceq):
        if poziceq>self.rect.y:
            self.rect.y = (poziceq)
        elif poziceq<self.rect.y:
            self.rect.y = (poziceq)
    def update(self,pozicew):
        self.apply_gravity(pozicew-50)
class Mrak(pygame.sprite.Sprite):
    def __init__(self,cimletim): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("mrak.png")
        self.image = pygame.transform.scale(self.image, (random.randint(150)+580,random.randint(150)+250))
        self.rect = self.image.get_rect(midbottom = (2300,random.randint(240, 1100) ))
        self.speed = random.randint(4+(cimletim*6),12+(cimletim*3))
    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < -5:
            self.kill()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,pozicee,x,cimletim): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("zlastrela.png")
        if x == 0:
            self.image = pygame.transform.scale(self.image, (50,9))
            self.rect = self.image.get_rect(midbottom=(1620, (pozicee)))
            self.speed = random.randint(40+(cimletim*6),49+(cimletim*8))
        elif x == 1:
            self.image = pygame.transform.scale(self.image, (39,7))
            self.rect = self.image.get_rect(midbottom=(1690, (pozicee)))
            self.speed = random.randint(36+(cimletim*6),60+(cimletim*7))
        else:
            self.image = pygame.transform.scale(self.image, (39,7))
            self.rect = self.image.get_rect(midbottom=(1570, (pozicee)))
            self.speed = random.randint(36+(cimletim*6),60+(cimletim*7))
    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < 35:
            self.kill()
    def killllll(self):
        self.kill()
class Hstrela(pygame.sprite.Sprite):
    def __init__(self,druhasouradnice,poziceed,rych): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("Hstrela.png")
        self.image = pygame.transform.scale(self.image, (50,9))
        self.rect = self.image.get_rect(midbottom=(druhasouradnice, (poziceed)))
        self.speed = (45+rych)
    def update(self):
        self.rect.right += self.speed
        if self.rect.left > 1680:
            self.kill()
    def killllll(self):
        self.kill()
class Srdicka(pygame.sprite.Sprite):
    def __init__(self):
          super().__init__()
          sr1=pygame.image.load("srdicka1.png")
          sr2=pygame.image.load("srdicka2.png")
          sr3=pygame.image.load("srdicka3.png")
          sr4=pygame.image.load("srdicka4.png")
          sr5=pygame.image.load("srdicka5.png")
          sr6=pygame.image.load("srdicka6.png")
          self.kardioseznam = [sr1,sr2,sr3,sr4,sr5,sr6]
          self.image = sr2
          self.image = pygame.transform.scale(self.image,(335,70))
          self.rect = self.image.get_rect(midbottom = (1600, 1000))
    def update(self, ICHS):
        self.image = self.kardioseznam[ICHS]
def is_collision():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty() # smažeme všechny překážky
        Hstrelagruppen.empty()
        return -1 # hra má skončit
    return 0 # hra má pokračovat
def ISIS_collision():
    if pygame.sprite.spritecollide(zloun.sprite, Hstrelagruppen, False):
        Hstrelagruppen.empty() # smažeme všechny překážky
        obstacle_group.empty()
        return 1 # hra má skončit
    return 0 # hra má pokračovat

# herní okno
window_width = 1920
window_height = 1080
screen = pygame.display.set_mode((window_width, window_height))
    # dvojice (w,h) v parametru se nazývá *tuple*
pygame.display.set_caption("FIGHT/ER") # nastavíme do hlavičky okna název hry

clock = pygame.time.Clock() # díky hodinám nastavíme frekvenci obnovování herního okna

# přidání objektů (tzv. surface) do scény
sky_surface = pygame.image.load("pozadíhra.png")
g0=pygame.image.load("gameover.png")
g1=pygame.image.load("gameoverlan.png")
gp = pygame.image.load("gameover47.png")
ground_surface = [g0,gp,g1]
vittoria = pygame.image.load("gameover2.png")
vyber0 = pygame.image.load("vyber0.png")
vyber1 = pygame.image.load("vyber1.png")
vyber2 = pygame.image.load("vyber2.png")
vybersi = [vyber0,vyber1,vyber2]
# GROUPS
# GroupSingle - skupina s 1 objektem (hráč)
# Group - skupina s více objekty (nepřátelé)
player = pygame.sprite.GroupSingle() #vytvoříme skupinu pro hráče
player.add(Player()) # přidáme do ní novéh hráče typu Player (třída, co jsme vytvořili)
zloun = pygame.sprite.GroupSingle()
zloun.add(Zloun())
Mrak_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
Hstrelagruppen = pygame.sprite.Group()
coolecko = pygame.sprite.GroupSingle()
coolecko.add(Nabito())
zivot = pygame.sprite.GroupSingle()
zivot.add(Srdicka())
#obstacle_group.add(Obstacle(pozice))

game_hyperactive = 1
text_font = pygame.font.Font(None,100) # 100 je velikost písma
text_surface = text_font.render("GAME OVER!", True, "Black")
text_rect = text_surface.get_rect(center=(window_width/2, window_height/2))
score_font = pygame.font.Font(None,29) # 100 je velikost písma
score=0
cimletim = 1
# herní smyčka
while True:
    ws=1
    Munice = Munice+1
    # zjistíme co dělá hráč za akci
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit() # úplně opustíme herní smyčku, celý program se ukončí
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if game_hyperactive <= 0 or game_hyperactive == 5: # když je GAME OVER stav
            score=0
            Munice=0 
            coolecko.update(1)
            game_hyperactive = 6
        elif game_hyperactive == 6 and score >1:
            score = 0
            Munice=0
            game_hyperactive = 1
        else: 
             None    
            
    if keys[pygame.K_RIGHT]:
        if Munice > 48 and score>50 and game_hyperactive>=1 and game_hyperactive <= 4:
            if cimletim == 2:
                 Hstrelagruppen.add(Hstrela(Promena+100,pozice+12,8))
                 Hstrelagruppen.add(Hstrela(Promena+100, pozice+120,8))
            elif cimletim == 1:
                 Hstrelagruppen.add(Hstrela(Promena+220,pozice+55,3))
            else:
                Hstrelagruppen.add(Hstrela(Promena+170, pozice+60,0))
            Munice = 0
    if keys[pygame.K_w]:
            ws=2
            zpozice = -18-(cimletim*3)
    if keys[pygame.K_s]:
            ws=ws-1
            zpozice =  +18+(cimletim*3)
    if keys[pygame.K_a]:
            aaapozice = -18-(cimletim*3)
            if game_hyperactive==6 and score%2==1:
                 cimletim = (3+cimletim-1)%3
    if keys[pygame.K_d]:
            aaapozice =  +18+(cimletim*3)
            if game_hyperactive==6 and score%2==1:
                 cimletim = (cimletim+1)%3
    if aaapozice>0 and Promena < 900:
            aaapozice +=-1
            Promena = (Promena + aaapozice)
    elif aaapozice<0 and Promena > 50:
            aaapozice +=1
            Promena = (Promena + aaapozice)
    else: 
        aaapozice = 0
    if Zlounpozice > 830:
         if zpozice>0 and pozice < 900:
            zpozice +=-1
            pozice = (pozice + zpozice)
            Zlounpozice = Zlounpozice
         elif zpozice<0 and pozice > 50:
            zpozice +=1
            pozice = (pozice + zpozice)
            Zlounpozice = (Zlounpozice+zpozice)+5
         else: 
                zpozice = 0
    elif Zlounpozice < 150:
         if zpozice>0 and pozice < 900:
            zpozice +=-1
            pozice = (pozice + zpozice)
            Zlounpozice = Zlounpozice+zpozice-5
         elif zpozice<0 and pozice > 50:
            zpozice +=1
            pozice = (pozice + zpozice)
            Zlounpozice = (Zlounpozice)
         else: 
                zpozice = 0
    else:
         if zpozice>0 and pozice < 900:
            zpozice +=-1
            pozice = (pozice + zpozice)
            Zlounpozice = (Zlounpozice + zpozice)-5
         elif zpozice<0 and pozice > 50:
            zpozice +=1
            pozice = (pozice + zpozice)
            Zlounpozice = (Zlounpozice + zpozice)+5
         else: 
            zpozice = 0
            if pozice>=900:
                    Zlounpozice=Zlounpozice+2
            elif pozice <=50:
                    Zlounpozice=Zlounpozice-2
            else: None
    if game_hyperactive>=1 and game_hyperactive<=4:
        if Munice%3==0 and Munice<=48:
            coolecko.update(0)
        # pozadí
        screen.blit(sky_surface,(0,0)) # položíme sky_surface na souřadnice [0,0]
        # položíme ground_surface na souřadnice [0,300] (pod oblohu)
        score_surface = score_font.render(f"Skóre: {score}", True, "Black")
        score_rect = text_surface.get_rect(center=(window_width-65, 55))
        screen.blit(score_surface,score_rect)
        # nepřítel
        Mrak_group.draw(screen)
        Mrak_group.update()
        coolecko.draw(screen)
        zivot.draw(screen)
        # HRÁČ
        obstacle_group.draw(screen)
        obstacle_group.update()
        zloun.draw(screen)
        zloun.update(Zlounpozice)
        Hstrelagruppen.draw(screen)
        Hstrelagruppen.update()
        player.draw(screen)
        player.update(Promena,pozice,ws,cimletim)
        game_hyperactive = game_hyperactive + (is_collision()) + (ISIS_collision()) # nastala kolize? pokud ano -> konec hry
        zivot.update(game_hyperactive)
        score=score+1
        if score%220==0:
            Mrak_group.add(Mrak(cimletim)) 
        if score%21==0 and score>20:
            obstacle_group.add(Obstacle(Zlounpozice+30,0,cimletim))
            obstacle_group.add(Obstacle(Zlounpozice+90,0,cimletim))
            obstacle_group.add(Obstacle(Zlounpozice-40,2,cimletim))
            obstacle_group.add(Obstacle(Zlounpozice+164,1,cimletim)) 
    elif game_hyperactive == 6:
        screen.blit(sky_surface,(0,0))
        Mrak_group.draw(screen)
        Mrak_group.update()
        screen.blit(vybersi[cimletim],(0,0))
        score=score+1
        if score%160==0:
            Mrak_group.add(Mrak(cimletim)) 
    else:  # hra neběží
        if game_hyperactive == 5:
             screen.blit(vittoria,(0,0))
             screen.blit(score_surface,score_rect)
        else:
            screen.blit(ground_surface[cimletim],(0,0))
            screen.blit(score_surface,score_rect)  
    pygame.display.update() # updatujeme vykreslené okno
    clock.tick(60) # herní smyčka proběhne maximálně 60x za sekundu