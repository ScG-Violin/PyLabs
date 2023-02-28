comp_nuc = {'G':'A', 'A':'G', 'C':'T', 'T':'C' }
input_s = str(input()); input_t = str(input())
num = 0; denom = 0

for i in range(len(input_s)):
    if (input_s[i] == input_t[i]):
        continue
    elif (comp_nuc[input_s[i]] == input_t[i]):
        num += 1
    else:
        denom += 1

res = num / denom

for (s,t) in zip(input_s,input_t):
    print(s, ":", t)
print(res)