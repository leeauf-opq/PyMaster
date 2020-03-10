import pygame
import pandas as pd
import openpyxl as op
pygame.init()
win = pygame.display.set_mode((0,0))

width = 1280
height = 720
file = r"bdd/card.xlsx"
data = pd.read_excel(file)
deck_ex = pd.read_excel(r"bdd/deck.xlsx")
book = op.load_workbook(filename = 'bdd/deck.xlsx')
data_deck = book.active

musique = pygame.mixer.music.load("side/musique.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
font = pygame.font.Font("side/upheavtt.ttf", 35)
petite_font = pygame.font.Font("side/upheavtt.ttf", 20)
big_font = pygame.font.Font("side/upheavtt.ttf", 76)

# ______            _                                   _ 
# | ___ \          | |                                 | |
# | |_/ / __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |
# | ___ \/ _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |
# | |_/ / (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |
# \____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|
#                        __/ |                            
#                       |___/

menu_back = pygame.image.load('image/fond.jpg').convert_alpha()
choose_back = pygame.image.load('image/fond.jpg').convert_alpha()
option_back = pygame.image.load('image/fond.jpg').convert_alpha()
play_back = pygame.image.load('image/fond.jpg').convert_alpha()
editor_hero_back = pygame.image.load('image/fond.jpg').convert_alpha()
editor_back = pygame.image.load('image/fond.jpg').convert_alpha()
choose_deck_back = pygame.image.load('image/fond.jpg').convert_alpha()
deck_viewer_back = pygame.image.load('image/fond.jpg').convert_alpha()
end_back = pygame.image.load('image/fond.jpg').convert_alpha()
tuto_back = pygame.image.load('image/fond.jpg').convert_alpha()
wait_other_back = pygame.image.load('image/fond.jpg').convert_alpha()
current_background = menu_back
vol_general = 0,5


# ______       _   _                                _   _   _ _____ 
# | ___ \     | | | |                              | | | | | |_   _|
# | |_/ /_   _| |_| |_ ___  _ __     __ _ _ __   __| | | | | | | |  
# | ___ \ | | | __| __/ _ \| '_ \   / _` | '_ \ / _` | | | | | | |  
# | |_/ / |_| | |_| || (_) | | | | | (_| | | | | (_| | | |_| |_| |_ 
# \____/ \__,_|\__|\__\___/|_| |_|  \__,_|_| |_|\__,_|  \___/ \___/ 

                                                                  
logo = pygame.image.load('image/logo.png').convert_alpha()                                                                   
play_0 = pygame.image.load('image/play_0.jpg').convert_alpha()
play_1 = pygame.image.load('image/play_1.jpg').convert_alpha()
option_0 = pygame.image.load('image/option_0.jpg').convert_alpha()
option_1 = pygame.image.load('image/option_1.jpg').convert_alpha()
editeur_0 = pygame.image.load('image/editor_0.jpg').convert_alpha()
editeur_1 = pygame.image.load('image/editor_1.jpg').convert_alpha()
retour_0 = pygame.image.load('image/retour_0.jpg').convert_alpha()
retour_1 = pygame.image.load('image/retour_1.jpg').convert_alpha()
exit_0 = pygame.image.load('image/exit_0.jpg').convert_alpha()
exit_1 = pygame.image.load('image/exit_1.jpg').convert_alpha()
fleche_retour_0 = pygame.image.load('image/fleche_retour_0.png').convert_alpha()
fleche_retour_1 = pygame.image.load('image/fleche_retour_1.png').convert_alpha()
volume = pygame.image.load('image/volume.png').convert_alpha()
barre = pygame.image.load('image/barre.png').convert_alpha()
secret = pygame.image.load('image/secret.png').convert_alpha()
cadre = pygame.image.load('image/cadre.png').convert_alpha()
end_turn_0 = pygame.image.load('image/end_turn_0.png').convert_alpha()
end_turn_1 = pygame.image.load('image/end_turn_1.png').convert_alpha()
aide_0 = pygame.image.load('image/aide_0.png').convert_alpha()
aide_1 = pygame.image.load('image/aide_1.png').convert_alpha()
tuto = pygame.image.load('image/tuto.png').convert_alpha()
parchemin = pygame.image.load('image/parchemin.png').convert_alpha()

#  _   _                          
# | | | |                         
# | |_| | ___ _ __ ___   ___  ___ 
# |  _  |/ _ \ '__/ _ \ / _ \/ __|
# | | | |  __/ | | (_) |  __/\__ \
# \_| |_/\___|_|  \___/ \___||___/
                                
                                
guerrier_0 = pygame.image.load('image/guerrier_0.png').convert_alpha()
guerrier_1 = pygame.image.load('image/guerrier_1.png').convert_alpha()
guerrier = pygame.image.load('image/guerrier.png').convert_alpha()

pretre_0 = pygame.image.load('image/pretre_0.png').convert_alpha()
pretre_1 = pygame.image.load('image/pretre_1.png').convert_alpha()
pretre = pygame.image.load('image/pretre.png').convert_alpha()

mecanicien_0 = pygame.image.load('image/mecanicien_0.png').convert_alpha()
mecanicien_1 = pygame.image.load('image/mecanicien_1.png').convert_alpha()
mecanicien = pygame.image.load('image/mecanicien.png').convert_alpha()

voleur_0 = pygame.image.load('image/voleur_0.png').convert_alpha()
voleur_1 = pygame.image.load('image/voleur_1.png').convert_alpha()
voleur = pygame.image.load('image/voleur.png').convert_alpha()

mage_0 = pygame.image.load('image/mage_0.png').convert_alpha()
mage_1 = pygame.image.load('image/mage_1.png').convert_alpha()
mage = pygame.image.load('image/mage.png').convert_alpha()

classe_ = ["guerrier", "pretre", "mage", "voleur", "mecanicien"]



#  _   _            _       _     _           
# | | | |          (_)     | |   | |          
# | | | | __ _ _ __ _  __ _| |__ | | ___  ___ 
# | | | |/ _` | '__| |/ _` | '_ \| |/ _ \/ __|
# \ \_/ / (_| | |  | | (_| | |_) | |  __/\__ \
#  \___/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
                                            
x_0 = (width/2)-8
x_1 = (width/2)-8
tour = 1
changed = False
online = False
code = ""
nom_joueur = "P1"
n = None
