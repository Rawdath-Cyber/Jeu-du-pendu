Mot_secret="Code"
Vies=5
print("Bienvenue dans le jeu ! Le mot secret a", len (Mot_secret) ,"lettes")
while Vies > 0:
    Proposition=input("Entrez une lettre ou le mot entier")
    if len(Proposition) > 1:
        if Proposition==Mot_secret:
            print("Incroyable! Vous avez trouvé le mot entier:", Mot_secret)
        break
    else :
         print("Faux ! Ce n'est pas le bon mot, vous perdez toutes vos vies")
         Vies= 0
else: 
        if Proposition in Mot_secret:
         print("Bonne lettre !Elle est dans le mot")
        else:
          Vies-=1
          print("Raté! Il vous restes:", Vies)
if Vies==0:
 print("Dommage, vous avez perdu! Le mot secret était:", Mot_secret)
    
