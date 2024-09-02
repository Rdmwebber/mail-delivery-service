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
    self.status = "At hub"
    self.departureTime = None
    self.deliveryTIme = None
    