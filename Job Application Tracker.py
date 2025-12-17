# Job Application Tracker

# aa program thi tame job application track kari shako
# tame add, view, update and delete kari shako

import os

# file jema data store thase
file_name = "jov_applications.txt"


# functions
# add new application

def add_application():
    company = input("Enter Company Name: ")
    position = input("Enter Position: ")
    date = input("Enter Application Date (DD-MM-YYYY): ")
    status = input("Enter Status (Applied/ Interview/ Offer/ Rejected): ")

    with open(file_name, "a") as file:
        file.write(f"{company}, {position}, {date}, {status}\n")

    print("Application Added Successfully !")



# view all applications

def view_applications():
    if not os.path.exists(file_name):
        print("No Application Found.")
        return
    
    print("\n---- All Applications ----")
    with open(file_name, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No Application Found.")
            return
        for i, line in enumerate(lines):
            company, position, date, status = line.strip().split(",")
            print(f"{i+1}.Company: {company}, Position: {position}, Date: {date}, Staus: {status}")


# update application status

def update_application():
    view_applications()
    index = int(input("Enter Application number to Update: ")) -1

    with open(file_name, "r") as file:
        lines=file.readlines()
 
    if index < 0 or index >= len(lines):
        print("Invalid Application number")
        return
    
    new_status = input("Enter New Status: (Applied/ Interview/ Offer/ Rejected): ")
    company, position, date, _ = lines[index].strip().split(",")
    lines[index] = f"{company}, {position}, {date}, {new_status}\n"

    with open(file_name, "w") as file:
        file.writelines(lines)

    print("Status Update Successfully !")


# delete application

def delete_application():
    view_applications()
    index = int(input("Enter Application number to Delete: "))  -1
    
    with open(file_name, "r") as file:
        lines = file.readlines()

    if index < 0 or index >= len(lines):
        print("Invalid Application Number")
        return
    
    lines.pop(index)

    with open(file_name, "w") as file:
        file.writelines(lines)

    print("Application Deleted Successfully !")


# Main Menu

def main():
    while True:
        print("===== Job Application Tracker =====")
        print("1. Add Application")
        print("2. View Application")
        print("3. Update Application Status")
        print("4. Delete Application")
        print("5. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            update_application()
        elif choice == "4":
            delete_application()
        elif choice == "5":
            print("Tracker Closed.")
            break
        else:
            print("Invalid Choice")


# program start karva mate
main()
