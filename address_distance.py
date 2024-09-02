class Address:
  def __init__(self,locationName,address,distanceList,index):
    #normalize name data and remove repeat address
    self.locationName = locationName
    self.address = address 
    self.distanceList = distanceList
    self.index = index

    def getDistance(index):
      return distanceList[index]