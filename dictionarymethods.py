#mydict.keys # returns all keys
# mydict.values() #returns all values
# mydict.items() #retuens all ( keys, values ) pairs as tuples
#mydict.get("key""") # retuns the key according to value 
#mydict.update ( newdict)# inserts the specified items to the diction
student = {
    "name" : "rahul  kumar",
    "sujects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95,
    }
}

print(list(student.keys()))# ab ye isko ak list main kr de ga 
print(student.keys())# returns all keys 
print(len(student)) #total number of keys value pair jis se dictionary ke lenght aa jai g
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))# return value in the form of list
print(student.items())# in the form of pairs
print(list(student.items())) # into typecast 
pairs = list(student.items())
print(pairs[0])