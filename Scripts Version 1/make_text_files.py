import os

if __name__ == "__main__":
    dir_name = input("Enter the directory name: ")
    try:
        os.mkdir(f"C:Users/TOSHIBA/Excel_Stuff/Data_Directories/{dir_name}")
    except:
        pass


    for x in range(5):
        x += 1
        with open(f"{dir_name}/{x}.txt",'w'):
            pass
