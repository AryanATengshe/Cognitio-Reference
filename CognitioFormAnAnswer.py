# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:03:48 2020

@author: Aryan Tengshe
"""

def CognitioFormAnAnswer(usr_qstn):

    notAllwdCityArray = ["Mumbai", "Banglore", "Chennai", "Sangli", "New Delhi", "Assam", "Shimla", "Manali", "Hydrabad", "Kolkata", "Jaipur", "Patna", "Ahmedabad", "Nashik", "Bhopal", "Agra", "Indore", "Lucknow", "Nagpur", "Ipmphal", "Pondicherry"]
    answrtxtSpch = ""
    
    if usr_qstn != "Error":
        for city in notAllwdCityArray:
            if city in usr_qstn:
                answrtxtSpch = "Invalid Question"
                #print(answrtxtSpch)
                break
        
        if answrtxtSpch == "":
            if (("biggest" in usr_qstn) and ("river" in usr_qstn)):
                answrtxtSpch = answrtxtSpch + "biggest river in Pooney is moolaa river, length 22.2 km. "
                #print(answrtxtSpch)
                
            if (("smallest" in usr_qstn) and ("river" in usr_qstn)):
                answrtxtSpch = answrtxtSpch + "The smallest river in Pooney is dev river, length 5 km. "
                #print(answrtxtSpch)   
                
            if answrtxtSpch == "":
                answrtxtSpch = "Invalid Question"
        else:
            answrtxtSpch = "could not hear the question"
    
    return answrtxtSpch
    
# Now will use the dictionary instead of "if" condition.