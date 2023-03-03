#what does this code do?
"""this code gets a part of a text from the user and extract the vowels
from it and stablish a dictionary of that vowels"""
#exaple: {a: 3, i:5,...}

text = input("please enter your text : ")
list_of_alphabets = list(text)
vowels_list =[]
for i in list_of_alphabets:
    if i in ["u", "o", "i", "e", "a"]:
        vowels_list.append(i)
a=vowels_list.count("a") 
e=vowels_list.count("e")
i=vowels_list.count("i")
o=vowels_list.count("o")
u=vowels_list.count("u")
information={"a":a, "e":e, "i":i , "o":o, "u":u}
for k, v in sorted(information.items()):
    print(k ,"found", v, "times")
