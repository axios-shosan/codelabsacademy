def palindrome(word):
    word = word.replace(' ', '')
    i,j = 0, len(word)-1
    while(i<j):
        if word[i] != word[j]:
            return False
        i=i+1
        j= j-1
    return True
print(palindrome("nurses run"))
