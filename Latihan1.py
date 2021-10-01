class Sepeda:
    def intro(self):
        print("Sepeda yang biasa kita lihat umumnya memiliki 2 roda")

    def roda(self):
        print("Namun, ada juga yang beroda 1 dan beroda 4")

class Sirkus(Sepeda):
    def roda(self):
        print("Roda 1 sering digunakan di acara sirkus")

class Anak(Sepeda):
    def roda(self):
        print("Roda 4 biasanya digunakan oleh anak-anak yang baru belajar bersepeda")

obj_Sepeda = Sepeda()
obj_Sirkus = Sirkus()
obj_Anak = Anak()

obj_Sepeda.intro()
obj_Sepeda.roda()

print("\n")

obj_Sirkus.intro()
obj_Sirkus.roda()

print("\n")

obj_Anak.intro()
obj_Anak.roda()
