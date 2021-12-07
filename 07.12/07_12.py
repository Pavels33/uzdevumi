#Treniņš ieskaitei

#Izveido klasi Transportlidzeklis
class Transportlidzeklis:

  krasa = "Melna"

  #Pievieno īpašības
  def __init__(self, nosaukums, max_atrums, nobraukums):
    self.nosaukums = nosaukums
    self.max_atrums = max_atrums
    self.nobraukums = nobraukums

  #Metode sedvietu_skaits() ar vienu mainīgo - skaits
  def sedvietu_skaits(self, skaits):
    self.skaits = skaits
    return f"Sēdvietu skaits {self.nosaukums} ir {self.skaits} vietas."

  def biletes(self):
    return self.skaits * 0.5

# modelisX = Transportlidzeklis("Mersedess",150,55)
# print(modelisX.nosaukums, modelisX.max_atrums, modelisX.nobraukums)

#Klase, kura "manto" mainīgos un metodes no klases Transportlidzeklis
class Buss(Transportlidzeklis):
  #Metode sedvietu_skaits, noklusējumvērtība 50
  def sedvietu_skaits(self, skaits = 50):
    return super().sedvietu_skaits(skaits)
  
  def biletes(self):
    return super().biletes()

# modelisY = Buss("Mersedess",150,55)
# print(modelisY.nosaukums, modelisY.max_atrums, modelisY.nobraukums)

Skolas_buss = Buss("Mersedess", 140, 20)
print(Skolas_buss.sedvietu_skaits(100))
print(Skolas_buss.krasa, Skolas_buss.nosaukums, "Ātrums:", Skolas_buss.max_atrums,
"Nobraukums:", Skolas_buss.nobraukums)
print(Skolas_buss.biletes())












