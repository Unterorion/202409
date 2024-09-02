a = "Life is too short. You need python."
print(len(a))

print(f'{"python":!^12}')

list = a.split()
print(list)

def word_join():
    sent = input("A sentence to split: ")
    lett = input("A letter to join in the sentence: ")
    wordlist = sent.split()
    result = ''
    for word in wordlist:
        if wordlist.index(word) < len(wordlist)-1:
            result = result + word + lett
        else:
            result = result + word
    
    print(result)
    return(result)

word_join()