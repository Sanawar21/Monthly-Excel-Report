from Excel_Package import excel_functions

if __name__ == "__main__":
    print("============================================")
    print("Production Record Keeping Software For Excel")
    print("============================================")

    print()
    wb_name = input("Enter the name of your workbook: ")
    headers = input("Enter headers separated by commas.\n"
                    "OR\n"
                    "Press enter for default headers: ").split(',')
    if headers[0] == '':
        headers = ["Serial No.","Date","Particulars","Bags","Folio","Reciepts","Issued"]
    print("Enter names associated with letters.\n"
          "For Example: aa = Ahmad Ali, bs = Bajwa Saleem\n"
          "OR\n"
          "You could use default keys i.e. a,b,c,d....\n"
          "OR\n"
          "You could upload a text file of the keys in the same format.\n")
    print()
    key_num_4_names = input("Press enter for default keys.\n"
                            "Press 1 for text file upload.\n"
                            "Press 2 for creating keys here.\n")
    keys_and_names = excel_functions.get_keys_of_names(key_num_4_names)

    starting_folio = int(input("Enter starting folio: "))
    starting_date = input("Enter starting date (dd/mm/yyyy): ")
    kgPerBag = (input("Kilogram per bag (optional, 25 by default): "))
    separator = input("In-program separator (optional, space by default): ")
    print()
    print()
    if kgPerBag == '':
        kgPerBag = 25
    else:
        kgPerBag = int(kgPerBag)
    if separator == '':
        separator = ' '

    received_list = []
    class_Received = []
    current_date = starting_date
    print("Enter the dates and names for bags received.")
    yORn = input("Do you want to enter a text file? (y/n) ")
    if yORn == 'n':
        print("Enter in the following format: ")
        print("<date><separator><name key>")
        print()
        Exec = True
        while Exec:
            for key,val in keys_and_names.items():
                print(f"{key} is {val}")
            print()
            raw_input = input("-->  ")
            raw_input = raw_input.split(separator)
            print(raw_input)
            if raw_input[0] != '':
                # raw_date = excel_functions.get_raw_date(raw_input)
                name = excel_functions.get_name(raw_input,keys_and_names)
                date = excel_functions.make_date_new(current_date,raw_input)
                received_list.append([date,name])
                current_date = date
            else:
                Exec = False
    else:
        file = input("Enter in the file name: ")+'.txt'
        if file == '$.txt':
            file = '../recieved.txt'
        lines = excel_functions.get_data_from_txt(file)
        for line in lines:
            line = line.split(separator)
            name = excel_functions.get_name(line,keys_and_names)
            date = excel_functions.make_date_new(current_date,line)
            received_list.append([date,name])
            current_date = date



    print("Now enter the number of bags.")
    q = excel_functions.ask_for_text()
    if not q:
        print("Enter the bags for the following: ")
        for reciepts in received_list:
            bags = int(input(f"{reciepts[0]}---{reciepts[1]}---> "))
            reciepts.append(bags)
    else:
        file = input("Enter the name of the text file: ")+'.txt'
        if file == '$.txt':
            file = '../bags.txt'
        lines = excel_functions.get_data_from_txt(file)
        for reciepts in received_list:
            ind = received_list.index(reciepts)
            reciepts.append(int(lines[ind]))
    #
    received_class_list = excel_functions.convert_to_class("received",received_list,kgPerBag)
    #
    issued_list = []
    current_date = starting_date
    print()
    print()
    print()
    print("Now enter the dates and names for issued.")
    yORn = input("Do you wish to provide a text file? (y/n)")
    if yORn == 'y':
        file = input("Enter the name of the file: ")+'.txt'
        if file == '$.txt':
            file = '../issued.txt'
        datalist = excel_functions.get_data_from_txt(file)
        for line in datalist\
                :
            line = line.split(separator)
            name = excel_functions.get_name(line,keys_and_names)
            date = excel_functions.make_date_new(current_date,line)
            issued_list.append([date,name])
            current_date = date
    else:
        print("Enter in the following format: ")
        print("<date><separator><name key>")
        print()
        Exec = True
        while Exec:
            for key, val in keys_and_names.items():
                print(f"{key} is {val}")
            print()
            raw_input = input("-->  ")
            raw_input = raw_input.split(separator)
            # print(raw_input)
            if raw_input[0] != '':
                # raw_date = excel_functions.get_raw_date(raw_input)
                name = excel_functions.get_name(raw_input, keys_and_names)
                date = excel_functions.make_date_new(current_date,raw_input)
                issued_list.append([date, name])
                current_date = date
            else:
                Exec = False
    print()
    print()
    print("Now enter the weight issued.")
    q = excel_functions.ask_for_text()
    if not q:
        print("Enter the issued weight for the following: ")
        for issued in issued_list:
            bags = float(input(f"{issued[0]}---{issued[1]}---> "))
            issued.append(bags)
    else:
        file = input("Enter the name of the text file: ")+'.txt'
        if file == '$.txt':
            file = '../weight.txt'
        lines = excel_functions.get_data_from_txt(file)
        for issued in issued_list:
            ind = issued_list.index(issued)
            issued.append(float(lines[ind]))
    # print(issued_list)
    folio = starting_folio
    for issued in issued_list:
        issued.insert(2,folio)
        folio+=1
    #
    issued_class_list = excel_functions.convert_to_class('issued',issued_list,kgPerBag)
    #

    full_sorted_list = excel_functions.add_serials_and_sort(issued_class_list,received_class_list)

    print()
    print()
    print()
    print("Data collected!")
    yORn = input("Do you wish to see the data? (y/n) ")
    if yORn == 'y':
        print()
        print()
        excel_functions.print_as_table(headers,full_sorted_list)
    else:
        pass
    backup = input("Do you wish to backup? (y/n) ")
    if backup == 'y':
        excel_functions.make_backup(full_sorted_list,keys_and_names)

    print()
    print("Making the excel file...")
    excel_functions.make_excel_file(full_sorted_list,headers,wb_name)
    print()
    print("Done!")
    print()
    for x in received_list:
        print(x)
    print()
    for x in issued_list:
        print(x)
    Exec = True
    while Exec:
        if input("Press q to quit: ") == 'q':
            Exec = False
        else:
            pass