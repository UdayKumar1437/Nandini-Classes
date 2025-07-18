myData = {
    "name":"Nandini",
    "age":19,
    "city":"Hyderabad",
    "isEligible":True,
    "isGraduated":False,
    "isWorking":True,
    "isMarried":False,
    "isSingle":True
}
# myData.clear() # Clears out the dict
# myKeys = myData.keys() # Get all keys
# myValues = myData.values() # Get all Values
# ans = myData.get("fullName","Nandini Sunkara") # Retrive value with key
# ans = myData.items() # Comb of both key and value pairs
# myData.pop("age") # Pop anitem with key
# myData.popitem() #Pop Last Item
# myData["isWorkingso"] = False # Update
myData.update({"state":"TG","phoneNumber":"989765412"}) #Update
print(myData)