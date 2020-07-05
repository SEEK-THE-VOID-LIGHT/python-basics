while True:
    print("\nHallo, ich bin ein kleiner Rechner uwu")
    print("Sag mir, ob ich + - * oder / machen soll °-°\noder quit")
    auswahl = input("Deine Auswahl: ")


    if auswahl == '+':
        print("erste Zahl")
        eingabe1 = float(input(": "))
        print("zweite")
        eingabe2 = float(input(": "))
        answer = eingabe1 + eingabe2
        print("Die Lösung ist " + str(answer))
        
    elif auswahl == '-':
        print("erste Zahl")
        eingabe1 = float(input(": "))
        print("zweite")
        eingabe2 = float(input(": "))
        answer = eingabe1 - eingabe2
        print("Die Lösung ist " + str(answer))
        
    elif auswahl == '*':
        print("erste Zahl")
        eingabe1 = float(input(": "))
        print("zweite")
        eingabe2 = float(input(": "))
        answer = eingabe1 * eingabe2
        print("Die Lösung ist " + str(answer))
        
    elif auswahl == '/':
        print("erste Zahl")
        eingabe1 = float(input(": "))
        print("zweite")
        eingabe2 = float(input(": "))
        answer = eingabe1 / eingabe2
        print("Die Lösung ist " + str(answer))
        
    elif auswahl == 'quit':
        break
        
    else:
        print("Falsche Auswahl")