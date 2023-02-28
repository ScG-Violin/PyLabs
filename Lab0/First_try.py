comp_nuc = {'T':'A', 'G':'C', 'A':'T', 'C':'G' }
input_str = ''.join(list(reversed(str( input() ))))
output_str = ""
reversed(input_str)
for i in range(len(input_str)):
    output_str += comp_nuc[input_str[i]]
print(output_str)