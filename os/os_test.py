import os

# affiche le nom de l'utilisateur courant
user = os.getlogin()
print(user)

# récupérer l'id de l'utilisateur
user_id = os.getuid()
if user_id != 0:
    print("Must be superuser to use this program...")
else:
    print("You're root. Ok !")

# affiche le répertoire courant
dir = os.getcwd()
print(dir)