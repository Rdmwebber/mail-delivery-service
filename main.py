# RYAN WEBBER 
# STUDENT NUMBER: 011889933
import csv
from datetime import timedelta
from hash_map import HashMap
from address_distance import Address
from package import Package
from truck import Truck


# Instantiate hashMap to be used for packages
packageHashMap = HashMap()

# Instantiate Address hashMap,encoding='utf-8-sig'
gpsMap = HashMap()


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
    gpsMap.insert(normalizedAddress,address)
    
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



packageBundleOne = [1,8,13,14,15,16,19,20,21,29,30,34,37,39,40]
packageBundleTwo = [3,6,9,18,25,28,31,32,36,38]
packageBundleThree = [2,4,5,7,10,11,12,17,22,23,24,26,27,33,35]



# Instantiate first two trucks
truckOne = Truck(timedelta(hours=8),gpsMap)
truckTwo = Truck(timedelta(hours=9,minutes =5),gpsMap)
truckOne.loadTruck(packageHashMap,packageBundleOne)
truckTwo.loadTruck(packageHashMap,packageBundleTwo)


#package 9 address updated at 10:20am (410 S. State St., Salt Lake City, UT 84111)
pkgNine = packageHashMap.getValue(9)
pkgNine.zipCode = "84111"
pkgNine.address = "410 S State St"



#First two trucks start their routes (at their departureTime)
truckOne.startRoute()
truckTwo.startRoute()

#Third trucks departs when  one of the first two drivers is done their deliveries with that truck
departTime= min(truckOne.time,truckTwo.time)
truckThree = Truck(departTime,gpsMap)
truckThree.loadTruck(packageHashMap,packageBundleThree)
truckThree.startRoute()





# User interface

totalMileage = '%.2f'%(truckOne.mileage+truckTwo.mileage+truckThree.mileage)

print("The Western Governors University Parcel Service (WGUPS)")
print(f"The total mileage for today's route is {totalMileage} Miles\n")


while(True):
  try:
    time = input("For what time would you like to check the status? (enter as HH:MM)\n")
    (hrs,mins)=time.split(":")
    
    oneOrAll = input("Would you like to see the status of ONE or ALL packages? (enter ONE or ALL)\n")
  
    if(oneOrAll.lower()=="all"):
      truckOne.truckStatus(timedelta(hours=int(hrs), minutes=int(mins)),"Truck 1")
      truckTwo.truckStatus(timedelta(hours=int(hrs), minutes=int(mins)),"Truck 2")
      truckThree.truckStatus(timedelta(hours=int(hrs), minutes=int(mins)),"Truck 3")

    elif(oneOrAll.lower()=="one"): 
      pkgNum = input("Enter package ID number 1 - 40\n")
      print(packageHashMap.getValue(int(pkgNum)).packageCheck(timedelta(hours=int(hrs), minutes=int(mins))),"\n")

    
    else: 
      print("Invalid input")
  except ValueError:
    print("Invalid input")

  exit = input("Would you like to search again? (enter Y for Yes or N for No)\n")

  if (exit.lower()=="n"):
      break
  
    