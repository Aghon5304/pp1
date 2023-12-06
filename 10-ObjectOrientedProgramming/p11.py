class TV():
    def __init__(self):
        self.isOn = False
        """zad 12"""
        self.channel_no = 1
    def turn_on(self):
        self.isOn = True
    def turn_off(self):
        self.isOn = False
    def turn_on_or_off(self):
        self.isOn = not self.isOn
    def show_status(self):
        if self.isOn:
            print(f"The Tv is curently On\nChannel: {self.channel_no}")
        else:
            print("Then, try using the TV set.")
    def setchannel(self,new_cahnnel_no):
        self.channel_no=new_cahnnel_no
    
samsung = TV()
samsung.show_status()
samsung.turn_on()
samsung.show_status()
samsung.setchannel(5)
samsung.show_status()
samsung.turn_on_or_off()
samsung.show_status()