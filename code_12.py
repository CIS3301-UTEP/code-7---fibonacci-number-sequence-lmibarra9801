def get_fibonacci_number(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    
    return get_fibonacci_number(position - 2) + get_fibonacci_number (position -1)

def get_fibonacci_number_sequence(number):
    fibonacci_sequence =[]
    for i in range(1, number +1):
        fibonacci_number = get_fibonacci_number(i)
        fibonacci_sequence.append(get_fibonacci_number(i))
    return fibonacci_sequence

if __name__ == "__main__":
    print(get_fibonacci_number_sequence(7))