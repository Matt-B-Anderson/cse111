import csv
from datetime import datetime

def read_dictionary(filename, key_coloumn_index):
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
    with open(f'{filename}', 'rt') as filename:
        reader = csv.reader(filename)
        
        next(reader)
            
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_coloumn_index]
                dictionary[key] = row_list

    return dictionary

def read_from_requests(dictionary):
    
    total = 0.00
    total_quantity = 0
    with open('request.csv', 'rt') as request:
        reader = csv.reader(request)
        next(reader)
    
        for row_list in reader:
            if len(row_list) != 0:
                try: 
                    item = dictionary[row_list[0]]
                except KeyError as key_error:
                    print(f'{key_error}')
                    print(f'{row_list[0]}')
                quantity = row_list[1]
                total += float(item[2])
                total_quantity += int(quantity)
                print(f'{item[1]}: {quantity} @ {item[2]}')
    print(f'Number of Items: {total_quantity}')
    return calculate_total_cost(total)
    

def calculate_total_cost(total):
    print(f'Subtotal: {total:.2f}')
    tax = total * 0.06
    print(f'Sales Tax: {tax:.2f}')
    total_cost = total + tax
    return total_cost
    
def main():
    try:
        product_dict = read_dictionary('products.csv', 0)
        print('Inkom Emporium')
        print('Requested Items')
        total_cost =read_from_requests(product_dict)    
        print(f'Total: {total_cost:.2f}')
        print('Thank you for shopping at Inkom Emporium')
        current_date_and_time = datetime.now()
        print(f'{current_date_and_time:%A %b   %#d %I:%M:%S %Y}')
    except (FileNotFoundError, PermissionError) as error:
        print(f'{error}')
    
if __name__ == "__main__":
    main()