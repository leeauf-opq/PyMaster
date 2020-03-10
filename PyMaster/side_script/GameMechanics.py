from side_script.variable import *
import random
import pygame
import math
import copy

class TextBox(object):
    def __init__(self,rect,**kwargs):
        self.rect = pygame.Rect(rect)
        self.texte = []
        self.final = None
        self.rendered = None
        self.render_rect = None
        self.render_area = None
        self.process_kwargs(kwargs)
        self.char_ligne = 0
        self.max_char = 40
        self.y_text = 5
        self.line_number = 0
 
    def process_kwargs(self,kwargs):
        defaults = {
                    "color" : pygame.Color("black"),
                    "font_color" : pygame.Color("white"),
                    "font" : pygame.font.Font("side/upheavtt.ttf", 15),
                    }
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("TextBox accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)   
 
    def update(self): 
        win.fill(self.color,self.rect)
        if len(self.texte) > 14:
            del self.texte[:3]
        for i, ligne in enumerate(self.texte):
            self.rendered = self.font.render(ligne, True, self.font_color)
            self.render_rect = self.rendered.get_rect(x=self.rect.x+2, y=(i*25)+self.y_text)
            win.blit(self.rendered,self.render_rect,self.render_area)

log = TextBox(rect=(0,0,400,400))

                            
#  _____                                            _                 _          
# |  __ \                                          | |               (_)         
# | |  \/ __ _ _ __ ___   ___   _ __ ___   ___  ___| |__   __ _ _ __  _  ___ ___ 
# | | __ / _` | '_ ` _ \ / _ \ | '_ ` _ \ / _ \/ __| '_ \ / _` | '_ \| |/ __/ __|
# | |_\ \ (_| | | | | | |  __/ | | | | | |  __/ (__| | | | (_| | | | | | (__\__ \
#  \____/\__,_|_| |_| |_|\___| |_| |_| |_|\___|\___|_| |_|\__,_|_| |_|_|\___|___/


def game(player_1, player_2, n):
    global tour, first, second
    player = [player_1, player_2]
    rand = random.randint(0,1)
    first = player_1#player[rand]
    second = player[not(rand)]
    second.hand.append(50)
    first.can_play = True
    if first == player_2 and online == False:
        bot_turn(player_2, player_1, n)

def play(carte, current_player, other_player, online, n):
    can_play = True
    if current_player.current_stamina < int(data["cout"][carte]):
        can_play = False
    if can_play == True:
        if online == True and current_player.isBot == False:
            n.send(f"play_card,{carte}")
        if "Secret" in data['effet'][carte]:
            pass
        else:
            log.texte.append(f''' -> {current_player.name} utilise la carte "{data['nom'][carte]}" :''')
        for i in range (data['nmb_effet'][carte]):
            if current_player.blocked == True and ( data[f'effet_{i}'][carte] == "heal" or data[f'effet_{i}'][carte] == "armor"):
                log.texte.append(f"{current_player.name} ne peut pas utiliser")
                log.texte.append(f"de heal ou d'armure pendant")
                log.texte.append(f"ce tour")2
                return
        print("play", current_player.hand, carte)
        try:
            current_player.hand.pop(current_player.hand.index(carte))
        except:
            print("nique")
            return
        for j in range (data['nmb_effet'][carte]):
            print("effet")
            effect(data[f'effet_{j}'][carte],data[f'valeur_effet_{j}'][carte], current_player, other_player)
        current_player.current_stamina -= int(data["cout"][carte]) + current_player.stamina_increase

def bot_turn(bot, player, n):
    for i in bot.hand:
        for j in range (data["nmb_effet"][i]):
            if (data[f"effet_{j}"][i] == "damage" and data[f"valeur_effet_{j}"][i] >= player.hp) or data[f"effet_{j}"][i] == "kill" and bot.current_stamina >= data["cout"][i]:
                play(i, bot, player, False, n)
                    
    if bot.hp + bot.armor < 10:
        for i in bot.hand:
            for j in range (data["nmb_effet"][i]):
                if (data[f"effet_{j}"][i] == "heal" or data[f"effet_{j}"][i] == "armor" or data[f"effet_{j}"][i] == "mult_hp") and bot.current_stamina >= data["cout"][i]:
                    play(i, bot, player, False, n)
                    
    endurance = bot.current_stamina
    cout_main = [data["cout"][i] for i in bot.hand]
    tampon_main = sorted(cout_main, reverse = True)
    run = True
    count = 0
    num = 0
    solution = []

    while run:
        card_played = []
        card_index = []
        tampon_endurance = endurance
        for cout in tampon_main:
            if tampon_endurance >= cout:
                tampon_endurance -= cout
                if cout_main.index(cout) in card_index:
                    card_index.append([i for i, n in enumerate(cout_main) if n == cout])
                else:
                    card_index.append(cout_main.index(cout))
                card_played.append(tampon_main[tampon_main.index(cout)])
        if tampon_endurance == 0 + math.floor(count/100):
            run = False
        else:
            tampon_main = sorted(cout_main, reverse = True)
            random.shuffle(tampon_main)
            count += 2
        if count > 1000:
            run = False

    played_card = dict(zip(card_played, card_index))
    for i in played_card.items():
        i = i[1]
        if type(i) == list:
            for j in i:
                solution.append(j)
        else:
            solution.append(i)
    bot_tampon = copy.deepcopy(bot.hand)
    for carte in solution:
        play(bot_tampon[carte], bot, player, False, n)         
    end_turn(bot, player, n)


def end_turn(current_player, other_player, n):
    global tour
    tour += 0.5
    current_player.blocked = False
    current_player.stamina_increase = 0
    current_player.power_used = False
    current_player.can_play = False
    current_player, other_player = other_player, current_player
    current_player.can_play = True
    draw(1, current_player)
    if tour >= 2:
        if current_player.stamina < 10:
            current_player.stamina += 1
    current_player.current_stamina = current_player.stamina
    if current_player.isBot == True:
        bot_turn(current_player, other_player, n)

                                                                           
def effect(effet, number, current_player, other_player):
    number = int(number)
    if effet == "draw":
        draw(number, current_player)
    if effet == "damage":
        damage(number, current_player, other_player)
    if effet == "heal":
        heal(number, current_player)
    if effet == "armor":
        armor(number, current_player)
    if effet == "discard":
        discard(number, current_player)
    if effet == "bloque":
        block(other_player)
    if effet == "boost_damage":
        boost_damage(current_player)
    if effet == "boost_heal":
        boost_heal(current_player)
    if effet == "div_hp":
        div_hp(other_player)
    if effet == "mult_hp":
        mult_hp(current_player)
    if effet == "stamina":
        stamina(current_player)
    if effet == "duplicate":
        duplicate(current_player)
    if effet == "refill":
        refill(current_player)
    if effet == "boost_def":
        boost_def(current_player)
    if effet == "card_damage":
        damage(len(current_player.hand),current_player, other_player)
    if effet == "return_damage":
        damage(current_player.damage_taken ,current_player, other_player)
    if effet == "esquive":
        esquive(current_player)
    if effet == "stamina_destroy":
        stamina_destroy(other_player)
    if effet == "stamina_increase":
        stamina_increase(other_player)
    if effet == "defausse_adv":
        discard(len(other_player.hand), other_player)
    if effet == "boost_armor":
        boost_armor(current_player)
    if effet == "armor_damage":
        damage(current_player.armor, current_player, other_player)
    if effet == "heal_damage":
        damage(current_player.hp_healed, current_player, other_player)
    if effet == "hand_heal":
        heal(len(current_player.hand),current_player)
    if effet == "temp_stamina":
        temp_stamina(current_player)
    if effet == "steal":
        steal(current_player, other_player)
    if effet == "secret_neutre1":    
        secret_neutre1(current_player)
    if effet == "secret_neutre2":
        secret_neutre2(current_player)
    if effet == "secret_neutre3":
        secret_neutre3(current_player)
    if effet == "secret_mage":
        secret_mage(current_player)
    if effet == "secret_guerrier":        
        secret_guerrier(current_player)
    if effet == "secret_voleur":
        secret_voleur(current_player)
    if effet == "secret_mecanicien":
        secret_mecanicien(current_player)
    if effet == "secret_pretre":
        secret_pretre(current_player)
    if effet == "kill":
        kill(other_player)

def draw(number, player):
    if len(player.deck) >= number:
        longueur = len(player.deck)-1
        for i in range(number):
            rand = random.randint(0,longueur)
            if len(player.hand) >= 10:
                log.texte.append(f"La carte {data['nom'][player.deck.pop(rand)]}") 
                log.texte.append(f"à été supprimé de la main de") 
                log.texte.append(f"{player.name} car il a déjà 10 cartes") 
            else:
                player.hand.append(player.deck.pop(random.randint(0,longueur)))
                longueur -= 1
    else:
        player.fatigue += 1
        log.texte.append(f"{player.name} n'a plus de cartes,") 
        log.texte.append(f"il subit {player.fatigue} dégats de fatigue") 
        player.hp -= player.fatigue
                          
def damage(number, current_player, other_player):
    can_attack = True
    if random.randint(0,100)/100 <= other_player.esquive:
        log.texte.append(f"{other_player.name} esquive les dégats !") 
        other_player.esquive = 0
    else:
        if  other_player.secret_neutre1 == True:
            log.texte.append("L'attaque déclenche le secret Divide") 
            log.texte.append("réduisant les dégats par deux") 
            boost_def(other_player)
            other_player.secret_neutre1 = False
            
        elif other_player.secret_neutre3 == True:
            log.texte.append("L'attaque déclenche le secret Gotcha") 
            log.texte.append(f"faisant piocher deux cartes à {other_player.name}") 
            draw(2, other_player)
            other_player.secret_neutre3 = False
            
        elif other_player.secret_mage == True:
            log.texte.append("L'attaque déclenche le secret Répit") 
            log.texte.append("bloquant les dégats") 
            other_player.boost_def = 0
            other_player.secret_mage = False
            
        elif other_player.secret_voleur == True:
            log.texte.append("L'attaque déclenche le secret Pickpocket") 
            log.texte.append(f"faisant voler {other_player.name} une carte de {current_player.name}") 
            steal(other_player, current_player)
            other_player.secret_voleur = False
            
        elif other_player.secret_mecanicien == True:
            log.texte.append("L'attaque déclenche le secret Agglomération") 
            log.texte.append(f"donnant 5 armure à {other_player.name}") 
            armor(5, other_player)
            other_player.secret_mecanicien = False
            
        elif other_player.secret_pretre == True:
            log.texte.append("L'attaque déclenche le secret Thank You") 
            log.texte.append("et transforment la moitié des dégats en soin") 
            heal(math.floor(number * current_player.boost_damage * other_player.boost_def / 2), other_player)
            other_player.secret_pretre = False
            can_attack = False

        if can_attack == True:
            degat = int(math.floor((number + current_player.heroic_boost_damage) * current_player.boost_damage * other_player.boost_def))
            
            if other_player.secret_neutre2 == True:
                log.texte.append("L'attaque déclenche le secret Parade") 
                log.texte.append(f"renvoyant la moitié des dégats subis à {current_player.name}") 
                damage(math.floor(degat/2), other_player, current_player)
                other_player.secret_neutre2 = False
                
            elif other_player.secret_guerrier == True:
                log.texte.append("L'attaque déclenche le secret Contre") 
                log.texte.append(f"renvoyant les dégats subis sur {current_player.name}") 
                damage(math.floor(degat), other_player, current_player)
                other_player.secret_guerrier = False
                
            if other_player.boost_def < 1:
                other_player.boost_def = 1
            if current_player.boost_damage > 1:
                current_player.boost_damage = 1
                
            if other_player.armor > 0:
                _damage = degat - other_player.armor
                if _damage > 0:
                    other_player.armor = 0
                    other_player.hp -= _damage
                else :
                    other_player.armor = -_damage
            else:
                other_player.hp -= degat
            other_player.damage_taken += degat
            if other_player.hp > 0:
                log.texte.append(f"{other_player.name} perd {degat} pv ! Il lui reste {other_player.hp} pv")
                log.texte.append(f"et {other_player.armor} armure")     
                    
def heal(number, player):
    heal = number * player.boost_heal
    if player.boost_heal > 1:
        player.boost_heal = 1
    player.hp += heal
    player.hp_healed += heal
    if player.hp > 20:
        player.hp = 20
    log.texte.append(f"{player.name} récupere {heal} hp") 
    log.texte.append(f"Il en a maintenant {player.hp}") 
    
def armor(number, player):
    player.armor += number
    log.texte.append(f"{player.name} gagne {number} point d'armure") 
    log.texte.append(f"Il en a maintenant {player.armor}") 
                                  
def discard(number, player):
    longueur = len(player.hand)-1
    for i in range(number):
        rand = random.randint(0,longueur)
        log.texte.append(f"La carte {data['nom'][player.hand.pop(rand)]}") 
        log.texte.append(f"à été défaussé de la main de {player.name}") 
        longueur -= 1
                      
def block(other_player):
    other_player.blocked = True
    log.texte.append(f"Les soins et gains d'armures seront bloqués") 
    log.texte.append(f"pendant le tour de {other_player.name}") 

def boost_damage(player):
    player.boost_damage = 2
    log.texte.append(f"Les prochains dégâts de {player.name}") 
    log.texte.append(f"seront multipliés par 2") 
                                   
                                                
def boost_heal(player):
    player.boost_heal = 2
    log.texte.append(f"Les prochains soins de {player.name}") 
    log.texte.append(f"seront multipliés par 2") 
    
def div_hp(player):
    player.hp = math.floor(player.hp/2)
    log.texte.append(f"La vie de {player.name} à été divisé par deux,")
    log.texte.append(f"il lui reste {player.hp} hp !")
          
def mult_hp(player):
    if player.hp >= 10:
        player.hp = 20
    else:
        player.hp *= 2
    log.texte.append(f"La vie de {player.name} à été multiplié par deux,")
    log.texte.append(f"il lui reste {player.hp} hp !")
                                     
def stamina(player):
    if player.stamina == 10:
        log.texte.append(f"{player.name} a déja 10 d'endurance,")
        log.texte.append(f"il pioche une carte.")
        draw(1, player)
    else:
        player.stamina += 1
        log.texte.append(f"{player.name} gagne 1 d'endurance, il en a {player.stamina}")
        
def duplicate(player):
    longueur = len(player.hand)-1
    player.hand.append(player.hand[random.randint(0,longueur)])
    log.texte.append(f"La carte {data['nom'][player.hand[random.randint(0,longueur)]]}") 
    log.texte.append(f"à été dupliqué dans la main de {player.name}")                  
                     
def refill(player):
    player.current_stamina += 9  
    log.texte.append(f"L'entiere de l'endurance")                                        
    log.texte.append(f"de {player.name} à été restitué")
                                            
def boost_def(player):
    player.boost_def = 0.5
    log.texte.append(f"Les prochains dégats subis")
    log.texte.append(f"par {player.name} seront divisé par 2")

def esquive(player):
    player.esquive = 1
    log.texte.append(f"{player.name} esquivera les prochains dégats")

def stamina_destroy(player):
    player.stamina -= 1
    log.texte.append(f"{player.name} a perdu un d'endurance,")
    log.texte.append(f"il lui en reste {player.stamina}")
                                                                               
def stamina_increase(player):
    player.stamina_increase += 2
    log.texte.append(f"Le coût en endurance des cartes")
    log.texte.append(f"de {player.name} est augmentée de 2")
                                                             
def boost_armor(player):
    player.armor *= 2
    log.texte.append(f"L'armure de {player.name} à été multiplié")
    log.texte.append(f"par 2, il en a {player.armor}")

def temp_stamina(player):
    player.current_stamina += 1
    log.texte.append(f"Le boost donne à {player.name} 1")
    log.texte.append(f"d'endurance pendant ce tour")

def steal(current_player, other_player):
    rand = random.randint(0, len(other_player.hand)-1)
    card = other_player.hand.pop(rand)
    current_player.hand.append(card)
    log.texte.append(f"{current_player.name} vole la carte")
    log.texte.append(f"{data['nom'][card]} à {other_player.name}")

def kill(player):
    player.hp = 0
    
def secret_neutre1(player):
    if player.secret_neutre1 != True:
        player.secret_neutre1 = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
    
def secret_neutre2(player):
    if player.secret_neutre2 != True:
        player.secret_neutre2 = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
    
def secret_neutre3(player):
    if player.secret_neutre3 != True:
        player.secret_neutre3 = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
    
def secret_mage(player):
    if player.secret_mage != True:
        player.secret_mage = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
    
def secret_guerrier(player):
    if player.secret_guerrier != True:
        player.secret_guerrier = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
    
def secret_voleur(player):
    if player.secret_voleur != True:
        player.secret_voleur = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
    
def secret_mecanicien(player):
    if player.secret_mecanicien != True:
        player.secret_mecanicien = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase
        
def secret_pretre(player):
    if player.secret_pretre != True:
        player.secret_pretre = True
        log.texte.append(f"{player.name} active un secret")
    else:
        log.texte.append("Le secret était déjà actif")
        player.current_stamina += 3 + player.stamina_increase


