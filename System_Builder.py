# coding=utf-8
import random
import bisect

# StarSystem Age
StarSystemAge = {-4: 'Extremely Young', -3: 'Very Young', -2: 'Young', -1: 'Maturing', 0: 'Mature', 1: 'Aging', 2: 'Old', 3: 'Very Old', 4: 'Ancient'}

# Attributes for Stellar Bodies

# First three mandatory. Name: String, Planets allowed: Boolean, Need Spectral Type: Boolean, HZone Period, HZone Distance
AsymptoticGiant = {'Name': 'Asymptotic Giant', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(50, 70), 'HZoneDist': random.randint(9, 34)}
BlackHole = {'Name': 'Stellar Black Hole', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(10, 750), 'HZoneDist': random.randint(6, 200)}
BlackStar = {'Name': 'Black Star', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(10, 750), 'HZoneDist': random.randint(6, 200)}
CollapsingStar = {'Name': 'Collapsing Star', 'Planets': True, 'SpectralType': True}
CoolSubdwarf = {'Name': 'Cool Subdwarf', 'Planets': True, 'SpectralType': False, 'HZonePer': random.uniform(0.11, 0.16), 'HZoneDist': random.uniform(0.15, 0.19)}
DarkMatter = {'Name': 'Dark Matter Star', 'Planets': False, 'SpectralType': False}
EruptiveVariable = {'Name': 'Eruptive Variable', 'Planets': True, 'SpectralType': True}
Electroweak = {'Name': 'Electroweak Star', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(10, 750), 'HZoneDist': random.randint(6, 200)}
Giant = {'Name': 'Giant', 'Planets': True, 'SpectralType': True}
H2Region = {'Name': 'H II Region', 'Planets': False, 'SpectralType': False}
HotSubdwarf = {'Name': 'Hot Subdwarf', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(7, 66), 'HZoneDist': random.randint(3, 13)}
InterstellarCloud = {'Name': 'Interstellar Cloud', 'Planets': False, 'SpectralType': False}
MainSeqStar = {'Name': 'Main Sequence Star', 'Planets': True, 'SpectralType': True}
MolecularCloud = {'Name': 'Molecular Cloud', 'Planets': False, 'SpectralType': False}
NeutronStar = {'Name': 'Neutron Star', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(10, 750), 'HZoneDist': random.randint(6, 200)}
PlanetaryNebula = {'Name': 'Planetary Nebula', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(10, 300), 'HZoneDist': random.randint(6, 99)}
PulsatingVariable = {'Name': 'Pulsating Variable Star', 'Planets': True, 'SpectralType': True}
PreMainSeq = {'Name': 'Pre-Main Sequence', 'Planets': False, 'SpectralType': False}
Protostar = {'Name': 'Protostar', 'Planets': False, 'SpectralType': False}
SubStellarObj = {'Name': 'Substellar Object', 'Planets': True, 'SpectralType': False, 'HZonePer': random.uniform(0.05, 0.10), 'HZoneDist': random.uniform(0.03, 0.05)}
Subgiant = {'Name': 'Subgiant', 'Planets': True, 'SpectralType': True}
Supergiant = {'Name': 'Supergiant', 'Planets': True, 'SpectralType': True}
StellarCore = {'Name': 'Stellar Core', 'Planets': True, 'SpectralType': True}
WhiteDwarf = {'Name': 'White Dwarf', 'Planets': True, 'SpectralType': False, 'HZonePer': random.randint(50, 70), 'HZoneDist': random.randint(9, 34)}


# Attributes for Main Sequence Spectral Classes

OClass = {'HZonePer': random.randint(750, 850), 'HZoneDist': random.randint(200, 300)}
BClass = {'HZonePer': random.randint(10, 750), 'HZoneDist': random.randint(6, 200)}
AClass = {'HZonePer': random.randint(4, 10), 'HZoneDist': random.randint(3, 6)}
FClass = {'HZonePer': random.randint(1, 4), 'HZoneDist': random.randint(1, 3)}
GClass = {'HZonePer': random.uniform(0.5, 1.3), 'HZoneDist': random.uniform(0.6, 1.2)}
KClass = {'HZonePer': random.uniform(0.16, 0.5), 'HZoneDist': random.uniform(0.23, 0.6)}
MClass = {'HZonePer': random.uniform(0.16, 0.26), 'HZoneDist': random.uniform(0.19, 0.23)}
SClass = {'HZonePer': random.uniform(0.16, 0.26), 'HZoneDist': random.uniform(0.19, 0.23)}
CClass = {'HZonePer': random.uniform(0.16, 1.3), 'HZoneDist': random.uniform(0.19, 1.2)}
LClass = {'HZonePer': random.uniform(0.09, 0.15), 'HZoneDist': random.uniform(0.10, 0.15)}
TClass = {'HZonePer': random.uniform(0.09, 0.15), 'HZoneDist': random.uniform(0.10, 0.15)}
YClass = {'HZonePer': random.uniform(0.09, 0.15), 'HZoneDist': random.uniform(0.10, 0.15)}

# Attributes for Giants

RedGiant = {'HZonePer': random.randint(50, 70), 'HZoneDist': random.randint(9, 34)}
YellowGiant = {'HZonePer': random.randint(50, 70), 'HZoneDist': random.randint(9, 34)}
BlueGiant = {'HZonePer': random.randint(4, 1300), 'HZoneDist': random.randint(3, 433)}

