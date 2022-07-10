"""
 Nom ......... : preprocessor.py
 Rôle ........ : Données et fonctions pour faire office de processus de preprocesseur au minilangage afin de permettre une souplesse d'expression des commandes.
 Auteur ...... : Mickaël D. Pernet
 Version ..... : 29/05/2022
 Licence ..... : chapître 10: interpretation et compilation - projet

"""
from sly import Lexer
from lexer import DLexer
import re


"""
Exemple de table de correspondance pour la traduction en anglais
"""
EN_Matrice = [
              ['AIDE', 'HELP'],
              ['All', 'GO', 'GO TO'],
              ['ATT', 'ATTACK', 'HIT'],
              ['AVEC', 'WITH'],
              ['DESC', 'GO DOWN'],
              ['EQUIP', 'PUT'],
              ['EST', 'EAST'],
              ['INV', 'INVENTORY', 'BAG'],
              ['MONT', 'GO UPSTRAIRS', 'ASCEND'],
              ['NORD', 'NORTH'],
              ['OUEST', 'WEST'],
              ['PREN', 'TAKE', 'TO TAKE'],
              ['QUIT', 'EXIT'],
              ['SUD', 'SOUTH'],
              ['UTIL', 'USE', 'UTILIZE'],
              ['VOIR', 'LOOK', 'LOOK AT']
            ]


"""
Exemple de table de correspondance pour des expressions semblable, différentes conjugaisons etc.
"""
FR_Racinisation = [ 
                    ["AIDE", "AIDES"],
                    ["ALL", "ALLEZ", "ALLEZ A", "ALLEZ VERS", "VA", "VA A", "VA VERS", "ALLER", "ALLER A", "ALLER VERS"],
                    ["ATT", "ATTAQUE", "ATTAQUES", "ATTAQUER", "FRAPPE", "TAPE", "FRAPPER", "TAPER"],
                    ["DESC", "DESCENDRE", "DESCEND"],
                    ["EQUIP", "EQUIPE", "EQUIPES", "EQUIPER"],
                    ["EST", "L'EST", "LEST", "L’EST"],
                    ["INV", "INVENTAIRE", "SAC"],
                    ["MONT", "MONTE", "MONTER"],
                    ["NORD", "LE NORD", "AU NORD"],
                    ["OUEST", "L'OUEST", "LOUEST", "L’OUEST"],
                    ["PREN", "PREND", "PRENDS", "PRENDRE", "RAMASSE", "RAMASSER"],
                    ["QUIT", "QUITTER"],
                    ["SUD", "LE SUD", "AU SUD"],
                    ["UTIL", "UTILISE", "UTILISES", "UTILISER"],
                    ["VOIR", "VOIR", "REGARDE", "REGARDES", "REGARDER", "REGARDEZ"],
                  ] 


def PProcessor(string, lexique, racine):
    """PPprocesseur agit comme un pré-processeur en remplaçant des expressions conjuguées en français ou en langue étrangère par leur équivalent dans la grammaire du langage développée
    Args:
        string (string): Ligne d'instructions
        lexique (matrice): matrice de correspondance multilangue
        racine (matrice): matrice de correspondance de token racinisé
    Returns:
        string: instructions compréhensibles par le parser
    """
    # REMPLACE PAR DU FRANCAIS
    result = Conform(string, lexique)
    # REMPLACE PAR LES TOKENS RACINISES
    result = Conform(result, racine)
    return result


def Conform(string, lexique):
    """Conform parcours une chaîne de caractère pour remplacé des expressions types par celles désirées
    Args:
        string (_type_): _description_
        lexique (_type_): _description_
    Returns:
        _type_: _description_
    """
    result = ""
    c = string.split(" ")
    p = len(c)
    offset = 0
    while(p > 0):
        # Calcul du nombre de mot maximum a verifier 8 ou moins
        MAX = 8
        if((len(c)-offset) < 8):
            MAX = len(c) - offset
        # Calcul du nombre de mot clés fonctions max 8
        wRange = MAX
        # reconstruction et remplacement des expressions
        if wRange > 0:
            while wRange > 0:
                test = ""
                for i in range(wRange):
                    if len(test) == 0:
                        test = c[-1-i-offset] 
                    else:
                        test = c[-1-i-offset] + " " + test     
                for line in lexique:
                    if test.upper() in line:
                        p -= wRange
                        offset += wRange
                        result = line[0] + " " + result
                        wRange = 0
                if wRange == 1:
                    p -= 1
                    offset += 1
                    result = test + " " + result
                    wRange = 0
                else:
                    wRange -= 1
        else:
            result = c[-1-offset] + " " + result
            p -= 1
            offset += 1
    #return result[:-1]
    return noAccent(result[:-1])

def noAccent(string):
    raw = re.sub(u"[àáâãäå]", 'a', string)
    raw = re.sub(u"[èéêë]", 'e', raw)
    raw = re.sub(u"[ìíîï]", 'i', raw)
    raw = re.sub(u"[òóôõö]", 'o', raw)
    raw = re.sub(u"[ùúûü]", 'u', raw)
    # on retire également les éventuelles caractère illégaux que le parser ne supporte pas:    
    raw = re.sub(u"^'", "", raw)
    raw.replace("'",'’')
    # Un nombre de " impaire provoque des problémes:
    if raw.count('"') % 2 != 0:
        raw = (' ').join(raw.rspplit('"', 1))
    return raw
        

"""TEST
    test les résultats de la combinaisons du preprocesseur et du lexer:
"""
"""
if __name__ == '__main__':
    lexer = DLexer()
    env = {}
    while True:
        try:
            text = input('PProcessor > ')
        except EOFError:
            break
        if text:
            text = PProcessor(text, EN_Matrice, FR_Racinisation)
            print(text)
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
"""
