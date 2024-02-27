import os
import shutil


#checks if path given is valid
def check_path(checking_path):
    if os.path.exists(checking_path):
        return True
    else:
        return False


#retuns list of items in dir
def dir_list(path):
    return os.listdir(path)

def



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


    while True:

        #program quits if program encunters starting dir and dir is empty
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






if __name__ == "__main__":
    main()