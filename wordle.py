# py -m pip install wordfreq
from wordfreq import zipf_frequency as f
while True:
    text_file = open('wordle.txt')
    data = text_file.read()
    text_file.close()
    def convert(string):
        return list(string.split(" "))
    wordle = convert(data)




    guess = list(input('Enter the guess:\n'))
    colors = list(input('Enter the colors corresponding with the word:\n'))

    yellow = []
    green = []

    in_word = []
    if input('Other letters not in word? y/n:\n') == 'y':
        not_word = list(input("Enter known letters not in word:\n"))
    else:
        not_word = []




    for i in range(5):
        #Grey
        if colors[i] == 'g':
            not_word.append(guess[i]) 
            yellow.append('_')
            green.append('_')
        #Green
        elif colors[i] == 'G':
            in_word.append(guess[i])
            green.append(guess[i])
            yellow.append('_')
        elif colors[i] == 'y':
            in_word.append(guess[i])
            green.append('_')
            yellow.append(guess[i])
    green_known = 5 - green.count('_')

    for i in range(len(not_word)):
        if not_word[i] in in_word:
            not_word.remove(not_word[i])
            break




    skip_list = []
    for i in range(len(wordle)):
        for x in range(len(in_word)):

            if in_word[x] not in wordle[i]:
                skip_list.append(wordle[i])
                break
    wordle = [i for i in wordle if i not in skip_list]

    if 'sower' in wordle:
        print('EEEE')

    print(green, in_word, not_word)
    skip_list = []
    for i in range(len(wordle)):
        for x in range(len(not_word)):
            if not_word[x] in wordle[i]:
                skip_list.append(wordle[i])
                break

    wordle = [x for x in wordle if x not in skip_list]

    if 'sower' in wordle:
        print('EEEE')


    #GREEN
    skip_list = []
    for i in range(len(wordle)):
        count = 0
        word = list(wordle[i])
        for x in range(5):
            if word[x] == green[x]:
                count += 1      
        if count == green_known:
            skip_list.append(wordle[i])
    wordle = skip_list
                

    if 'sower' in wordle:
        print('EEEE')

    skip_list = []
    for i in range(len(wordle)):
        count = 0
        word = list(wordle[i])
        for x in range(5):
            if word[x] != yellow[x]:
                count += 1      
        if count == 5:
            skip_list.append(wordle[i])

    if 'sower' in wordle:
        print('EEEE')


    wordle = skip_list





    skip_list = []
    for i in range(len(wordle)):
        skip_list.append(f(wordle[i], 'en'))



    

    print("Done!")
    if len(skip_list) - skip_list.count(0.0) >= 3:
        for i in range(3):
            num = max(skip_list)
            word = wordle[skip_list.index(num)]
            print(f'#{i+1} - {num}   {word}')
            skip_list.remove(num)
            wordle.remove(word)
        if input(f'Other words({len(wordle)} words long)\n') == '':
            print(wordle)
    else:
        print(wordle)
        print(skip_list)
