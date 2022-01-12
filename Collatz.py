###########################################################
#                                                         #
#  The Collatz Problem - Das Collatz-Problem              #
#  Thomas Hoppe January 2022                              #
#  https://github.com/Thomas20232030/The-Collatz-Problem  #
#                                                         #
###########################################################

import time
import matplotlib.pyplot as plt


def collatz(n):
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            liste.append(n)
        else:
            n = 3 * n + 1
            liste.append(n)
    return liste


while True:

    print("\nDas Collatz-Problem:")
    print("--------------------")
    print("(1) Definition und Erläuterung")
    print("(2) Berechnung in einem beliebigen Intervall")
    print("(0) Ende\n")
    auswahl = input("Deine Wahl: ")

    if auswahl == "1":
        print("\nDas Collatz-Problem, auch als (3n+1)-Vermutung bezeichnet, ist ein ungelöstes mathematisches Problem,")
        print("das 1937 von Lothar Collatz gestellt wurde. Es hat Verbindungen zur Zahlentheorie, zur Theorie")
        print("dynamischer Systeme und Ergodentheorie und zur Theorie der Berechenbarkeit in der Informatik.")
        print("Das Problem gilt als notorisch schwierig, obwohl es einfach zu formulieren ist. Jeffrey Lagarias,")
        print("der als Experte für das Problem gilt, zitiert eine mündliche Mitteilung von Paul Erdős, der es")
        print("als „absolut hoffnungslos“ bezeichnete.\n")
        print("Präzisierung der Problemstellung\n")
        print("Bei dem Problem geht es um Zahlenfolgen, die nach einem einfachen Bildungsgesetz konstruiert werden:\n")
        print("- Beginne mit irgendeiner natürlichen Zahl n")
        print("- Ist n gerade, so nimm als nächstes n / 2")
        print("- Ist n ungerade, so nimm als nächstes 3 * n + 1")
        print("- Wiederhole die Vorgehensweise mit der erhaltenen Zahl\n")
        print("Die Collatz-Vermutung lautet:\n")
        print("Jede Zahlenfolge mündet in den Zyklus 4, 2, 1, egal, mit welcher natürlichen Zahl n>0 man beginnt.\n")
        print("Trotz zahlreicher Anstrengungen gehört diese Vermutung noch immer zu den ungelösten Problemen der")
        print("Mathematik. Mehrfach wurden Preise für eine Lösung ausgelobt...")
        print("\nWikipedia https://de.wikipedia.org/w/index.php?title=Collatz-Problem&oldid=217796154")

        input("\nWeiter mit jeder beliebigen Taste...")

    if auswahl == "2":

        while True:
            try:
                anfang = int(input("\nBitte den Startwert eingeben: "))
                ende = int(input("Bitte den Endwert eingeben  : "))
                if anfang <= 0 or ende < anfang:
                    print("\nStartwert mindestens 1, Endwert größer oder gleich Startwert...\n")
                    continue
                break
            except ValueError:
                print("\nBitte die Zahlen im richtigen Format als ganze Zahl eingeben...\n")

        start = time.time()
        laengen = []

        for i in range(anfang, ende + 1):
            laengen.append(len(collatz(i)))

        collatzmaxwert = max(laengen)
        collatzmaxindex = laengen.index(collatzmaxwert)
        collatzmaxzahl = anfang + collatzmaxindex
        delta = int(time.time() - start)
        m, s = divmod(delta, 60)
        h, m = divmod(m, 60)

        print(f"\nAusgabe der Folgen: \n\n{laengen}")
        print(f"\nAusgabe von {anfang:,.0f} bis {ende:,.0f} und insgesamt {ende - anfang + 1:,.0f} Folge(n)")
        print(f"Die längste Folge macht {collatzmaxwert:,.0f} Schritte bei der Zahl {collatzmaxzahl:,.0f}\n")
        print(collatz(collatzmaxzahl))
        print(f"\nDie größe erreichte Zahl ist {max(collatz(collatzmaxzahl)):,.0f}")
        print(f"\nDauer in Stunden, Minuten und Sekunden: {h:02}:{m:02}:{s:02}")

        plt.title("Die Collatzwerte von " + str(anfang) + " bis " + str(ende))
        plt.scatter(list(range(anfang, ende + 1)), laengen)
        plt.grid(True)
        plt.axis()
        plt.ylabel("Iterationen")
        plt.xlabel("Intervall")
        plt.show()

    elif auswahl == "0":

        print("\nDas Programm wird beendet...")
        break

    else:

        print("\nFalsche Eingabe. Bitte wiederholen...")
