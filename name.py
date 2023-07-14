What's in a name?
...Or rather, what's a name in? For us, a particular string is where we are looking for a name.

Task
Write a function, taking two strings in parameter, that tests whether or not the first string contains all of the letters of the second string, in order.

The function should return true if that is the case, and else false. Letter comparison should be case-INsensitive.

Examples
    nameInStr("Across the rivers", "chris") --> true
                ^      ^  ^^   ^
                c      h  ri   s
                
    Contains all of the letters in "chris", in order.
----------------------------------------------------------
    nameInStr("Next to a lake", "chris") --> false
    
    Contains none of the letters in "chris".
--------------------------------------------------------------------
    nameInStr("Under a sea", "chris") --> false
                   ^   ^
                   r   s
                   
    Contains only some of the letters in "chris".
--------------------------------------------------------------------
    nameInStr("A crew that boards the ship", "chris") --> false
                 cr    h              s i
                 cr                h  s i  
                 c     h      r       s i
                 ...
                 
    Contains all of the letters in "chris", but not in order.
--------------------------------------------------------------------
    nameInStr("A live son", "Allison") --> false
               ^ ^^   ^^^
               A li   son
                 
    Contains all of the correct letters in "Allison", in order, 
    but not enough of all of them (missing an 'l').


def name_in_str(str, name):
    str = str.lower()
    name = name.lower()
    i, j = 0,0
    amountLeft = len(name)
    strLength = len(str)
    
    while i < strLength and j < len(name):
        if str[i] == name[j]:
            i += 1
            j+= 1
            amountLeft -= 1
        else:
            i += 1
    if amountLeft == 0:
        return True
    else:
        return False
