class Smartphone():
    def  __init__(self,model,marka,kolor,dysk,numer):
        self.model = model
        self.marka = marka
        self.kolor = kolor
        self.dysk = dysk
        self.wolnyDysk=100
        self.isTurnedOn=False
        self.nubmer=numer
    def isOn(self):
        if( self.isTurnedOn): stan = "On" 
        else: stan = "Off"
        print(f"Telephone is curently {stan}")
    def turnOnOrOff(self):
        self.isTurnedOn=not self.isTurnedOn
    def zmienWolneMiejsce(self,miejsce):
        self.wolnyDysk=miejsce
    def showPhoneNumber(self):
        print(f"The phone number = {self.nubmer}")

mojTelefon = Smartphone("a234","Samsung","czarny","750GB","111222333")
mojTelefon.turnOnOrOff()
mojTelefon.isOn()
mojTelefon.showPhoneNumber()
mojTelefon.zmienWolneMiejsce(63)