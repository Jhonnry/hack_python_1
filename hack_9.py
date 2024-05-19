"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    i = 1
    while i < len(result) * 2 - 1:
        result.insert(i, '@')
        i += 2
    return result

r = fn_hack_9()

print(r)