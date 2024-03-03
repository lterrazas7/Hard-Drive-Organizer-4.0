import os
import shutil
import datetime


def __init__(item, path):
    year = file_year(item, path)
    month = file_month(item, path)
    ext = file_type(item, path)
    path = os.path.join(path, item)
    return year

def file_year(item, path):
    file_directory = os.path.join(path, item)
    file_date = os.path.getmtime(file_directory)
    file_date_modified = datetime.datetime.fromtimestamp(file_date)
    return str(file_date_modified.year)

def file_month(item, path):
    file_directory = os.path.join(path, item)
    file_date = os.path.getmtime(file_directory)
    file_date_modified = datetime.datetime.fromtimestamp(file_date)
    return str(file_date_modified.month)

def file_type(item, path):
    file_directory = os.path.join(path, item)
    _, file_type = os.path.splitext(file_directory)
    return file_type[1:]

#checks if path given is valid
def check_path(checking_path):
    if os.path.exists(checking_path):
        return True
    else:
        return False


#retuns list of items in dir
def dir_list(path):
    exclude_list = ["New - Organized Files"]
    items_in_list = []
    for item in os.listdir(path):
        if item not in exclude_list:
            items_in_list.append(item)
    return items_in_list

#returns list of file(s) in dir given
def dir_files(list, path):
    files = []
    for item in list:
        if os.path.isfile(path + "\\" + item):
            files.append(item)
    return files

#returns list of folder(s) in dir given
def dir_folders(list, path):
    folders = []
    for item in list:
        if os.path.isdir(path + "\\" + item):
            folders.append(item)
    return folders

def main():
    print("The path you provide will be the starting and ending point of the organizing.")

    #stores dir path from user
    user_dir_input = input("Please copy and paste the folder path to start organizing: ")

    #runs if path was not valid, gives user ability to quit program
    while not check_path(user_dir_input):
        print("")
        user_dir_input = input("Path provided is not valid dir path, please input path or hit Q to quit: ")
        if user_dir_input.upper() == "Q":
            print("Quiting program!")
            quit()
        else:
            check_path(user_dir_input)

    #start of organizing program
    print("If here, it worked!") #remove this before final iteration

    #storing original starting dir path
    starting_dir = user_dir_input

    #variable used for rest of program
    working_dir = starting_dir

    #creating folder within file path given where files will be organized and stored
    organized_files = "New - Organized Files"
    organized_files_path = starting_dir + "\\" + organized_files
    #os.mkdir(organized_files_path) turn back on when trying new folder

    while True:

        #holds list of items in current dir
        list_of_dir = dir_list(working_dir)

        #condition that should be met after program ends it's cycle of organizing
        if working_dir == starting_dir and not list_of_dir:
            print("Inside final iteration - program should quit")
            quit()

        #condition where list returns empty, dir gets deleted
        if not list_of_dir:
            print("Folder is empty - moving back up to another folder")
            delete_dir = working_dir #variable storing current dir/ deleting dir
            working_dir = os.path.dirname(working_dir) #changing dir to one step up
            shutil.rmtree(delete_dir) #deleting old dir
            print(working_dir)
            break
        #automatic condition to run - list has items
        else:

            #list of files from current dir
            list_of_files_dir = dir_files(list_of_dir, working_dir)

            #list of folders from current dir
            list_of_folders_dir = dir_folders(list_of_dir, working_dir)

            #condition runs if list of files is empty/ moves to new dir
            if not list_of_files_dir:
                #changes dir to new dir w/ first folder it encounters
                working_dir = os.path.join(working_dir, list_of_folders_dir[0])

            #condition runs since list of files is NOT empty
            else:
                for item in list_of_files_dir:
                    working_file = __init__(item, working_dir)
                    print(working_file)

            break





"""    while True:

        #program quits if program encounters starting dir and dir is empty
        if working_dir == starting_dir and not dir_list(working_dir):
            print("inside first if")
            quit()
        #if list returned from folder empty, delete folder
        elif not dir_list(working_dir):
            #delete folder and move back up to previous dir
        #runs when folder has items
        else:
            #grab items from list
            #if file
                #grab

"""




if __name__ == "__main__":
    main()