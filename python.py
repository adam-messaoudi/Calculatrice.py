def calculatrice():
    print("Bienvenue dans la calculatrice simple!")
    historique = []
    
    while True:
        try:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")

            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
                if nombre2 == 0:
                    print("Erreur : Division par zéro non autorisée.")
                    continue
                resultat = nombre1 / nombre2
            else:
                print("Opération non reconnue.")
                continue

            print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à : {resultat}")
            historique.append((nombre1, operation, nombre2, resultat))
            
            continuer = input("Voulez-vous continuer ? (Oui/Non) : ")
            if continuer.lower() != 'oui':
                print("Historique des calculs :")
                for calcul in historique:
                    print(f"{calcul[0]} {calcul[1]} {calcul[2]} = {calcul[3]}")
                
                effacer = input("Voulez-vous effacer l'historique ? (Oui/Non) : ")
                if effacer.lower() == 'oui':
                    historique = []
                    
                print("Merci d'avoir utilisé la calculatrice!")
                break
        
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

calculatrice()
