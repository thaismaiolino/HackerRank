''''
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.
For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.
''''

def repeatedString(s, n):
    qty_start = 0
    for item in s:
        if item == 'a':
            qty_start += 1
    qty = (n/len(s)) * qty_start
    rest = n%len(s)
    if rest != 0:
        temp_qty = 0
        for item in s[:rest]:
            if item == 'a':
                temp_qty += 1
        qty += temp_qty
    return qty

# repeatedString('udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps', 872514961806)

# repeatedString('aba', 10)