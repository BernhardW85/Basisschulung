# Bsp: Eingabe von Zahl zw. 1 und 100, alle Zahlen bis zur Eingabe sollen ausgegeben weden. Immer wenn die Zahl durch 3 dividierbar ist ohne Rest, solldas Wort "fizz" ausgegeben werden, wenn durch 5 dann "buzz".
# wenn beides zutrifft, "fizzbuzz"
end_zahl = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein: "))

for number in range(1, end_zahl+1):
    if number % 3 == 0 and number % 5 == 0: # % ist modulo; gibt Rest als ganze Zahl aus
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)