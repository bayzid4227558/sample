
from datetime import datetime

class DataManagement:
    def __init__(self):
        self.student_array = []

    def store_student_data(self, data):
        cleaned_data = str(datetime.now()) + " -> " + str(data)
        with open('store_data.txt', 'a') as store_file_data:
            store_file_data.write("\n" + cleaned_data)

    def read_data_from_store_file(self):
        with open('store_data.txt') as file_data:
            print("===============\n")
            print(file_data.read())
            print("\n===============")

    def take_student_data_input(self):
        order_number = ""
        student_name = ""

        while order_number != "exit":
            data = {}
            order_number = input("Please insert your order number: ")
            if order_number == 'exit':
                self.store_student_data(self.student_array)
                self.user_input_function()

            student_name = input("Please insert a student name: ")

            data[order_number] = student_name

            self.student_array.append(data)

    def student_list_show(self):
        self.read_data_from_store_file()
        print("")
        self.user_input_function()

    def check_by_order_number(self):
        order_num = input("Please insert an order number to search: ")
        for data in self.student_array:
            if order_num in data:
                print(f"Record found: {order_num} - {data[order_num]}")

    def user_input_function(self):
        print("Options:")
        print("1. Enter Student Data")
        print("2. Display Student List")
        print("3. Check Order Number")
        print("4. Exit")

        option = input("Enter your choice (1|2|3|4): ")
        self.check_input_condition(option)

    def check_input_condition(self, option):
        if option == '1':
            self.take_student_data_input()
        elif option == '2':
            self.student_list_show()
        elif option == '3':
            self.check_by_order_number()
        elif option == '4':
            exit()
        else:
            print("Invalid option. Please select a valid option.")
            self.user_input_function()

if __name__ == "__main__":
    data_manager = DataManagement()
    data_manager.user_input_function()

