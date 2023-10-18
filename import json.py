import json

student_array = []
date_time_file = "date_time_data.json"  

# Define the file where date and time data will be stored

def save_date_time_data():
    with open(date_time_file, 'w') as file:
        json.dump(student_array, file)

def load_date_time_data():
    try:
        with open(date_time_file, 'r') as file:
            data = json.load(file)
            student_array.extend(data)
    except FileNotFoundError:
        pass

def user_input_function():
    print("Options:")
    print("1. Enter Student Data")
    print("2. Display Student List")
    print("3. Check Order Number")
    print("4. Save and Exit")
    
    option = input("Enter your choice (1/2/3/4): ")
    check_input_condition(option)

def check_by_order_number():
    order_num = input("Please insert an order number to search: ")
    error_found = True

    for rows in student_array:
        if order_num in rows:
            print("Record found: {} - {}".format(order_num, rows[order_num]))
            error_found = False
            break

    if error_found:
        print("Order number not found in program memory.")
    
    print()
    user_input_function()

def take_student_data_input():
    order_number = ""
    student_name = ""

    while order_number.lower() != "exit":
        data = {}
        order_number = input("Please insert your order number (type 'exit' to stop): ")
        
        if order_number.lower() == 'exit':
            break

        student_name = input("Please insert a student name: ")

        data[order_number] = student_name
        student_array.append(data)

    print()
    user_input_function()

def student_list_show():
    if not student_array:
        print("No data found!!!")
    else:
        for row in student_array:
            print(row)
    print()
    user_input_function()

def check_input_condition(option):
    if option == '1':
        take_student_data_input()
    elif option == '2':
        student_list_show()
    elif option == '3':
        check_by_order_number()
    elif option == '4':
        save_date_time_data()
        exit()
    else:
        print("Invalid option. Please select a valid option.")
        print()
        user_input_function()

if __name__ == "__main__":
    load_date_time_data()
    user_input_function()
