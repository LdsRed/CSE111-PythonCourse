import csv


def main():
    

    PRODUCT_PRICE = 2
    PRODUCT_NAME = 1
    KEY_COLUM_INDEX = 0


    products_dict = read_dictionary("C:/Users/jordan.larcher/Documents/BYU/CSE111-PythonCourse/week9/products.csv", KEY_COLUM_INDEX)
    print("All products")
    print(products_dict)
    print()


    with open("C:/Users/jordan.larcher/Documents/BYU/CSE111-PythonCourse/week9/request.csv" , "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        print("Requested Items")

        for row_list in reader:

            #Here we save the values from the request.csv file 
            product_number = row_list[0]
            product_quantity = row_list[1]
            #We will check if the product number exist in the request.csv file 
            if product_number in products_dict:
                
                #Then we will store each value in a separate variable 
                value = products_dict[product_number]
                product_name = value[PRODUCT_NAME]
                product_price = value[PRODUCT_PRICE]

                print(f"{product_name}: {product_quantity} @ {product_price}")


            

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

    with open(filename , "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            
            if len(row_list) != 0:
                key = row_list[key_column_index]

                dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()