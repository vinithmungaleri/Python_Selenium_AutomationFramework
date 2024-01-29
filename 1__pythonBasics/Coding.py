from math import isqrt


def do(inp_str):
    print("Input received is", inp_str)

    cf = {}
    for char in inp_str:
        cf[char] = cf.get(char, 0) + 1

    print(cf)

    for key, val in cf.items():
        print(key, val)

    print(max(cf, key=cf.get))


def remove_ch_str(string, index):
    inp_str = string

    new_str1 = ''.join(char for i, char in enumerate(inp_str) if i != index)
    print(new_str1)

    new_str2 = ""
    for i in range(0, len(inp_str)):
        if i!= index:
            new_str2 += inp_str[i]

    print(new_str2)


def print_stars_pattern(n):
    #    *
    #   ***
    #  *****
    # *******
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '* ' * (2 * i + 1)
        print(spaces + stars)

def split_arr_with_i(arr, i):
    new_arr = arr[i:] + (arr[:i])
    print(new_arr)

def get_prime(n):
    prime = []
    for num in range(2, n+1):
        is_prime = True
        for j in range(2, isqrt(num) + 1):
            if num % j == 0:
                is_prime =False
                break
        if is_prime:
            prime.append(num)
    print(prime)

def get_fibbinocci(n):
    fs = [0, 1]
    while fs[-1] + fs[-2] <=n:
     fs.append(fs[-1] + fs[-2])

    print(fs)

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        print(fib_series)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series


if __name__ == '__main__':
    # do(input(str))
    # remove_ch_str("vickyy", 5)
    # print_stars_pattern(int(input("Enter the steps :")))
    # split_arr_with_i([1,2,3,4,5,6], 2)
    # get_prime(100)
    # get_fibbinocci(100)
    print(fibonacci_recursive(10))