"""
 Nom ......... : interpreter.py
 Rôle ........ : Surcouche d'interpretation pour faire le lien avec l'utilisateur et les différentes étapes 
                 et sa fonction de lancement
 Auteur ...... : Mickaël D. Pernet
 Version ..... : 30/05/2022
 Licence ..... : chapître 10: interpretation et compilation - projet
"""

from sly import Lexer
from sly import Parser
from math import sqrt
from lexer import DLexer
from preprocessor import EN_Matrice, FR_Racinisation, PProcessor, Conform 
from game import game as imp_game
from game import combine, description, hero_damage, hero_inventaire, piece_inventaire, pnj, position, special, styleFormat, use
from parser import DParser

game = imp_game.copy()


def launcher(game):
    lexer = DLexer()
    parser = DParser()
    introduction = game["welcome"][:-2] + description(position()[1])() + """\n\n`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"""
    print(introduction)
    while game["current"]["RUN"]:
        try:
            text = input('Manoir > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize((PProcessor(text, EN_Matrice, FR_Racinisation)).replace("'", " ")))
            #print(tree) #debug
            game = Exec(tree, game)


def Exec(tree, game):
    """
    Exec: 
        fonction qui reçoit les arbres à partir de la grammaire et applique les actions nécessaires.
    Args:
        tree(arbre): arbre d'instruction
    Returns:
        string: résultat
    """
    if tree is None:
        result = None
    elif tree[0] == 'aide':
        result = styleFormat("""
AIDE DES DIFFERENTES ACTIONS POSSIBLES: 
Aide                                    aide
Se deplacer                             allez/va au/à <direction> (nord, surd, est, ouest)
Attaquer                                attaquer <cible>
                                        attaquer <cible> avec <objet>
Prendre                                 prendre <objet>
Utiliser                                utiliser <objet>
                                        utiliser <objet> avec <élément>
Regarder                                regarder <objet>
Afficher son inventaire                 inventaire
Quitter                                 sortir du jeu
note: les "objets" en plusieurs mots doivent obligatoirement être entre guillemet "" les autres non.
""")
    elif tree[0] == 'attaque':
        if pnj(position()[1], str(tree[1].replace('"',''))):
            game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] -= hero_damage()
            if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"]  > 0:
                deg_riposte = game["personnage"][position()[1]][str(tree[1].replace('"',''))]["degats"]
                game["hero"]["VIE_PERSONNAGE"] -= deg_riposte
            result = styleFormat(f"""
Vous attaquez {tree[1]} et lui infligez {hero_damage()} dégats""" + (f' et {tree[1]} tombe inanimé.' if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"]  <= 0 else '.') + '\n' + (f'{tree[1]} riposte et vous inflige {deg_riposte} dégats' if  game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] > 0 else '') + (f' et il vous reste {game["hero"]["VIE_PERSONNAGE"]} points de vie.' if game["hero"]["VIE_PERSONNAGE"] > 0 else ' et vous êtes mort') + '.\n')
            if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] <= 0:
                del game['personnage'][position()[1]][str(tree[1].replace('"',''))]
                position()[2] = [1 if e == 2 else e for e in position()[2]]
            # fin de partie
            if game["hero"]["VIE_PERSONNAGE"] <= 0:
                game["current"]["RUN"] = 0
        else:
            result =  styleFormat(f"""
{tree[1]} ne se trouve pas dans {position()[1]}
""")
    # attaque avec un objet 
    elif tree[0] == 'attaque_avec':
        if game["damage"].get(str(tree[2].replace('"','')), 0) > 0: 
            if pnj(position()[1], str(tree[1].replace('"',''))):
                game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] -= game["damage"][str(tree[2].replace('"',''))] 
                if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] > 0:
                    deg_riposte = game["personnage"][position()[1]][str(tree[1].replace('"',''))]["degats"]
                    game["hero"]["VIE_PERSONNAGE"] -= deg_riposte
                result =  styleFormat(f"""
Vous attaquez {tree[1]} et lui infligez {game["damage"][str(tree[2].replace('"',''))]} dégats""" + (f' et {tree[1]} tombe inanimé.' if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"]  <= 0 else '.') + '\n' + (f'{tree[1]} riposte et vous inflige {deg_riposte} dégats' if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] > 0 else '') + (f' et il vous reste {game["hero"]["VIE_PERSONNAGE"]} points de vie.' if game["hero"]["VIE_PERSONNAGE"] > 0 else ' et vous êtes mort') + '.\n') 
                if game["personnage"][position()[1]][str(tree[1].replace('"',''))]["vie"] <= 0:
                    del game['personnage'][position()[1]][str(tree[1].replace('"',''))]
                    position()[2] = [1 if e == 2 else e for e in position()[2]]
                # fin de partie 
                if game["hero"]["VIE_PERSONNAGE"] <= 0:
                    game["current"]["RUN"] = 0
            else:
                result = styleFormat(f"""       
{tree[1]} ne se trouve pas dans {position()[1]}
""")
        else:
            result = styleFormat(f"""
Il ne semble pas possible d'utiliser {tree[2]} pour ce genre d'action
""")
    #('deplacement', ModifETAGE, ModifPIECE, direction <0: nord, 1: est, 2: sud, 3: ouest, 4: haut, 5:bas)
    elif tree[0] == 'deplacement':
        if position()[2][tree[3]] == 0:
            result = styleFormat(f"""
Il n'y a pas d'issue dans cette direction depuis {position()[1]}
""")
        elif position()[2][tree[3]] == 1: 
            if (game['current']['ETAGE']+tree[1]<0 or game['current']['ETAGE']+tree[1]>len(game['current'])) or (game["current"]["PIECE"]+tree[2]<0 or game["current"]["PIECE"]+tree[2]>len(game["DMAP"][game["current"]["ETAGE"]])):
                game["current"]["RUN"] = 0
                result = styleFormat(f"""
Vous vous êtes échappé du manoir!
""")
            else: 
                game["current"]["ETAGE"] += tree[1]
                game["current"]["PIECE"] += tree[2]
                result = styleFormat(f"""
{description(position()[1])()}
""")
        else: 
            result = styleFormat(f"""
{game["special"][position()[1]]["special"]()}
""")
    elif tree[0] == 'inventaire':
        result = ""
        if len(hero_inventaire())== 0:
            result = styleFormat(f"""
Inventaire vide
""")
        for e in hero_inventaire():
            if result == "":
                result += "Inventaire:\n" + " - " + e + "\n"
            else:
                result += " - " + e + "\n"
        result = styleFormat(f"""
{result}
""") 
    elif tree[0] == 'pha' or tree[0] == 'var':
        result = None
    elif tree[0] == 'prendre':
        inv = piece_inventaire(position()[1])
        if str(tree[1].replace('"', '')) in inv and inv[inv.index(str(tree[1].replace('"', '')))+1] == 1:
            hero_inventaire().append(str(tree[1].replace('"', '')))    
            piece_inventaire(position()[1]).remove(piece_inventaire(position()[1])[piece_inventaire(position()[1]).index(str(tree[1].replace('"','')))+1])
            piece_inventaire(position()[1]).remove(str(tree[1].replace('"','')))
            result = styleFormat(f"""
Vous ramassez {tree[1]}!
""")
        elif str(tree[1].replace('"', '')) in inv:
            result = styleFormat(f"""
Impossible de prendre {str(tree[1].replace('"', ''))} !\n
""")
        else:
            result = styleFormat(f"""
Il n'y a pas de {tree[1]} à ramasser.
""")
    elif tree[0] == 'utilise':
        result = ""
        if str(tree[1].replace('"','')) in hero_inventaire():
            result = use(str(tree[1].replace('"','')), "seul")()
        elif str(tree[1].replace('"', '')) in piece_inventaire(position()[1]):
            result = special(position()[1], "util", str(tree[1].replace('"','')))()
        if result:
            result = styleFormat(f"""
{result}
""")
        else:
            result = styleFormat(f"""           
vous ne possédez pas {str(tree[1])}
""")
    elif tree[0] == 'utilise_avec':
        if str(tree[1].replace('"','')) in hero_inventaire() and (str(tree[2].replace('"','')) in hero_inventaire() or (str(tree[2].replace('"','')) in piece_inventaire(position()[1]) and piece_inventaire(position()[1])[piece_inventaire(position()[1]).index(str(tree[2].replace('"','')))+1] == 1)):
            new = combine(str(tree[1].replace('"','')), str(tree[2].replace('"','')))
            if new:
                hero_inventaire().remove(str(tree[1].replace('"','')))
                if tree[2].replace('"','') in hero_inventaire():
                    hero_inventaire().remove(str(tree[2].replace('"','')))
                else:
                    piece_inventaire(position()[1]).remove(tree[2].replace('"', ""))
                hero_inventaire().append(new)
                result = styleFormat(f"""
{use(str(tree[1].replace('"','')), str(tree[2].replace('"','')))()}
""")
            else:
                result = styleFormat(f"""
Impossible d'utiliser ensemble {tree[1]} et {tree[2]}.
""")
        elif str(tree[1].replace('"','')) in hero_inventaire() and (str(tree[2].replace('"','')) in piece_inventaire(position()[1]) and piece_inventaire(position()[1])[piece_inventaire(position()[1]).index(str(tree[2].replace('"','')))+1] == 2):
            new = combine(str(tree[1].replace('"','')), str(tree[2].replace('"','')))
            if new:
                hero_inventaire().remove(str(tree[1].replace('"','')))
                index = piece_inventaire(position()[1]).index(str(tree[2].replace('"', "")))
                del piece_inventaire(position()[1])[index+1]
                del piece_inventaire(position()[1])[index]
                piece_inventaire(position()[1]).append(new)
                piece_inventaire(position()[1]).append(0)
                position()[2] = [1 if e == 2 else e for e in position()[2]]
                result = styleFormat(f"""
{use(str(tree[1].replace('"','')), str(tree[2].replace('"','')))()}
""")
            else:
                result = styleFormat(f"""
Impossible d'utiliser ensemble {tree[1]} et {tree[2]}.
""")
        elif str(tree[1].replace('"','')) in hero_inventaire() and (str(tree[2].replace('"','')) in piece_inventaire(position()[1]) and piece_inventaire(position()[1])[piece_inventaire(position()[1]).index(str(tree[2].replace('"','')))+1]== 3):
            if pnj(position()[1], str(tree[2].replace('"','')))["faible"] == str(tree[1].replace("'",'')):
                new = combine(str(tree[1].replace('"','')), str(tree[2].replace('"','')))
                index = piece_inventaire(position()[1]).index(str(tree[2].replace('"', "")))
                del piece_inventaire(position()[1])[index+1]
                del piece_inventaire(position()[1])[index]
                del game['personnage'][position()[1]][str(tree[2].replace('"',''))]
                hero_inventaire().remove(str(tree[1].replace('"','')))
                piece_inventaire(position()[1]).append(new)
                piece_inventaire(position()[1]).append(0)
                position()[2] = [1 if e == 2 else e for e in position()[2]]
                result = styleFormat(f"""
{use(str(tree[1].replace('"','')), str(tree[2].replace('"','')))()}
""")
            else:
                result = styleFormat(f"""
Impossible d'utiliser ensemble {tree[1]} et {tree[2]}.
""")
        elif not tree[1].replace('"', '') in hero_inventaire():
            result = styleFormat(f"""  
Vous ne possedez pas {tree[1]}."
""")
        else:
            result = styleFormat(f""" 
Il n'y a pas de {tree[2]} ici.
""")
    elif tree[0] == 'voir':
        result = special(position()[1], "voir", str(tree[1].replace('"','')))()
        if not result:
            result = styleFormat(f"""          
Il n'y a rien de spécial à propos de {str(tree[1])}"
""")
        else: result = styleFormat(f""" 
{result}
""")
    # commande pour mode éditeur:
    elif tree[0] == 'new':
        game = {
                "current":  {
                                "RUN": 1,
                                "ETAGE": 0,
                                "PIECE": 0, },
                "hero":     {
                                "VIE_PERSONNAGE": 10,
                                "INV_PERSONNAGE": [],
                                "DEGAT_PERSONNAGE": 1, },
                "mode":    1
        }
        result = styleFormat(f"""          
Mode édition:
""")
    elif tree[0] == 'set_etage':
        game["current"]["ETAGE"] = tree[1]
        result = game["current"]["ETAGE"]
    elif tree[0] == 'set_piece':
        game["current"]["PIECE"] = tree[1] 
        result = game["current"]["PIECE"] 
    elif tree[0] == 'dmap_cree':
        game["DMAP"] = [[x for x in range(tree[2])] for y in range(tree[1])]
        result = game["DMAP"]
    elif tree[0] == 'dmap_ajoute':
        game["DMAP"][tree[1]][tree[2]] =[tree[2], str(tree[3].replace('"','')), [tree[4],tree[5],tree[6],tree[7],tree[8],tree[9]]]
        result = game["DMAP"][tree[1]][tree[2]]
    elif tree[0] == 'dmap_show':
        result = game["DMAP"][tree[1]][tree[2]]
    elif tree[0] == 'combine_cree':
        game["combine"] = {str(tree[1].replace('"','')): {str(tree[2].replace('"','')): str(tree[3].replace('"',''))}}
        result = game["combine"]
    elif tree[0] == 'combine_ajoute':
        game["combine"][str(tree[1].replace('"',''))] =  {str(tree[2].replace('"','')): str(tree[3].replace('"',''))}
        result = game["combine"]
    elif tree[0] == 'combine_del':
        del game["combine"][str(tree[1].replace('"',''))]
        result = game["combine"]
    elif tree[0] == 'damage_cree':
        game["damage"] = {str(tree[1].replace('"','')): tree[2]}
        result = game["damage"]
    elif tree[0] == 'damage_ajoute':
        game["damage"][str(tree[1].replace('"',''))] = tree[2]
        result = game["damage"]
    elif tree[0] == 'damage_del':
        del game["damage"][str(tree[1].replace('"',''))]
        result = game["damage"]
    elif tree[0] == 'description_cree':
        game["description"] = {str(tree[1].replace('"','')): eval(str(tree[2].replace('"','')))}
        result = game["description"]
    elif tree[0] == 'description_ajoute':
        game["description"][str(tree[1].replace('"',''))] = eval(str(tree[2].replace('"','')))
        result = game["description"]
    elif tree[0] == 'description_del':
        del game["description"][str(tree[1].replace('"',''))]
        result = game["description"]
    elif tree[0] == 'inv_cree':
        game["inventaire"] = {str(tree[1].replace('"','')): [str(tree[2].replace('"','')), tree[3]]}
        result = game["inventaire"]
    elif tree[0] == 'inv_add':
        if game["inventaire"].get(str(tree[1].replace('"','')), 0):
            game["inventaire"][str(tree[1].replace('"',''))].append(str(tree[2].replace('"',''))) 
            game["inventaire"][str(tree[1].replace('"',''))].append(tree[3]) 
        else:
            game["inventaire"][str(tree[1].replace('"',''))] = [str(tree[2].replace('"','')), tree[3]]
        result = game["inventaire"]
    elif tree[0] == 'inv_del':
        if game["inventaire"].get(str(tree[1].replace('"','')), 0) and type(game["inventaire"][str(tree[1].replace('"',''))]) == list:  
            index = game["inventaire"][str(tree[1].replace('"',''))].index(str(tree[2].replace('"','')))
            del game["inventaire"][str(tree[1].replace('"',''))][index+1]
            del game["inventaire"][str(tree[1].replace('"',''))][index]
            result = game["inventaire"]
        else:
            result = f"""{str(tree[1].replace('"',''))} n'est pas dans inventaire"""
    elif tree[0] == 'personnage_cree':
        game["personnage"] = {str(tree[1].replace('"','')): {str(tree[2].replace('"','')): {"vie":tree[3], "degats":tree[4], "inv": [str(tree[5].replace('"',''))], "faible": str(tree[6].replace('"',''))}}}
        result = game["personnage"]
    elif tree[0] == 'personnage_add':
        if game["personnage"].get(str(tree[1].replace('"','')), 0):
            game["personnage"][str(tree[1].replace('"',''))][str(tree[2].replace('"',''))] = {"vie":tree[3], "degats":tree[4], "inv": [str(tree[5].replace('"',''))], "faible": str(tree[6].replace('"',''))}
        else: 
            game["personnage"][str(tree[1].replace('"',''))] = {str(tree[2].replace('"','')): {"vie":tree[3], "degats":tree[4], "inv": [str(tree[5].replace('"',''))], "faible": str(tree[6].replace('"',''))}}
        result = game["personnage"]
    elif tree[0] == 'personnage_del':
        if game["personnage"].get(str(tree[1].replace('"', '')), {"vide": 0}).get(str(tree[2].replace('"','')), 0):
            del game["personnage"][str(tree[1].replace('"', ''))][str(tree[2].replace('"',''))]
            result = game["personnage"]
        else:
            print(game["personnage"][str(tree[1].replace('"', ''))])
            result = f"""Il n'y a pas de personnage {str(tree[2].replace('"',''))} dans {str(tree[1].replace('"', ''))}"""
    elif tree[0] == 'usecase_cree':
        game["useCase"] = {str(tree[1].replace('"','')): {str(tree[2].replace('"','')): eval(str(tree[3].replace('"','')))}}
        result = game["useCase"]
    elif tree[0] == 'usecase_ajoute':
        game["useCase"][str(tree[1].replace('"',''))] = {str(tree[2].replace('"','')): eval(str(tree[3].replace('"','')))}
        result = game["useCase"]
    elif tree[0] == 'usecase_del':
        del game["useCase"][str(tree[1].replace('"',''))]
        result = game["useCase"]
    elif tree[0] == 'special_cree':
        game["special"] = {str(tree[1].replace('"','')): {str(tree[2].replace('"','')): {str(tree[3].replace('"','')): eval(str(tree[4].replace('"','')))}}}
        result = game["special"]
    elif tree[0] == 'special_ajoute':
        game["special"][str(tree[1].replace('"',''))] = {str(tree[2].replace('"','')): {str(tree[3].replace('"','')): eval(str(tree[4].replace('"','')))}}
        result = game["special"]
    elif tree[0] == 'special_del':
        del game["special"][str(tree[1].replace('"',''))]
        result = game["special"]
    elif tree[0] == 'welcome':
        game["welcome"] = str(tree[1].replace('"',''))
        result = game["welcome"]
    elif tree[0] == 'exit':
        game["current"]["RUN"] = 0
        result = "A bientôt!"
    elif isinstance(tree, str):
        result = tree
    else:
        pass
    #resultat final 
    if not result:
        result = None   
    if result is not None:
        print(result)
    return game

