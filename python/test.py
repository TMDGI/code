from math import *

for i in range(144):
    int_exp  = int(exp(i));       int_len_exp  = len(str(int_exp))
    int_fact = int(factorial(i)); int_len_fact = len(str(int_fact))
    int_pow  = int(pow(i, i));    int_len_pow = len(str(int_pow))
    #print(f"[{i}]")
    #print(f"{int_exp}\n{int_fact}\n{int_pow}")
    #print(f"lens: {int_len_exp} << {int_len_fact} << {int_len_pow}")
    print(f"diff_lens: {int_len_fact - int_len_exp} << {int_len_pow - int_len_fact}")
    