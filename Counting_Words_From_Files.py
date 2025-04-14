def counting_words(path) :
    """Doc string
    Counting the words from .txt files
    example = Key [word] : value [counting no of times it appeared]
                    
    """
    words = {}
    word = []
    with open(path,'r') as file :
        for lines in file :
            word = lines.split()
            for i in word :
                if i not in words :
                    words[i] = 1
                else :
                    words[i]+=1
    return words
path = "Wc.txt"
print(counting_words(path))





