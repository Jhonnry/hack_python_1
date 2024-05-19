"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    # ...
    result = list(result.upper())
    result[1] = "0"
    result[2] = "0"
    result[4] = "1"
    result[6] = "@"
    return result

r = fn_hack_10()

print(r)