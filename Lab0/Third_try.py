input_str = str(input())
key_word = str(input())
res = ''
len_key = len(key_word)

for i in range(len(input_str) - len_key + 1):
    if (input_str[i:i+len_key] == key_word):
        res += str(i) + ' '
if res == '':
    res = 'none'
else:
    res = res[:-1]

print(res)