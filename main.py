
# Lists with data
destination_list = ['Chicago', 'Cincinnati', 'Detroit', 'Indianapolis']
restaurant_list = ['Wing Stop', 'Longhorns', 'Four Day Ray', 'Kilroys']
transportation_list = ['Party Bus', 'Personal Car', 'Rental Car', 'Motorycles']
entertainment_list = ['Colts Game', 'Bears Game', 'Lions Game', 'Bengals Game']
    

import random 

random_city = random.choice(destination_list)
print("Destination City is: " + str(random_city))

if random_city == "Chicago":
    print("Entertainment: Bears Game")
if random_city == "Cincinnati":
    print("Entertainment: Bengals Game")
if random_city == "Detroit":
    print("Entertainment: Lions Game")
if random_city == "Indianapolis":
    print("Entertainment: Colts Game")

random_restaurant = random.choice(restaurant_list)
print("Restaurant: " + str(random_restaurant))

random_transportation = random.choice(transportation_list)
print("Transportation: " + str(random_transportation))


