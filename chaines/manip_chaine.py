#!usr/bin/python env
# -*- coding: utf-8 -*-

# Quelques manipulations de chaines de caractères


phrase="Bonjour les gens"
print "Phrase initiale : "+phrase+"\n"


print "Phrase découpée en mots avec split() : "
for mot in phrase.split():
		print mot
print "\n"

print "Récupération du premier mot de la phrase :"
phrase_decoupee=phrase.split()
print phrase_decoupee[0]
print "\n"

print "Découpage de ce mot en lettres : "
for lettre in phrase_decoupee[0]:
		print lettre		