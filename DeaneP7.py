class GeoPoint:

    def init(self):
        self.lat = 0
        self.lon = 0
        self.description= ""
        print('The program is initialized....')
    def SetPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def GetPoint(self):
        return (self.lat, self.lon)
    def SetDescription(self, description):
        self.description = description
    def GetDescription(self):
        return(self.description)
    
    def Distance(self,userlat,userlon):
        from math import sin, cos, sqrt, atan2, radians
        R = 3956  #radius in miles
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(userlat)
        lon2 = radians(userlon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance

    #Header
print("Welcome User")
print("This program calculates whether a location is closer to ABQ or Denver based its coordinates.")
print('Lets Begin... Share with me a location by latitude and longitude in decimal degrees.')


#Make Objects
Denver = GeoPoint()
Denver.SetPoint(39.7420, -104.9915)
Denver.SetDescription('The Mile High City.')
ABQ = GeoPoint()
ABQ.SetPoint(35.1067, -106.6291)
ABQ.SetDescription('The Land of Enchantment.')

doanother = 'y'
while doanother == 'y':
    try:   # try block: code that might cause an exception to follow 
        
#UserInput
        userlat = (float(input("Please enter the latitude of a location in decimal degrees: ".strip())))
        userlon = (float(input("Please enter the longitude of a location in decimal degrees: ".strip())))
        userlocation = (userlat, userlon)

#Distance Calculations
        distanceToOne = ABQ.Distance(userlat,userlon)
        distanceToTwo=Denver.Distance(userlat,userlon)

#UserOutput for Distance
        print('The distance to ABQ is',round(ABQ.Distance(userlat,userlon),2),' miles.')
        print('The distance to Denver is',round(Denver.Distance(userlat,userlon),2),' miles.')

        if (distanceToOne) < (distanceToTwo):
            print('\nYou are closer to',(ABQ.GetDescription()))
        else:
            print('\nYou are closer to',(Denver.GetDescription()))
    except:
        print("Something was not entered correctly. Please check your coordinates and try again. ")

    doanother = input("Would you like to try again? (y/n) ") 
    if doanother == 'n':
        print("Thanks. Goodbye!")
        break
