'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # is word at least 2 char long?
    if len(word) < 2:
        return 0
    
    # for word more than 2 char long
    # check first 3 chars for 'th'
    if word[:2] == "th":
        # start from where first if left off
        # to search for 'th'
        return 1 + count_th(word[2:])
    else:
        # start search for 'th' in between other attempts
        return (count_th(word[1:]))
