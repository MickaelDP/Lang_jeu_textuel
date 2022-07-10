"""
 Nom ......... : game.py
 Rôle ........ : structure en dictionnaire regroupant les informations à un jeu complet et fonctions auxiliaires d'accès et modifications.
 Auteur ...... : Mickaël D. Pernet
 Version ..... : 29/05/2022
 Licence ..... : chapître 10: interpretation et compilation - projet
"""

"""
note:    
    DMAP:
        matrice ou chaque ligne représente un étage et chaque sous liste une pièce:
        [<numéro de pièce>, <clé>, <sortie Nord, Est, Sud, Ouest, Haut, bas (0=non, 1=oui ouvert, 2=oui spécial)>]
        note: utiliser le caractère ’ et non '.
"""
game = {
        "combine": {
            "rondins": {
                       "echelle cassee": "échelle"
            },
            "verre": {
                        "wiskey": "verre de wiskey"
            },
            "wiskey": {
                        "verre": "verre de wiskey"
            },
            "verre de wiskey": {
                        "buldog": "buldog endormis"
            },
            "clef en fer": {
                        "porte de fer": "porte ouverte"
            },
            "clef en argent": {
                        "porte en argent": "porte ouverte"
            },
            "hache": {
                   "arbustes": "rondins"
            },
            "coffret a code": {
                   "codes": "clef en argent"
            } },
        "current": {
            "RUN": 1,
            "ETAGE": 1,
            "PIECE": 6, },
        "damage": {
            "saucissons": 2 },
        "DMAP": [
            [ [0, "l’escalier vers le haut", [0,1,0,0,1,0]], [1, "salle à manger nord"     , [0,2,1,1,0,0]], [2, "la cuisine"          , [0,0,0,1,0,0]],   # rez de chaussée
              [3, "accés nord"             , [0,1,1,0,0,0]], [4, "salle à manger sud"      , [1,0,0,1,0,0]], [5, "La serre nord"       , [0,0,1,0,0,0]],
              [6, "accés sud"              , [1,1,0,0,0,0]], [7, "Hall d’entrée"           , [0,1,2,1,0,0]], [8, "La serre sud"        , [1,0,0,1,0,0]] ],
            [ [0, "l’escalier vers le bas" , [0,1,0,0,0,1]], [1, "le hall du premier étage", [0,2,1,2,0,0]], [2, "la chambre du maitre", [0,0,1,1,0,0]],   # 1er étage
              [3, "le bureau"              , [0,1,0,0,0,0]], [4, "le couloir nord"         , [1,0,1,1,2,0]], [5, "le lit du maitre"    , [1,0,0,0,0,0]],
              [6, "la chambre d’ami"       , [0,1,0,0,0,0]], [7, "le couloir sud"          , [1,1,0,1,0,0]], [8, "la réserve"          , [0,0,0,1,0,0]] ],
            [ ['X'], ['X']                                  , ['X'],                                                                                       # Second étage
              ['X'], [4, "L’observatoire"  , [0,0,0,0,0,1]] , ['X'],
              ['X'], ['X']                                  , ['X'] ]  ],
        "description": { #Utilisation de lambda pour de la  "lazy evaluation":
                # ETAGE 0 PIECE 0:
                "l’escalier vers le haut": lambda:"Un escalier en colimaçon de marbre blanc et poli permettant d'accéder à l'étage supérieur, il mène vers une salle à manger à l'est",
                # ETAGE 0 PIECE 1:
                "salle à manger nord": lambda:"Une salle à manger se poursuivant sur le sud, cette partie et le bout de la table réserver au maitre de maison. Il y a également un [buffet] contre le mur. Un escalier vers l'étage supérieur à l'ouest et une [porte de fer] à l'est.", 
                # ETAGE 0 PIECE 2:
                "la cuisine": lambda:f"""Vous pénetrez dans une pièce avec un grand [âtre] éteind contenant une énormem marmite, des ustensiles de cuisines{', un [couteau]' if 'couteau' in piece_inventaire(position()[1]) else ''}{' et même une [hache]' if 'hache' in piece_inventaire(position()[1]) else ''}.""",
                # ETAGE 0 PIECE 3:
                "accés nord": lambda:"Vous accédez à un long corridor avec une [baie vitrée] remplaçant le mur ouest et des [tableaux] et une porte ornant le mur est, il se prolonge vers le sud.",
                # ETAGE 0 PIECE 4:
                "salle à manger sud": lambda:"Vous longez une table de réception longue de plusieurs mètres entourée de chaises lourdes en bois, au nord la place en bout de table de maitre de maison, dans la partie sud une porte sur le mur ouest.",
                # ETAGE 0 PIECE 5:
                "La serre nord": lambda:"Vous arrivez au fond de la serre qui est beaucoup plus sauvage que la partie sud, ici nombre de petits arbres et [arbustes] poussent à leur guise.", 
                # ETAGE 0 PIECE 6:
                "accés sud": lambda:"Un long corridor avec sur le mur est une [baie vitrée], sur le mur est une porte et il se prolonge vers le nord.",
                # ETAGE 0 PIECE 7:
                "Hall d’entrée": lambda:"Un hall d'entrée dallé de pierre compétement vide à l'exception des accès est et ouest, et d'une [porte en argent] au sud",
                # ETAGE 0 PIECE 8:
                "La serre sud": lambda:"Vous vous trouvez dans une sorte de serre relié au hall d'entrée par une petite porte à l'ouest et qui se prolonge au nord, ici des [fleurs] sont disposées esthétiquement de manière à produire des formes géométriques.", 
                # ETAGE 1 PIECE 0:
                "l’escalier vers le bas": lambda:"Un escalier en colimaçon de marbre blanc et poli permettant d'accéder à l'étage inférieur, il mène vers une sorte de hall à l'est.",
                # ETAGE 1 PIECE 1:
                "le hall du premier étage": lambda:f"""{"Un [buldog] de bonne taille vous fixe avec insistance, il vous bloque le passage allongé sur " if pnj("le hall du premier étage", "buldog")  else " "}un tapis plutôt défraichis et rogné sur tous ses bord trônant au milieu d'un hall d'entrer permettant de rejoindre un escalier de marbre à l'ouest, un couloir s'enfonçant vers le sud ou une porte particuliérement vernis à l'est.""",
                # ETAGE 1 PIECE 2:
                "la chambre du maitre": lambda:"Une grande pièce séparée par une semi-Alcôve, dans la partie où vous trouvez une [bibliothèque] ainsi qu'un beau [fauteuil] de cuir meuble la pièce, une porte permet de sortir à l'ouest, tandis qu'au sud trône le lit de la chambre",
                # ETAGE 1 PIECE 3:
                "le bureau": lambda:"L'unique [fenêtre] de la pièce est obstruée par des planches et ne laisse filtrer que quelques rayons de lumière détourant un lourd [bureau] à tiroirs et une chaise face à la porte du mur est",
                # ETAGE 1 PIECE 4:
                "le couloir nord": lambda:f"Un couloir ornée d'un [tapis] rouge en mauvais état permettant de relier le fond de celui-ci au sud à une sorte de hall au nord. {'Une [échelle cassée] avec des barreaux manquants' if 'echelle cassee' in piece_inventaire(position()[1]) else 'Une [échelle]'} est posée contre le mur est et semble mener à une trappe au plafond, tandis que sur le mur ouest se trouve une porte",
                # ETAGE 1 PIECE 5:
                "le lit du maitre": lambda:"Cette partie de la pièce est séparée de la partie nord, un grand [lit] à deux place occupe presque tout l'espace.",
                # ETAGE 1 PIECE 6:
                "la chambre d’ami": lambda:f"Une petite pièce contenant un [lit] assez sommaire et une [table] de chevet{' sur laquelle repose un [verre]' if 'verre' in piece_inventaire(position()[1]) else ''}, une lumière pâle filtrant entre les rideaux obstruant l'unique fenêtre de la pièce donne à l'ensemble une humeur triste. Une porte sur le mur Est permet d'entrer et de sortir",
                # ETAGE 1 PIECE 7:
                "le couloir sud": lambda:"Vous découvrez un long couloir qui se poursuit vers le nord dans un long [tapis] poussièreux d'une couleur qui avait surement été une variante de rouge, le tout éclairé par une [fenêtre] sur le mur sud. A l'est et à l'ouest se trouve une porte.",
                # ETAGE 1 PIECE 8:
                "la réserve": lambda:f"Cette pièce sans fenêtre n'a qu'une entrée la porte de l'ouest. Grâce à la lumière vous devinez une reserve de [bric à brac]{', vous remarquez tout particulièrement une bouteille de [wiskey]' if 'wiskey' in piece_inventaire(position()[1]) else ''}{' et des [saucissons] au plafond' if 'saucissons' in piece_inventaire(position()[1]) else ''} .",
                # ETAGE 2 PIECE 4:
                "L’observatoire": lambda:f"En prenant l'échelle vous arrivez dans une petite tour avec un [télescope] pointer sur une montagne." },                                                                                                              
        "hero": {
            "VIE_PERSONNAGE": 10,
            "INV_PERSONNAGE": [],
            "DEGAT_PERSONNAGE": 1, },
        # {"piece": [element, option] - 1 prenable, 0 fixe, 2 fixe mais le résultat d'une utilisation dans l'inventaire du joueur, 3 pnj}
        "inventaire": {      
                  "la chambre d’ami":         ["verre", 1, "lit", 0, "fenetre", 0, "table", 0],
                  "la réserve":               ["wiskey", 1, "saucissons", 1, "bric a brac", 0],
                  "le couloir sud":           ["fenetre", 0, "tapis", 0],
                  "le couloir nord":          ["echelle cassee", 2, "tapis", 0],
                  "le bureau":                ["coffret a code", 1, "fenetre", 0, "bureau", 0],
                  "le hall du premier étage": ["buldog", 3],
                  "la chambre du maitre":     ["bibliotheque", 0, "fauteuil", 0],
                  "le lit du maitre":         ["lit", 0, "clef en fer", 1],
                  "salle à manger nord":      ["buffet", 0, "porte de fer", 2],
                  "la cuisine":               ["atre", 0, "couteau", 1, "hache", 1],
                  "accés nord":               ["baie vitree", 0, "tableaux", 0],
                  "accés sud":                ["baie vitree", 0],
                  "Hall d’entrée":            ["porte en argent", 2],
                  "La serre sud":             ["fleurs", 0],
                  "La serre nord":            ["arbustes", 1],
                  "L’observatoire":           ["telescope", 0, "codes", 1] },

        "personnage": {    
                  # ETAGE 1 PIECE 1:
                  "le hall du premier étage":{
                                                'buldog': {
                                                               "vie": 5,
                                                               "degats": 5,
                                                               "inv": [],
                                                               "faible": '"verre de wiskey"'
                                                }
                  } },
        "useCase": {
            "coffret a code": {
                        "telescope": lambda: f"Vous regardez dans le télescope et testez les séries de chiffres sur la serrure à code jusqu'à réussir à le déverrouiller. Il contient une clé en argent."
                     },
            "verre": {
                       "seul": lambda: f"Bien que le verre soit propre, il reste complètement vide et sans utilité.",
                       "wiskey": lambda: f"Vous remplissez le verre avec le wiskey."
            },
            "wiskey": {
                       "seul": lambda: f"Vous ouvrez la bouteille et prenez une petite lampé, il faut peut-être en garder pour plus tard.",
                       "verre": lambda: f"Vous remplissez le verre avec le wiskey."
            },
            "verre de wiskey": {
                        "seul": lambda: f"Vous prenez une lampé pour vous imprégner du goût agréable de la boisson.",
                        "buldog": lambda: f"Vous présentez le verre au buldog et il se dépêche de venir le boire goulument. Une fois le verre vide il s'effondre endormis."
            },
            "rondins": {
                        "echelle cassee": lambda: f"Vous consolidez l'échelle en insérant les rondins dans les encoches des marches manquantes."
            },
            "clef en fer": {
                        "porte de fer": lambda: f"Vous entrez la lourde clef en fer dans la serrure et la tourné doucement, un click prévient que la porte est à présent ouverte."
            },
            "hache": {
                        "arbustes": lambda: f"Vous tranchez les branches des arbustes à coup de hache et faites un petit tas de rondins, quand soudain le fer de la hache se détache et vole jusqu'à se planter au plafond."
            },
            "clef en argent": {
                        "porte en argent": lambda: f"Vous introduisez la délicate clef d'argent dans la porte en argent!"
            },
            "coffret a code": {
                        "codes": lambda: f"Vous essayez les différentes combinaisons sur le coffret jusqu'à ce que l'une d'elle le déverrouille, il contient une [clef en argent]."
            } },
        "special": {
            "la chambre d’ami": { 
                                 "voir": {
                                        "lit": lambda: "Le lit dans lequel vous vous êtes réveillé, les draps sont défaits.",
                                        "fenetre": lambda: f"En écartant les rideaux une nature pastoral sous une aube levant se révèle devant vos yeux légèrement éblouie.",
                                        "table": lambda: f"C'est une table de chevet simple {',Un verre vide repose dessus' if 'verre' in piece_inventaire(position()[1]) else ''}."

                                 },
                                 "util": {
                                        "lit": lambda: "Vous avez dormi il y a peu et ne ressentez pas le besoin de dormir à nouveau.",
                                        "fenetre": lambda: "Vous avez beau forcer impossible d'ouvrir la fenêtre.",
                                        "table": lambda: "Vous déplacez la table, mais rien ne se trouve en dessous ou derrière elle."
                                 } }, 
            "le couloir sud":  {
                                 "voir": {
                                        "fenetre": lambda: "En écartant les rideaux une nature pastoral sous une aube levant se révèle devant vos yeux légèrement éblouie.",
                                        "tapis": lambda: "Ce tapis a connus des jours meilleurs, sa couleur est passée et il est envahi de poussière."
                                 },
                                 "util": {
                                          "fenetre": lambda: "Vous avez beau forcer impossible d'ouvrir la fenêtre.",
                                          "tapis": lambda: "Vous remuez le tapis, la poussière s'élève doucement, mais non ... ce tapis n'a décidément rien de magique."
                                 } },
            "le couloir nord": {
                                 "voir": {
                                        "tapis": lambda: "Ce tapis a connus des jours meilleurs, sa couleur est passée et il est envahi de poussière."
                                 },
                                 "util": {
                                        "tapis": lambda: "Vous remuez le tapis, la poussière s'élève doucement, mais non ... ce tapis n'a décidément rien de magique."
                                 },
                                 "special": lambda: "Pour accéder au niveau supérieur il va falloir utiliser l'échelle, mais son état ne permet pas d'utiliser pour le moment." 
                              },
            "la réserve":      {
                                 "voir": {
                                          "bric a brac": lambda: "Des sacs de farines et de riz, des petits outils cassées, du foin... bref tout un tas de chose sans utilitée."
                                 },
                                 "util": {
                                          "bric a brac": lambda: "Hors de question de remuer tous ces trucs, d'autant plus qu'on risquerait de nous demander de les ranger plus tard..."
                                 } },
            "le bureau":       {      
                                 "voir": {
                                          "bureau": lambda: f"le bureau est bien rangé, une ramette de papier avec une plume et un encrier sur le plateau.{' Après avoir rapidement vérifié les tiroirs, un seul contient un [coffret à code] dont la serrure attend une combinaison de six chiffres pour être déverrouillée.' if 'coffret a code' in  piece_inventaire(position()[1]) else ''}",
                                          "fenetre": lambda: "Cette fenêtre a été étrangement barrée par de solide planche, mais pourquoi faire?"
                                 },
                                 "util": {
                                          "bureau": lambda: "C'est pas vraiment le moment de se pencher sur ses exercices.",
                                          "fenetre": lambda: "Les planches empêchent d'actionner la fenêtre."                                   
                                 } },
            "le hall du premier étage": {
                                 "special": lambda: "Vous essayez de vous avancer, mais dès que vous approchez le [buldog] se redresse et grogne bien décidé à ne pas vous laissez passer" 
                                 },
            "la chambre du maitre": {
                                 "voir":{
                                          "bibliotheque": lambda: "Une collection de livres ancien à reliure de cuir, ces bibliothèques sont des bien précieux!",
                                          "fauteuil": lambda: "Le fauteuil semble si confortable que la forme de son propriétaire est incrustée à l'intérieur"
                                 },
                                 "util":{
                                          "bibliotheque": lambda: "Vous déplacez plusieurs livres, mais non rien, pas de passage secret.",
                                          "fauteuil": lambda: "Une petite pause bien méritée, il faut trouver la sortie à présent."
                                 } },
            "le lit du maitre":   {
                                 "voir":{
                                          "lit": lambda: "Ce lit est bien plus moelleux et luxueux que celui dans lequel vous avez dormi."
                                 },
                                 "util":{
                                          "lit": lambda: f"""Vous défaites les couvertures et retournez les oreillers. {'Vous découvrez parmi les draps une [clef en fer].' if "clef en fer" in piece_inventaire(position()[1]) else ''}"""   
                                 } },
            "salle à manger nord":{
                                 "voir":{
                                          "buffet": lambda: "C'est un beau meuble remplit d'une vaisselle luxueuse."
                                 },
                                 "util":{
                                          "buffet": lambda: "Le buffet est beaucoup trop lourd pour être déplacer."
                                 },
                                 "special": lambda: "La porte de fer est verouillée et vous empêche de rejoindre la pièce suivante."
                                 },
            "la cuisine":         {
                                 "voir": {
                                        "atre": lambda: "c'est un grand âtre en pierre recueillant une marmite et beaucoup de cendre, manifestement il n'a pas été nettoyé récemment."
                                 },
                                 "util": {
                                        "atre": lambda: "Non non ce n'est pas l'heure de manger!"
                                 } },
            "accés nord":         {
                                 "voir": {
                                        "baie vitree": lambda: "La grande baie vitrée ne permet pas de voir très loin puisqu'une haie d'au moins deux mètres de haut se trouve à 3 mètres de celle-ci, sans compter d'épais barreau de fer la protégeant",
                                        "tableaux": lambda: "Un triptyque de portraits représentant un homme à trois âges différents."
                                 },
                                 "util": {
                                        "baie vitree": lambda: "Non même en parvenant à briser la vitre sans se blesser, les barreaux empêcheraient tout de même de sortir.",
                                        "tableaux": lambda: "Vous faites balancez les tableaux qui restent bien accrochés, rien ne semble caché derrière."
                                 } },
            "accés sud":         {
                                 "voir": {
                                        "baie vitree": lambda: "La grande baie vitrée ne permet pas de voir très loin puisqu'une haie d'au moins deux mètres de haut se trouve à 3 mètres de celle-ci, sans compter d'épais barreau de fer la protégeant"
                                 },
                                 "util": {
                                        "baie vitree": lambda: "Non même en parvenant à briser la vitre sans se blesser, les barreaux empêcheraient tout de même de sortir."
                                 } },
            "La serre sud":      {
                                 "voir": {
                                        "fleurs": lambda: "Aconit, bergénie, camélia, fleur d'arlequin... mmm visiblement le maitre de maison à une passion pour la botanique."
                                 },
                                 "util": {
                                        "fleurs": lambda: "la fleur en bouquet fâne et jamais ne renait! laissons les vivres."
                                 } },
            "L’observatoire":     {
                                 "voir": {
                                        "telescope": lambda: "Il semble fonctionnel et est pointé dans une direction un peu singulière."
                                 },
                                 "util": {
                                        "telescope": lambda: "Vous utilisez le télescope et apercevez la montagne de plus près, il semblerait qu'il soit réglé ainsi pour permettre de distinguer des panneaux de bois sur lesquels est inscrit des sortes de [codes] à six chiffres"
                                 } },
            "Hall d’entrée":      {
                                 "special": lambda: f"La porte est solide et sa serrure en argent semble bien fermée!"
            } },
        "welcome": """
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
note: les "objets" en plusieurs mots doivent obligatoirement être entre guillemet "" les autres non.
"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'\n
Vous ne vous souvenez pas de la nuit dernière et lorsque vous ouvrez les yeux vous n'êtes manifestement pas dans votre lit, vous vous levez et vous trouvez dans  
"""
}


