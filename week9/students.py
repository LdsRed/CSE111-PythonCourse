import csv


def main():
    INUMBER_INDEX = 0

    student_number_id = input("Enter the student id number: ")

    get_INumber_student(read_dictionary("C:/Users/jordan.larcher/Documents/BYU/CSE111-PythonCourse/week9/students.csv", INUMBER_INDEX), student_number_id)


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


def get_INumber_student(dictionary, id_number ):  
    id_without_dashes = id_number.replace("-", "")

    if len(id_without_dashes) <= 5: 
        print("too few digits")
    elif len(id_without_dashes) > 12:
        print("too many digits")
    else:    
        if id_without_dashes in dictionary:
            value = dictionary[id_without_dashes]
            name = value[1]
            print(f"{name}")
        else:
            print("No such student")

# Call main to start this program.
if __name__ == "__main__":
    main()