class Rekins:

   def __init__(self,klients,veltijums,izmers,materials):
  
      self.klients = klients
      self.veltijums = veltijums
      self.izmers = izmers
      self.materials = materials

      self.teksta_gar = len(self.veltijums)
      self.ladites_izm = self.izmeri.split(',')
      self.garums = self.ladites_izm[0]
      self.platums = self.ladities_izm[1] 
      self.augstums = self.ladtites_izm[2]
  

   def izdrukat(self):
    print(f'Klienta vards {self.klients}')
    print(f'veltijuma teksts {self.veltijums}')
    print(f'Izmers {self.izmers}')
    print(f'lodites material {self.materials}')

   def aprekins(self):
     darba_samaksa = 15
     PVN = 21
     produkta_cena = (self.teksta.gar) * 1.2 +(self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * materiala_cena
     PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
     rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
pass

klients = input('Ūzraksti savu vardu un uzvardu')
veltijums = input('Uzraksti veltijumu')
izmeri = input('Ievadi ladites izmeru\n Garums,platums,augstums(raksti veselus skaitlus, atdalot tos ar komatiem\n')
materials = input('materiala cena EUR/m2:')

rekins = Rekins(klients, veltijums, izmeri, materials)
print(rekins.klients)
print(rekins.veltijums)
print(rekins.izmeri)
print(rekins.izmeri_sar)


print(rekins.sprekins)

# print(izmeri)
# print(type(izmeri))
# print(izmeri.split(','))
# sadal = izmeri.split(',')
# print(sadal[0])
# print(sadal[1])
# print(sadal[2])

print

 


















