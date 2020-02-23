def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    compare_list = []
    letter_list = list(secretWord)
    for idx in range(len(lettersGuessed)):
        if lettersGuessed[idx] in letter_list:
            compare_list.append(lettersGuessed[idx])
    compare_list.sort()
    letter_list.sort()

    return(compare_list == letter_list)


print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
