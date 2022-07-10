"""
 Nom ......... : lexer.py
 Rôle ........ : Classe pour tokeniser les instructions données au sein du minilangage dédié pour le jeu textuel
 Auteur ...... : D'après les instuctions sur l'usage de la librairie sly : https://sly.readthedocs.io/en/latest/
                 Mickaël D. Pernet
 Version ..... : 29/05/2022
 Licence ..... : chapître 10: interpretation et compilation - projet
"""
from sly import Lexer

class DLexer(Lexer):
    """class Lexer pour tokenisé une commande live en français avec une étape de preprocessing pour permettre l'usage en anglais
    Args:
        Lexer (lexer): lexer de la lib sly

    Returns:
        list: liste d'objets 'tokens' déterminée en fonctions des paramètres
    """
    # liste des tokens 
    tokens = { AIDE, ALL, ATT, AVEC, DESC, EST, INV, MONT, MOT, NOMBRE, NORD, OUEST, PREN, PHRASE, SUD, UTIL, VOIR, NOUVEAU_JEU, GENERER, AFFICHER, AJOUTER, DETRUIRE, COMBINER, DAMAGE_TABLE, SET_DESCRIPTION, SET_DMAP, SET_ETAGE, SET_INV, SET_PIECE, SET_PERSONNAGE, SET_SPECIAL, SET_USECASE, SET_WELCOME, QUIT}
    ignore = '\t '
    # Definition des tokens
    AIDE = r"AIDE"
    ALL = r'ALL'
    ATT = r'ATT'
    AVEC = r'AVEC'
    DESC = r'DESC'
    EST = r'EST'
    INV = r'INV'
    MONT = r'MONT'
    NORD = r'NORD'
    OUEST = r'OUEST'
    PREN = r'PREN'
    SUD = r'SUD'
    UTIL = r'UTIL'
    VOIR = r'VOIR'
    NOUVEAU_JEU = r"NOUVEAU_JEU"
    GENERER = r'GENERER'
    AFFICHER = r'AFFICHER'
    AJOUTER = r'AJOUTER'
    DETRUIRE = r'DETRUIRE'
    COMBINER = r'COMBINER'
    DAMAGE_TABLE = r'DAMAGE_TABLE'
    SET_DESCRIPTION = r'SET_DESCRIPTION'
    SET_DMAP = r'SET_DMAP'
    SET_ETAGE = r'SET_ETAGE'
    SET_INV = r'SET_INV'
    SET_PIECE = r'SET_PIECE'
    SET_PERSONNAGE = r'SET_PERSONNAGE'
    SET_SPECIAL = r'SET_SPECIAL'
    SET_USECASE = r'SET_USECASE'
    SET_WELCOME = r'SET_WELCOME'
    QUIT = r'QUIT'
    MOT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    PHRASE = r'\".*?\"'
    # Definition de types
    @_(r'\d+')
    def NOMBRE(self, t):
        t.value = int(t.value)
        return t
    @_(r'#.*')
    def COMMENT(self, t):
        pass
    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

"""
test si lancé depuis ce fichier de la tokeninsation:
"""
"""
if __name__ == '__main__':
    lexer = DLexer()
    env = {}
    while True:
        try:
            text = input('Lexer > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
"""
