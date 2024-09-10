class Package:
   
  def __init__(self,pkgID,address,city,state,zipCode,deliveryDeadline,weight,specialNotes="No Notes"):
    self.pkgID = pkgID
    self.address = address
    self.city = city
    self.state = state
    self.zipCode = zipCode
    self.deliveryDeadline = deliveryDeadline
    self.weight = weight
    self.specialNotes = specialNotes
    self.status = "At Hub"
    self.departureTime = None
    self.deliveryTime = None
    
  #Over ride return string to print status of package object
  def __str__(self):
    return f"ID:{self.pkgID} Address:{self.address} City:{self.city} ZipCode:{self.zipCode} Weight:{self.weight} DeliveryTime:{self.deliveryTime} Status:{self.status}"
  
  #will show package status at given time
  def packageCheck(self, time):

    curStatus = "At Hub"
    deliveryPrefix="Estimated"

    if time > self.departureTime and time < self.deliveryTime:
      curStatus = "En Route"

    elif time > self.departureTime and time >= self.deliveryTime:
      curStatus = "Delivered"
      deliveryPrefix=""


    return f"ID:{self.pkgID} Address:{self.address} City:{self.city} ZipCode:{self.zipCode} Weight:{self.weight} {deliveryPrefix}DeliveryTime:{self.deliveryTime} Status:{curStatus}"