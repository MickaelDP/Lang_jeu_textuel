"""
 Nom ......... : parser.py
 Rôle ........ : règle grammatical sur l'utilisation des tokens
 Auteur ...... : D'après les instuctions sur l'usage de la librairie sly : https://sly.readthedocs.io/en/latest/ 
                 Mickaël D. Pernet
 Version ..... : 30/05/2022
 Licence ..... : chapître 10: interpretation et compilation - projet
"""

from sly import Lexer
from sly import Parser
from math import sqrt
from lexer import DLexer
from preprocessor import EN_Matrice, FR_Racinisation, PProcessor, Conform 
from game import game

class DParser(Parser):
    tokens = DLexer.tokens
    def __init__(self):
        self.env = {}
    @_('')
    def statement(self, p):
        pass
    # aide
    @_('AIDE')
    def statement(self, p):
        return('aide', 0)
    @_('expr AIDE')
    def statement(self, p):
        return('aide', 0)
    @_('AIDE expr')
    def statement(self, p):
        return('aide', 0)
    @_('expr AIDE expr')
    def statement(self, p):
        return('aide', 0)
    # se deplacer
    @_('ALL NORD')
    def statement(self, p):
        return('deplacement', 0, -int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 0)
    @_('ALL NORD expr')
    def statement(self, p):
        return('deplacement', 0, -int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 0)
    @_('expr ALL NORD')
    def statement(self, p):
        return('deplacement', 0, -int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 0)
    @_('expr ALL NORD expr')
    def statement(self, p):
        return('deplacement', 0, -int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 0)
    @_('ALL SUD')
    def statement(self, p):
         return('deplacement', 0, int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 2)
    @_('ALL SUD expr')
    def statement(self, p):
         return('deplacement', 0, int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 2)
    @_('expr ALL SUD')
    def statement(self, p):
         return('deplacement', 0, int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 2)
    @_('expr ALL SUD expr')
    def statement(self, p):
         return('deplacement', 0, int(sqrt(len(game.get("DMAP", {"vide:0"})[0]))), 2)
    @_('ALL EST')
    def statement(self, p):
        return('deplacement', 0, 1, 1)
    @_('ALL EST expr')
    def statement(self, p):
        return('deplacement', 0, 1, 1)
    @_('expr ALL EST')
    def statement(self, p):
        return('deplacement', 0, 1, 1)    
    @_('expr ALL EST expr')
    def statement(self, p):
        return('deplacement', 0, 1, 1)    
    @_('ALL OUEST')
    def statement(self, p):
        return('deplacement', 0, -1, 3)
    @_('ALL OUEST expr')
    def statement(self, p):
        return('deplacement', 0, -1, 3)
    @_('expr ALL OUEST')
    def statement(self, p):
        return('deplacement', 0, -1, 3)
    @_('expr ALL OUEST expr')
    def statement(self, p):
        return('deplacement', 0, -1, 3)
    @_('DESC')
    def statement(self, p):
        return('deplacement', -1, 0, 5)
    @_('DESC expr')
    def statement(self, p):
        return('deplacement', -1, 0, 5)
    @_('expr DESC')
    def statement(self, p):
        return('deplacement', -1, 0, 5)
    @_('expr DESC expr')
    def statement(self, p):
        return('deplacement', -1, 0, 5)
    @_('MONT')
    def statement(self, p):
        return('deplacement', 1, 0, 4)
    @_('MONT expr')
    def statement(self, p):
        return('deplacement', 1, 0, 4)
    @_('expr MONT')
    def statement(self, p):
        return('deplacement', 1, 0, 4)
    @_('expr MONT expr')
    def statement(self, p):
        return('deplacement', 1, 0, 4)
    # combattre
    @_('ATT PHRASE')
    def statement(self, p):
        return ('attaque', p.PHRASE)
    @_('ATT PHRASE expr')
    def statement(self, p):
        return ('attaque', p.PHRASE)
    @_('expr ATT PHRASE')
    def statement(self, p):
        return ('attaque', p.PHRASE)
    @_('expr ATT PHRASE expr')
    def statement(self, p):
        return ('attaque', p.PHRASE)
    @_('ATT MOT')
    def statement(self, p):
        return ('attaque', p.MOT)  
    @_('ATT MOT expr')
    def statement(self, p):
        return ('attaque', p.MOT)
    @_('expr ATT MOT')
    def statement(self, p):
        return ('attaque', p.MOT)  
    @_('expr ATT MOT expr')
    def statement(self, p):
        return ('attaque', p.MOT)  
    @_('ATT PHRASE AVEC PHRASE')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE0, p.PHRASE1)
    @_('ATT PHRASE AVEC PHRASE expr')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE0, p.PHRASE1) 
    @_('expr ATT PHRASE AVEC PHRASE')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE0, p.PHRASE1) 
    @_('expr ATT PHRASE AVEC PHRASE expr')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE0, p.PHRASE1) 
    @_('ATT MOT AVEC MOT')
    def statement(self, p):
        return ('attaque_avec', p.MOT0, p.MOT1)
    @_('ATT MOT AVEC MOT expr')
    def statement(self, p):
        return ('attaque_avec', p.MOT0, p.MOT1)
    @_('expr ATT MOT AVEC MOT')
    def statement(self, p):
        return ('attaque_avec', p.MOT0, p.MOT1)
    @_('expr ATT MOT AVEC MOT expr')
    def statement(self, p):
        return ('attaque_avec', p.MOT0, p.MOT1)
    @_('ATT PHRASE AVEC MOT')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE, p.MOT)
    @_('ATT PHRASE AVEC MOT expr')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE, p.MOT)
    @_('expr ATT PHRASE AVEC MOT')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE, p.MOT)
    @_('expr ATT PHRASE AVEC MOT expr')
    def statement(self, p):
        return ('attaque_avec', p.PHRASE, p.MOT)
    @_('ATT MOT AVEC PHRASE')
    def statement(self, p):
        return ('attaque_avec', p.MOT, p.PHRASE)
    @_('ATT MOT AVEC PHRASE expr')
    def statement(self, p):
        return ('attaque_avec', p.MOT, p.PHRASE)
    @_('expr ATT MOT AVEC PHRASE')
    def statement(self, p):
        return ('attaque_avec', p.MOT, p.PHRASE)
    @_('expr ATT MOT AVEC PHRASE expr')
    def statement(self, p):
        return ('attaque_avec', p.MOT, p.PHRASE)
    # interaction objets 
    @_('INV')
    def statement(self, p):
        return ('inventaire', 0) 
    @_('INV expr')
    def statement(self, p):
        return ('inventaire', 0)
    @_('expr INV')
    def statement(self, p):
        return ('inventaire', 0) 
    @_('expr INV expr')
    def statement(self, p):
        return ('inventaire', 0) 
    @_('VOIR INV')
    def statement(self, p):
        return ('inventaire', 0)
    @_('VOIR INV expr')
    def statement(self, p):
        return ('inventaire', 0)
    @_('expr VOIR INV')
    def statement(self, p):
        return ('inventaire', 0)
    @_('expr VOIR INV expr')
    def statement(self, p):
        return ('inventaire', 0)
    @_('VOIR PHRASE')
    def statement(self, p):
        return ('voir', p.PHRASE)
    @_('VOIR PHRASE expr')
    def statement(self, p):
        return ('voir', p.PHRASE) 
    @_('expr VOIR PHRASE')
    def statement(self, p):
        return ('voir', p.PHRASE) 
    @_('expr VOIR PHRASE expr')
    def statement(self, p):
        return ('voir', p.PHRASE) 
    @_('VOIR MOT')
    def statement(self, p):
        return ('voir', p.MOT)
    @_('VOIR MOT expr')
    def statement(self, p):
        return ('voir', p.MOT)
    @_('expr VOIR MOT')
    def statement(self, p):
        return ('voir', p.MOT)  
    @_('expr VOIR MOT expr')
    def statement(self, p):
        return ('voir', p.MOT) 
    @_('UTIL PHRASE')
    def statement(self, p):
        return ('utilise', p.PHRASE)
    @_('UTIL PHRASE expr')
    def statement(self, p):
        return ('utilise', p.PHRASE)
    @_('expr UTIL PHRASE')
    def statement(self, p):
        return ('utilise', p.PHRASE)
    @_('expr UTIL PHRASE expr')
    def statement(self, p):
        return ('utilise', p.PHRASE)
    @_('UTIL MOT')
    def statement(self, p):
        return ('utilise', p.MOT)
    @_('UTIL MOT expr')
    def statement(self, p):
        return ('utilise', p.MOT)
    @_('expr UTIL MOT')
    def statement(self, p):
        return ('utilise', p.MOT)
    @_('expr UTIL MOT expr')
    def statement(self, p):
        return ('utilise', p.MOT)     
    @_('UTIL PHRASE AVEC PHRASE')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE0, p.PHRASE1)
    @_('UTIL PHRASE AVEC PHRASE expr')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE0, p.PHRASE1)
    @_('expr UTIL PHRASE AVEC PHRASE')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE0, p.PHRASE1)
    @_('expr UTIL PHRASE AVEC PHRASE expr')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE0, p.PHRASE1)
    @_('UTIL PHRASE AVEC MOT')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE, p.MOT)
    @_('UTIL PHRASE AVEC MOT expr')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE, p.MOT)
    @_('expr UTIL PHRASE AVEC MOT')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE, p.MOT)
    @_('expr UTIL PHRASE AVEC MOT expr')
    def statement(self, p):
        return ('utilise_avec', p.PHRASE, p.MOT)
    @_('UTIL MOT AVEC MOT')
    def statement(self, p):
        return ('utilise_avec', p.MOT0, p.MOT1)
    @_('UTIL MOT AVEC MOT expr')
    def statement(self, p):
        return ('utilise_avec', p.MOT0, p.MOT1)   
    @_('expr UTIL MOT AVEC MOT')
    def statement(self, p):
        return ('utilise_avec', p.MOT0, p.MOT1)   
    @_('expr UTIL MOT AVEC MOT expr')
    def statement(self, p):
        return ('utilise_avec', p.MOT0, p.MOT1)  
    @_('UTIL MOT AVEC PHRASE')
    def statement(self, p):
        return ('utilise_avec', p.MOT, p.PHRASE)   
    @_('UTIL MOT AVEC PHRASE expr')
    def statement(self, p):
        return ('utilise_avec', p.MOT, p.PHRASE)  
    @_('expr UTIL MOT AVEC PHRASE')
    def statement(self, p):
        return ('utilise_avec', p.MOT, p.PHRASE) 
    @_('expr UTIL MOT AVEC PHRASE expr')
    def statement(self, p):
        return ('utilise_avec', p.MOT, p.PHRASE)              
    @_('PREN PHRASE')
    def statement(self, p):
        return ('prendre', p.PHRASE)
    @_('PREN PHRASE expr')
    def statement(self, p):
        return ('prendre', p.PHRASE) 
    @_('expr PREN PHRASE')
    def statement(self, p):
        return ('prendre', p.PHRASE)
    @_('expr PREN PHRASE expr')
    def statement(self, p):
        return ('prendre', p.PHRASE)  
    @_('PREN MOT')
    def statement(self, p):
        return ('prendre', p.MOT)
    @_('PREN MOT expr')
    def statement(self, p):
        return ('prendre', p.MOT)  
    @_('expr PREN MOT')
    def statement(self, p):
        return ('prendre', p.MOT)  
    @_('expr PREN MOT expr') 
    def statement(self, p):
        return ('prendre', p.MOT)  
    # Mode editeur:
    @_('NOUVEAU_JEU')
    def statement(self, p):
        return ('new', 0)
    @_('SET_ETAGE NOMBRE')
    def statement(self, p):
        return ('set_etage', p.NOMBRE)  
    @_('SET_PIECE NOMBRE')
    def statement(self, p):
        return ('set_piece', p.NOMBRE) 
    # DMAP: {game: {"DMAP": [[x, "name", [0,0,0,0,0,0]]]}
    @_('GENERER SET_DMAP NOMBRE NOMBRE')
    def statement(self, p):
        return ('dmap_cree', p.NOMBRE0, p.NOMBRE1)
    @_('SET_DMAP NOMBRE NOMBRE PHRASE NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE')
    def statement(self, p):
        return ('dmap_ajoute', p.NOMBRE0, p.NOMBRE1, p.PHRASE, p.NOMBRE2, p.NOMBRE3, p.NOMBRE4, p.NOMBRE5, p.NOMBRE6, p.NOMBRE7)
    @_('AFFICHER SET_DMAP NOMBRE NOMBRE')
    def statement(self, p):
        return ('dmap_show', p.NOMBRE0, p.NOMBRE1)
    # Combinaison combine: {game: {"combine": {"element1": {"element2": "element3"}}}}   
    @_('GENERER COMBINER MOT MOT MOT')
    def statement(self, p):
        return ('combine_cree', p.MOT0, p.MOT1, p.MOT2)
    @_('GENERER COMBINER PHRASE MOT MOT')
    def statement(self, p):
        return ('combine_cree', p.PHRASE, p.MOT0, p.MOT1)
    @_('GENERER COMBINER MOT PHRASE MOT')
    def statement(self, p):
        return ('combine_cree', p.MOT0, p.PHRASE, p.MOT1)
    @_('GENERER COMBINER MOT MOT PHRASE')
    def statement(self, p):
        return ('combine_cree', p.MOT0, p.MOT1, p.PHRASE)
    @_('GENERER COMBINER PHRASE PHRASE MOT')
    def statement(self, p):
        return ('combine_cree', p.PHRASE0, p.PHRASE1, p.MOT)
    @_('GENERER COMBINER PHRASE MOT PHRASE')
    def statement(self, p):
        return ('combine_cree', p.PHRASE0, p.MOT, p.PHRASE1)
    @_('GENERER COMBINER MOT PHRASE PHRASE')
    def statement(self, p):
        return ('combine_cree', p.MOT, p.PHRASE0, p.PHRASE1)
    @_('GENERER COMBINER PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('combine_cree', p.PHRASE0, p.PHRASE1, p.PHRASE2)
    @_('AJOUTER COMBINER MOT MOT MOT')
    def statement(self, p):
        return ('combine_ajoute', p.MOT0, p.MOT1, p.MOT2)
    @_('AJOUTER COMBINER PHRASE MOT MOT')
    def statement(self, p):
        return ('combine_ajoute', p.PHRASE, p.MOT0, p.MOT1)
    @_('AJOUTER COMBINER MOT PHRASE MOT')
    def statement(self, p):
        return ('combine_ajoute', p.MOT0, p.PHRASE, p.MOT1)
    @_('AJOUTER COMBINER MOT MOT PHRASE')
    def statement(self, p):
        return ('combine_ajoute', p.MOT0, p.MOT1, p.PHRASE)
    @_('AJOUTER COMBINER PHRASE PHRASE MOT')
    def statement(self, p):
        return ('combine_ajoute', p.PHRASE0, p.PHRASE1, p.MOT)
    @_('AJOUTER COMBINER PHRASE MOT PHRASE')
    def statement(self, p):
        return ('combine_ajoute', p.PHRASE0, p.MOT, p.PHRASE1)
    @_('AJOUTER COMBINER MOT PHRASE PHRASE')
    def statement(self, p):
        return ('combine_ajoute', p.MOT, p.PHRASE0, p.PHRASE1)
    @_('AJOUTER COMBINER PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('combine_ajoute', p.PHRASE0, p.PHRASE1, p.PHRASE2)
    @_('DETRUIRE COMBINER MOT')
    def statement(self, p):
        return ('combine_del', p.MOT)
    @_('DETRUIRE COMBINER PHRASE')
    def statement(self, p):
        return ('combine_del', p.PHRASE)
    # Combinaison damage: {game: {"damage": {"element1": "element2"}}}
    @_('GENERER DAMAGE_TABLE MOT NOMBRE')
    def statement(self, p):
        return ('damage_cree', p.MOT, p.NOMBRE)
    @_('GENERER DAMAGE_TABLE PHRASE NOMBRE')
    def statement(self, p):
        return ('damage_cree', p.PHRASE, p.NOMBRE)
    @_('AJOUTER DAMAGE_TABLE MOT NOMBRE')
    def statement(self, p):
        return ('damage_ajoute', p.MOT, p.NOMBRE)
    @_('AJOUTER DAMAGE_TABLE PHRASE NOMBRE')
    def statement(self, p):
        return ('damage_ajoute', p.PHRASE, p.NOMBRE)
    @_('DETRUIRE DAMAGE_TABLE MOT')
    def statement(self, p):
        return ('damage_del', p.MOT)
    @_('DETRUIRE DAMAGE_TABLE PHRASE')
    def statement(self, p):
        return ('damage_del', p.PHRASE)
    # description: {game: {"description": {"E1", "lambda: E2"}}}
    @_('GENERER SET_DESCRIPTION MOT PHRASE')
    def statement(self, p):
        return ('description_cree', p.MOT, p.PHRASE)
    @_('AJOUTER SET_DESCRIPTION MOT PHRASE')
    def statement(self, p):
        return ('description_ajoute', p.MOT, p.PHRASE)
    @_('DETRUIRE SET_DESCRIPTION MOT')
    def statement(self, p):
        return ('description_del', p.MOT)
    # inventaire de pièce: {"inventaire": {"piece": [objet, ind]}}
    @_('GENERER SET_INV MOT MOT NOMBRE')
    def statement(self, p):
        return ('inv_cree', p.MOT0, p.MOT1, p.NOMBRE)
    @_('GENERER SET_INV PHRASE MOT NOMBRE')
    def statement(self, p):
        return ('inv_cree', p.PHRASE, p.MOT, p.NOMBRE)
    @_('GENERER SET_INV MOT PHRASE NOMBRE')
    def statement(self, p):
        return ('inv_cree', p.MOT, p.PHRASE, p.NOMBRE)
    @_('GENERER SET_INV PHRASE PHRASE NOMBRE')
    def statement(self, p):
        return ('inv_cree', p.PHRASE0, p.PHRASE1, p.NOMBRE)
    @_('AJOUTER SET_INV MOT MOT NOMBRE') 
    def statement(self, p):
        return ('inv_add', p.MOT0, p.MOT1, p.NOMBRE)
    @_('AJOUTER SET_INV MOT PHRASE NOMBRE') 
    def statement(self, p):
        return ('inv_add', p.MOT, p.PHRASE, p.NOMBRE)
    @_('AJOUTER SET_INV PHRASE MOT NOMBRE') 
    def statement(self, p):
        return ('inv_add', p.PHRASE, p.MOT, p.NOMBRE)
    @_('AJOUTER SET_INV PHRASE PHRASE NOMBRE') 
    def statement(self, p):
        return ('inv_add', p.PHRASE0, p.PHRASE1, p.NOMBRE)
    @_('DETRUIRE SET_INV MOT MOT') 
    def statement(self, p):
        return ('inv_del', p.MOT0, p.MOT1)
    @_('DETRUIRE SET_INV PHRASE MOT') 
    def statement(self, p):
        return ('inv_del', p.PHRASE, p.MOT)
    @_('DETRUIRE SET_INV MOT PHRASE') 
    def statement(self, p):
        return ('inv_del', p.MOT, p.PHRASE)
    @_('DETRUIRE SET_INV PHRASE PHRASE') 
    def statement(self, p):
        return ('inv_del', p.PHRASE0, p.PHRASE1)
    # Personnage: {game: {"personnage": {"piece": {"perso":{"vie":5, "degats":5, "inv":[], "faible": "faiblesse"}}}}}
    @_('GENERER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.MOT2, p.MOT3)
    @_('GENERER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE, p.MOT0, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.MOT2)
    @_('GENERER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.PHRASE, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.MOT2)
    @_('GENERER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.PHRASE, p.MOT2)
    @_('GENERER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.MOT2, p.PHRASE)
    @_('GENERER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.MOT2)
    @_('GENERER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.MOT0, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.MOT1)
    @_('GENERER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.MOT0, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.PHRASE1)
    @_('GENERER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.PHRASE0, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.MOT1)
    @_('GENERER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.PHRASE0, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.PHRASE1)
    @_('GENERER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.PHRASE0, p.PHRASE1)
    @_('GENERER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.PHRASE2, p.MOT)
    @_('GENERER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.MOT, p.PHRASE2)
    @_('GENERER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.MOT, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.PHRASE2)
    @_('GENERER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.MOT, p.PHRASE0, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.PHRASE2)
    @_('GENERER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_cree', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.PHRASE2, p.PHRASE3)
    #Ajouter
    @_('AJOUTER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.MOT2, p.MOT3)
    @_('AJOUTER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_add', p.PHRASE, p.MOT0, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.MOT2)
    @_('AJOUTER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.PHRASE, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.MOT2)
    @_('AJOUTER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.PHRASE, p.MOT2)
    @_('AJOUTER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.MOT2, p.PHRASE)
    @_('AJOUTER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE MOT MOT')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.MOT2)
    @_('AJOUTER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.MOT0, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.MOT1)
    @_('AJOUTER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.MOT0, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.PHRASE1)
    @_('AJOUTER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.PHRASE0, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.MOT1)
    @_('AJOUTER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.PHRASE0, p.NOMBRE0, p.NOMBRE1, p.MOT1, p.PHRASE1)
    @_('AJOUTER SET_PERSONNAGE MOT MOT NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_add', p.MOT0, p.MOT1, p.NOMBRE0, p.NOMBRE1, p.PHRASE0, p.PHRASE1)
    @_('AJOUTER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE PHRASE MOT')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.PHRASE2, p.MOT)
    @_('AJOUTER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE MOT PHRASE')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.MOT, p.PHRASE2)
    @_('AJOUTER SET_PERSONNAGE PHRASE MOT NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.MOT, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.PHRASE2)
    @_('AJOUTER SET_PERSONNAGE MOT PHRASE NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_add', p.MOT, p.PHRASE0, p.NOMBRE0, p.NOMBRE1, p.PHRASE1, p.PHRASE2)
    @_('AJOUTER SET_PERSONNAGE PHRASE PHRASE NOMBRE NOMBRE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_add', p.PHRASE0, p.PHRASE1, p.NOMBRE0, p.NOMBRE1, p.PHRASE2, p.PHRASE3)
    @_('DETRUIRE SET_PERSONNAGE MOT MOT')
    def statement(self, p):
        return ('personnage_del', p.MOT0, p.MOT1)
    @_('DETRUIRE SET_PERSONNAGE PHRASE MOT')
    def statement(self, p):
        return ('personnage_del', p.PHRASE, p.MOT)
    @_('DETRUIRE SET_PERSONNAGE MOT PHRASE')
    def statement(self, p):
        return ('personnage_del', p.MOT, p.PHRASE)
    @_('DETRUIRE SET_PERSONNAGE PHRASE PHRASE')
    def statement(self, p):
        return ('personnage_del', p.PHRASE0, p.PHRASE1)
    #useCase {"game": {"useCase": {E1: {E2: "lambda: E3"}}}}
    @_('GENERER SET_USECASE MOT MOT PHRASE')
    def statement(self, p):
        return ('usecase_cree', p.MOT0, p.MOT1, p.PHRASE)
    @_('GENERER SET_USECASE PHRASE MOT PHRASE')
    def statement(self, p):
        return ('usecase_cree', p.PHRASE0, p.MOT, p.PHRASE)
    @_('GENERER SET_USECASE MOT PHRASE PHRASE')
    def statement(self, p):
        return ('usecase_cree', p.MOT, p.PHRASE0, p.PHRASE1)
    @_('GENERER SET_USECASE PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('usecase_cree', p.PHRASE0, p.PHRASE1, p.PHRASE2)
    @_('AJOUTER SET_USECASE MOT MOT PHRASE')
    def statement(self, p):
        return ('usecase_ajoute', p.MOT0, p.MOT1, p.PHRASE)
    @_('AJOUTER SET_USECASE PHRASE MOT PHRASE')
    def statement(self, p):
        return ('usecase_ajoute', p.PHRASE0, p.MOT, p.PHRASE)
    @_('AJOUTER SET_USECASE MOT PHRASE PHRASE')
    def statement(self, p):
        return ('usecase_ajoute', p.MOT, p.PHRASE0, p.PHRASE1)
    @_('AJOUTER SET_USECASE PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('usecase_ajoute', p.PHRASE0, p.PHRASE1, p.PHRASE2)
    @_('DETRUIRE SET_USECASE MOT')
    def statement(self, p):
        return ('usecase_del', p.MOT)
    @_('DETRUIRE SET_USECASE PHRASE')
    def statement(self, p):
        return ('usecase_del', p.PHRASE)
    # Special: {"game": {"special": {E1: {E2: {E3: "lambda: E4"}}}}}
    @_('GENERER SET_SPECIAL MOT MOT MOT PHRASE')
    def statement(self, p):
        return ('special_cree', p.MOT0, p.MOT1, p.MOT2, p.PHRASE)
    @_('GENERER SET_SPECIAL PHRASE MOT MOT PHRASE')
    def statement(self, p):
        return ('special_cree', p.PHRASE0, p.MOT0, p.MOT1, p.PHRASE1)
    @_('GENERER SET_SPECIAL MOT PHRASE MOT PHRASE')
    def statement(self, p):
        return ('special_cree', p.MOT0, p.PHRASE0, p.MOT1, p.PHRASE1)
    @_('GENERER SET_SPECIAL MOT MOT PHRASE PHRASE')
    def statement(self, p):
        return ('special_cree', p.MOT0, p.MOT1, p.PHRASE0, p.PHRASE1)
    @_('GENERER SET_SPECIAL PHRASE PHRASE MOT PHRASE')
    def statement(self, p):
        return ('special_cree', p.PHRASE0, p.PHRASE1, p.MOT, p.PHRASE2)
    @_('GENERER SET_SPECIAL PHRASE MOT PHRASE PHRASE')
    def statement(self, p):
        return ('special_cree', p.PHRASE0, p.MOT, p.PHRASE1, p.PHRASE0)
    @_('GENERER SET_SPECIAL MOT PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('special_cree', p.MOT, p.PHRASE0, p.PHRASE1, p.PHRASE2)
    @_('GENERER SET_SPECIAL PHRASE PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('special_cree', p.PHRASE0, p.PHRASE1, p.PHRASE2, p.PHRASE3)
    # ajoute
    @_('AJOUTER SET_SPECIAL MOT MOT MOT PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.MOT0, p.MOT1, p.MOT2, p.PHRASE)
    @_('AJOUTER SET_SPECIAL PHRASE MOT MOT PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.PHRASE0, p.MOT0, p.MOT1, p.PHRASE1)
    @_('AJOUTER SET_SPECIAL MOT PHRASE MOT PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.MOT0, p.PHRASE0, p.MOT1, p.PHRASE1)
    @_('AJOUTER SET_SPECIAL MOT MOT PHRASE PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.MOT0, p.MOT1, p.PHRASE0, p.PHRASE1)
    @_('AJOUTER SET_SPECIAL PHRASE PHRASE MOT PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.PHRASE0, p.PHRASE1, p.MOT, p.PHRASE2)
    @_('AJOUTER SET_SPECIAL PHRASE MOT PHRASE PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.PHRASE0, p.MOT, p.PHRASE1, p.PHRASE0)
    @_('AJOUTER SET_SPECIAL MOT PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.MOT, p.PHRASE0, p.PHRASE1, p.PHRASE2)
    @_('AJOUTER SET_SPECIAL PHRASE PHRASE PHRASE PHRASE')
    def statement(self, p):
        return ('special_ajoute', p.PHRASE0, p.PHRASE1, p.PHRASE2, p.PHRASE3)
    # del
    @_('DETRUIRE SET_SPECIAL MOT')
    def statement(self, p):
        return ('special_del', p.MOT)
    @_('DETRUIRE SET_SPECIAL PHRASE')
    def statement(self, p):
        return ('special_del', p.PHRASE)
    @_('GENERER SET_WELCOME PHRASE')
    def statement(self, p):
        return ('welcome', p.PHRASE)
    @_('QUIT')
    def statement(self, p):
        return ('exit', 0)
    @_('MOT')
    def expr(self, p):
        return ('var', p.MOT)
    @_('PHRASE')
    def expr(self, p):
        return ('pha', p.PHRASE)
    @_('expr')
    def statement(self, p):
        return (p.expr)
    @_('NOMBRE')
    def expr(self, p):
        return ('num', p.NOMBRE)
    @_('MOT PHRASE')
    def expr(self, p):
        return ('pha', p.MOT + " " + p.PHRASE)
    @_('PHRASE MOT')
    def expr(self, p):
        return ('pha', p.PHRASE + " " + p.MOT)
    @_('PHRASE PHRASE')
    def expr(self, p):
        return ('pha', p.PHRASE0 + " " + p.PHRASE1)
    @_('PHRASE PHRASE PHRASE')
    def expr(self, p):
        return ('pha', p.PHRASE0 + " " + p.PHRASE1 + " " + p.PHRASE2)
    @_('MOT MOT')
    def expr(self, p):
        return ('pha', p.MOT0 + " " + p.MOT1)
    @_('MOT MOT MOT')
    def expr(self, p):
        return ('pha', p.MOT0 + " " + p.MOT1 +  " " + p.MOT2)
    @_('PHRASE MOT MOT')
    def expr(self, p):
        return ('pha', p.PHRASE + " " + p.MOT0 +  " " + p.MOT1)
    @_('MOT PHRASE MOT')
    def expr(self, p):
        return ('pha', p.MOT0 + " " + p.PHRASE +  " " + p.MOT1)
    @_('MOT MOT PHRASE')
    def expr(self, p):
        return ('pha', p.MOT0 + " " + p.MOT1 +  " " + p.PHRASE)
    @_('PHRASE PHRASE MOT')
    def expr(self, p):
        return ('pha', p.PHRASE0 + " " + p.PHRASE1 +  " " + p.MOT)
    @_('PHRASE MOT PHRASE')
    def expr(self, p):
        return ('pha', p.PHRASE0 + " " + p.MOT +  " " + p.PHRASE1)
    @_('MOT PHRASE PHRASE')
    def expr(self, p):
        return ('pha', p.MOT + " " + p.PHRASE0 +  " " + p.PHRASE1)

"""TEST
"""
"""
if __name__ == '__main__':
    lexer = DLexer()
    parser = DParser()
    env = {}
    while True:
        try:
            text = input('Parser > ')
            text += " "
        except EOFError:
            break
        if text:
            print(text)
            tree = parser.parse(lexer.tokenize((PProcessor(text, EN_Matrice, FR_Racinisation)).replace("'", " ")))
            print(tree)
"""         