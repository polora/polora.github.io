# source : https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/
#
# "Le blog 'ledatascientist' est le blog français de référence en Data Science."
#
# Créer une fonction qui calcule la longueur moyenne des mots de cette phrase

sentence = "Le blog 'ledatascientist' est le blog français de référence en Data Science."
sentence2 = "Même les phrases avec des caractères de la langue française peuvent être utilisées."

def average_words_length(sentence):

    # enlever la ponctuation
    for punctuation in ".,;:!,'":
        sentence = sentence.replace(punctuation, ' ')

        # couper la chaine de caractères en mots
        words = sentence.split()

        #calculs
        somme = sum(len(word) for word in words)
        return round(somme / len(words),2)

print(average_words_length(sentence2))