from datetime import timedelta
class Truck:

  def __init__(self,packages,departureTime):
    self.packages = packages
    self.depatureTime = departureTime
    self.speed = 18
    self.time = departureTime
    self.capacity = 16
    self.mileage = 0

  def updateTime(self,distance):
    self.time += timedelta(distance/self.speed)

  def increaseMileage(self,miles):
    self.mileage+=miles


