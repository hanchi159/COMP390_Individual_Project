

class MeteorDataEntry:
    def __init__(self, nm, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation, states, countries):
        self.name = nm
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.states = states
        self.countries = countries


# Name, id, nametype, recclass, mass (g), fall, year, reclat, reclong, GeoLocation, States, Countries
f = open('meteorites_test.txt', 'r')

firstline = f.readline()
firstline = firstline.split("\t")
entry_meteor = MeteorDataEntry(firstline[0],firstline[1],firstline[2],firstline[3],firstline[4],firstline[5],firstline[6],firstline[7], firstline[8],firstline[9],firstline[10],firstline[11])
print(entry_meteor.countries)
# meteor1 = f.readline().split()
# print(meteor1[0], meteor1[4])

name_label = 'NAME'
mass_label = 'MASS (g)'
print(f'{name_label:<24}{mass_label:<20}')
print("="*44)
# print(f'{meteor1[0]:24}{meteor1[4]:20}')
tempmeteor = "none"
meteorlist = []
meteorlist_year = []
while tempmeteor[0] != "Zulu Queen":
    templine = f.readline()
    tempmeteor = templine.split("\t")
    tempmeteorclass = ''
    # print(len(tempmeteor))
    if tempmeteor[4] == '' and len(tempmeteor) >= 10:
        tempmeteor[4] = 0
    elif '.' in tempmeteor[4] and len(tempmeteor) >= 10:
        temp = tempmeteor[4].split('.')
        mass_int = int(temp[0])
        if mass_int > 2900000:
            tempmeteorclass = MeteorDataEntry(tempmeteor[0],tempmeteor[1],tempmeteor[2],tempmeteor[3],tempmeteor[4],tempmeteor[5],tempmeteor[6],tempmeteor[7],tempmeteor[8],tempmeteor[9],tempmeteor[10],tempmeteor[11])
            # print(f'{tempmeteor[0]:<24}{tempmeteor[4]:20}')
            print('added')
            meteorlist.append(tempmeteorclass)
    elif len(tempmeteor) >= 10:
        mass_int = int(tempmeteor[4])
        if mass_int > 2900000:
            tempmeteorclass = MeteorDataEntry(tempmeteor[0], tempmeteor[1], tempmeteor[2], tempmeteor[3], tempmeteor[4],
                                              tempmeteor[5], tempmeteor[6], tempmeteor[7], tempmeteor[8], tempmeteor[9],
                                              '', '')
            meteorlist.append(tempmeteorclass)

    if len(tempmeteor) >= 7 and tempmeteor[6] != '':
        year_int = int(tempmeteor[6])
        if year_int >= 2013:
            tempmeteorclass = MeteorDataEntry(tempmeteor[0], tempmeteor[1], tempmeteor[2], tempmeteor[3], tempmeteor[4],
                                              tempmeteor[5], tempmeteor[6], tempmeteor[7], tempmeteor[8], tempmeteor[9],
                                              '', '')
            meteorlist_year.append(tempmeteorclass)
# print(f'{tempmeteor[0]:<24}{tempmeteor[4]:<20}')

for meteor in meteorlist:
    print(f'{meteor.name:<24}{meteor.mass:20}')

print()
name_label = 'NAME'
mass_label = 'YEAR'
print(f'{name_label:<24}{mass_label:<20}')
print("="*44)

for meteor in meteorlist_year:
    print(f'{meteor.name:<24}{meteor.year:20}')