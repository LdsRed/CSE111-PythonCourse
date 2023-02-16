import random

def main():
    
    # 
    numbers = [16.2, 75.1, 52.3]
    #printing numbers list before append_random_numbers() function
    print(f"numbers list: {numbers}")
    # Calling apprend_random_numbers with quantity = 1.
    append_random_numbers(numbers)
    print(f"numbers list after it has been called append_random_numbers function: {numbers}")
    # Calling apprend_random_numbers() with quantity = 3 
    append_random_numbers(numbers, 3)
    print(f"numbers list after it has been called append_random_numbers function: {numbers}")

    # Here an empty word list is created 
    list_of_words = []

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_float_number = random.uniform(0, 200)
        random_float_number = round(random_float_number, 1)
        numbers_list.append(random_float_number)

def append_random_words(words_list, quantity=1):
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]
    for _ in range(quantity):
        words = random.choice(candidates)
        words_list.append(words)

if __name__ == "__main__":
    main()