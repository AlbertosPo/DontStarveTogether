import numpy as np
import pandas as pd
import random



class DataOfCharacter:
    def __init__(self,name_in,Health_in,Hunger_in ,Sanity_in,Special_Ability_in):
        self.name = name_in
        self.health = Health_in
        self.hunger = Hunger_in
        self.sanity = Sanity_in
        self.special_ability = Special_Ability_in

    def getter(self):
        return self.name, self.health, self.hunger, self.sanity, self.special_ability
    
    def get_Name(self):
        return self.name

    def get_Special_Ability(self):
        return self.special_ability



    def setter(self,ChangeType,ChangeValue):
        if ChangeType == "name":
            self.name = ChangeValue
        elif ChangeType == "health":
            self.health = ChangeValue
        elif ChangeType == "hunger":
            self.hunger = ChangeValue
        elif ChangeType == "sanity":
            self.sanity = ChangeValue
        elif ChangeType == "special_ability":
            self.special_ability = ChangeValue
        else:
            print("You give me wrong type to change")

    
    



def SplittingData(data_in):
    names = data_in["Name"]
    healths = data_in["Health"]
    hungers = data_in["Hunger"]
    sanities = data_in["Sanity"]
    special_abilities = data_in["Special_Ability"]

    #Finding how many ids exist into the data set . 
    #we can take same result if we use method len in any data set(names, healths,hungers ... etc.)
    numberOfIds = data_in["Name"].value_counts().count()

    

    return names,healths,hungers,sanities,special_abilities,numberOfIds


def List_of_Objects(data_in):
    names,healths,hungers,sanities,special_abilities,numberOfIds = SplittingData(data_in)

    ListOfObjects = []
    for i in range(numberOfIds):
        ListOfObjects.append(DataOfCharacter(names[i],int(healths[i]),int(hungers[i]),int(sanities[i]),special_abilities[i]))

    return ListOfObjects


def PrintingDataOfObjects(ListOfObjects_in):
    for i in range(len(ListOfObjects_in)):
        print(ListOfObjects_in[i].getter())

def PickRandomlySomeObjects(ListOfObjects_in):
    RandomlyPickedObjects = random.sample(ListOfObjects_in, 3)
    for RandObj in RandomlyPickedObjects:
        print ("\n")
        print("Name : ",RandObj.get_Name())
        print("Special Ability : ",RandObj.get_Special_Ability())


DataDST = pd.read_csv("DSTdata.csv")

Object_List =List_of_Objects(DataDST)

PrintingDataOfObjects(Object_List)
PickRandomlySomeObjects(Object_List)

