# 1630338
# David Leonel Gonzalez

import csv

# used the same method from part 1 of the final project that
# was derived from stackoverflow.

with open("ManufacturerList.csv", 'r') as manufacturer_list:
    inventory1 = []
    csv_reader1 = csv.reader(manufacturer_list)
    for line in manufacturer_list:
        inventory1.append(line.split(','))
# so first I opened the manufacturer list csv and converted
# into list with csv reader reading file.
# Then a for loop was created to assigned line in manufacturer list
# from inventory 1 which stackoverflow showed by appending inventory 1 and
# splitting line from manufacturer list would work properly.
# Thus, the inventory list would connect with the remaining inventory
# below

with open("PriceList.csv", 'r') as price_list:
    inventory2 = []
    csv_reader2 = csv.reader(price_list)
    for line in price_list:
        inventory2.append(line.split(','))
# same thing as above the csv file for price list was opened
# with csv reader reading file then converting into inventory 2
# same as above line was assigned to price list with a for loop created
# inventory 2 was appended with line split
# below was the same approach
with open("ServiceDatesList.csv", 'r') as service_dates_list:
    inventory3 = []
    csv_reader3 = csv.reader(service_dates_list)
    for line in service_dates_list:
        inventory3.append(line.split(','))
# as above file was open for service dates list
# csv reader was written to read file service dates list
# inventory 3 list was created from service dates list data
# for loop was created to assign line in service dates list
# with inventory 3 being appended and line being split


# now for the query part of the instructions for part 2 of final project
# I used the approach from lectures by making input statements with one asking
# for manufacturer and other for item type
    manufacturer_choice = input('Choose Manufacturer:\n')
    item_type_choice = input('Choose Item Type:\n')

# I used same approach for targeting individual values in a for loop
# from inventory 1-3 as suggested from stackoverflow
    for (item_id, manufacturer, item_type, damaged_item) in inventory1:
        for (price_id, price) in inventory2:
            for (service_id, service_date) in inventory3:
                # if statement was created to target specific details to output correct value from
                # input written in input statement
                # first if manufacturer and item type where correct then
                # Available was printed along with 'Your item is:' and the corresponding output

                if item_id == price_id and item_id == service_id and manufacturer_choice == manufacturer \
                        and item_type_choice == item_type:
                    print('Available')
                    print("Your item is:", item_id, manufacturer, item_type, price)
                break
                # adding break to stop repeating
# I chose to start a new for loop because i was having trouble with repeating of output
# in this situation i used for loop with if statement to print out different manufacturer
# with same item type and all other corresponding output
    for (item_id, manufacturer, item_type, damaged_item) in inventory1:
        for (price_id, price) in inventory2:
            for (service_id, service_date) in inventory3:
                if item_id == price_id and item_id == service_id and manufacturer_choice != manufacturer \
                        and item_type_choice == item_type:
                    print('You may, also, consider:', item_id, manufacturer, item_type, price)
                    break
                    # adding break to stop repeating
# I chose to start another for loop targeting the option of having both manufacturer and item type
# being incorrect thus printing 'no such item in inventory' with a while statement present to help
# display correct output.

    for (item_id, manufacturer, item_type, damaged_item) in inventory1:
        while False:
            if manufacturer_choice != manufacturer \
                    or item_type_choice != item_type:
                print('No such item in inventory')
            break
            # adding break to stop repeating

# lastly came the instruction to make code quit with 'q' in query
    # i took method from stack over flow to create input method different from above
    # with a while loop indicating true for input statement
    # targeting the if statement requesting if input statement equal 'q'
    # then break to quit
    choice_input = input("Choose Option:\n")
    while True:
        if choice_input == 'q':
            break
            # break ends the code continuation with 'q' input
# thus end of part 2 of final project
