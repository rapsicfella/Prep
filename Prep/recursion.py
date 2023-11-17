def rec_sum(num):
    if num < 10: return num
    return num%10 + rec_sum(num//10)


def wordSplit(phrase, wordlst, output = None):
    '''
    Note: This is a very "python-y" solution.
    ''' 
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in wordlst:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return wordSplit(phrase[len(word):],wordlst,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output  


def reverseString(s):
    if len(s) <= 1: return s
    return reverseString(s[1:]) + s[0]


def permute(s):
    out = []
    if len(s) == 1: return [s]

    for i in range(len(s)):
        for perm in permute(s[:i]+s[i+1:]):
            out += [s[i]+perm]
    return out


lis = [1,3]
lis+=[4,5]
print(lis)
print(permute('abc'))
phrase = 'mancanrun'
wordlst = ['man', 'run', 'can']
print(wordSplit(phrase, wordlst))
print(rec_sum(111111))
print(reverseString('harsha'))