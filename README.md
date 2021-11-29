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
 
print(type(num))
 
converted_num = "{}".format(num)
print(type(converted_num))

```

## 4. What is Garbage Collection?

## Answer

* Pythonda Garbage Collection istifadə olunmayan obyektlərin depolanması üçün bir yerdir. Bu funksiya uzun müddət istifadə olunmayan obyektləri siradan çıxarır və yaddaşda yeni obyektlər üçün yer açır. Bunu komputerdə  recycling system(yenidən emal) prosesi kimi təsəvvür edə bilərsiniz. 


## 5. How do you create your own package in Python?

## Answer

1. Əvvəlcə directory yaradırıq və ona package name veririk
2. Sonra ora lazım olan funksiyaları və classları yerləşdiririk.
3. Sonunda isə directory`nin içində init.py faylı yaradırıq ki, Python bu directory-nin  package olduğunu anlasın.

## 6. Explain the use "with" statement in python?

## Answer

"With" statement kodların daha oxunaqlı və təmiz olmasında önəmli rol oynayır. Bunun yanı sıra, faylların idarə olunmasına da köməklik edir. Aşağıdakı kod parçasında bunun nümunısini görə bilərik.

```py 

# 1) with statementdən istifadə edilmədikdə
file = open('file_path', 'w')
file.write('hello world !')
file.close()
  
# 2) with statementdən istifadə edilmədikdə
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

  
# with statementdən istifadə edildikdə
with open('file_path', 'w') as file:
    file.write('hello world !')

```

## 7. Mention the use of the split function in Python?

## Answer

Pythonda split() methodu listləri verilmiş şərtə əsasən bölür. Default olaraq(Əgər şərt verilməsə) listləri boşluğa əsasən bölür. Aşağıdakı nümunədə necə işlədiyini görmək olar.

```py 

text = 'geeks for geeks'
  
# boşluğa əsasən bölür
print(text.split())
  
word = 'geeks, for, geeks'
  
# Vergülə əsasən bölür
print(word.split(','))
  
word = 'geeks:for:geeks'
  
# Qoşa nöqtəyə əsasən bölür
print(word.split(':'))
  
word = 'CatBatSatFatOr'
  
# t hərfinə əsasən bölür
print(word.split('t'))

```


## 8. How do you take input in Python?


## Answer

* Pythonda input üçün input() funksiyasından istifadə olunur. Userdən hər hansısa bir datanı götürmək üçün istifadə olunur. Məsələn age = input("Yaşınızı qeyd edin: ")  formasında yazsaq userdən gələn datanı bir dəyərə bərabər edə bilirik. Bir nüansı qeyd etmək lazımdır ki, input() methodu string qaytarır, əgər int qaytarmasını istəyirsinizsə age = int(input("Yaşınızı qeyd edin: ")) kimi yaza bilərsiniz.



## 9. Explain logical operators in Python.

Bir çox programlaşdırma dilində olduğu kimi Pythonda da 3 dənə logical operator var. And , Or, Not.

# 1. And operator 
* Bu operatorla verilən bütün şərtlər ödənməlidir.
  
```py 

a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

```

# Nəticə 

```
The numbers are greater than 0

Atleast one number is not greater than 0
```
# 2. Or operator 
* Bu oparetorla verilən statementlar bir şərt ödəndikdə işləyir.

```py 

a = 10
b = -10
c = 0
  
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
  
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

```

# Nəticə 

```

Either of the number is greater than 0
No number is greater than 0

```

# 3. Not operator 
* Pythonda Not operatoru boolean valuelarla işlənir. Məsələn boolean value True-dursa, bu False qaytarır.

```py 
a = 10
  
if not a:
    print("Boolean value of a is True")
  
if not (a%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

```

# Nəticə

``` 
10 is divisible by either 3 or 5

```

## 10. Mention five benefits of using Python?

## Answer

1. Yeni başlayanlar üçün öyrənilməsi asan olan bir dildir.
2. Multi-purpose bir dildir. Yəni bir çox platforma üçün layihə hazırlamaq olur. Web app, desktop app, oyun, Aİ(suni intellekt) kimi bir fərqli sahələrdə istifadə oluna bilir.
3. Pythonun fərqli və geniş kitabxanasının olması developerlərə də rahatlıq təmin edir. Beləliklə developerlərin daha productive olmasına kömək edir.
4. Python developers community digər dillərə baxanda daha geniş yayıldığına görə bir məsələnin həllini tapmaq daha az vaxt alır.
5. OOPni dəstəklədiyinə görə hard codingdən bizi qoruyur. OOPnin bütün üstünlüklərini istifadə edə bilirik.


## 11. Mention what are the rules for local and global variables in Python?


## Answer

* Funksiyaların içində yaranan hər bir variable (məs: x=3) local variable sayılır. Onun istifadəsi və icazəsi yalnız həmin funksiya üçün olur. 

```py 
def foo():
    y = "local"
    print(y)

foo()

```

* Nəticə 
  
```
local
```

* Məsələn yuxarıdakı kod parçasına baxdıqda y dəyəri funksiyanın içində yaranıb və içində də istifadə olunur. Əgər print funksiyası funsiyanın çölündə icra olunsaydı kod error verecekdi.

## Global Value

* Bu o variabledir ki funksiyanın çölündə də yaransa da onu bütün funksiyalarda istifadəsi mümkündür.

```py 

x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)


```
* Nəticə 

```
x inside: global
x outside: global

```

* Bu misalda isə x global variable olduğu üçün həm funksiyanın içində həm də çölündə istifadəsi mümkündür.



## 11. What Are The Types of Objects Support in Python Language?

* Pythonda sabit və dəyişən data tiplər vardır

## Sabit data tiplər

1. Strings
2. Tuples
3. Numbers

## Dəyişən data tiplər

1. Lists
2. Dictionaries
3. Sets

* Sabit və dəyişən data tiplərinin fərqi ondadır ki, məsələn bir list verilmişdir a = ['Ayten', 'Rustemova', 22 ]. Sonradan a[2]= 25 kimi yazsaq listin 2ci indexindəki elementi dəyişə bilirik, amma bunu tuple, string, numbers kimi data tiplərdə bunu etmək mümkün deyil.


## 12. Is Python object oriented? what is object oriented programming?

* Bəli Python obyekt yönümlü proqramlaşdırmadır. Obyekt yönümlü proqramlaşdırma classlardan ibarət olan sistemdir. OOP`nin konseptləri: Encapsulation, İnheritance, Abstact, Polymorphism. OOPnin əsas məntiqi proyekti müəyyən hissələrə (classlara) ayırıb bir birindən asılı olmayan hala gətirməsidir. Bu həm bir proyekt üstündə bir neçə nəfərin rahat işləməsini təmin edir həm də gələcəkdə yeni funksiyalar əlavə etməyi və ya dəyişiklik etməyi asanlaşdırır.


## 13. What are Accessors, mutators, @property?

* Pythonda Accessor`lar getter'lar deyə də adlanır. Hər hansısa bir value qaytaran funksiyalara accessorlar deyilir və əsasən dəyişilməyən valuelar olur. Mutatorlar isə setterlar olaraq adlanır. Bu funksiyalar isə adətən value dəyişmək üçün istifadə olunur. @property isə Pythonda bir decaratordur hansı ki, onun köməyi ilə bir funksiyanı funksiya atributu kimi istifadə edə bilirik. 