def combine(E1, E2):
    """
    combine: 
        Retourne la valeur pour la combinaison entre E1 et E2
    Args:
        E1 sting: un objet
        E2 string: un objet
    Returns:
        string: résultat de la combinaison.
    """
    return game.get("combine", {"vide": 0}).get(str(E1), {"vide": 0}).get(str(E2), 0)

def RUN():
    """
    RUN: 
        Reroutne la valeur actuel de RUN dans la structure.
    Returns:
        int: 0 ou 1
    """
    return game.get("current", {"vide", 0}).get("RUN", -1)

def position():
    """
    position: 
        retourne la position actuel dans la matrice DMAP
    Returns:
        string: résultat
    """
    return game.get("DMAP", 0)[game.get("current").get("ETAGE")][game.get("current").get("PIECE")]

def description(E1):
    """
    description: 
        retourne la description pour E1 de la structure
    Args:
        E1 string: "nom de piece"
    Returns:
        string: résultat
    """
    return game.get("description", {"vide": 0}).get(E1,lambda: 0)

def hero_inventaire():
    """
    hero_inventaire: 
        Récupére l'inventaire dans la structure "hero"
    Returns:
        list: liste d'inventaire
    """
    return game.get("hero", {"vide": 0}).get("INV_PERSONNAGE", 0)

