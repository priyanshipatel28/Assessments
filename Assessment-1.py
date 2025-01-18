#Assessment :- Write a program to demonstrate the Python E-Note Book Console based 
# application. 

import datetime
def e_note_menu():
    print(""" Welcome to python E-note
          
            Press 1 for generate Note
            Press 2 for view Note
            press 3 for exit
            press 4 To clear the log-file
          """)
    
status = True
while status:
    e_note_menu()
    user = int(input("Enter your choice : "))
    d=datetime.datetime.today()
#--------------------to exit from the loop----------------------------
    if user == 3:
        print("Thank you ! visit again")
        break
#--------------------end of program --------------------------------

#-----------------To raed the file in python---------------------------
    elif user == 2:
        try:
            file = open("Log_file.txt",'r')
            display = file.read()
            if display == "": # to check if the file is empty or not, just in case if user is directly takeing 2 ...
                print("The file is empty, first print the data.")
            else:
                print(display)
                file.close()# just a programmer routine to close the file after use, not compalsary. but it will bw good if i do it!
                break # to break the loop after printing data from log file
        except FileNotFoundError: # just to take safely precaution
            print("The log is not created yet! ")
#------------------end of reading mode------------------------------

#-------------------To write the data in file-----------------------
    elif user == 1:
        Name = input("Enter Python E-Note Generator Name : ") # collect data from user
        Title = input("Enter Python E=Note Title : ")
        content =  input("Enter E-note Content : ")
        if not Name.isdigit() and not Title.isdigit() and not content.isdigit(): # it will check if the data is valid or no.
            file = open("Log_file.txt",'a') # i have to write the data in file , so i can use write mode, but someoe is adding another data then the privious data shouldn't be removed, so i am using append, to store all the data.
            file.write('-'*30 + '\n')
            file.write(f"{str(d)} \n") # it will print the date and tiem in log file
            file.write(f"E-Note Title : {Title}\nE-Note Description : {content} \n{" "*10}Note Generator :{Name}\n")
            file.close() # just a programmer routine to close the file after use, not compalsary. but it will bw good if i do it!
            print("saved") # just for my confirmation
        else:
            print("Error : Invalid Input")
#---------------------end of write mode------------------------------

#------------------------to delete-----------------------------
#this is not a part of assessment, just i want to do it.
    else:
        file = open("Log_file.txt",'w')# i write mode it will delete the previous data and add new one
        # i juat want to delete it. 
        print("done") # just for my confirmation, wheather it is working or not
#------------------------end of delete-------------------------------------



