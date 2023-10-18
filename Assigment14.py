


def search_data(input_ID):
    Students_data = {
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





