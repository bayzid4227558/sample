


#                            Function to display all data from the database


def view_data(Pyth_B_N233_1):
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
view_data(Pyth_B_N233_1)