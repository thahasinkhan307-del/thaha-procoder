def move_hyphen(s):
    if s is None:
        return None
    hyphens=s.count('-')
    result='_'*hyphens
    for ch in s:
        if ch !='_':
           result+=ch
        return result
    #Test
    s=input("Enter bstring:")
    print("Original:",s)
    print("Modified:",move_hyphen(s))
