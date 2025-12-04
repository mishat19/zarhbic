def calcul_zarhbic(expression):
    chiffres = []
    operateurs = []
    # Parsing de l'expression
    for c in expression:
        if c.isdigit():
            chiffres.append(int(c))
        else:
            operateurs.append(c)
    # Vérification de la validité
    if len(chiffres) < 2 and operateurs:
        return "Erreur : Il faut au moins deux chiffres pour un opérateur dyadique."
    # Application des règles
    resultat = chiffres[0]
    for i in range(len(operateurs)):
        if operateurs[i] == '+':
            resultat += chiffres[i+1]
        elif operateurs[i] == '*':
            resultat *= chiffres[i+1]
        elif operateurs[i] == '-':
            resultat -= chiffres[i+1]
        elif operateurs[i] == '$':
            resultat = int(str(resultat)[::-1])  # Inversion
    return resultat
