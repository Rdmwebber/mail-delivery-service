class HashMap:

# Constructor function for class with default capacity of 
  def __init__(self, initialCapacity = 16):
    self.capacity = initialCapacity
    # creates a fixed array initialized with None as a value in each cell
    self.map = [None] * self.capacity
    self.count = 0


  def getHashBucket(self, key):
    hashBucket = hash(key) % self.capacity  
    return hashBucket

  def insert(self, key, value):
    hashBucket = self.getHashBucket(key)

    # if bucket is currently empty it creates a list with the first item being a nested list of the K/V
    if self.map[hashBucket] is None:
      self.map[hashBucket] = list([[key,value]])
      #increment count of hash
      self.count += 1
      self.checkLoad()
      return True

    else: 
      for item in self.map[hashBucket]: # Checks if key is already located in bucket
        if item[0] == key: #Overrides value if key is found
          item[1] = value 
          return True
      
      # if key isnt in bucket the key value pair is appended
      self.map[hashBucket].append([key,value])
       #increment count of hash
      self.count += 1
      self.checkLoad()

      

  def getValue(self, key):
    hashBucket = self.getHashBucket(key)

    for item in self.map[hashBucket]:
      if item[0] == key: # if key is found
        return item[1]  # return value
      
    return None #if Key is not found return None
  
  # checks the current load of the hashtable and if over 1.5 will trigger resize
  def checkLoad(self):
    load = self.count / self.capacity 

    if load >= 1.5:
      self.resize()

  #will copy the current items in table to a new resized table
  def resize(self):
    #change capacity of table reset count
    self.capacity *= 2
    self.count = 0

    #store current table as temp
    temp = self.map

    #create new empty expanded table
    self.map = [None] * self.capacity

    #copies elements from old table a rehashes and inserts into expanded table
    for bucket in temp:
      if bucket != None:
       for item in bucket:
          self.insert(item[0],item[1])

    temp.clear()
    







