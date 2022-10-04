import random
from unittest import result 

destination_list = ['Chicago', 'Cincinnati', 'Detroit', 'Indianapolis']
restaurant_list = ['Wing Stop', 'Longhorns', 'Four Day Ray', 'Kilroys']
transportation_list = ['Party Bus', 'Personal Car', 'Rental Car', 'Motorycles']
entertainment_list = ['Comedy Show', 'Concert', 'Trade Show', 'Golfing']

def random_city(destination_list):
    random_city = random.choice(destination_list)
    print(random_city)
    return random_city
print("City: " + str(random.choice(destination_list)))

print("Do you like your chosen Destination? Y or N")
answer = input('')
if answer == 'N':
    print(random_city(destination_list))
    print("Do you like your chosen destination? Y or N")
    answer = input('')
elif answer == 'Y':
    print("I like that place!"


def random_entertainment(entertainment_list):
    random_entertainment = random.choice(entertainment_list)
    return random_entertainment
print("Entertainment: " + str(random.choice(entertainment_list)))

print("Do you like your chosen Entertainment? Y or N")
answer = input('')
while answer == 'N':
    print(random_entertainment(entertainment_list))
    print("Do you like your chosen Entertainment? Y or N")
    answer = input('')
if answer == 'Y':
    print('Have fun!') 


def random_restaurant(restaurant_list):
    random_restaurant = random.choice(restaurant_list)
    return random_restaurant
print("Restaurant: " + str(random.choice(restaurant_list)))

print("Do you like the restaurant that was chosen? Y or N")
answer = input('')
while answer == 'N':
    print(random_restaurant(restaurant_list))
    print("Do you like the restaurant that was chosen? Y or N")
    answer = input('')
if answer == 'Y':
    print('Hope you enjoy the restaurant!')


def random_transportation(transportation_list):
    random_transportation = random.choice(transportation_list)
    return random_transportation
print("Mode of transportation: " + str(random.choice(transportation_list)))

print("Do you like this mode of transportation?: Y or N")
answer = input('')
while answer == 'N':
    print(random_transportation(transportation_list))
    print("Do you like this mode of transportation that was chosen? Y or N")
    answer = input('')
if answer == 'Y':
    print('Hope you have a safe travel!')


print("Enjoy the trip you have selected!")