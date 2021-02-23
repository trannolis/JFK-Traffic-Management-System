class Air_Traffic_Controller:
  def __init___(name, PhoneNumber, Email, Password, Airport):
    self.name = name
    self.phoneNumber = PhoneNumber
    self.email = Email
    self.password = Password #this needs to be hidden
    self.airport = Airport

  def getFlights(self):
    return ...
  def requestFlightUpdate(self, flightid):
    return ...
  def authorizeLanding(self, flightid,location):
    return ...
  def authorizeTakeOff(self, flightid,location):
    return ...
  
class Pilot:
  def __init___(Name, PhoneNumber, Email, Password, CanLand, CanTakeOff):
    self.name = Name
    self.PhoneNumber = PhoneNumber
    self.email = Email
    self.password = Password
    self.canLand = False
    self.CanTakeOff = False
  
  def updateFlightInfo(flightid,location,time):
  
  def land(flightId):

  def takeOff(flightid):
  
