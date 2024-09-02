from hash_map import HashMap
import csv
from address_distance import Address
from package import Package


# Instantiate hashMap to be used for packages
packageHashMap = HashMap()

# Instantiate Address hashMap,encoding='utf-8-sig'
addressHashMap = HashMap()


#Open CSV Files
#Parse Address files
with open('CSV/DistanceTable.csv','r',encoding='utf-8-sig') as csvAddresses:
  csvReader = csv.reader(csvAddresses)
  #index to use a reference to distance array
  index = 0
  for line in csvReader:
   #normalize name data and remove repeat addresses
    normalizedLocationName = line[0].split("\n")[0].strip()

  #normalize Address info to use as lookup. hub address doenst include address info so its inserted as is (stripped)
    normalizedAddress = line[1].strip()
    if len(line[1].strip()) > 3:
      normalizedAddress = line[1][:-7].strip()
    
    distanceList = []
    for i in range(2,len(line)):
      
      distanceList.append(line[i])

    
    #Create new address instance
    address = Address(normalizedLocationName,normalizedAddress,distanceList,index)

    #add address instance to hashMap
    addressHashMap.insert(address.address,address)
    
    index+= 1

#Open and parse Package csv
with open('CSV/PackageFile.csv','r',encoding='utf-8-sig') as csvPackages:
  csvReader = csv.reader(csvPackages)
  for line in csvReader:
    pkgId = int(line[0])
    address = line[1]
    city = line[2]
    state = line[3]
    zipCode = line[4]
    deliveryDeadline = line[5]
    weight = line[6]
    specialNotes = line[7]


    #create package instance from csv
    package = Package(pkgId,address,city,state,zipCode,deliveryDeadline,weight,specialNotes)

    #insert package into hashmap
    packageHashMap.insert(pkgId,package)



