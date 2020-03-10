import random
from side_script.variable import *
class Hero:

    def __init__(self, classe, name, isBot):
        self.isBot = isBot
        self.classe = classe
        self.name = name
        self.stamina = 10
        self.fatigue = 0
        self.current_stamina = self.stamina
        self.blocked = False
        self.boost_damage = 1
        self.heroic_boost_damage = 0
        self.boost_heal = 1
        self.boost_def = 1
        self.damage_taken = 0
        self.esquive = 0
        self.stamina_increase = 0
        self.hp_healed = 0
        self.power_used = False
        self.secret_neutre1 = False
        self.secret_neutre2 = False
        self.secret_neutre3 = False
        self.secret_mage = False
        self.secret_guerrier = False
        self.secret_voleur = False
        self.secret_mecanicien = False
        self.secret_pretre = False
        self.can_play = False

        if classe == "mage":
            self.hp = 15
            self.armor = 0
            self.class_number = 25
            self.deck = []
            self.hand = []
            self.image = mage
            self.class_power_small = pygame.image.load('sprite/pouvoir_mage.png').convert_alpha()
            self.class_power_big = pygame.image.load('sprite/pouvoir_mage1.png').convert_alpha()
            self.class_power_small_off = pygame.image.load('sprite/pouvoir_mage_off.png').convert_alpha()
            self.class_power_big_off = pygame.image.load('sprite/pouvoir_mage1_off.png').convert_alpha()

        if classe == "guerrier":
            self.hp = 15
            self.armor = 0
            self.class_number = 30
            self.deck = []
            self.hand = []
            self.image = guerrier
            self.class_power_small = pygame.image.load('sprite/pouvoir_guerrier.png').convert_alpha()
            self.class_power_big = pygame.image.load('sprite/pouvoir_guerrier1.png').convert_alpha()
            self.class_power_small_off = pygame.image.load('sprite/pouvoir_guerrier_off.png').convert_alpha()
            self.class_power_big_off = pygame.image.load('sprite/pouvoir_guerrier1_off.png').convert_alpha()

        if classe == "voleur":
            self.hp = 15
            self.armor = 0
            self.class_number = 35
            self.deck = []
            self.hand = []
            self.image = voleur
            self.class_power_small = pygame.image.load('sprite/pouvoir_voleur.png').convert_alpha()
            self.class_power_big = pygame.image.load('sprite/pouvoir_voleur1.png').convert_alpha()
            self.class_power_small_off = pygame.image.load('sprite/pouvoir_voleur_off.png').convert_alpha()
            self.class_power_big_off = pygame.image.load('sprite/pouvoir_voleur1_off.png').convert_alpha()

        if classe == "mecanicien":
            self.hp = 10
            self.armor = 5
            self.class_number = 40
            self.deck = []
            self.hand = []
            self.image = mecanicien
            self.class_power_small = pygame.image.load('sprite/pouvoir_mecanicien.png').convert_alpha()
            self.class_power_big = pygame.image.load('sprite/pouvoir_mecanicien1.png').convert_alpha()
            self.class_power_small_off = pygame.image.load('sprite/pouvoir_mecanicien_off.png').convert_alpha()
            self.class_power_big_off = pygame.image.load('sprite/pouvoir_mecanicien1_off.png').convert_alpha()

        if classe == "pretre":
            self.hp = 15
            self.armor = 0
            self.class_number = 45
            self.deck = []
            self.hand = []
            self.image = pretre
            self.class_power_small = pygame.image.load('sprite/pouvoir_pretre.png').convert_alpha()
            self.class_power_big = pygame.image.load('sprite/pouvoir_pretre1.png').convert_alpha()
            self.class_power_small_off = pygame.image.load('sprite/pouvoir_pretre_off.png').convert_alpha()
            self.class_power_big_off = pygame.image.load('sprite/pouvoir_pretre1_off.png').convert_alpha()

    def create_deck(self, class_number):
        deck = []
        for i in range(25):
            deck.append(random.randint(0,24))
        for i in range(5):
            deck.append(class_number+i)
        return sorted(deck)
    
    def create_hand(self, deck):
        hand = []
        longueur = len(deck)-1
        for i in range(5):
            rand = random.randint(0,longueur)
            hand.append(deck.pop(rand))
            longueur -= 1
        return hand
