class Bug:
    licznik = 0
    
    def __init__(self):
        Bug.licznik = Bug.licznik + 1
        self.id = Bug.licznik
    
    def __del__(self):
        Bug.licznik = Bug.licznik - 1
        print("Koniec ||", "licznik:", Bug.licznik, "id:", self.id)
        
    def __str__(self):
        return "licznik: " + str(Bug.licznik) + "  id: " + str(self.id)

    """ class Bug is created """

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])


