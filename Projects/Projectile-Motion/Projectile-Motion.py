import math
from ExperimentData import ExperimentData

import os
from pathlib import Path

import json

# Gunname = "Knight's Armament Company SR-25"
# Guncartridge = "7.62x51mm NATO"
# Round = "7.62x51mm M993"
# RoundVelocity_ms = 910 
# Building = "Central Park Tower"
# BuildingHeight_m = 472
# Gravity_ms= 9.81

# Here in calculating the time by plugging in the formula with the variables defined on top. But first, you need to import the fuction of the square root. 
def ProjectileFunction(experimentData:ExperimentData):
    time_s = math.sqrt((2 * experimentData.BuildingHeight_m) / experimentData.Gravity_ms)
    Distance_m = (experimentData.RoundVelocity_ms * time_s)
    print(f"""Chris is planning on killing an old lady on Central park.
    He will use an {experimentData.Gunname} which uses a cartridge of {experimentData.Guncartridge}. 
    The round of this weapon is {experimentData.Round}and the velocity of the round is {experimentData.RoundVelocity_ms}m/s.
    He will shoot the gun from {experimentData.Building}, this building has a height of {experimentData.BuildingHeight_m}m.
    The gravity on earth is {experimentData.Gravity_ms}m/s, the time it will take the gun to kill the lady is {time_s},
    and the distance it will run is {Distance_m}. Chris just killed the old lady.
    """)

# experimentalData = {
#  "Gunname" : "Knight's Armament Company SR-25",
#  "Guncartridge" : "7.62x51mm NATO",
#  "Round" : "7.62x51mm M993",
#  "RoundVelocity_ms" : 910,
#  "Building" : "Central Park Tower",
#  "BuildingHeight_m" : 472,
#  "Gravity_ms": 9.81
# }

myDataSet = [
     ExperimentData("Knight's Armament Company SR-25",)



]

MyOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(myOutputPath , 'ExperimentData.json')

with open(myOutputFilePath, 'w') as outfile:
    json.dump(experimentData.__dict__ , outfile)





