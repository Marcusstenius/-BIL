import pygame
import sys
import random
from pygame.locals import *

# Börian pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()


pygame.mixer.music.load("Musik.mp3")
pygame.mixer.music.play(-1)


fontti =  pygame.font.SysFont("Roboto",30)
tekstivari = (245, 32, 17)

fontti2 =  pygame.font.SysFont("Roboto",120)
tekstivari = (0, 9, 186)

koko = (700,700)

loppuveri = (207, 2, 2)

ruutu=pygame.display.set_mode(koko)
pygame.display.set_caption("Auto peli")

ruutu=pygame.display.set_mode(koko)
pygame.display.set_caption("Auto peli")

Bil= pygame .image. load("Bil.png")
Buske = pygame .image. load("Buske.png")
Veg = pygame .image. load("Veg.png")
# storlek OCH hastighet och liv
pelx = 100
pely = 500
nopeus = 6
viholinennopeus =4
hp = 5
Haiskore = 0

viholiset = [[300,50],[300,100],[300,150],[300,200],[300,250],[300,300],[300,0],]

on_kirjoitetu = False 

with open("Haiskor", "r") as tiedosto:
    luetu = tiedosto.read()
    Haiskore = float(luetu)

ajastin = pygame.time.Clock()
FPS = 30
loppuaika = 0

alkuaika = pygame.time.get_ticks()

# storlek
Bil = pygame.transform.scale(Bil,(170,80))
Bil = pygame.transform.rotate(Bil,90)

Veg = pygame.transform.scale(Veg,(700,700))
Buske = pygame.transform.scale(Buske,(60,60))

def peruna():

    #Händelser 
    tapahtumat =pygame.event.get()  
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()

            sys.exit()
 # spel logik 
          
def porkkana():
    # bakgrund
    ruutu.blit(Veg,(0,0))
    global pelx
    global pely
    global hp
    global Haiskore
    global viholinennopeus
 
   # spelre
    nappaimet = pygame.key.get_pressed()
    if nappaimet[pygame.K_RIGHT ]:
        pelx += nopeus
    

    if nappaimet[pygame.K_LEFT]:
        pelx -= nopeus

    if pelx < -10:
        pelx = -10
    if pelx > 600:
        pelx = 600
# fiende 
    for viholinen in viholiset:
        ruutu.blit(Buske,viholinen)
        viholinen[1]+=viholinennopeus
        if viholinen[1] > 690:
           viholinen[1] = -100
           viholinen[0]  = random.randint(12,680)
    # vid röring
    for viholinen in viholiset:
        if viholinen [1] +60 > pely  and   viholinen[1] < pely+ 170:
            if viholinen [0] +60> pelx  and   viholinen[0] <pelx +80:
                #rör
                hp-= 1
                viholinen[1] = -250


    # FUSK
    nappaimet = pygame.key.get_pressed()
    if nappaimet[pygame.K_F2   ]:
        hp += 1

        nappaimet = pygame.key.get_pressed()
    if nappaimet[ K_F3   ]:
        hp -= 1

            
     # Text,tid
    teksti=fontti.render("Liv:"+ str(hp),True,tekstivari)
    ruutu.blit (teksti,(30,30))

    aika = pygame.time.get_ticks()- alkuaika 
    teksti=fontti.render("aika:"+ str(aika//1000),True,tekstivari)
    ruutu.blit (teksti,(30,60))

    if aika//1000 > Haiskore:
        Haiskore = aika // 1000
        print(Haiskore)
    if aika//1000 %  10 == 00:
        viholinennopeus += 0.008

# annat
    ruutu.blit(Bil,(pelx,pely))
    pygame.display.flip()

#Spel lop
def stop():
    global  on_kirjoitetu
    global Haiskore
    global loppuaika 

    ruutu.fill(loppuveri)


    teksti=fontti2.render("Game over" ,True,tekstivari)
    ruutu.blit (teksti,(30,30))
    
    teksti=fontti2.render("Rekord. "+str(Haiskore) ,True,tekstivari)
    ruutu.blit (teksti,(80,300))

    if not on_kirjoitetu:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Alarm.mp3")
        pygame.mixer.music.play(0)
        on_kirjoitetu = True
        loppuaika = pygame.time.get_ticks()
        with open("Haiskor", "w") as tiedosto:
            print(str(Haiskore))
            tiedosto.write(str(Haiskore))

    if pygame.time.get_ticks() -  loppuaika > 6000:

        pygame.quit()

        sys.exit()
    
           
    pygame.display.flip()

while True:
    peruna()
    if  hp > 0:
        porkkana()
    else:
        stop()
    

