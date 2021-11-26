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


## 3. How do I convert a number to a string?

### Answer 

Pythonda number data tipini string data tipinə dəyişməyin bir neçə yolu var.
str(), "%s" , "f-string" , format()  kimi methodlardan istifadə oluna bilər

###  str() function istifadəsi

```py 

num = 10

print(type(num))

converted_num = str(num) 

print(type(converted_num))

```

###   “%s” keyword istifadəsi

```py 


num = 10
 
print(type(num))
 
converted_num = "% s" % num
print(type(converted_num))

```

###   f-string`in istifadəsi

```py 
num = 10

print(type(num))
 
converted_num = f'{num}'
 
print(type(converted_num))

```

###  .format() function istifadəsi

```py 

num = 10
 
# check  and print type of num variable
print(type(num))
 
# convert the num into string and print
converted_num = "{}".format(num)
print(type(converted_num))

```