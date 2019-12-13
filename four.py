"""
Day Four: Secure Container

* 6 digits
* Within given range
* Two adjacent digits are the same (at least)
* Digits increase or stay the same from left to right
"""


def int_to_array(number):
    int_str = str(number)
    return [int(int_str[i]) for i in range(0,6)]


def array_to_int(arr):
    return int("".join([str(x) for x in arr]))


def two_adjacent(x):
    for i in range(0,5):
        if x[i] == x[i+1]:
            return True
    return False


def find_substrings(x):
    substrings = []
    i = 0
    j = 0
    while i < len(x):
        while j < len(x) and x[j] == x[i]:
            j += 1
        substrings.append(x[i:j])
        i = j
    return substrings

        
def min_adjacent(x):
    lens = [len(s) for s in find_substrings(x)]
    adj_lens = [s for s in lens if s > 1]
    if len(adj_lens) == 0:
        return 0
    return min(adj_lens)        

    
def generate_arrays(start, end):
    start_arr = int_to_array(start)
    end_arr = int_to_array(end)
    
    for i0 in range(start_arr[0], end_arr[0] + 1):
        for i1 in range(0, 10):
            if i1 < i0:
                continue
            for i2 in range(0, 10):
                if i2 < i1:
                    continue
                for i3 in range(0, 10):
                    if i3 < i2:
                        continue
                    for i4 in range(0, 10):
                        if i4 < i3:
                            continue
                        for i5 in range(0, 10):
                            if i5 < i4:
                                continue
                            x = [i0, i1, i2, i3, i4, i5]
                            int_x = array_to_int(x)
                            if int_x < start:
                                continue
                            elif int_x > end:
                                return
                            yield x


def generate_passwords(start, end):
    for pwd in generate_arrays(start, end):
        if min_adjacent(pwd) == 2:
            yield pwd
    

def main():
    start = 156218
    end = 652527
    count = 0
    for pwd in generate_passwords(start, end):
        count += 1
    return count


print(main())
