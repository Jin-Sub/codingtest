words = input().upper()
unique = list(set(words))
cnt_list = []
for i in unique:
    count = words.count(i)
    cnt_list.append(count)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_word = cnt_list.index(max(cnt_list))
    print(unique[max_word])
