#nested dictionary ak dict main dosri dict create kr dna 

student = {
    "name" : "rahul kumar",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95,
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"]) # agr muje surf chem ke marks print krwane hai 
