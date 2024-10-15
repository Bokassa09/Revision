# Affiche un message d'accueil
print("👋 Bienvenue dans ce programme !, ce jeu est un jeu dangereux")

# Demande les informations de l'utilisateur
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

# Vérifie si l'utilisateur est majeur ou mineur
if age >= 18:
    print(f"Salut {prenom} {nom}, tu es majeur ! 🎉 Tu peux jouer à ce jeu.")
else:
    print(f"Désolé {prenom}, tu es mineur. 🚫 Quitte ici vite !")
