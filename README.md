# 50PythonQuestions

## 1.How can you improve the following code?

```py

i = 0
for letter in string.letters:
    print("The letter at index %i is %s" % (i, letter))
    i = i + 1

```
## Answer

```py 

import string
for index , letter in enumerate(string.ascii_letters):
    print(f'The letter at index {index} is {letter}')

```
* Enumerate methodu iterable'lərin sayını özündə saxladığına görə itarableləri artırmaq kimi işlərə ehtiyac duyulmur. 


## 2.What will be the output of the code below?

```py 

List = ['a', 'b', 'c', 'd', 'e']
print(List[10:])

```
## Answer 

* Bu method listi bölmək üçün istifadə olunur, 10-cu indexdən sonrakı indexdə duran valueları print edilməsini istəyir. Amma 10cu index olmadığına görə də sadə içi boş list qaytaracaq.
