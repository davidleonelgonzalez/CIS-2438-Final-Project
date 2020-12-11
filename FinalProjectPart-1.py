# 1630338
# David Leonel Gonzalez

import csv

# the idea for the concept of converting csv file into list was derived
# from discussing with TA.
# though stackoverflow suggested the format below would work best
# for joining csv files together

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


# now for the approach of writing the 4 output files i took into consideration
# the approach of stackoverflow of joining input files

# i opened full inventory csv as a with statement assigning full_inventory as variable
# csv writer 1 as variable to write csv of full inventory
with open("FullInventory.csv", 'w') as full_inventory:
    csv_writer1 = csv.writer(full_inventory, delimiter=',')

    # i included a for loop to include the variables from each inventory assigned from each input file
    for (item_id, manufacturer, item_type, damaged) in inventory1:
        for (price_id, price) in inventory2:
            for (service_id, service_date) in inventory3:
                # an if statement was included to specify requirements of the full inventory file
                if item_id == price_id and item_id == service_id:
                    csv_writer1.writerow([item_id, manufacturer, item_type, [price], [service_date], [damaged]])
                    # lastly wrote csv writer 1 to writerow to write input to output file full_inventory

# i opened laptop inventory csv as a with statement assigning laptop_inventory as variable
# csv writer 2 as variable to write csv of laptop inventory
    with open("LaptopInventory.csv", 'w') as laptop_inventory:
        csv_writer2 = csv.writer(laptop_inventory, delimiter=',')

        # same approach as above i included a for loop to include the variables from each
        # inventory assigned from each input file
        for (item_id, manufacturer, item_type, damaged) in inventory1:
            for (price_id, price) in inventory2:
                for (service_id, service_date) in inventory3:

                    # an if statement was included to specify requirements of the laptop inventory output file
                    # this time i called for item type to be a laptop
                    if item_id == price_id and item_id == service_id and item_type == 'laptop':
                        csv_writer2.writerow([item_id, manufacturer, [price], [service_date], [damaged]])
                    # lastly wrote csv writer 1 to writerow to write input to output file laptop_inventory

# i opened laptop inventory csv as a with statement assigning service_date_inventory as variable
# csv writer 3 as variable to write csv of service date inventory
        with open("PastServiceDateInventory.csv", 'w') as service_date_inventory:
            csv_writer3 = csv.writer(service_date_inventory, delimiter=',')

            # same approach as above i included a for loop to include the variables from each
            # inventory assigned from each input file
            for (item_id, manufacturer, item_type, damaged) in inventory1:
                for (price_id, price) in inventory2:
                    for (service_id, service_date) in inventory3:

                        # an if statement was included to specify requirements of the service dates inventory
                        # this time i called for service date to be past service date
                        if item_id == price_id and item_id == service_id and service_date >= '12/11/2020':
                            csv_writer3.writerow([item_id, manufacturer, item_type, [price], [service_date], [damaged]])
                        # lastly wrote csv writer 3 to writerow to write input to output file service_dates_inventory

# i opened damaged inventory csv as a with statement assigning damaged_inventory as variable
# csv writer 4 as variable to write csv of damaged inventory
            with open("DamagedInventory.csv", 'w') as damaged_inventory:
                csv_writer4 = csv.writer(damaged_inventory, delimiter=',')

                # same approach as above i included a for loop to include the variables from each
                # inventory assigned from each input file
                for (item_id, manufacturer, item_type, damaged) in inventory1:
                    for (price_id, price) in inventory2:
                        for (service_id, service_date) in inventory3:
                            # an if statement was included to specify requirements of the damaged inventory output file
                            # this time i called for damaged item in column damaged
                            if item_id == price_id and item_id == service_id and damaged == 'damaged':
                                csv_writer4.writerow([item_id, manufacturer, item_type, [price], [service_date]])

                            # lastly wrote csv writer 4 to writerow to write input to output file damaged_inventory
# now all 4 required output files have been created with corresponding output
# full inventory, laptop inventory, service dates inventory, and damaged inventory have been created
# from the input files manufacturer list, price list, and service list
# the end of part 1 of the final project
