#  _____      _ _   
# |_   _|    (_) |  
#   | | _ __  _| |_ 
#   | || '_ \| | __|
#  _| || | | | | |_ 
#  \___/_| |_|_|\__|
                                    
import pygame
from side_script.network import Network
from side_script.variable import *
from side_script.Hero import *
from side_script.GameMechanics import *

pygame.init()
pygame.display.set_caption("PyMaster")
win = pygame.display.set_mode((width,height))

def ReloadBDD():
    global deck_ex, book, data_deck
    deck_ex = pd.read_excel(r"bdd/deck.xlsx")
    book = op.load_workbook(filename = 'bdd/deck.xlsx')
    data_deck = book.active


    
#  _   _ _____   _____           _   _             
# | | | |_   _| |  __ \         | | (_)            
# | | | | | |   | |  \/ ___  ___| |_ _  ___  _ __  
# | | | | | |   | | __ / _ \/ __| __| |/ _ \| '_ \ 
# | |_| |_| |_  | |_\ \  __/\__ \ |_| | (_) | | | |
#  \___/ \___/   \____/\___||___/\__|_|\___/|_| |_|
                                
                                        
def redrawGameWindow(background):
    win.blit(background, (0,0))
    
    if background == menu_back:
        Menu_Background()
           
    if background == option_back:
        Option_Background()
            
    if background == choose_back:
        Choose_Background()

    if background == play_back:
        Play_Background()

    if background == editor_hero_back:
        Editor_Hero_Background()

    if background == editor_back:
        Editor_Background()

    if background == choose_deck_back:
        Choose_Deck_Background()

    if background == deck_viewer_back:
        Deck_Viewer_Background()

    if background == end_back:
        End_Background()

    if background == tuto_back:
        Tuto_Background()
    if background == wait_other_back:
        Wait_Other_Background()
        
    pygame.display.update()

def Menu_Background():
    win.blit(logo, ((width-350)/2,20))
    win.blit(play_0, ((width-400)/4,300))
    win.blit(editeur_0, ((width-400)*(3/4),300))
    win.blit(option_0, ((width-400)/4,500))
    win.blit(exit_0, ((width-400)*(3/4),500))
    win.blit(aide_0, (1150, 10))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if 1150 <= mouse_x <= 1250 and 20 <= mouse_y <= 105:
        win.blit(aide_1, (1150, 10))
    
    if 300 <= mouse_y <= 420:
        if 220 <= mouse_x <= 620:
            win.blit(play_1, ((width-400)/4,300))
        if 660 <= mouse_x <= 1060:
            win.blit(editeur_1, ((width-400)*(3/4),300))
            
    if 500 <= mouse_y <= 620:
        if 220 <= mouse_x <= 620:
            win.blit(option_1, ((width-400)/4,500))
        if 660 <= mouse_x <= 1060:
            win.blit(exit_1, ((width-400)*(3/4),500))
            

