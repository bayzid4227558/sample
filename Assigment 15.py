

#                                     Function to insert data into the database

def insert_data(id,name):
    data = {
        "ID": id,
        "Name": name,
    }

    
   
    while True:
        id = input("Enter ID number (or press Enter to exit): ")
            
        if not id:
            break
            
        name = input("Enter name: ")
        result = insert_data(id,name)
        print("Data List:",insert_data(data,id, name,result))
    



#                            Function to display all data from the database


def view_data():
    Course_Istetructor = {
        "Name": "Md. Mahidul Moon",
        "Age" : 28,
        "SSC" : 2014,
        "HSC" : 2016,
        "BSC" : 2020,
        "Location": "Savar"
    }
    
    Students = {
    "4227558": "Md. Bayzid Islam",
    "4079303": "Chironjit Adhikary",
    "4223810": "Sharmin Akter",
    "4224630": "Md Mahdiul Hasan",
    "4224863": "Wahid Jamal",
    "4224867": "AKM. Rofiqul Alam",
    "4225042": "Maruf Hossen Fahim",
    "4225092": "Al Fahad Hossen Rifat",
    "4227217": "Muhammad Abdur Rahim",
    "4227526": "Jabed Al-dhen",
    "4227830": "Syeda Shafayet Othy",
    "4228142": "Tohidul Islam",
    "4228206": "Arifa Absar Esham",
    "4227820": "Kawser Ahmed Nihad",
    "4228563": "Abdullah Al Maswud"
}

    if Pyth_B_N233_1 == 1:
        return Course_Istetructor
    elif Pyth_B_N233_1 == 2:
        return Students
    else:
        print("Invalid option. Please choose 1 or 2.")

    print("1. Enter data into the Course Istetructor")
    print("2. See data stored in the Students list")
    Pyth_B_N233_1 = int(input("Choose an option (1 or 2): "))

    Data_list = view_data(Pyth_B_N233_1)

    if Data_list:
        print("Selected Dictionary:", Data_list)
    else:
        print("Invalid option. Please choose 1 or 2.")




#                                     Function to search data in the database



def search_data():
    Students_data = {
        "4227558": "Md.Bayzid Islam",
        "4079303": "Chironjit Adhikary",
        "4223810": "Sharmin Akter",
        "4224630": "Md Mahdiul Hasan",
        "4224863": "Wahid Jamal",
        "4224867": "AKM. Rofiqul Alam",
        "4225042": "Maruf Hossen Fahim",
        "4225092": "Al Fahad Hossen Rifat",
        "4227217": "Muhammad Abdur Rahim",
        "4227526": "Jabed Al-dhen",
        "4227830": "Syeda Shafayet Othy",
        "4228142": "Tohidul Islam",
        "4228206": "Arifa Absar Esham",
        "4227820": "Kawser Ahmed Nihad",
        "4228563": "Abdullah Al Maswud"
    }
    
    if input_ID in Students_data:
        print(f"Data found: {input_ID} :- {Students_data[input_ID]}")
    else:
        print(f"Not found for ID: {input_ID}")
        save = input("Do you want to save this ID? (yes/no): ")
        
        if save == "yes":
            new = input("Enter the name to for this save : ")
            Students_data[input_ID] = new
            print(f"New Save ID: {input_ID} And Name: {new}")


    input_ID = input("Enter an ID number to check: ")
    search_data(input_ID)




if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Function to insert data into the database :")
        print("2. Function to display all data from the database :")
        print("3. Function to search data in the database :")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            insert_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            search_data()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")




