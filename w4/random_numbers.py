import random

def append_random_numbers(numbers_list, quantity = 1):
    i = 0
    while quantity > i:
        psuedo_number = random.uniform(1, 10)
        psuedo_quantity = round(psuedo_number, 1)
        numbers_list.append(psuedo_quantity)
        i += 1
        
def main():
    numbers = [16.2, 75.1, 52.3]
    
    append_random_numbers(numbers)
    print(numbers)
    
    append_random_numbers(numbers, 3)
    print(numbers)
    
    
if __name__ == '__main__':
    main()