def Option_Background():
    global x_0, x_1, nom_joueur
    text = big_font.render(nom_joueur, True, (255,255,255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (width/2,height/2)
    win.blit(text, textRect)
    win.blit(retour_0, ((width-400)/2,550))
    win.blit(volume, ((width/2)-310,150))
    win.blit(barre, (x_0,150))

    win.blit(pygame.image.load("image/son.png").convert_alpha(), (525, 80))

    button = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    
    if 440 <= mouse_x <= 840:
        if 550 <= mouse_y <= 670:
            win.blit(retour_1, ((width-400)/2,550))
    
    if (width/2)-305 <= mouse_x <= (width/2)+295 and 150 <= mouse_y <= 197:  
        if button[0] != 0:
            pos = pygame.mouse.get_pos()
            x_0 = pos[0]
            pygame.mixer.music.set_volume(((x_0-335)*6)/3600) 
        button = pygame.mouse.get_pressed()

    if (width/2)-305 <= mouse_x <= (width/2)+295 and 350 <= mouse_y <= 397:    
        if button[0] != 0:
            pos = pygame.mouse.get_pos()
            x_1 = pos[0]
            pygame.mixer.music.set_volume(((x_1-335)*6)/3600)
        button = pygame.mouse.get_pressed()
    

                
def Choose_Background():
    win.blit(guerrier_0, (110,150))
    win.blit(voleur_0, (310,390))
    win.blit(pretre_0, (510,150))
    win.blit(mage_0, (710,390))
    win.blit(mecanicien_0, (910,150))
    win.blit(fleche_retour_0, (10,650))
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    if 150 <= mouse_y <= 450:
        if 130 <= mouse_x <= 350:
            win.blit(guerrier_1, (110,150))
        if 530 <= mouse_x <= 750:
            win.blit(pretre_1, (510,150))
        if 930 <= mouse_x <= 1150:
            win.blit(mecanicien_1, (910,150))
    if 400 <= mouse_y <= 700:
        if 330 <= mouse_x <= 550:
            win.blit(voleur_1, (310,390))
        if 730 <= mouse_x <= 950:
            win.blit(mage_1, (710,390))
        
    if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
        win.blit(fleche_retour_1, (10,650))

def Editor_Hero_Background():
    win.blit(guerrier_0, (110,150))
    win.blit(voleur_0, (310,390))
    win.blit(pretre_0, (510,150))
    win.blit(mage_0, (710,390))
    win.blit(mecanicien_0, (910,150))
    win.blit(fleche_retour_0, (10,650))
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    if 150 <= mouse_y <= 450:
        if 130 <= mouse_x <= 350:
            win.blit(guerrier_1, (110,150))
        if 530 <= mouse_x <= 750:
            win.blit(pretre_1, (510,150))
        if 930 <= mouse_x <= 1150:
            win.blit(mecanicien_1, (910,150))
    if 400 <= mouse_y <= 700:
        if 330 <= mouse_x <= 550:
            win.blit(voleur_1, (310,390))
        if 730 <= mouse_x <= 950:
            win.blit(mage_1, (710,390))
            
    if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
        win.blit(fleche_retour_1, (10,650))

def Play_Background():
    log.update()
    win.blit(cadre, (-15,-15))
    win.blit(end_turn_0, (1110,450))
    win.blit(player_1.image, (10,440))
    win.blit(player_2.image, (1030, 10))
    if player_1.power_used == False:
        win.blit(player_1.class_power_small, (280,450))
    else:
        win.blit(player_1.class_power_small_off, (280,450))
    if player_1.hp < 10:
        win.blit(font.render(str(player_1.hp),3,(255,255,255)), (35,650))
    else:
        win.blit(font.render(str(player_1.hp),3,(255,255,255)), (30,650))
    if player_1.armor < 10:
        win.blit(font.render(str(player_1.armor),3,(0,0,0)), (210,637))
    else:
        win.blit(font.render(str(player_1.armor),3,(0,0,0)), (205,635))
    if player_1.current_stamina < 10:
        win.blit(font.render(str(player_1.current_stamina),3,(255,255,255)), (127,453))
    else:
        win.blit(font.render(str(player_1.current_stamina),3,(255,255,255)), (117,453))

    if player_2.hp < 10:
        win.blit(font.render(str(player_2.hp),3,(255,255,255)), (1050,220))
    else:
        win.blit(font.render(str(player_2.hp),3,(255,255,255)), (1053,220))
    if player_2.armor < 10:
        win.blit(font.render(str(player_2.armor),3,(0,0,0)), (1229,210))
    else:
        win.blit(font.render(str(player_2.armor),3,(0,0,0)), (1223,210))
    if player_2.current_stamina < 10:
        win.blit(font.render(str(player_2.current_stamina),3,(255,255,255)), (1147,24))
    else:
        win.blit(font.render(str(player_2.current_stamina),3,(255,255,255)), (1137,24))
    if (
        player_1.secret_neutre1 == True
        or player_1.secret_neutre2 == True
        or player_1.secret_neutre3 == True
        or player_1.secret_mage == True
        or player_1.secret_guerrier == True
        or player_1.secret_voleur == True
        or player_1.secret_mecanicien == True
        or player_1.secret_pretre == True
    ):
        win.blit(secret, (115, 650))
    if (
    player_2.secret_neutre1 == True
    or player_2.secret_neutre2 == True
    or player_2.secret_neutre3 == True
    or player_2.secret_mage == True
    or player_2.secret_guerrier == True
    or player_2.secret_voleur == True
    or player_2.secret_mecanicien == True
    or player_2.secret_pretre == True
    ):
        win.blit(secret, (1130, 220))
        
    i = 1
    j = 1
    mouse_x, mouse_y = pygame.mouse.get_pos()
    card_blit = -1
    for i, card in enumerate(player_1.hand):
        win.blit(pygame.image.load(data["petit_sprite"][card]).convert_alpha(), (100*i+280, 600))
        if 600 <= mouse_y <= 800:
            if 100*i+280 <= mouse_x <= (100*i+280)+100:
                card_blit = card
                pos_card = i
    if card_blit >= 0:
        if pos_card == 9:
            win.blit(pygame.image.load(data["grand_sprite"][card_blit]).convert_alpha(), (100*pos_card+280-120, 420))
        else: 
            win.blit(pygame.image.load(data["grand_sprite"][card_blit]).convert_alpha(), (100*pos_card+280-75, 420))
            
    if online == True:
        nmb_carte_ennemi = int(n.send(f"nmb_carte,{len(player_1.hand)}"))
    else:
        nmb_carte_ennemi = len(player_2.hand)
        
    for j in range(nmb_carte_ennemi):
        win.blit(pygame.image.load("image/carte_ennemi.png").convert_alpha(), ((width-330)-60*j, 0))

    if 280 < mouse_x < 370 and 460 < mouse_y < 580:
        if player_1.power_used == False:
            win.blit(player_1.class_power_big, (205,347))
        else:
            win.blit(player_1.class_power_big_off, (205,347))

def Editor_Background():
    global nom_deck, created_deck, current_background, deck_edited, code
    mouse_x, mouse_y = pygame.mouse.get_pos()
    win.blit(pygame.image.load("image/recherche.png").convert_alpha(), (740, 10))
    win.blit(pygame.image.load("image/ok.png").convert_alpha(), (1100, 660))
    win.blit(parchemin, (740, 110))
    text = font.render("Supprimer", True, (255,255,255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (950, 680)
    win.blit(text, textRect)

    if "27327327427427627527627598113" in code:
        win.blit(pygame.image.load(data["petit_sprite"][51]).convert_alpha(), (420,440))
            
    if 1200 < mouse_x < 1260 and 650 < mouse_y < 700:
        win.blit(pygame.image.load("image/fleche_retour_1.png").convert_alpha(), (1200, 650))
    else:
        win.blit(pygame.image.load("image/fleche_retour_0.png").convert_alpha(), (1200, 650))       
    card = 0
    for i in range(4):
        for j in range(7):
            if card < 25:
                win.blit(pygame.image.load(data["petit_sprite"][card]).convert_alpha(), (j*100+20,i*140+20))
                card += 1
    for i in range(5):
        win.blit(pygame.image.load(data["petit_sprite"][hero_editor.class_number+i]).convert_alpha(), (i*100+20,580))
    for i in range(4):
        if i*140+20 <= mouse_y <= i*140+136:
            for j in range(7):
                if j*100+20 <= mouse_x <= j*100+120 and j+(7*i) < 25:
                    if i == 0:
                        if j == 0:
                            win.blit(pygame.image.load(data["grand_sprite"][j+(7*i)]).convert_alpha(), (j*100,i*140))
                        else:
                            win.blit(pygame.image.load(data["grand_sprite"][j+(7*i)]).convert_alpha(), (j*100-60,i*140))
                    else:
                        if j == 0:
                            win.blit(pygame.image.load(data["grand_sprite"][j+(7*i)]).convert_alpha(), (j*100,i*140-80))
                        else:
                            win.blit(pygame.image.load(data["grand_sprite"][j+(7*i)]).convert_alpha(), (j*100-60,i*140-80))
    for i in range(5):
        if 580 <= mouse_y <= 696:
            if i*100+20 <= mouse_x <= i*100+120 and i != 0: 
                win.blit(pygame.image.load(data["grand_sprite"][hero_editor.class_number+i]).convert_alpha(), (i*100-60,390))
            elif i*100+20 <= mouse_x <= i*100+120:
                win.blit(pygame.image.load(data["grand_sprite"][hero_editor.class_number+i]).convert_alpha(), (i*100,390))

    if "27327327427427627527627598113" in code:
        if 420 < mouse_x < 420+136 and 440 < mouse_y < 560:
            win.blit(pygame.image.load(data["grand_sprite"][51]).convert_alpha(), (420-80,340))
    
    for i in created_deck:
        if i < 15:
            if created_deck.count(i) == 1:
                win.blit(petite_font.render(data["nom"][i],1,(0,0,0)), (770,i*30+130))
            else:
                win.blit(petite_font.render(data["nom"][i],1,(255,0,0)), (770,i*30+130))
        elif i < 30 <= 50:
            if created_deck.count(i) == 1:
                win.blit(petite_font.render(data["nom"][i],1,(0,0,0)), (960,(i-15)*30+130))
            else:
                win.blit(petite_font.render(data["nom"][i],1,(255,0,0)), (960,(i-15)*30+130))
        elif i == 51:
            win.blit(petite_font.render(data["nom"][i],1,(random.randint(0,255),random.randint(0,255),random.randint(0,255))), (900,570))
        else:
            if created_deck.count(i) == 1:
                win.blit(petite_font.render(data["nom"][i],1,(0,0,255)), (960,(i-hero_editor.class_number+10)*30+130))
            else:
                win.blit(petite_font.render(data["nom"][i],1,(255,0,255)), (960,(i-hero_editor.class_number+10)*30+130))
              
                
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                nom_deck = nom_deck[:-1]
            elif len(nom_deck) <= 12:
                nom_deck += event.unicode 
    

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(4):
                if i*140+20 <= mouse_y <= i*140+136:
                    for j in range(7):
                        if j*100+20 <= mouse_x <= j*100+120 and j+(7*i) < 25:
                            if len(created_deck) < 30:
                                if created_deck.count(j+(7*i)) < 2:
                                    created_deck.append(j+(7*i))

            for i in range(5):
                if 580 <= mouse_y <= 696:
                    if i*100+20 <= mouse_x <= i*100+120:
                        if len(created_deck) < 30:
                            if created_deck.count(hero_editor.class_number+i) < 2:
                                created_deck.append(hero_editor.class_number+i)

            for i in range(15):
                if 770 <= mouse_x <= 940:
                    if i*30+120 <= mouse_y <= i*30+140:
                        if i in created_deck:
                            created_deck.pop(created_deck.index(i))
                if 960 <= mouse_x <= 1180:
                    if i*30+120 <= mouse_y <= i*30+140 and i < 10:
                        if i+15 in created_deck:
                            created_deck.pop(created_deck.index(i+15))
                    elif i*30+120 <= mouse_y <= i*30+140:
                        if hero_editor.class_number+i-10 in created_deck:
                            created_deck.pop(created_deck.index(hero_editor.class_number+i-10))
                            
            if "273" in code:
                if 420 < mouse_x < 420+136 and 440 < mouse_y < 540 and len(created_deck) < 30 and created_deck.count(51) == 0:
                    created_deck.append(51)
                if 900 < mouse_x < 990 and 575 < mouse_y < 585 and 51 in created_deck:
                    created_deck.pop(created_deck.index(51))
    


            if 1100 <= mouse_x <= 1170 and 670 <= mouse_y <= 710:
                if len(created_deck) == 30:
                    if nom_deck == "":
                        nom_deck = f"{hero_editor.classe} new"
                    created_deck.insert(0,nom_deck)
                    created_deck.insert(0,hero_editor.classe)
                    if deck_edited < 0:
                        data_deck.append(created_deck)
                        book.save('bdd/deck.xlsx')
                        ReloadBDD()
                        current_background = menu_back
                    else:
                        for i, cell in enumerate(data_deck[str(deck_edited+2)]):
                            cell.value = created_deck[i]
                        book.save('bdd/deck.xlsx')
                        ReloadBDD()
                        current_background = menu_back

                    
            if 1200 <= mouse_x <= 1260 and 650 <= mouse_y <= 700:
                current_background = deck_viewer_back
                code = ""
                    

            if 860 <= mouse_x <= 1030 and 660 <= mouse_y <= 700 and deck_edited > 0:
                data_deck.delete_rows(idx=deck_edited+2)
                book.save('bdd/deck.xlsx')
                ReloadBDD()
                current_background = deck_viewer_back

    if len(created_deck) == 30:
        win.blit(font.render("Deck complet !",3,(255,255,255)), (700,620))
    else:
        win.blit(font.render(f"Nombres de cartes : {len(created_deck)}",3,(255,255,255)), (540,620))
        
    if len(created_deck) == 0:
        win.blit(font.render(f"Coût moyen : 0",3,(255,255,255)), (980,620))
    else:
        moyen, somme = 0, 0
        try:
            for i in created_deck:
                    somme += int(data["cout"][i])
            moyen = round(somme/len(created_deck), 1)
            win.blit(font.render(f"Coût moyen : {moyen}",3,(255,255,255)), (980,620))
        except:
            pass
    
    win.blit(font.render(nom_deck,2,(0,0,0)), (850,38))


def Choose_Deck_Background():
    win.blit(fleche_retour_0, (10,650))
    mouse_x, mouse_y = pygame.mouse.get_pos()        
    if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
        win.blit(fleche_retour_1, (10,650))
    if player_1.classe == "guerrier":
        win.blit(guerrier_1, (width/2-125,10))
    if player_1.classe == "pretre":
        win.blit(pretre_1, (width/2-125,10))
    if player_1.classe == "mecanicien":
        win.blit(mecanicien_1, (width/2-125,10))
    if player_1.classe == "voleur":
        win.blit(voleur_1, (width/2-125,10))
    if player_1.classe == "mage":
        win.blit(mage_1, (width/2-125,10))
    place = 1
    text = font.render("Vos decks :", True, (255,255,255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (width/2, height/2)
    win.blit(text, textRect)
    for i in range(data_deck.max_row-1):
        if deck_ex['classe'][i] == player_1.classe:
            text = font.render((deck_ex['nom'][i]), True, (255,255,255), (0,0,0)) 
            textRect = text.get_rect()
            if place <= 3:
                textRect.center = (width*(place/4), 500)
            elif place <= 6:
                textRect.center = (width*((place-3)/4), 600)
            win.blit(text, textRect)
            place += 1


def Deck_Viewer_Background():
    global code
    win.blit(fleche_retour_0, (10,650))
    mouse_x, mouse_y = pygame.mouse.get_pos()        
    if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
        win.blit(fleche_retour_1, (10,650))
    if hero_editor.classe == "guerrier":
        win.blit(guerrier_1, (width/2-125,10))
    if hero_editor.classe == "pretre":
        win.blit(pretre_1, (width/2-125,10))
    if hero_editor.classe == "mecanicien":
        win.blit(mecanicien_1, (width/2-125,10))
    if hero_editor.classe == "voleur":
        win.blit(voleur_1, (width/2-125,10))
    if hero_editor.classe == "mage":
        win.blit(mage_1, (width/2-125,10))
    place = 1
    text = font.render("Editer vos decks :", True, (255,255,255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (width/2, height/2)
    win.blit(text, textRect)
    for i in range(data_deck.max_row-1):
        if deck_ex['classe'][i] == hero_editor.classe:
            text = font.render((deck_ex['nom'][i]), True, (255,255,255), (0,0,0)) 
            textRect = text.get_rect()
            if place <= 3:
                textRect.center = (width*(place/4), 450)
            elif place <= 6:
                textRect.center = (width*((place-3)/4), 550)
            win.blit(text, textRect)
            place += 1
    text = font.render("Créer un nouveau Deck", True, (255,255,255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (width/2, 600)
    win.blit(text, textRect)



def End_Background():
    if player_1.hp <= 0:
        if player_2.hp <= 0:
            text = big_font.render("Egalité !", True, (255,255,255), (0,0,0)) 
        else:
            text = big_font.render("P2 a gagné !", True, (255,255,255), (0,0,0)) 
    else:
        text = big_font.render("P1 a gagné !", True, (255,255,255), (0,0,0)) 
    textRect = text.get_rect()
    textRect.center = (width/2, height/2-100)
    win.blit(text, textRect)
    retour = font.render("Menu Principal", True, (255,255,255), (0,0,0)) 
    retourRect = retour.get_rect()
    retourRect.center = (width/2, height/2)
    win.blit(retour, retourRect)

def Tuto_Background():
    win.blit(tuto, (200,100))
    win.blit(fleche_retour_0, (10,650))    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
        win.blit(fleche_retour_1, (10,650))

def Wait_Other_Background():
    global current_background, player_2
    retour = big_font.render("Waiting for other player..", True, (255,255,255), (0,0,0)) 
    retourRect = retour.get_rect()
    retourRect.center = (width/2, height/2)
    win.blit(retour, retourRect)
    number = int(n.send("number_player, "))
    if number == 2:
        ennemy_hero = n.send(f"hero,{player_1.classe}")
        ennemy_name = n.send(f"name,{player_1.name}")

        hand = (str(player_1.hand).replace("[", "")).replace("]", "").replace(",",";")
        ennemy_hand = n.send(f"hand,{hand}")
        
        deck = (str(player_1.deck).replace("[", "")).replace("]", "").replace(",",";")
        ennemy_deck = n.send(f"deck,{deck}")

        ennemy_hand = ennemy_hand.replace(" ","").split(";")
        for i, _ in enumerate(ennemy_hand):
            ennemy_hand[i] = int(ennemy_hand[i])
        ennemy_deck = ennemy_deck.replace(" ","").split(";")
        for i, _ in enumerate(ennemy_deck):
            ennemy_deck[i] = int(ennemy_deck[i])
        player_2 = Hero(ennemy_hero, ennemy_name, False)
        player_2.deck = ennemy_deck
        player_2.hand = ennemy_hand
        current_background = play_back

# ___  ___      _         _                   
# |  \/  |     (_)       | |                  
# | .  . | __ _ _ _ __   | | ___   ___  _ __  
# | |\/| |/ _` | | '_ \  | |/ _ \ / _ \| '_ \ 
# | |  | | (_| | | | | | | | (_) | (_) | |_) |
# \_|  |_/\__,_|_|_| |_| |_|\___/ \___/| .__/ 
#                                      | |    
#                                      |_|    


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if current_background == deck_viewer_back:
                code += str(event.key)
            if current_background == option_back:
                if event.key == pygame.K_BACKSPACE:
                    nom_joueur = nom_joueur[:-1]
                elif len(nom_joueur) < 8:
                    nom_joueur += str(event.unicode)
             
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if current_background == menu_back and changed == True:
                if 300 <= mouse_y <= 420:
                    if 220 <= mouse_x <= 620:
                        current_background = choose_back
                        changed = False
                    if 660 <= mouse_x <= 1060:
                        current_background = editor_hero_back
                        changed = False
            
                if 500 <= mouse_y <= 620:
                    if 220 <= mouse_x <= 620:
                        current_background = option_back
                        changed = False
                    if 660 <= mouse_x <= 1060:
                        run = False                 

                if 1150 <= mouse_x <= 1250 and 20 <= mouse_y <= 105:
                    current_background = tuto_back


            if current_background == choose_back and changed == True:
                if 150 <= mouse_y <= 450:          
                    if 130 <= mouse_x <= 350:
                        player_1 = Hero("guerrier", nom_joueur, False)
                        player_2 = Hero(classe_[random.randint(0,len(classe_)-1)], "P2", True)
                        player_2.deck = player_2.create_deck(player_2.class_number)
                        player_2.hand = player_2.create_hand(player_2.deck)
                        current_background = choose_deck_back
                        changed = False
                        
                    if 530 <= mouse_x <= 750:
                        player_1 = Hero("pretre", nom_joueur, False)
                        player_2 = Hero(classe_[random.randint(0,len(classe_)-1)], "P3", True)
                        player_2.deck = player_2.create_deck(player_2.class_number)
                        player_2.hand = player_2.create_hand(player_2.deck)
                        current_background = choose_deck_back
                        changed = False
                        
                    if 930 <= mouse_x <= 1150:
                        player_1 = Hero("mecanicien", nom_joueur, False)
                        player_2 = Hero(classe_[random.randint(0,len(classe_)-1)], "P4", True)
                        player_2.deck = player_2.create_deck(player_2.class_number)
                        player_2.hand = player_2.create_hand(player_2.deck)
                        current_background = choose_deck_back
                        changed = False
                        
                if 390 <= mouse_y <= 720:
                    
                    if 330 <= mouse_x <= 550:
                        player_1 = Hero("voleur", nom_joueur, False)
                        player_2 = Hero(classe_[random.randint(0,len(classe_)-1)], "P5", True)
                        player_2.deck = player_2.create_deck(player_2.class_number)
                        player_2.hand = player_2.create_hand(player_2.deck)
                        current_background = choose_deck_back
                        changed = False
                        
                    if 730 <= mouse_x <= 950:
                        player_1 = Hero("mage", nom_joueur, False)
                        player_2 = Hero(classe_[random.randint(0,len(classe_)-1)], "P6", True)
                        player_2.deck = player_2.create_deck(player_2.class_number)
                        player_2.hand = player_2.create_hand(player_2.deck)
                        current_background = choose_deck_back
                        changed = False

                if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
                    current_background = menu_back
                    changed = False


            if current_background == option_back and changed == True:
                if (width-400)/2 <= mouse_x <= (width+400)/2 and 550 <= mouse_y <= 670:
                    current_background = menu_back
                    changed = False
                if 0 < mouse_x < 200:
                    online = not(online)

            if current_background == play_back and changed == True:
                if player_1.can_play == True:
                    if 280 < mouse_x < 370 and 460 < mouse_y < 580:
                        if player_1.current_stamina >= 2 and player_1.power_used == False:
                            if player_1.classe == "guerrier":
                                player_1.heroic_boost_damage = 1
                            elif player_1.classe == "mage":
                                damage(1, player_1, player_2)
                            elif player_1.classe == "voleur":
                                player_1.esquive = 0.2
                            elif player_1.classe == "pretre":
                                heal(1, player_1)
                            elif player_1.classe == "mecanicien":
                                armor(1, player_1)
                            player_1.current_stamina -= 2
                            player_1.power_used = True

                    if 600 <= mouse_y <= 800:
                        for i in range(1, len(player_1.hand)+1):
                            if 100*i+180 <= mouse_x <= (100*i+180)+100:
                                play(player_1.hand[i-1], player_1, player_2, online, n)
                if 450 <= mouse_y <= 600:
                    if 1100 <= mouse_x <= 1260:
                        end_turn(player_1, player_2, n)

            if current_background == end_back and changed == True:
                if 520 <= mouse_x <= 760 and 340 <= mouse_y <= 380:
                    current_background = menu_back


            if current_background == choose_deck_back and changed == True:
                if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
                    current_background = choose_back
                    changed = False
                number_deck = 0
                for i in range(data_deck.max_row-1):
                    if deck_ex['classe'][i] == player_1.classe:
                        number_deck += 1
                if number_deck > 3:
                    first_line = 4
                    second_line = number_deck - 2
                else:
                    first_line = number_deck+1
                    second_line = 0
                number_deck = 0
                if 485 <= mouse_y <= 520:
                    for i in range(1, first_line):
                        if width*(i/4)-115 <= mouse_x <= width*(i/4)+115:
                            for j in range(data_deck.max_row-1):
                                if deck_ex['classe'][j] == player_1.classe:
                                    number_deck += 1
                                    if number_deck == i:
                                        for k in range(1,31):
                                            player_1.deck.append(deck_ex['carte_'+str(k)][j])
                                        player_1.hand = player_1.create_hand(player_1.deck)
                                        game(player_1, player_2, n)
                                        current_background = play_back
                                        if online == True:
                                            n = Network()
                                            n.send(f"hero,{player_1.classe}")
                                            n.send(f"name,{player_1.name}")
                                            hand = (str(player_1.hand).replace("[", "")).replace("]", "").replace(",",";")
                                            n.send(f"hand,{hand}")
                                            deck = (str(player_1.deck).replace("[", "")).replace("]", "").replace(",",";")
                                            n.send(f"deck,{deck}")
                                            current_background = wait_other_back
                                        log.texte = []
                                        changed = False
                if 585 <= mouse_y <= 620:
                    for i in range(1, second_line):
                        if width*(i/4)-115 <= mouse_x <= width*(i/4)+115:
                            for j in range(data_deck.max_row-1):
                                if deck_ex['classe'][j] == player_1.classe:
                                    number_deck += 1
                                    if number_deck == i+3:
                                        deck_edited = j
                                        for k in range(1,31):
                                            player_1.deck.append(deck_ex['carte_'+str(k)][j])
                                        player_1.hand = player_1.create_hand(player_1.deck)
                                        game(player_1, player_2, n)
                                        current_background = play_back
                                        if online == True:
                                            n = Network()
                                            a = n.send(f"hero,{player_1.classe}")
                                            a = n.send(f"name,{player_1.name}")
                                            hand = (str(player_1.hand).replace("[", "")).replace("]", "").replace(",",";")
                                            a = n.send(f"hand,{hand}")
                                            deck = (str(player_1.deck).replace("[", "")).replace("]", "").replace(",",";")
                                            a = n.send(f"deck,{deck}")
                                            current_background = wait_other_back
                                        log.texte = []
                                        changed = False

            if current_background == editor_hero_back and changed == True:
                if 150 <= mouse_y <= 450:          
                    if 130 <= mouse_x <= 350:
                        hero_editor = Hero("guerrier", "", False)
                        current_background = deck_viewer_back
                        changed = False
                        nom_deck = ""
                        created_deck = []
                                               
                    if 530 <= mouse_x <= 750:
                        hero_editor = Hero("pretre", "", False)
                        current_background = deck_viewer_back
                        changed = False
                        nom_deck = ""
                        created_deck = []
                                              
                    if 930 <= mouse_x <= 1150:
                        hero_editor = Hero("mecanicien", "", False)
                        current_background = deck_viewer_back
                        changed = False
                        nom_deck = ""
                        created_deck = []
                        
                elif 400 <= mouse_y <= 700:    
                    
                    if 330 <= mouse_x <= 550:
                        hero_editor = Hero("voleur", "", False)
                        current_background = deck_viewer_back
                        changed = False
                        nom_deck = ""
                        created_deck = []
                        
                    if 730 <= mouse_x <= 950:
                        hero_editor = Hero("mage", "", False)
                        current_background = deck_viewer_back
                        changed = False
                        nom_deck = ""
                        created_deck = []



                if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
                    current_background = menu_back
                    changed = False

    

            if current_background == deck_viewer_back and changed == True:

                if width/2-100 <= mouse_x <= width/2+100:
                    if 590 <= mouse_y <= 610:
                        current_background = editor_back
                        changed = False
                created_deck = []
                nom_deck = ""
                deck_edited = -1
                number_deck = 0
                for i in range(data_deck.max_row-1):
                    if deck_ex['classe'][i] == hero_editor.classe:
                        number_deck += 1
                if number_deck > 3:
                    first_line = 4
                    second_line = number_deck - 2
                else:
                    first_line = number_deck+1
                    second_line = 0
                number_deck = 0
                if 435 <= mouse_y <= 465:
                    for i in range(1, first_line):
                        if width*(i/4)-115 <= mouse_x <= width*(i/4)+115:
                            for j in range(data_deck.max_row-1):
                                if deck_ex['classe'][j] == hero_editor.classe:
                                    number_deck += 1
                                    if number_deck == i:
                                        deck_edited = j
                                        for k in range(1,31):
                                            created_deck.append(deck_ex['carte_'+str(k)][j])
                                        nom_deck = deck_ex['nom'][j] 
                                        current_background = editor_back
                                        changed = False
                if 535 <= mouse_y <= 565:
                    for i in range(1, second_line):
                        if width*(i/4)-115 <= mouse_x <= width*(i/4)+115:
                            for j in range(data_deck.max_row-1):
                                if deck_ex['classe'][j] == hero_editor.classe:
                                    number_deck += 1
                                    if number_deck == i+3:
                                        deck_edited = j
                                        for k in range(1,31):
                                            created_deck.append(deck_ex['carte_'+str(k)][j])
                                        nom_deck = deck_ex['nom'][j] 
                                        current_background = editor_back
                                        changed = False

                if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
                    current_background = editor_hero_back
                    changed = False

            if current_background == tuto_back:
                if 10 <= mouse_x <= 70 and 650 <= mouse_y <= 710:
                    current_background = menu_back

        if current_background == play_back:     
            if player_1.hp <= 0 or player_2.hp <= 0:
                current_background = end_back
                changed= False
                tour = 1
            if player_1.can_play == False:
                carte = n.send(f"play_card,None")
                if carte != "None":
                    play(int(carte), player_2, player_1, online, n)
            if online == True:
                print(player_1.hand, player_2.hand)
                hand = (str(player_1.hand).replace("[", "")).replace("]", "").replace(",",";")
                ennemy_hand = n.send(f"hand,{hand}")
                ennemy_hand = ennemy_hand.replace(" ","").split(";")
                for i, _ in enumerate(ennemy_hand):
                    ennemy_hand[i] = int(ennemy_hand[i])
                player_2.hand = ennemy_hand
                print(player_1.hand, player_2.hand)
                
                        
    redrawGameWindow(current_background)
    changed = True

        
pygame.quit()
