#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

# Importation du module datetime
import datetime

# récupérer la date du moment
today = datetime.datetime.now()
print(today)

# comme le résultat est un peu brut, on va formater la sortie
str_date = today.strftime("%d/%m/%m")
print(str_date)

str_date2 = today.strftime("%d %h %Y")
print(str_date2)

str_time = today.strftime("%H:%M:%S")
print(str_time)

# timestamp
import time
t = time.time()

print(t)

print(time.ctime())

# time sleep
print("wait 5 seconds....")
time.sleep(5)
print("Done")