# Tables Stellar Body Determination
Stellar_Body_Pre = {-4: InterstellarCloud, -3: H2Region, -2: MolecularCloud, 0: Protostar,
                    2: EruptiveVariable}
Stellar_Body_Star = {-4: HotSubdwarf, -3: PreMainSeq, -2: CoolSubdwarf, -1: SubStellarObj,
                     0: MainSeqStar, 2: Subgiant, 3: Giant, 4: Supergiant}
Stellar_Body_Post = {-4: StellarCore, -3: CollapsingStar, -2: PlanetaryNebula, 0: WhiteDwarf,
                     2: NeutronStar, 3: Electroweak, 4: BlackHole}
Stellar_Body_Exotic = {-4: DarkMatter, -3: AsymptoticGiant, -1: EruptiveVariable, 0: PulsatingVariable,
                       2: EruptiveVariable, 4: BlackStar}

# Typbestimmung Stern
Stellar_Body_Type = {-4: Stellar_Body_Pre, -2: Stellar_Body_Star, 3: Stellar_Body_Post, 4: Stellar_Body_Exotic}

# Spektraltypen Main Sequence Stars
SpectralType = [['O', 'B', 'F', 'K', 'K', 'M', 'M', 'M', 'M'],
                ['A', 'F', 'G', 'K', 'M', 'M', 'M', 'M', 'M'],
                ['F', 'G', 'G', 'K', 'M', 'M', 'M', 'M', 'M'],
                ['G', 'G', 'G', 'K', 'M', 'M', 'M', 'M', 'M'],
                ['K', 'K', 'K', 'K', 'K', 'M', 'M', 'M', 'M'],
                ['K', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'],
                ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'C'],
                ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'S', 'T'],
                ['M', 'M', 'M', 'M', 'M', 'M', 'C', 'L', 'Y']]

# Giant Type
GiantType = {'K': 'Red', 'M': 'Red', 'S': 'Red', 'C': 'Red',
             'G': 'Yellow', 'F': 'Yellow', 'A': 'Yellow',
             'O': 'Blue', 'B': 'Blue'}

# Planeten
Orbit = {-4: 'Highly Eccentric', -3: 'Extreme Inner', -2: 'Inner', -1: 'H-Zone - Inner', 0: 'H-Zone', 2: 'Outer',
         4: 'Extreme Outer'}
Size = {-4: 'Planetesimal', -3: 'Planetoid', -2: 'Small', -1: 'Small Standard', 0: 'Standard', 1: 'Large Standard',
        2: 'Large', 3: 'Very Large', 4: 'Giant'}
Density = {-4: 'Extremely Low', -3: 'Very Low', -2: 'Low', -1: 'Low Standard', 0: 'Standard', 1: 'High Standard',
           2: 'Dense', 3: 'Very Dense', 4: 'Extremely Dense', 10: 'Exotic'}


# Würfelwurf, 4DF
def GetFudgeResult():
    result = 0
    for i in range(0, 4):
        result += random.randint(-1, 1)
    return result


# Gibt den Wert für einen Schlüssel eines dictionary's zurück.
def GetValueForNumber(dict, number):
    # Sortiert das dictionary, damit bisect damit arbeiten kann.
    sortedKeys = sorted(dict.keys())
    #
    insertionPoint = bisect.bisect(sortedKeys, number)
    if insertionPoint > 0:
        insertionPoint = insertionPoint - 1
    key = sortedKeys[insertionPoint]
    return dict[key]


class Star:
    def __init__(self):
        starBodyDetTable = GetValueForNumber(Stellar_Body_Type, GetFudgeResult())
        starTable = GetValueForNumber(starBodyDetTable, GetFudgeResult())
        self.name = starTable['Name']
        self.spectralType = ""

        if self.isGiant():
            self.spectralType = SpectralType[GetFudgeResult() + 4][GetFudgeResult() + 4]
            if self.name == 'Giant':
                self.name = GiantType[self.spectralType]+' Giant'
            else:
                self.name = GiantType[self.spectralType]+' Supergiant'
        if starTable['SpectralType']:
            self.spectralType = ' ' + SpectralType[GetFudgeResult() + 4][GetFudgeResult() + 4]

    def isMainStar(self):
        return self.name == 'Main Sequence Star'

    def isGiant(self):
        return self.name == 'Giant' or self.name == 'Supergiant'

    def __str__(self):
        stringRepresentation = self.name
        if self.spectralType != "":
            stringRepresentation += " " + self.spectralType
        return stringRepresentation


class Planet:
    def __init__(self):
        self.satelliteModifier = 0
        self.name = "HANS " + str(random.randint(1, 10000))

    def __str__(self):
        return "A planet named " + self.name


class StarSystem:
    def __init__(self, numberOfPlanets):
        self.star = Star()
        self.planets = []
        self.age = GetValueForNumber(StarSystemAge, GetFudgeResult())
        for _ in range(numberOfPlanets):
            self.planets.append(Planet())

    def __str__(self):
        strRep = str(self.star) + "\n" + "Age: " + str(self.age)
        for p in self.planets:
            strRep += "\n" + str(p)
        return strRep


# Gravity = Density * Diameter
systems = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in systems:
    print(StarSystem(i))
