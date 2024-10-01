# Funktion zur Berechnung des Preises mit Mehrwertsteuer
def price_with_tax(price):
    tax_rate = 0.19  # Mehrwertsteuersatz von 19%
    total_price = price * (1 + tax_rate)
    return total_price

# Test der Funktion
print("Gesamtpreis für 99.99€:", price_with_tax(99.99))
print("Gesamtpreis für 1.99€:", price_with_tax(1.99))