'''
Read the file 'iris.json' as a text file :

1. Create a list having each line of the file as an element
2. Convert it into a list of dictionary objects.
3. Show the details of all flowers whose species is
"setosa".
4. Print the minimum petal area and max sepal area in
each species
5. Sort the list of dictionaries according to the total area
are sepal and petal.
'''

import json
import os
global data


def speciesdat(data):
    species_stats = {}
    for flower in data:
        species = flower["species"]
        petal_area = flower["petal_length"] * flower["petal_width"]
        sepal_area = flower["sepal_length"] * flower["sepal_width"]
        
        if species not in species_stats:
            species_stats[species] = {"min_petal_area": petal_area, "max_sepal_area": sepal_area}
        else:
            species_stats[species]["min_petal_area"] = min(species_stats[species]["min_petal_area"], petal_area)
            species_stats[species]["max_sepal_area"] = max(species_stats[species]["max_sepal_area"], sepal_area)

    print("Species Statistics:", species_stats)

def main():

    ch=input("""
1. Create a list having each line of the file as an element
2. Convert it into a list of dictionary objects.
3. Show the details of all flowers whose species is
"setosa".
4. Print the minimum petal area and max sepal area in
each species
5. Sort the list of dictionaries according to the total area
are sepal and petal.
        (1-5):
             """)

    match(ch):
        case '1':
            print(data)
        case '2':
            lis=[]
            for x in data:
                lis.append(dict(data[x]))
            print(f"list={lis}")
        case '3':
            for x in data:
                if data[x].get("species")=="setosa":
                    print(data[x])
        case '4':
            # unique=set()
            # newlist=[]
            # cnt=1
            # for x in data:
            #     unique.add(data[x].get("species"))
            #     # if unique.__contains__(data[x].get("species")):
            #     #     print({data[x]})
            #     #     unique[x].update({data[x]})
            #     #     print(unique)
            #     # print(data[x].get("species"))
            #     # unique.update(data[x].get("species"))
            # print(unique)
            # for i in len(unique):
            #     for x in data:
            #         if unique[i]==data[x].get("species"):
            
                 speciesdat(data)       

        case '5':
            exit()

if os.path.exists('Lab2\iris.json'):
    with open('Lab2\iris.json','r') as f:
        data=json.load(f)
    main()
else:
    print("File dont exist")