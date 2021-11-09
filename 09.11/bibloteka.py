#Klases nosaukumu

class Robots:
  """Klase reprezenta ar specifisko vardu"""

  #Klases konstruktoru. inicilizesana.
  def __init__(self,vards):
    """Datu inicializacija"""


    self.vards=vards

    print(f"Inicialuzejam {self.vards}")

  def sasviecinaties(self):
    print(f"Sveiks! Mani sauc {self.vards}")


#klases parbaudisana

#1. robota izveide
rob1 = Robots("R1")

#1. robota metode parbaude
rob1.sasviecinaties()


#2 robota izveide

rob2 = Robots("R2")

rob2.sasviecinaties()