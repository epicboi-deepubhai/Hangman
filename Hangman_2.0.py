from words import word_listimport randomdef get_word():    word = random.choice(word_list).upper()    return worddef play(word):    word_competion = '_' * len(word)    guessed = False    guessed_letters = ''    guessed_words = ''    tries = 6    print("Let's play Hangman!")    print(display_hangman(tries))    print(word_competion)    print('\n')    word_competion = ''    while not guessed and tries > 0:        guess = input('Please input a letter or word: ').upper()        if len(guess) == 1 and guess.isalpha():            if guess in guessed_letters:                print('You already gussed the letter!', guess)            elif guess not in word:                print(guess, ' is not in the word!')                tries -= 1                guessed_letters += guess            else:                print('Good job! ', guess, ' is in the word')                guessed_letters += guess                word_competion = ''                for i in word:                    if i in guessed_letters:                        word_competion += i                    else:                        word_competion += '_'            if word_competion == word:                guessed = True        elif len(guess) == len(word) and guess.isalpha():            if guess == word:                print('You are absolutely right! ', guess,' is the word' )                guessed = True                word_competion = word            else:                if guess in guessed_words:                    print(guess, ' has already been guessed!')                else:                    print(guess, ' is not the word!')                    guessed_words += guess                    tries -= 1                    word_competion = ''                    for i in word:                        if i in guessed_letters:                            word_competion += i                        else:                            word_competion += '_'                        if word_competion == word:                            guessed = True        elif len(guess)!=1 and len(guess)!=len(word):            print('No cheating')        else:            print('Not a valid guess!')        print(display_hangman(tries))        print(word_competion)        print('\n')    if not guessed:        print('You loose!')    else:        print('congratulation you won!')    print('the word was ', word)def display_hangman(tries):    stages = [                """                   --------                   |      |                   |      O                   |     \\|/                   |      |                   |     / \\                   -                """,                """                   --------                   |      |                   |      O                   |     \\|/                   |      |                   |     /                    -                """,                """                   --------                   |      |                   |      O                   |     \\|/                   |      |                   |                         -                """,                """                   --------                   |      |                   |      O                   |     \\|                   |      |                   |                        -                """,                """                   --------                   |      |                   |      O                   |      |                   |      |                   |                        -                """,                """                   --------                   |      |                   |      O                   |                       |                         |                        -                """,                """                   --------                   |      |                   |                         |                       |                         |                        -                """    ]    return stages[6-tries]def main():    word = get_word()    play(word)    while input("Play Again? (Y/N) ").upper() == "Y":        word = get_word()        play(word)main()