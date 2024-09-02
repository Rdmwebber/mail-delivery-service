class HashMap:

# Constructor function for class with default capacity of 
  def __init__(self, initialCapacity = 32):
    self.capacity = initialCapacity
    # creates a fixed array initialized with None as a value in each cell
    self.map = [None] * initialCapacity

  def getHashBucket(self, key):
    hashBucket = hash(key) % self.capacity  
    return hashBucket

  def insert(self, key, value):
    hashBucket = self.getHashBucket(key)

    # if bucket is currently empty it creates a list with the first item being a nested list of the K/V
    if self.map[hashBucket] is None:
      self.map[hashBucket] = list([[key,value]])
      
      return True

    else: 
      for item in self.map[hashBucket]: # Checks if key is already located in bucket
        if item[0] == key: #Overrides value if key is found
          item[1] = value 
          return True
      
      # if key isnt in bucket the key value pair is appended
      self.map[hashBucket].append([key,value])
      

  def getValue(self, key):
    hashBucket = self.getHashBucket(key)

    for item in self.map[hashBucket]:
      if item[0] == key: # if key is found
        return item[1]  # return value
      
    return None #if Key is not found return None
    







