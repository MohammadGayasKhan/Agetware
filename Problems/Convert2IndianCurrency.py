'''Problem: Convert number into a comma separated Indian currency format
In Indian numbering system the terms used are different from what is used in the western numbering system. 
Terms like Lakh to represent one hundred thousand and Crore to represent 10 Million.
Write code that takes as input a floating point number and returns an indian number string representation with commas separating the digits.
Eg: 123456.7891 should return 1,23,456.7891'''

def convert_to_indian_currency(number):
    integer_part, decimal_part = str(number).split('.')
    reversed_integer = integer_part[::-1]
    result = []
    result.append(reversed_integer[:3])
    for i in range(3, len(reversed_integer), 2):
        result.append(reversed_integer[i:i+2])
    formatted_integer = ','.join(result)[::-1]
    if decimal_part:
        return f"{formatted_integer}.{decimal_part}"
    else:
        return formatted_integer
    
if __name__ == "__main__":
    number_input = float(input("Enter a floating point number: "))
    formatted_currency = convert_to_indian_currency(number_input)
    print(f"Formatted Indian Currency: {formatted_currency}")