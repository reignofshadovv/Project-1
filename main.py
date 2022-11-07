#Project Start Date : "07.11.2022-22:00"
#MyPythonProject1

banner1 = ("=============================================================")
banner2 = ("==========      HELLO & WELCOME TO MY PROJECT      ==========")
banner3 = ("=============================================================")
#print(banner1)
#print(banner2)
#print(banner3)


# Koin Alım & Satım Girişi
title1="Koin Alım&Satım Girişi"
print(banner1)
print(title1)
print(banner3)

x = input("Alınan Koin Cinsi Gir...\n")
y = input("Alınan Koin Miktarı Gir...\n")
z = input("Toplam Ödenen USDT Gir...\n")

result = float(z) / float(y)
print("Alış Kuru")
print("----------------")
print(result, "USDT")