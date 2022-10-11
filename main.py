import random
from unittest import result 

destination_list = ['Chicago', 'Cincinnati', 'Detroit', 'Indianapolis']
restaurant_list = ['Wing Stop', 'Longhorns', 'Four Day Ray', 'Kilroys']
transportation_list = ['Party Bus', 'Personal Car', 'Rental Car', 'Motorycles']
entertainment_list = ['Comedy Show', 'Concert', 'Trade Show', 'Golfing']

print("Welcome to your Day Trip Generator! You will be randomly selected a City, Restaurant, Entertainment and Vehicle.")

def random_picker(list):
    random_item = random.choice(list)
    return random_item

def destination():
    random_dest = random_picker(destination_list)
    print("City: " + random_dest)
    print("Do you like your chosen Destination? Y or N")
    answer = input('')
    while answer == 'N':
        if answer == 'N':
            random_dest = random_picker(destination_list)
            print(f'How about {random_dest}')
            print("Do you like your chosen destination? Y or N")
            answer = input('')
    if answer == 'Y':
        print(f'I like {random_dest}')
        return random_dest

def entertainment():
    random_fun = random_picker(entertainment_list)
    print("Entertainment: " + random_fun)
    print("Do you like your chosen Entertainment? Y or N")
    answer = input('')
    while answer == 'N':
        if answer == 'N':
            random_fun = random_picker(entertainment_list)
            print(f'How about {random_fun}')
            print("Do you like your chosen Entertainment? Y or N")
            answer = input('')
    if answer == 'Y':
        print("Have fun!")
        return random_fun

def transportation():
    random_vehicle = random_picker(transportation_list)
    print("Vehcile: " + random_vehicle)
    print("Do you like your chosen Entertainment? Y or N")
    answer = input('')
    while answer == 'N':
        if answer == 'N':
            random_vehicle = random_picker(transportation_list)
            print(f'How about {random_vehicle}')
            print("Do you like your chosen vehicle? Y or N")
            answer = input('')
    if answer == 'Y':
        print("Drive Safe!")
        return random_vehicle

def restaurant():
    random_eatery = random_picker(restaurant_list)
    print("Restaurant: " + random_eatery)
    print("Do you like your chosen Restaurant? Y or N")
    answer = input('')
    while answer == 'N':
        if answer == 'N':
            random_eatery = random_picker(restaurant_list)
            print(f'How about {random_eatery}')
            print("Do you like your chosen restaurant? Y or N")
            answer = input('')
    if answer == 'Y':
        print(f'Enjoy {random_eatery}!')
        return random_eatery

confirmed_dest = destination()  
confirmed_ent = entertainment()
confirmed_vehicle = transportation()
confirmed_eatery = restaurant()
full_trip = confirmed_dest, confirmed_vehicle, confirmed_ent, confirmed_eatery

print(f'Thank you for confirming all of your choices.')
print(full_trip)