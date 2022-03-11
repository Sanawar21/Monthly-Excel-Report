import os
import random
import pandas as pd
from Excel_Package.issued import Issued
from Excel_Package.received import Received
import string
import xlsxwriter
from tabulate import tabulate

def get_keys_of_names(key_num_4_names):
    print()
    name_keys_dictionary = dict()
    if key_num_4_names == '':
        for letter in list(string.ascii_lowercase):
            val_name = input(f"{letter} = ")
            if val_name == '':
                break
            else:
                name_keys_dictionary[letter] = val_name
        should_save = input("Do you want to save the current keys so you could use "
                            "them next time? (y/n) ")
        if should_save == 'y':
            filename = input("Enter the file name you want to save in ending with .txt: ")
            with open(filename, 'w') as namekeys:
                for key, val in name_keys_dictionary.items():
                    namekeys.write(f"{key}={val}\n")
            print(f"Saved the keys in {filename}.")
        else:
            print("Ok. Not saving.")

    elif key_num_4_names == '1':
        dir_name = input("Enter the file path of the text file: ")+'.txt'
        if dir_name == '$.txt':
            dir_name = 'keys.txt'
        with open(dir_name, 'r') as reading_data:
            lines = reading_data.readlines()
            for line in lines:
                key, val = line.split('=')
                name_keys_dictionary[key] = val.strip()
        print("Done.")

    elif key_num_4_names == "2":
        print()
        while True:
            name = input("Enter the name: ")
            if name == '':
                break
            key = input(f"Enter the key you want to link with {name}: ")
            name_keys_dictionary[key] = name

        print("Done")
        should_save = input("Do you want to save the current keys so you could use "
                            "them next time? (y/n) ")
        if should_save == 'y':
            filename = input("Enter the file name you want to save in ending in .txt: ")
            with open(filename, 'w') as namekeys:
                for key, val in name_keys_dictionary.items():
                    namekeys.write(f"{key}={val}\n")
            print(f"Saved the keys in {filename}.")
        else:
            print("Ok. Not saving.")

    return name_keys_dictionary

def make_date_new(currentDate,raw_date_and_name_list):
    if len(raw_date_and_name_list) == 1:
        return currentDate
    elif raw_date_and_name_list[0] == '1':
        dnm = currentDate.split('/')
        new_day = int(dnm[0]) + 1
        return f'{new_day}/{dnm[1]}/{dnm[2]}'
    else:
        dnm = currentDate.split('/')
        return f"{raw_date_and_name_list[0]}/{dnm[1]}/{dnm[2]}"

def ask_for_text():
    yn = input("Do you wish to provide a text file? (y/n): ")
    if yn == 'y':
        return True
    else:
        return False

def get_name(raw_input, names_and_keys):
    raw_input = list(raw_input)
    if raw_input[0][0] not in '0123456789':
        return names_and_keys[raw_input[0]]
    else:
        return names_and_keys[raw_input[1]]

def get_data_from_txt(file):
    with open(file,'r') as data:
        lines = data.readlines()
        for line in lines:
            lines[lines.index(line)] = line.strip()
        return lines

def convert_to_class(class_name, objects, kgsPerBag=25):
    class_list = []
    if class_name == "received":
        for object in objects:
            new_object = Received(object[0],object[1],object[2],kgsPerBag)
            class_list.append(new_object)
    elif class_name == "issued":
        for x in objects:
            new_object = Issued(x[0],x[1],x[2],x[3])
            class_list.append(new_object)
    return class_list

def add_serials_and_sort(issued_list,recieved_list):
    full_list = issued_list+recieved_list
    full_list = sorted(full_list,key=lambda classes: classes.day)

    x = 1
    for item in full_list:
        ind = full_list.index(item)
        item.serial = x
        full_list[ind] = item
        x +=1

    return full_list

def get_key_of(val,my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

def make_backup(full_sorted_list,keys_and_names):
    dir_name = f"backup_id_{str(random.random())[2:5]}"
    os.mkdir(dir_name)

    with open(f"{dir_name}/full.txt", 'w') as full:
        for classes in full_sorted_list:
            full.write(f"{str(classes)}\n")

    with open(f"{dir_name}/keys.txt", 'w') as keys:
        for key, val in keys_and_names.items():
            keys.write(f"{key}={val}\n")

    with open(f'{dir_name}/date_and_namekeys.txt','w') as dnm:
        for classes in full_sorted_list:
            dnm.write(f"{classes.date} {get_key_of(classes.name,keys_and_names)}\n")

    with open(f'{dir_name}/weight_issued.txt','w') as w:
        for Class in full_sorted_list:
            w.write(f"{Class.weight}\n")

    with open(f'{dir_name}/bags.txt','w') as bags:
        for Class in full_sorted_list:
            bags.write(f"{Class.bags}\n")

    print(f"Backup made in {dir_name}.")

def print_as_table_V2(headers, sorted_list, balance):
    printing_list = []
    sum_received = 0
    sum_issued = 0
    op_balance = balance.pop(0)
    for Class in sorted_list:
        printing_list.append(Class.as_list())
    for printing_line in printing_list:
        ind = printing_list.index(printing_line)
        printing_line.append(balance[ind])
        # print(text)
    printing_list.insert(0, ['', '', 'Opening Balance', '', '', '', '', (op_balance)])
    for line in printing_list:
        try:
            sum_received += float(line[5])
        except:
            pass

    for line in printing_list:
        try:
            sum_issued += float(line[6])
        except:
            pass
    printing_list.append(['', '', '', '', '', '', '', ''])
    printing_list.append(['', '', 'Total', '', '', sum_received, sum_issued, balance[-1]])

    print(tabulate(printing_list, headers=headers, tablefmt="pipe"))
    return printing_list


def print_as_table(headers,sorted_list, balance):
    text_list = []
    sum_received = 0
    sum_issued = 0
    op_balance = balance.pop(0)
    for Class in sorted_list:
        text_list.append(str(Class).split(','))
    for text in text_list:
        ind = text_list.index(text)
        text.append(balance[ind])
    text_list.insert(0,['','','Opening Balance','','','','',str(op_balance)])
    for line in text_list:
        try:
            sum_received += float(line[5])
        except:
            pass
    for line in text_list:
        try:
            sum_issued += float(line[6])
        except:
            pass
    text_list.append(['','','','','','','',''])
    text_list.append(['','','Total','','',format(sum_received,'.3f'),format(sum_issued,'.3f'),balance[-1]])

    print(tabulate(text_list,headers=headers,tablefmt="pipe"))
    return text_list

def make_excel_file_V2(text_list,headers_list,name,cwd,balance):
    workbook = name+'.xlsx'
    os.chdir(cwd)
    os.chdir('../Excel_Files')
    df = pd.DataFrame(data=text_list, columns=headers_list)
    writer = pd.ExcelWriter(f"{os.getcwd()}\\{workbook}", engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()