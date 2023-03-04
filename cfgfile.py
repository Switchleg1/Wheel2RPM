import sys
import yaml

class cfgfile:
    def __init__(self, fileName, debug=False):
        with open(fileName, "r") as configFile:
            configuration = yaml.safe_load(configFile)

            self.engineRPM = configuration["Engine RPM"]
            self.gear = configuration["Gear"]
            self.wheelSpeed = configuration["Wheel Speed"]
            self.multipliers = [configuration["Multiplier 1"],
                             configuration["Multiplier 2"],
                             configuration["Multiplier 3"],
                             configuration["Multiplier 4"],
                             configuration["Multiplier 5"],
                             configuration["Multiplier 6"]]

            if debug:
                print("[Config]")
                print("  engineRPM: " + self.engineRPM)
                print("  gear: " + self.gear)
                print("  wheelSpeed: " + self.wheelSpeed)
                print("  multiplier 1: " + str(self.multipliers[0]))
                print("  multiplier 2: " + str(self.multipliers[1]))
                print("  multiplier 3: " + str(self.multipliers[2]))
                print("  multiplier 4: " + str(self.multipliers[3]))
                print("  multiplier 5: " + str(self.multipliers[4]))
                print("  multiplier 6: " + str(self.multipliers[5]))
