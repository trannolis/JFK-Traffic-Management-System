# This class represents the person who will be handling the flight schedule management and assignment
class Air_Traffic_Controller:
  def __init___(name, PhoneNumber, Email, Password, Airport):
    self.name = name
    self.phoneNumber = PhoneNumber
    self.email = Email
    self._password = Password #this needs to be hidden
    self.airport = Airport

  #For the air traffic controller to be able to see all the flights 
  def getFlights(self):
    return ...
  #To see the current flight status of a particular flight 
  def requestFlightUpdate(self, flightid):
    return ...
  #To authorize landing on the runway for a particular flight
  def authorizeLanding(self, flightid,location):
    return ...
  #To authorize takeoff on the runway for a particular flight
  def authorizeTakeOff(self, flightid,location):
    return ...

#This class represents the pilots who will be communicating with the Air Traffic Controller
class Pilot:
  def __init___(Name, PhoneNumber, Email, Password, CanLand, CanTakeOff):
    self.Name = Name
    self.PhoneNumber = PhoneNumber
    self.Email = Email
    self.Password = Password
    self.canLand = False
    self.CanTakeOff = False
  
  #For the pilot to be able to make any changes mid-flight if necessary 
  def updateFlightInfo(flightid,location,time):
    return ...
  #for the pilot to indicate that the plane has landed 
  def land(self, flightId):
    return ... 
  #for the pilot to indicate that the plane has taken off
  def takeOff(self, flightid):
    return ...
    
#This class represents the flights that might be landing, taxiing or taking off.
class Flight:
  def __init___(flightID, airplaneID, arrivalTime, departureTime, arrivalLocation, departureLocation, Location)
  #Note: need to address location in air vs location on ground
    self.flightId = flightID
    self.airplaneID = airplaneID
    self.arrivalTime = arrivalTime
    self.departureTime = departureTime
    self.arrivalLocation = arrivalLocation
    self.departureLocation = departureLocation
    self.Location= Location
  #to be able to see arrival time of the flight 
  def getArrivalTime(self):
    return arrivalTime
  #to be able to see arrival time of the flight
  def getDepartureTime(self):
    return departureTime
  
  #No cancel function
  def __del__(self):

  #Setters for arrival and depature times and locations  
  def setArrivalTime(self, time):
    self.arrivalTime = time
    return True
  
  def setDepartureTime(self, time):
    self.departureTime = time
    return True
  
  def changeArrivalLocation(self,location):
    self.arrivalLocation = location
    return True

  def changeDepatureLocation(self,location):
    self.departureLocation = location
    return True

#This represents the individual gates at the airport
class Location:
  def __init___(AiportCode, Gate, IsVacant):
    self.AirportCode = AiportCode
    self.Gate = Gate
    self.IsVacant = False
  
  #to change the status gate availability
  def updateVacancyStatus(self, vacancyStatus):
    self.vacancyStatus = vacancyStatus
    
  #to get current status of the gates of the arrival gate
  def getVacancyStatus(self):
    return self.IsVacant

#This represents the airport at which the planes will be landing and taking off
class Airport:
  def __init___(flights, AirTrafficControllers, runway1=False, runway2=False, runway3=False, runway4=False):
    self.flights = flights
    self.AirTrafficControllers = AirTrafficControllers
     
  #to add new flight record at the airport
  def addFlight(self, flightid):
    return True
  
  def updateRunway1(self, new_status):
    self.runway1 = new_status
    return True
  def updateRunway2(self, new_status):
    self.runway2 = new_status
    return True
  def updateRunway3(self, new_status):
    self.runway3 = new_status
    return True
  def updateRunway4(self, new_status):
    self.runway4 = new_status
    return True
