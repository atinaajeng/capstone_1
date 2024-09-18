# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:54:45 2024

@author: ATINA
"""

import datetime
 
#function to display data
def read(borrowers):
    while True:
        print('\nWelcome to the Read Menu of the Library')
        print("Read Data Menu: ")
        print("1. Display Data")
        print("2. Borrower status")
        print("3. Exit")
        
        number = int(input("Please type the number of the menu you want to proceed: "))
        
        if number == 1:
            if borrowers:  
                print('ID\t\t\t| First Name\t| Last Name\t| Date of Birth\t| Contact Info\t| Book Titles\t\t\t\t| Book Authors\t\t\t\t| Date Borrowed')
                print('-'*150)
                
                for borrower in borrowers:
                    
                    id_str = f'{borrower["ID"]}\t'
                    first_name = f'{borrower["First Name"]}\t\t'
                    last_name = f'{borrower["Last Name"]}\t\t'
                    dob = f'{borrower["Date of Birth (DD-MM-YY)"]}\t'
                    contact = f'{borrower["Contact Info"]}\t'
                    book_titles = f'{", ".join(borrower["Book Title"])}\t\t'
                    book_authors = f'{", ".join(borrower["Author"])}\t\t'
                    date_borrowed = f'{borrower["Date Borrowed (DD-MM-YYYY)"]}\t'

                    
                    print(f'{id_str}| {first_name}| {last_name}| {dob}| {contact}| {book_titles}| {book_authors}| {date_borrowed}')
            else:
                print("Data does not exist")
                
        elif number == 2:
            if borrowers:
                id_number = input("Please type in the ID number: ")
                id_found = False  
                
                for i in range(len(borrowers)):
                    if borrowers[i]["ID"] == id_number:
                        id_found = True  
                        current_date = datetime.datetime.now()
                        borrowed_date = borrowers[i]["Date Borrowed (DD-MM-YYYY)"]
                        borrowed_date = datetime.datetime.strptime(borrowed_date, "%d-%m-%Y")
                        due_date = borrowed_date + datetime.timedelta(weeks=2)
                        days_left = (due_date - current_date).days
                        print("Borrowed date:", borrowed_date.strftime("%d-%m-%Y"))
                        print("Due date:", due_date.strftime("%d-%m-%Y"))
                        
                        if days_left > 0:
                            print(f"You have {days_left} days left to return the book.")
                        elif days_left == 0:
                            print("Today is the due date, please return the book.")
                        else:
                            print(f"You have been late for {abs(days_left)} days.")
                        break
                
                if not id_found:
                    print("The data that you are looking for does not exist.")
            else:
                print("Data does not exist.")
        
        elif number == 3:
            break
        
        else:
            print("Option does not exist, please choose number 1-3")

#Create function to add more borrowers
def create(borrowers):
    while True:
        print('\nWelcome to the Create Menu of the Library')
        print("Create Data Menu: ")
        print("1. Create new borrower data")
        print("2. Exit")
        
        number = int(input("Please type the number of the menu you want to proceed: "))
        
        if number == 1:
            print("Please input borrower's biodata")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("Date of Birth (DD-MM-YY): ")
            id_name = first_name[0] + last_name[0] + dob.replace("-","")
            
            for i in range(len(borrowers)):
                if borrowers[i]["ID"] == id_name:
                    print("Borrower already exists")
                    break
            else:
                contact = input("Phone Number: ")
                
                book_list = []
                while True:
                    print("Type 'stop' when you have finished")
                    book_title = input("Book Title: ")
                    if book_title.lower() == 'stop':
                        break
                    book_list.append(book_title)
                        
                author_list = []
                while True:
                    print("Type 'stop' when you have finished")
                    book_author = input("Book Author: ")
                    if book_author.lower() == 'stop':
                        break
                    author_list.append(book_author)
                        
                date_borrowed = input("Date Borrowed (DD-MM-YYYY): ")
                
                borrower_record = {
                    "ID": id_name,
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Date of Birth (DD-MM-YY)": dob,
                    "Contact Info": contact,
                    "Book Title": book_list,
                    "Author": author_list,
                    "Date Borrowed (DD-MM-YYYY)": date_borrowed,
                }
                
                question = input("Do you want to save the data (Y/N)? ")
                if question.upper() == 'Y':
                    borrowers.append(borrower_record)
                    print("Data successfully saved")
        
        elif number == 2:
            break
        
        else:
            print("Option does not exist, please choose number 1-2")
            
        
#To be placed in the update function below
def modify_list(item_list, item_type):
    modify = input(f"\nDo you want to delete, add, or change a {item_type}? (delete/add/change): ").lower()
    
    if modify == 'delete':
        print(f"\nList of current {item_type.lower()}s:")
        print(item_list)
        item_to_delete = input(f"Enter the {item_type} you want to delete: ")
        if item_to_delete in item_list:
            item_list.remove(item_to_delete)
            print(f'"{item_to_delete}" has been successfully removed.')
        else:
            print(f'"{item_to_delete}" is not in the list.')
    
    elif modify == 'add':
        print(f"\nList of current {item_type.lower()}s:")
        print(item_list)
        item_to_add = input(f"Enter the {item_type} you want to add: ")
        item_list.append(item_to_add)
        print(f"The new {item_type.lower()} list is {item_list}")
    
    elif modify == 'change':
        print(f"\nList of current {item_type.lower()}s:")
        print(item_list)
        item_to_change = input(f"Enter the {item_type} you want to change: ")
        new_value = input(f"Enter the new {item_type}: ")

        if item_to_change in item_list:
            index = item_list.index(item_to_change)
            item_list[index] = new_value
            print(f'"{item_to_change}" has been successfully changed to "{new_value}".')
        else:
            print(f'"{item_to_change}" is not in the list.')
    else:
        print("Invalid option.")

            
#Update function
def update(borrowers):
    while True:
        print('\nWelcome to the Update Menu of the Library')
        print("Update Data Menu: ")
        print("1. Update borrower data")
        print("2. Exit")
        
        number = int(input("Please type the number of the menu you want to proceed: "))
      
        if number == 1:
            id_number = input("Please input borrower's ID: ")
            
            id_found = False  

            for i in range(len(borrowers)):
                if borrowers[i]["ID"] == id_number:
                    id_found = True  
                    print('Borrower Details\n')
                    print('ID\t\t\t| First Name  \t| Last Name\t\t| Book Title')
                    print(f'{borrowers[i]["ID"]}\t| {borrowers[i]["First Name"]}  \t\t| {borrowers[i]["Last Name"]}\t\t| {", ".join(borrowers[i]["Book Title"])}')
                    
                    question = input("Continue to update (Y/N): ")
                    if question.upper() == "Y":
                        print("List of fields: ")
                        print("1. First Name")
                        print("2. Last Name")
                        print("3. Date of Birth (DD-MM-YY)")
                        print("4. Contact Info")
                        print("5. Book Title")
                        print("6. Author")
                        print("7. Date Borrowed (DD-MM-YYYY)")
                        
                        key = int(input("Please specify the field you want to update (1-7): "))
                        
                        if key in [1, 2, 3, 4, 7]:  # For simple text updates
                            field_map = {
                                1: "First Name",
                                2: "Last Name",
                                3: "Date of Birth (DD-MM-YY)",
                                4: "Contact Info",
                                7: "Date Borrowed (DD-MM-YYYY)"
                            }
                            field_to_update = field_map[key]
                            new_val = input(f"Please type the new value for {field_to_update}: ")
                            question_2 = input(f"Are you sure you want to update {field_to_update} (Y/N)? ")
                            if question_2.upper() == 'Y':
                                borrowers[i][field_to_update] = new_val
                                print(f"{field_to_update} has been successfully updated!")
                            else:
                                print("Update canceled.")
                             
                        elif key == 5: 
                            question_2 = input("Are you sure you want to update Book Title (Y/N)? ")
                            if question_2.upper() == 'Y':
                                modify_list(borrowers[i]["Book Title"], "Book Title")
                            else:
                                print("Update canceled.")
                            

                        elif key == 6: 
                            question_2 = input("Are you sure you want to update Author (Y/N)? ")
                            if question_2.upper() == 'Y':
                                modify_list(borrowers[i]["Author"], "Author")
                            else:
                                print("Update canceled.")
                            
                        
                        else:
                            print("Invalid option.")
                    
                    break  

            if not id_found:
                print("The data that you are looking for does not exist.")
                        
        
        elif number == 2:
            break
        
        else:
            print("Option does not exist, please choose number 1 or 2.")
       
#Delete function             
def delete(borrowers):
    while True:
        print('\nWelcome to the Delete Menu of the Library')
        print("Delete Data Menu: ")
        print("1. Delete borrower data")
        print("2. Exit")
        number = int(input("Please type the number of the menu you want to proceed: "))
        
        if number == 1:
            id_number = input("Please input borrower's ID: ")
            id_found = False  
            
            for i in range(len(borrowers)):
                if borrowers[i]["ID"] == id_number:
                    id_found = True  
                    question = input("Are you sure to delete the data (Y/N)? ")
                    if question.upper() == 'Y':
                        del borrowers[i]
                        print("Data has been successfully deleted.")
                        break
                    else:
                        break
                    
            if not id_found:
                print("The data that you are looking for does not exist.")
                
        elif number == 2:
            break
        
        else:
            print("Option does not exist, please choose number 1-2")

                    

#Main menu of the library
def main(borrowers):
    print("Welcome to the Main Menu of the Library")
    while True:
        print("\n")
        print("Main Menu: ")
        print("1. Display Data")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        
        number = int(input("Please type the number of the menu you want to proceed: "))
        
        if number == 1:
            read(borrowers)
        elif number == 2:
            create(borrowers)
        elif number == 3:
            update(borrowers)
        elif number == 4:
            delete(borrowers)
        elif number == 5:
            print("Exit program")
            break
        else:
            print("The option you entered is not valid")
    
