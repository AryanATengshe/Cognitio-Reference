# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:30:03 2020

@author: Aryan Tengshe
"""


def dictionary():
    
    # First of all, we make a dictionary:    
    student_dict = {
        
        "name": "Aryan",
        "age": "11",
        "standard": "7th"
        }
    # student, age, standard are the keys.
    # Aryan, 11, 7 are the values of the keys.
    print("Print the dictionary:\n", student_dict)
    
    # There is also an other way to create a dictionary:
    student_dict_2 = dict(name = "Aryan", age = "11", standard = "7th")
    print("\nCreating a dictionary with 'dict()' method:\n", student_dict_2)
    # please note:
    # we use "\n" to enter in a print.
    
    # To get the value of a key, there are 2 ways:
    
    # Example:
    print("\nExtracting the value of 'name' key:\n", student_dict["name"])
    
    # Another way is to use the get() function:
    print("\nUsing 'get()' method:\n", student_dict.get("age"))
    
    # We use the values() function to get all the values:
    print("\nExtracting all the values of all the keys:\n", student_dict.values())
    
    # We use the items() function to get the the key:
    print("\nExtracting all the key-value pairs:\n", student_dict.items(), "\n")
    
    # LOOP THROUGH THE DICTIONARY:
    print("\nPrinting all the keys of the dictionary with the loop block:")
    for x in student_dict:
        print("Key:", x)
        # You can also add any of the above functions to the loop.
        # Example:
    print("\nPrinting all the values of the dictionary with the loop block:")
    for x in student_dict:
        print("Value of key", x, "is:", student_dict[x])
    # CHANGING VALUES OF THE DICTIONARY:
    # Example:
    # Change age to 12:
        
    print("\nChanging values\nExisting value of the key 'age'\n age = ", student_dict["age"])
    student_dict["age"] = "12"
    print("\nChanged value of the key 'age'\n age = ", student_dict["age"])
    
    # TO CHECK IF THE KEY IS PRESENT IN THE DICTIONARY OR NOT:
    # To check if the key "Ammey" is there in the dictionary:
    if "standard" in student_dict:
        print("\nThe key named as 'standard' is present in the dictionary 'student_dict'")
    else:
        print("\nNo key named 'standard' is there in the dictionary")
        
    # TO DETERMINE HOW MANY ITEMS (Key-Values pairs) THE DICTIONARY HAS:
    # Use the len() function.
    print("\nDetermining the number of items in the dictionary:\n", len(student_dict))
    
    # TO ADD AN ITEM TO THE DICTIONARY:
    print("\nAdding the item with key named as 'last name':\nPrinting the dictionary before adding an item with key named as'last name':\n", student_dict)
    student_dict["last_name"] = "Tengshe"
    print("\nPrinting the dictionary after adding an item with key named as 'last name':\n", student_dict)
    
    # TO REMOVE AN ITEM FROM A DICTIONARY:
    # To remove an item, we use the pop() function.
    print("\nRemoving items\nPrinting the dictionary before removing an item with key names as 'standard':\n", student_dict)
    student_dict.pop("standard")
    print("\nPrinting the dictionary after removing an item with key named as 'standard':\n", student_dict)
    
    # The popitem function removes the last inserted item.
    print("\nPrinting the dictionary before removing the last item of the dictionary:\n", student_dict)
    student_dict.popitem()
    print("\nPrinting the dictionary after removing the last item of the dictionary:\n", student_dict)
    
    # NESTED DICTIONARIES:
    dict_of_students = {
        
        # 1st nested dictionary:
        "studend_1": {
            "name": "Aryan",
            "age": "12",
            "standard": "7th"
            },
        
        # 2nd nested dictionary:
        "student_2": {
            "name": "Shlok",
            "age": "11",
            "standard": "6th"
            },
        
        # 3rd nested dictionary:
        "student_3": {
            "name": "Ammey",
            "age": "10",
            "standard": "5th"
            }
        }
    print("\nPrinting the nested dictionary:\n", dict_of_students)
    # You can also operate nested dictionary with the functions discussed before.