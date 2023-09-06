def total_price(net_price, tax_rate, discount=False):
    if not discount:
        return int(net_price * (1 + tax_rate / 100))
    else:
        return int(met_price * (1 + tax_rate / 100) * 0.9)
    
print(total_price(1000, 23))
print(total_price(1000, 23, True))

# Prostty błąd literowy, który nie zostanie zauważony (pomijając stosowanie edytora) wywoła błąd 
# w momencie wywołania funkcji print(total_price(1000, 23, True)). Jeśli nie wywołamy funkcji, BŁĄD NIE ZOSTANIE 
# ZAUWAŻONY W MOMENCIE URUCHOMIENIA KODU


   