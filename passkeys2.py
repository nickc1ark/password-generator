import random
import string
import time
import os
t = time.sleep
s = string

title = ['passkey generator',
         'Passkey generator',
         'PAsskey generator',
         'PASskey generator',
         'PASSkey generator',
         'PASSKey generator',
         'PASSKEy generator',
         'PASSKEY generator',
         'PASSKEY Generator',
         'PASSKEY GEnerator',
         'PASSKEY GENerator',
         'PASSKEY GENErator',
         'PASSKEY GENERator',
         'PASSKEY GENERAtor',
         'PASSKEY GENERATor',
         'PASSKEY GENERATOr',
         'PASSKEY GENERATOR']

# clear screen and for loop to display title
os.system('clear||cls')
t(1)
for i in title:
    t(.03)
    os.system('clear||cls')
    print i
    print "\n"

# for loop to display password options
a = ['1. 8 CHAR PASSKEY',
     '2. 12 CHAR PASSKEY',
     '3. 16 CHAR PASSKEY',
     '4. <shift> PASSKEY']
for i in a:
    print i
    continue
    print "\n"

# variable to store characters used in options 1-3
# user input to select options 1-4
# functions to generate 8, 12, or 16 key passwords
char_set = s.ascii_letters + s.digits + s.punctuation

select = raw_input('-> ')

if select == '1':
    print ''.join(random.sample(char_set*8, 8 ))
elif select == '2':
    print ''.join(random.sample(char_set*12, 12 ))
elif select == '3':
    print ''.join(random.sample(char_set*16, 16 ))
elif select == '4':

    # option 4 generates passwords to be typed while holding the shift key.
    # used for the convenience of having complex passwords while
    # making them quicker/easier to type and/or remember.
    # list of shift key symbols.
    # assign all uppercase letters to variable.
    # concatenate string of uppercase letters to list of symbols.
    # user input to choose number of characters in password
       
    shift_sets = ['1. 8 key shift set',
                  '2. 12 key shift set',
                  '3. 16 key shift set']
    for i in shift_sets:
        print i
        continue

    shift = ['~','!','@','#','$','%','^',
             '&','*','(',')','_','+','{',
             '}','|',':','"','<','>','?']

    shift2 = string.uppercase
    shift.extend(shift2)
    
    chars_1 = raw_input('> ')
    
    if chars_1 == '1':
        print "\n"
        print ''.join(random.sample(shift*8, 8))
        print '\n'
    elif chars_1 == '2':
        print '\n'
        print ''.join(random.sample(shift*12, 12))
        print '\n'
    elif chars_1 == '3':
        print '\n'
        print ''.join(random.sample(shift*16, 16))
        print "\n"
    else:
        print "choose options 1-3"
else:
    print "choose options 1-4"