def hero_vie():
    """
    hero_vie: 
        retourne la valeur de vie du hero dans la structure "hero"
    Returns:
        int: point de vie
    """
    return game.get("hero", {"vide": 0}).get("VIE_PERSONNAGE", 0)

def hero_damage():
    """
    hero_damage: 
        retourne le montant de dommages dans la structure "hero"
    Returns:
        ind: dommages
    """
    return game.get("hero", {"vide": 0}).get("DEGAT_PERSONNAGE", 0)

def piece_inventaire(piece):
    """
    Exec: 
        fonction qui reçoit les arbres à partir de la grammaire et applique les actions nécessaires.
    Args:
        tree(arbre): arbre d'instruction
    Returns:
        string: résultat
    """
    return game.get("inventaire", {"vide":0}).get(piece, 0)

def pnj(PIECE, E1):
    """
    pnj: 
        récupére la structure pour un personnage donné
    Args:
        PIECE string: "nom de la piece"
        E1 string: "nom du pnj"
    Returns:
        dict: structure du personnage
    """
    return game.get("personnage", {"vide": 0}).get(PIECE, {"vide": 0}).get(E1, 0)

def use(E1, E2):
    """
    use: 
        Retourne le résultat d'utilisation entre E1 et E12
    Args:
        E1 string: "objet1"
        E2 string: "objet2"
    Returns:
        string: résultat
    """
    return game.get("useCase", {"vide": 0}).get(E1, {"vide": 0}).get(E2, lambda: 0)

def special(PIECE, E1, E2):
    """
    special: 
        retourne le résultat des actions par rapport à un objet
    Args:
        PIECE string: "nom de la piece"
        E1 string: "action"
        E2 string: "objet"
    Returns:
        string: résultat
    """
    return game.get("special", {"vide": 0}).get(PIECE, {"vide": 0}).get(E1, {"vide": 0}).get(E2, lambda: 0)

def styleFormat(E):
    """
    styleFormat: 
       fonction pour intégrer un resultat dans un standard "graphique"
    Args:
        E string: chaîne de caractère à décorer.
    Returns:
        string: résultat
    """
    return f"""
"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'\n
{E}
\n"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'"`-._,-'
"""