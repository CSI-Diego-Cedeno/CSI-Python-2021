import math

# Gunname = "Knight's Armament Company SR-25"
# Guncartridge = "7.62x51mm NATO"
# Round = "7.62x51mm M993"
# RoundVelocity_ms = 910 
# Building = "Central Park Tower"
# BuildingHeight_m = 472
# Gravity_ms= 9.81

def gunBuilding (Gunname:str, Guncartridge:str, Round:str, RoundVelocity_ms:str, Building:str
, BuildingHeight_m:str, Gravity_ms:str):

    Time = math.sqrt((2 * BuildingHeight_m) / Gravity_ms)
    Distance = (RoundVelocity_ms * Time)


    print(f"""Chris is planning on killing an old lady on Central park.
    He will use an {Gunname} which uses a cartridge of {Guncartridge}. 
    The round of this weapon is {Round}and the velocity of the round is {RoundVelocity_ms}m/s.
    He will shoot the gun from {Building}, this building has a height of {BuildingHeight_m}m.
    The gravity on earth is {Gravity_ms}m/s, the time it will take the gun to kill the lady is {Time},
    and the distance it will run is {Distance}. Chris just killed the old lady.
    """)


gunBuilding ("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm M993", 910
, "Central Park Tower", 472, 9.81)





