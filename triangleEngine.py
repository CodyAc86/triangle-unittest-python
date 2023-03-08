def define_lenght(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)

    if a == b == c:

        return "triangle is equilateral"

    elif a == b or b == c or a == c:

        return "triangle is isoscele"

    else :

        return "triangle is irregular"

    ## Aurel Codarcea

    
