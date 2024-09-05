from datetime import timedelta
class Truck:

  def __init__(self,packages,departureTime,currentLocation,gpsMap):
    self.packages = packages
    self.gpsMap = gpsMap
    self.depatureTime = departureTime
    self.speed = 18
    self.time = departureTime
    self.capacity = 16
    self.mileage = 0
    self.currentLocation = currentLocation

  def updateTime(self,distance):
    self.time += timedelta(distance/self.speed)

  def increaseMileage(self,miles):
    self.mileage+=miles


  #Check distance to next address
  def checkDistance(self,locationOne,locationTwo):
    curAddress= self.gpsMap.getValue(locationOne)
    nextAddress= self.gpsMap.getValue(locationTwo)

  #distance reference isn't bidirectional so you have to check both x(y) and y(x)
    if curAddress.getDistance(nextAddress.index) == "":
     return nextAddress.getDistance(curAddress.index)
    else: 
      return curAddress.getDistance(nextAddress.index)
   
   # find which package in the truck that hasn't been delivered is closest  
  def nextClosest(self):
    minDistance = float('inf')
    closestPackage = self.packages[0]

    for pkg in self.packages:

      distance = self.checkDistance(self.currentLocation,pkg.address)

      if pkg.status != "Delivered" and distance < minDistance:
        minDistance = distance
        closestPackage = pkg
    
    return closestPackage


  def loadTruck(self,packageHashMap, packageIDs)
    for id in packageIDs:
      
    
 