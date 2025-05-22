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
        self.image = pygame.image.load("electra2.png")
        self.image = pygame.transform.scale(self.image, (220,112))
        self.rect = self.image.get_rect(midbottom = (Promena, pozice))
    def apply_gravity(self,poziceee):
            self.rect.y = (poziceee)
    def apply_dopredudozadu(self, pozicex):
            self.rect.x = (pozicex)
    def update(self,pozicex,pozicey):
        self.apply_gravity(pozicey)
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
        na = pygame.image.load("nabito.png")
        self.kolecko=[nena1,nena2,nena3,nena4,nena5,nena6,nena7,nena8,na]
        self.fazor=0
        self.image = self.kolecko[self.fazor]
        self.image = pygame.transform.scale(self.image, (88,88))
        self.rect = self.image.get_rect(midbottom = (100, 1000))
    def update(self,k):
        if k == 1:
             self.fazor=0
        else:
            if self.fazor>8:
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
    def __init__(self): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("mrak.png")
        self.image = pygame.transform.scale(self.image, (random.randint(150)+580,random.randint(150)+250))
        self.rect = self.image.get_rect(midbottom = (2300,random.randint(240, 1100) ))
        self.speed = random.randint(4,12)
    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < -5:
            self.kill()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,pozicee,x): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("zlastrela.png")
        if x == 0:
            self.image = pygame.transform.scale(self.image, (50,9))
            self.rect = self.image.get_rect(midbottom=(1620, (pozicee)))
            self.speed = random.randint(38,45)
        elif x == 1:
            self.image = pygame.transform.scale(self.image, (39,7))
            self.rect = self.image.get_rect(midbottom=(1690, (pozicee)))
            self.speed = random.randint(38,62)
        else:
            self.image = pygame.transform.scale(self.image, (39,7))
            self.rect = self.image.get_rect(midbottom=(1570, (pozicee)))
            self.speed = random.randint(38,62)
    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < 35:
            self.kill()
    def killllll(self):
        self.kill()
class Hstrela(pygame.sprite.Sprite):
    def __init__(self,druhasouradnice,poziceed): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__() # volá konstruktor třídy Sprite pro správnou inicializaci
        self.image = pygame.image.load("Hstrela.png")
        self.image = pygame.transform.scale(self.image, (50,9))
        self.rect = self.image.get_rect(midbottom=(druhasouradnice, (poziceed)))
        self.speed = random.randint(31,55)
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
ground_surface = pygame.image.load("gameover.png")
vittoria = pygame.image.load("gameover2.png")
# GROUPS
# GroupSingle - skupina s 1 objektem (hráč)
# Group - skupina s více objekty (nepřátelé)
player = pygame.sprite.GroupSingle() #vytvoříme skupinu pro hráče
player.add(Player()) # přidáme do ní novéh hráče typu Player (třída, co jsme vytvořili)
zloun = pygame.sprite.GroupSingle()
zloun.add(Zloun())
Mrak_group = pygame.sprite.Group()
Mrak_group.add(Mrak())
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
# herní smyčka
while True:
    Munice = Munice+1
    # zjistíme co dělá hráč za akci
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit() # úplně opustíme herní smyčku, celý program se ukončí
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if game_hyperactive <= 0 or game_hyperactive >= 5: # když je GAME OVER stav
            score=0
            Munice=0 
            game_hyperactive = 1
            coolecko.update(1)
    if keys[pygame.K_RIGHT]:
        if Munice > 56 and score>50 and game_hyperactive>=1 and game_hyperactive <= 4:
            Hstrelagruppen.add(Hstrela(Promena+170, pozice+60))
            Munice = 0
    if keys[pygame.K_w]:
            zpozice = -20
    if keys[pygame.K_s]:
            zpozice =  +20
    if keys[pygame.K_a]:
            aaapozice = -20
    if keys[pygame.K_d]:
            aaapozice =  +20
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
        if Munice%7==0 and Munice<=56:
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
        player.update(Promena,pozice)

        game_hyperactive = game_hyperactive + (is_collision()) + (ISIS_collision()) # nastala kolize? pokud ano -> konec hry
        zivot.update(game_hyperactive)
        score=score+1
        if score%220==0:
            Mrak_group.add(Mrak()) 
        if score%23==0 and score>20:
            obstacle_group.add(Obstacle(Zlounpozice+30,0))
            obstacle_group.add(Obstacle(Zlounpozice+90,0))
            obstacle_group.add(Obstacle(Zlounpozice-40,2))
            obstacle_group.add(Obstacle(Zlounpozice+164,1)) 
    else:  # hra neběží
        if game_hyperactive >= 5:
             screen.blit(vittoria,(0,0))
             screen.blit(score_surface,score_rect)
        else:
            screen.blit(ground_surface,(0,0))
            screen.blit(score_surface,score_rect)  

    pygame.display.update() # updatujeme vykreslené okno
    clock.tick(60) # herní smyčka proběhne maximálně 60x za sekundu