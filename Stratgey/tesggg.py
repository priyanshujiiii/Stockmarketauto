L = ['good', 'string', 'good', 'again', 'good']
word = 'good'
def count(L, word):
    a = L[0]
    print(a)
    if a == word:
        return 1 + count(L[1:],word)
    else:
        return count(L[1:],word)