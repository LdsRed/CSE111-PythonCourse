def main():
    print("\nThis program is an implementation of the Rosenberg" +
          "\nSelf-Esteem Scale. This program will show you ten" +
          "\nstatements that you could possibly apply to yourself." +
          "\nPlease rate how much you agree with each of the" +
          "\nstatements by responding with one of these four letters:")
    print()
    print("\nD means you strongly disagree with the statement." +
          "\nd means you disagree with the statement." +
          "\na means you agree with the statement." +
          "\nA means you strongly agree with the statement.")
    print()

    score = 0

    score += positive_question(
        "1. I feel that I am a person of worth, at least on an"
        " equal plane with others.")
    score += positive_question(
        "2. I feel that I have a number of good qualities.")
    score += negative_question(
        "3. All in all, I am inclined to feel that I am a failure.")
    score += positive_question(
        "4. I am able to do things as well as most other people.")
    score += negative_question(
        "5. I feel I do not have much to be proud of.")
    score += positive_question(
        "6. I take a positive attitude toward myself.")
    score += positive_question(
        "7. On the whole, I am satisfied with myself.")
    score += negative_question(
        "8. I wish I could have more respect for myself.")
    score += negative_question(
        "9. I certainly feel useless at times.")
    score += negative_question(
        "10. At times I think I am no good at all.")

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def positive_question(response):
    print(response)
    answer = input(" Enter D, d, a, or A: ")
    score = 0
    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3
    return score


def negative_question(response):
    print(response)
    answer = input(" Enter D, d, a, or a: ")
    score = 0
    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3
    return score


if __name__ == "__main__":
    main()
