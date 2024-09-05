from datetime import timedelta
class Truck:

  def __init__(self,departureTime,gpsMap,currentLocation='HUB'):
    self.packages = []
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
     return float(nextAddress.getDistance(curAddress.index))
    else: 
      return float(curAddress.getDistance(nextAddress.index))
   
   # find which package in the truck that hasn't been delivered is closest using nearest neighbour. Time complexity of O(nm)
  def nextClosest(self):
    minDistance = float('inf')
    closestPackage = self.packages[0]

    for pkg in self.packages:

      distance = self.checkDistance(self.currentLocation,pkg.address)

      if pkg.status != "Delivered" and distance < minDistance:
        minDistance = distance
        closestPackage = pkg

        print("Shortest is", minDistance)
        print("")
    
    return [closestPackage,minDistance]
  
  def deliverPackage(self,nextPackage,distance):
    #update truck data
    
    self.currentLocation = nextPackage.address
    print("PACKAGE DELIVERED AT", self.currentLocation)
    self.mileage+= distance
    print("MILEAGE IS NOW ", self.mileage)
    self.time += timedelta(hours=distance/self.speed)
    print("The time is", self.time)

    #update package data
    nextPackage.status = "Delivered"
  
  def startRoute(self):
    for i in range(1,len(self.packages)):
      (nextPackage,distance) = self.nextClosest()
      self.deliverPackage(nextPackage,distance)


  def loadTruck(self,packageHashMap, packageIDs):
    for id in packageIDs:
      pkg = packageHashMap.getValue(id)
      pkg.departureTime = self.time
      pkg.status = "On Truck"
      self.packages.append(pkg)

    
 