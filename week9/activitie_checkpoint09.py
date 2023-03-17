def main():
    text_list = read_list("C:/Users/jordan.larcher/Documents/BYU/CSE111-PythonCourse/week9/provinces.txt")
    print(text_list)


def read_list(filename):
    list_text = []

    with open(filename, "rt") as text_list:

        for line in text_list:

            clean_line = line.strip()
            if clean_line == "AB":
                list_text.append("Alberta")
            else:
                list_text.append(clean_line)
    list_text.pop(0)
    list_text.pop(len(list_text) - 1)
    return list_text


if __name__ == "__main__":
    main()
