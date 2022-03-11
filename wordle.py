text_file = open("wordle.txt")
data = text_file.read()
text_file.close()
def convert(string):
    return list(string.split(" "))
wordle = convert(data)

data = input("Enter known letters:\n")
in_word = convert(data)
data = input("Enter known letters not in word:\n")
not_word = convert(data)

green = input("Enter the green positons, enter other letters using _. Format: p_ols\n")
green_known = 5 - green.count('_')
green = list(green)

print(green_known)

skip_list = []
for i in range(len(wordle)):
    for x in range(len(in_word)):
        print(wordle[i])
        if in_word[x] not in wordle[i]:
            skip_list.append(wordle[i])
            break
wordle = [i for i in wordle if i not in skip_list]

skip_list = []
for i in range(len(wordle)):
    for x in range(len(not_word)):
        if not_word[x] in wordle[i]:
            skip_list.append(wordle[i])
            break

wordle = [x for x in wordle if x not in skip_list]

skip_list = []

for i in range(len(wordle)):
    count = 0
    for x in range(5):
        word = list(wordle[i])
        # word into list 


        if word[x] == green[x]:
            count += 1



        if count == green_known:
            skip_list.append(wordle[i])
            

print(f"Words that fit criteria ({len(skip_list)}):\n")
print(set(skip_list))







