import random
import string
print(' !!!! Welcome to password Generator !!!!')
print()
print('Please give space while entering max and min characters/numbers/special characters')
print()
a,b= [int(x) for x in input("Enter minimum and maximum length number of Complex Password Generator  :").split()]
c,d= [int(x) for x in input("Enter minimum and maximum number of lower case characters you want in your password :").split()]
e,f= [int(x) for x in input("Enter minimum and maximum number of upper case characters you want in your password :").split()]
g,h= [int(x) for x in input("Enter minimum and maximum number of numerics you want in your password :").split()]
i,j= [int(x) for x in input("Enter minimum and maximum number of special characters you want in your password :").split()]
a_lower=random.sample(string.ascii_lowercase,(random.randint(c,d)))
a_upper=random.sample(string.ascii_uppercase,(random.randint(e,f)))
n_number=random.sample(string.digits,(random.randint(g,h)))
s_special=random.sample(string.punctuation,(random.randint(i,j)))
f_sample=a_lower+a_upper+n_number+s_special
pass_raw=random.sample(f_sample,random.randint(a, b))
final_password="".join(pass_raw)
print('Password Generated :',final_password)
print()
def gen_again():
    x=input('Do You want to  generate Password again [y/n]:')
    if x.lower()=='y':
        pass_raw=random.sample(f_sample,random.randint(a, b))
        final_password="".join(pass_raw)
        print('Password Generated :',final_password)
        print()
        gen_again()
    else:
        print(' !!!! Thank you !!!')


gen_again()
