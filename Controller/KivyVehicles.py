class Rover:
    def __init__(self, Id, Name, IPAddress, MegadishIPAddress, Connected, Calibration):
        self.Id = Id
        self.Name = Name
        self.IPAddress = IPAddress
        self.MegadishIPAddress = MegadishIPAddress
        self.Connected = Connected
        self.Calibration = Calibration

class Rovers:
    def __init__(self):
        self.rovers = []
        self.InitRovers()

    def InitRovers(self):
         # clear the list of rovers
        self.rovers.clear()

        rover_data = [
            (50, "Pi Zero Usb", "192.168.1.50", "192.168.17.50", False, ""),
            (51, "Food Delivery Vehicle", "192.168.1.51", "192.168.17.51", False, "2LM1.0:RM1.0"),
            (52, "Research Vehicle One", "192.168.1.52", "192.168.17.52", False, "2LM0.63:RM1.0"),
            (53, "Hedgehog Observation Vehicle", "192.168.1.53", "192.168.17.53", False, "4LMF1.0:LMR1.0:RMF1.0:RMB1.0"),
            (54, "Roof Exploration Vehicle", "192.168.1.54", "192.168.17.54", False, "2LM1.0:RM1.0")
        ]

        for rover_info in rover_data:
            rover = Rover(*rover_info)
            self.rovers.append(rover)

        print("Number of rovers:", len(self.rovers))

    def get_rovers(self):
        return self.rovers
