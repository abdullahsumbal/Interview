


s = "I love programmming and money"
t = "I and money"

s_list = s.split(' ')
t_list = t.split(' ')
pointer_t = 0
pointer_s = 0

missing = []

for word in s_list:

    if(pointer_t >=len(t_list)):
        break
    #print("word:", word, "t:",t_list[pointer_t])

    if word == t_list[pointer_t]:

        pointer_t+=1
    else:
        missing.append(word)
    pointer_s += 1

missing = missing + s_list[pointer_s:]

return missing

print(missing)
