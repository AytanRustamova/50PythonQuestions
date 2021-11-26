1. How can you improve the following code?

i = 0
for letter in string.letters:
    print("The letter at index %i is %s" % (i, letter))
    i = i + 1

////////////////////////////////////////////////////////////////////////////

import string
for index , letter in enumerate(string.ascii_letters):
    print(f'The letter at index {index} is {letter}')

Enumerate methodu iterable'lərin sayını özündə saxladığına görə itarableləri artırmaq kimi işlərə ehtiyac duyulmur. 