import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print the current
# day of the week and the current time.
current_date = f"{current_date_and_time:%a %b  %w %I:%M:%S %Y}"
current_day = f"{current_date_and_time:%A}".lower()
current_hour = int(f"{current_date_and_time:%H}")


def main():
    PRODUCT_PRICE = 2
    PRODUCT_NAME = 1
    KEY_COLUM_INDEX = 0
    SALES_TAXES = 0.06

    products_dict = read_dictionary("C:/Users/jordan.larcher/Documents/BYU/CSE111-PythonCourse/week9/products.csv",
                                    KEY_COLUM_INDEX)
    print("Store Sweet Dreams")
    print()

    try:
        with open("C:/Users/jordan.larcher/Documents/BYU/CSE111-PythonCourse/week9/request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)

            next(reader)

            print("Requested Items:")

            number_items = 0
            subtotal = 0
            for row_list in reader:
                # Here we save the values from the request.csv file
                product_number = row_list[0]
                product_quantity = row_list[1]

                number_items += int(product_quantity)
                # We will check if the product number exist in the request.csv file

                # Then we will store each value in a separate variable
                value = products_dict[product_number]
                product_name = value[PRODUCT_NAME]
                product_price = value[PRODUCT_PRICE]
                subtotal += float(product_price) * float(product_quantity)

                print(f"{product_name}: {product_quantity} @ {product_price}")

        print()

        # Calculating and rounding sales taxes, subtotals, and total amount
        subtotal = round(subtotal, 2)
        sales_taxes = subtotal * round(SALES_TAXES, 3)
        sales_taxes = round(sales_taxes, 2)
        total = subtotal + sales_taxes
        total = round(total, 2)

        # Printing number of items in the request, the subtotal, sales taxes and the total amount
        print(f"Number of items: {number_items}\nSubtotal: {subtotal}\nSales Tax: {sales_taxes}\nTotal: {total}")
        print()

        new_total = 0
        if current_day == "saturday" or current_hour < 11:
            print("Congratulations you won a 10% discount on the total of your purchase!")
            new_total = total - (total * 0.10)
            new_total = round(new_total, 2)
        print(f"The total with the discount is: {new_total}$")

        print()
        print("Thank you for shopping at the Store Sweet Dreams.")
        print(current_date)
        print()

    except KeyError as error:
        print()
        print(f"Error: unknown product ID in the request.csv {error}")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    try:
        with open(filename, "rt") as csv_file:

            reader = csv.reader(csv_file)

            next(reader)

            for row_list in reader:

                if len(row_list) != 0:
                    key = row_list[key_column_index]

                    dictionary[key] = row_list
    except (FileNotFoundError, PermissionError) as error:
        print("Error: missing file")
        print(error)

    return dictionary


if __name__ == "__main__":
    main()
