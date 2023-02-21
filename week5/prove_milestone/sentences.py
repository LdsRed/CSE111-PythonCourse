# Author: Jordan Erick Larcher
# Course: CSE111

import random


def main():
    print("Welcome to the Generator of simple English Sentences!")
    print("At the beginning of the program, we will ask you to Select the tense,\n and that tense will be used to "
          "generate the sentences")
    print("The tenses available are: ´past', 'present' and 'future'")

    flag = True
    while flag:

        tense = input("\nPlease, select the verb tense --->  'past', 'present' or 'future': ")
        quantity = int(input("\n Select a quantity between 0 and 10: "))
        for i in range(6):
            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            print(f"{determiner} {noun} {verb}")

        continue_python_program = input("Do you like to continue testing this feature? Select --> Y/N: ")

        if continue_python_program.upper() == "Y":
            flag = True
        else:
            flag = False


# Step 2
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
        a word like "the", "a", "one", "some", "many".
        If quantity is 1, this function will return either "a",
        "one", or "the". Otherwise, this function will return
        either "some", "many", or "the".

        Parameter
            quantity: an integer.
                If quantity is 1, this function will return a
                determiner for a single noun. Otherwise, this
                function will return a determiner for a plural
                noun.
        Return: a randomly chosen determiner.
        """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
        If quantity is 1, this function will
        return one of these ten single nouns:
            "bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"
        Otherwise, this function will return one of
        these ten plural nouns:
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"

        Parameter
            quantity: an integer that determines if
                the returned noun is single or plural.
        Return: a randomly chosen noun.
        """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"

        Parameters
            quantity: an integer that determines if the
                returned verb is single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.
        """
    if tense.lower() == "past":
        tenses = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif (tense.lower() == "present") and quantity == 1:
        tenses = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif (tense.lower() == "present") and quantity != 1:
        tenses = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense.lower() == "future":
        tenses = ["will drink", "will eat", "will grow", "will laugh",
                  "will think", "will run", "will sleep", "will talk",
                  "will walk", "will write"]
    verb = random.choice(tenses)
    return verb


if __name__ == "__main__":
    main()
