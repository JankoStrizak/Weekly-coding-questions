def num_length(num):
    count = 1
    while(num >= 10):
        num = num//10
        count += 1
    return count

def get_first_n_dig(num, n):
    while(num >= (10**n)):
        num = num//10
    return num
                
def get_new_val(prev,curr):
    
    #get number of digits in each number
    l_prev = num_length(prev)
    l_curr = num_length(curr)

    #first n digigts of prev, where n is the number of digits of curr
    first_n_digits_prev = get_first_n_dig(prev, l_curr)

    #the first digits of prev are less than curr
    if(first_n_digits_prev < curr):
        num_new_digits = l_prev - l_curr
        new_val = curr * (10**num_new_digits)

    #the first digits of prev are equal to curr and are not followed by all 9s
    elif(first_n_digits_prev == curr) \
    and (get_first_n_dig(prev+1,l_curr) == first_n_digits_prev):
        num_new_digits = l_prev - l_curr
        new_val = prev+1

    #the digits of prev are greater than curr
    #or
    #the digits of prev are equal to curr and are followed by all 9s
    elif(first_n_digits_prev > curr) \
    or ((get_first_n_dig(prev+1,l_curr) != first_n_digits_prev) \
    and (first_n_digits_prev == curr)):
        num_new_digits = l_prev - l_curr +1
        new_val = curr * (10**num_new_digits)

    return new_val, num_new_digits

def append_sort(num_elements, arr):
    num_new_digits = 0
    for i in range(1, num_elements):
        prev = arr[i-1]
        curr = arr[i]
        if (curr <= prev):
            arr[i], num_new_digits_this_loop = get_new_val(prev, curr)
            num_new_digits += num_new_digits_this_loop
    
    return num_new_digits

num_tests = int(input())
for n in range(num_tests):
    num = int(input())
    ar = [int(x) for x in input().split()]
    ans = append_sort(num, ar)
    print("Case #" + str(n+1) + ": " + str(ans))