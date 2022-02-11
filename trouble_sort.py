def valid(subarr_1, subarr_2, s, f):
    if(subarr_1[f] == subarr_2[s]):
        return True
        
    needs_bigger = "s"
    
    if(f>s):
        needs_bigger = "f"
    
    max_v = max(subarr_1[f], subarr_2[s])
    max_e = "s" if (max_v == subarr_2[s]) else "f"
    
    if (needs_bigger == max_e):
        return True
    else:
        return False

def ceil(n):
    if(n%1 == 0):
        return n
    else:
        return int(n - (n%1) +1)

def trouble_sort(num_elements, arr):
    #create sublist one
    subarr_1 = []
    for x in range(0, num_elements, 2):
        subarr_1.append(arr[x])
            
    #create sublist two
    subarr_2 = []
    for x in range(1, num_elements, 2):
        subarr_2.append(arr[x])
    
    #sort
    subarr_1.sort()
    subarr_2.sort()
    
    err = -1
    for i in range(num_elements-1):
        f = int(ceil(i/2))
        s = int(i//2)
        
        if(not valid(subarr_1, subarr_2, s, f)):
            err = s+f
            break
        
    if(err == -1):
        return "OK"
    else:
        return str(err)

num_tests = int(input())
for n in range(num_tests):
    num = int(input())
    ar = [int(x) for x in input().split()]
    ans = trouble_sort(num, ar)
    print("Case #" + str(n+1) + ": " + ans)