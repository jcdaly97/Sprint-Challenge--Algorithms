'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = None):
    index = 0
    if not count:
        count = 0
    if len(word)<2:
        return count
    else:
        try:
            index = word.index("th")
        except:
            return count
        else:
            count += 1
            return count_th(word[index+2:], count)
        

