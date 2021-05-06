def SayHello (name):
    return  "Hello {0}".format(name)
    # Return kann die Variable wieder an das aufrufende Programm zurückgeben

def main():
    strHello1 = SayHello(name="Christoph")
    print(strHello1)

    print(SayHello(name="Dude"))

if __name__ == "__main__": # Ruft diese Funktion initial auf, falls diese noch nicht ausgeführt wurde.
    main()
