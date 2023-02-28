f_name = str(input())
f = open(f_name, 'r')
str_list = []
data = str(f.readline())

while ( data != ''):
    if data[0] != '>':
        str_list.append(data.strip('\n'))
    data = str(f.readline())
f.close()

str_list = sorted(str_list, key= lambda s: len(s))

if len(str_list) == 0:
    print('none')
    exit(0)
elif len(str_list) == 1:
    print(str_list[0])
    exit(0)

def substrings(origin_str):
    list_substr = []
    len_origin = len(origin_str)
    for i in range(len_origin):
        for il in range(i + 1, len_origin + 1):
            list_substr.append(origin_str[i:il])
    return list_substr

list_substr = substrings(str_list[0])

for i in range(1, len(str_list)):
    if (len(list_substr) == 0 ):
        print('none')
        exit(0)
    list_substr = list(filter(lambda s: str_list[i].find(s) > -1, list_substr))

res = max(list_substr, key= lambda s: len(s))
print(res)