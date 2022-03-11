from Excel_Package import excel_functions

if __name__ == "__main__":
    xlsx_name = input("Document name: ")
    headers = ["Serial No.","Date","Particulars","Bags","Folio","Reciepts","Issued"]
    starting_date = input("Starting Date: ")
    starting_folio = int(input("Starting Folio: "))
    dir_name = input("Data Directory: ")
    keys, dnm_recieved, bags, dnm_issued, weight = 1,2,3,4,5
    all_text_files = [keys,dnm_recieved,bags,dnm_issued,weight]

    for file in all_text_files:
        newfile = f"{dir_name}/{file}.txt"
        all_text_files[all_text_files.index(file)] = newfile

    keys_and_names = {}
    with open(all_text_files[0],'r') as keys:
        lines = keys.readlines()
        for line in lines:
            key,val = line.split('=')
            keys_and_names[key] = val.strip()

    received_list = []
    current_date = starting_date
    lines = excel_functions.get_data_from_txt(all_text_files[1])
    for line in lines:
        line = line.split(' ')
        name = excel_functions.get_name(line,keys_and_names)
        date = excel_functions.make_date_new(current_date,line)
        received_list.append([date,name])
        current_date = date

    bagz = excel_functions.get_data_from_txt(all_text_files[2])
    for bags in bagz:
        bagz[bagz.index(bags)] = int(bags)
    for received in received_list:
        received.append(bagz[received_list.index(received)])

    received_class_list = excel_functions.convert_to_class("received",received_list)


    issued_list = []
    current_date = starting_date
    folio = int(starting_folio)
    lines = excel_functions.get_data_from_txt(all_text_files[3])
    for line in lines:
        line = line.split(' ')
        name = excel_functions.get_name(line,keys_and_names)
        date = excel_functions.make_date_new(current_date,line)
        issued_list.append([date,name,folio])
        folio += 1
        current_date = date

    issued = excel_functions.get_data_from_txt(all_text_files[4])
    for issuede in issued_list:
        issuede.append(float(issued[issued_list.index(issuede)]))

    issued_class_list = excel_functions.convert_to_class('issued',issued_list)

    full_sorted_list = excel_functions.add_serials_and_sort(issued_class_list,received_class_list)

    print()
    excel_functions.print_as_table(headers,full_sorted_list)
    print()
    print("Making excel file. ")
    excel_functions.make_excel_file(full_sorted_list,headers,xlsx_name)
    print("Done.")
    print()
    # for x in received_list:
    #     print(x)
    # print()
    # for y in issued_list:
    #     print(y)

    Exec = True
    while Exec:
        if input("Press q to quit: ") == 'q':
            Exec = False
        else:
            pass
