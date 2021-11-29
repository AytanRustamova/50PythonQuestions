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



## 12. What Are The Types of Objects Support in Python Language?

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


## 13. Is Python object oriented? what is object oriented programming?

* Bəli Python obyekt yönümlü proqramlaşdırmadır. Obyekt yönümlü proqramlaşdırma classlardan ibarət olan sistemdir. OOP`nin konseptləri: Encapsulation, İnheritance, Abstact, Polymorphism. OOPnin əsas məntiqi proyekti müəyyən hissələrə (classlara) ayırıb bir birindən asılı olmayan hala gətirməsidir. Bu həm bir proyekt üstündə bir neçə nəfərin rahat işləməsini təmin edir həm də gələcəkdə yeni funksiyalar əlavə etməyi və ya dəyişiklik etməyi asanlaşdırır.


## 14. What are Accessors, mutators, @property?

* Pythonda Accessor`lar getter'lar deyə də adlanır. Hər hansısa bir value qaytaran funksiyalara accessorlar deyilir və əsasən dəyişilməyən valuelar olur. Mutatorlar isə setterlar olaraq adlanır. Bu funksiyalar isə adətən value dəyişmək üçün istifadə olunur. @property isə Pythonda bir decaratordur hansı ki, onun köməyi ilə bir funksiyanı funksiya atributu kimi istifadə edə bilirik. 


## 15. Differentiate between append() and extend() methods.?

* Bu iki method da list methodlarıdır və listə element əlavə etmək üçün istifadə olunur. 

1. append() menthodu listin sonuna 1 element əlavə etmək üçündür. Bu method listin uzunluğunu bir vahid artırır. Aşağıda verilmiş nümunədə də görə bilərik ki, append methodu yalnız 1 arqument qəbul edir.

```py 

l = ['Ayten']
 
l.append('Rustemova')
l.append('22')
 
print(l)

```

## Nəticə 

```

['Ayten', 'Rustemova', '22']

```

2. Extend() menthodu vasitəsilə isə eyni anda bir neçə dənə element əlavə edə bilirik. Bu method listin uzunluğunu əlavə edilən elementin sayına uyğun artırır.

```py

l = ['Ayten', 'Rüstəm', 'Hüseyn']
 

l.extend(['Yusif', 'Araz', 'Aydan'])
 

print(l)

```


## Nəticə 

```
['Ayten', 'Rüstəm', 'Hüseyn', 'Yusif', 'Araz', 'Aydan']

```

## 16. How will you remove last object from a list?


## Answer

* list.pop(obj=list[-1]) − pop metodu siyahıdan sonuncu elementi silir.



## 17. What is TkInter?

* TkInter Python kitabxanasıdır. GUI (graphical user interface) üçün toolkit'dir (alət). Əsasən, masaüstü proqramları üçün istifadə olunur. Rənglər, şriftlər, ölçülər və kursorlar kimi atributları mövcuddur.


## 18. What is the output of the following?

```py 
x = ['ab', 'cd']
print(len(map(list, x)))

```

## Answer

* Listin uzunluğu 2 olduğu üçün, 2 qaytaracaq.


## 19. How to retrieve data from a table in MySQL database through Python code?

## Answer

```py 
#1. Mysql ilə əlaqə qurulur.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

#2. Cursor obyekti yaranır

mycursor = mydb.cursor()

#3. Databazaya sorğu göndərilir

mycursor.execute("SELECT * FROM customers")

#4. Sorğuya uyğun seçdiyimiz datanı row şəklində bizə qaytarır.

myresult = mycursor.fetchall()

#5. Databaza əlaqəsi bağlanılır.

db.close()

```

## 20. Explain join() and split() in Python.

## Answer

* .join() metodu istənilən iterativ (sadalanan, list şəklində olan) elementi qəbul edir və onları müəyyən edilmiş simvollara ayırmağa kömək edir.

``` ','.join('12345') ```

Output - '1,2,3,4,5' (string return edir.)

* .split() metodu təyin etdiyimiz simvol ətrafında string'ləri ayırır.

``` 'example@gmail.com'.split('@') ```

Output - ['example', 'gmail.com'] (list içərisində simvola görə ayrılmış string'ləri return edir.)


## 21. What is multithreading? Give an example.

* Multithreading mövzusu bir çox dillərdə olduğu kimi Pythonda da mövcuddur. Multithreading ən çox process mövzusu ilə qarışdırılır. Process ilə threadin fərqi ondadır ki, process mövzusunda bir kod parçası engine tərəfindən ardıcıl olaraq oxunur. Bir process`i bir neçə threadlərə ayıraraq kodun ardıcıl yox eyni zamanda işləməsinə şərait yaradırıq. Və bu zaman bir threadin işi bitibsə onun nəticəsi əvvəl veriləcək. Qısacası, kodlar ardıcıllıqda yox hansının işi tez bitirsə ona uyğun nəticə çıxaracaq. Təbii ki, bu  processlərin daha sürətli işləməsini təmin edir. Məsələn aşağıdakı nümunəyə baxsaq

```py 

import threading

def calistir(threadName): 
    for i in range(7):
        print(threadName ,"işləyir")

t1 = threading.Thread(target=run, args = ("thread-1", ))
t2 = threading.Thread(target=run, args = ("thread-2", ))

t1.start()
t2.start()

```


## Nəticə 

``` 
thread-1 işləyir
thread-1 işləyir
thread-2 işləyir
thread-2 işləyir
thread-2 işləyir
thread-2 işləyir
thread-2 işləyir
thread-2 işləyir
thread-2 işləyir
thread-1 işləyir
thread-1 işləyir
thread-1 işləyir
thread-1 işləyir
thread-1 işləyir

```

* Thread-1 işləyərkən araya thread-2 də girib. Tam olaraq threadlər bu işi görür.


## 22. What is a dictionary in Python?

## Answer 

* Dictionary məlumatları key value şəklində saxlayan sırasız , dəyişkən data tipdir. Dictionarylər buruqlu mötərizə ilə ({}) yazılır. Məsələn məhsul və qiyməti kimi düşünmək olar. Burda key məhsuldur qiymət isə valuedir.

```py 

dict={'çanta':'50','şapka':'5','şalvar':'150'}

print(dict)

```

## 23. How do you get a list of all the keys in a dictionary?

* Bunun üçün key() methodundan istifadə olunur. 

```py 

mydict={'a':1,'b':2,'c':3,'e':5}
mydict.keys()
print(dict_keys)

```

Output 

```
(['a', 'b', 'c', 'e'])

```

## 24. How would you randomize the contents of a list in-place?

* Bunun üçün shuffle() methodundan istifadə olunur. 

```py 

from random import shuffle
shuffle(mylist)
mylist


```

Output: [3, 4, 8, 0, 5, 7, 6, 2, 1]



## 25. What is slicing?

## Answer 

* Slice() metodu bizə stringi və ya list elementlərini hissələrə ayırmaq üçün istifadə olunur.

```py 

  (1,2,3,4,5)[2:4]
        (3, 4)
     [7,6,8,5,9][2:]
        [8, 5, 9]
     'Hello'[:-1]
        'Hell'


```

## 26. What is a docstring?

## Answer 

* Docstring hər hansı bit funsiyanın və ya metodun daxilində yazılır. Və həmin funksiya/metodun nə etdiyini açıqlayır. Docstringlər 3 ədəd tək/cüt dırnaq arasında yazılır.

```py


def salam():
    """
    Bu funskiya ekrana salam yazısını çıxarır
    """
    print("salam")

salam()

```

Funksiyanın docstringini görmək üçün doc atributu istifadə edilir.


```py 

print (salam.__doc__)


```

## 27. Is Python case-sensitive?

## Answer

Bəli Python case-sensitive bir dildir. Bunu HTML ilə müqayisə edə bilərik. HTML'də `<p>` ilə `<P>` eyni mənanı verir. Yalnız Python böyük və kiçik hərfləri tanıdığı üçün 'number' variable'ni başqa yerdə istifadə edərkən 'Number' yazsanız Python error verəcək. 

```py 

#Yalnış nümunə

first_name = 'Tim'
last_name = 'Statler'

print('My name is ' + First_Name + ' ' + LAST_Name)

```

```py 

# Doğru nümunə

first_name = 'Tim'
last_name = 'Statler'

print('My name is ' + first_name + ' ' + last_name)

```


## 28. Explain the //, %, and ** operators in Python.

## Answer

// Bölünmə zamanı nəticənin integer hissəsini göstərir.

```py 


7 // 2

3

Normal bölünmə zamanı cavab 3.5 olmalı idi.


```

** Operatoru ədədin qüvvətini almaq üçündür. a üstü b almaq üçün a**b yazma lazımdır.

```py 

2**10

1024

```
% Operatoru qalıqlı bölünmədə qalığı görmək üçün istifadə edilir.

```py 

13 % 7 

6

```

## 29.What are assignment operators in Python?

## Answer

Pythonda xüsusi simvollarla işlənən bəzi operatorlar vardır. Bunu nümunələrlə daha yaxşı anlamaq olar. 

1. '+' operatoru. 

```py 
 a = 7
 a += 1
 a
```
Output: 8 

2.  '-' operatoru. 

```py 
 a = 7
 a -= 1
 a
```
Output: 6

3. '*' operatoru. 

```py 
 a = 7
 a*2
 a
```
Output: 14

4. '/' operatoru. 

```py 
 a = 14
 a/2
 a
```
Output: 7


5. '%' operatoru. (Bölmə zamanı qalığı göstərir)

```py 
 a = 5
 a%2
 a
```
Output: 1


6. '//' operatoru. (Bölmə zamanı tam rəqəmi göstərir)

```py 
 a = 5
 a//2
 a
```
Output: 2


7. '**' operatoru. (verilən rəqəmi qüvvətə yüksəldir.)

```py 
 a = 5
 a**2
 a
```
Output: 25


## 30. What are membership, operators?

## Answer 

* Bu operatorlar 'in' və 'not in' operatorlarıdır. Məsələn bir textdə hər hansısa bir hərfin, bir listdə hər hansısa bir elementin olub olmamasını yoxlamaq üçün istifadə edilə bilər. 

```py 
if 'a' in 'ayten':
    print(True)

```
Output: True


```py 

if 'x' not in 'ayten':
    print(False)

```

Output: False


## 31. What data types does Python support?

## Answer

* Python bizə 5 növ data tipi təqdim edir.

```py 

     a=7.0
     title="Ramayan's Book"
     colors=['red','green','blue']
     type(colors)
        <class 'list'>
     name=('Ramayan','Sharma')
     name[0]='Avery'
        Traceback (most recent call last):
        File "<pyshell#129>, line 1, in <module> name[0]='Avery'
        TypeError: 'tuple' object does not support item assignment # tuple kənardan dəyişdirilə bilmədiyi üçün TypeError verir.
     squares={1:1,2:4,3:9,4:16,5:25}
     type(squares)
        <class 'dict'>
     type({})
        <class 'dict'>
     squares={x:x**2 for x in range(1,6)}
     squares
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


```

## 32. How would you declare a comment in Python?

## Answer

* Pythonda comment'i '#' işarəsi ilə təyin edilir. 

```py 

# if name in my_list: 
#     print("salam")

```

## 33. How would you convert a string into an int in Python?

## Answer 

* Pythonda string data tipini int data tipinə çevirmək üçün int() methodundan istifadə edilir.

```py 

 int('227')

```
227

Biz hər bir obyekti type() methodu ilə hansı data tip olduğunu müəyyənləşdirə bilərik. 

```py 

 type('227')

```

<class 'str'>


```py 

 type(int('227'))

```

<class 'int'>


## 34. What is the concatenation?

* Pythonda '+' operatoru ilə stringəri, listləri bir birinə birləşdirmək üçün istifadə olunur.

```py 
 '32'+'32'
```
3232

```py 

 [1,2,3]+[4,5,6]

```
[1, 2, 3, 4, 5, 6]

* Burda diqqət etməli olduğumuz mövzu fərqli ata tipdə olan valueları bir birilə birləşdirə bilmərik.

```py 

 (2,3)+(4)  # burda error verəcək çünki, 4 integer olduğu üçün list ilə birləşdirə bilmərik. 

```

* Bunun üçün aşağıdakı kimi yazmaq olar.

```py 

 (2,3)+(4,)

```
(2, 3, 4)


## 35. What is Garbage Collection?

## Answer 

* Pythonda yaddaş tənzimləmək üçün proqramda istifadə edilməyən obyektləri avtomatik olaraq silir. Bu proses Garbage Collection adlanır. Garbage collection hər bir obyekt üçün reference count (referans sayı) sayır. Və reference count 0-a bərabır olduğu zaman həmin obyekti silir. Obyektin referans sayı bu obyekt yeni bir dəyişənə ötürüldüyü zaman və ya list, tuple, dictionary-də istifadə olunduğu zaman artır. Obyektin referansları yenidən təyin edildiyi zaman və ya dəyişdirildiyi zaman isə reference count azalır.


```py


a = 100  // <100> obyekti yaranır

b = a // <100>-ün reference count-u artır

c = b // <100>-ün reference count-u artır

d = [a] // <100>-ün reference count-u artır

b = 50 // <100>-ün reference count-u azalır

d[0] = 30 // <100>-ün reference count-u azalır



```

## 36. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?

## Answer

* Yuxarıdakı sualda qeyd etdiyimiz kimi -1 indexi listin daxilində sonuncu elementi təmsil edir. Bu halda bizim listimizdə sonuncu element 25 olduğu üçün, cavab 25 olacaqdır.


## 37. What are negative indexes and why are they used?


## Answer 

* Pythonda listin indexi neqativ və pozitiv ola bilər. İndex pozitiv olduğu zaman 0 birinci index, 1 ikinci index olur və indexlər bu ardıcıllıqla davam edir. İndex neqativ olduqda isə -1 sondan birinci index, -2 sondan ikinci index olur və bu ardıcıllıqla davam edir. Neqativ index adətən listə yeni əlavə olunmuş obyekti silmək üçün və ya ən son əlavə olunmuş obyekti görmək üçün istifadə edilir.



## 38.  What is Monkey patching ?

## Answer 

* Hansısa classı və ya metodu sonradan dəyişmək prosesinə pythonda monkey patching deyilir. Bəzən böyük proyektlərdə işləyən zaman third-party bir kitabxananın bizin üçün əlverişli olmadığını görə bilirik. Bu zaman monkey patching istifadə edilə bilər.


## 39. How to open a file c:\scores.txt for writing?

## Answer 

```py 

file = open("c:\\sample.txt", "w")

```

## 40. How will you remove last object from a list?

## Answer 

* pop() methodundan istifadə olunur.
  
```py 
listOfCountries = ['India','China', 'Bhutan','Nepal']
print("List Of Countries are:",listOfCountries)
removedCountry = listOfCountries.pop()
print("List Of Countries after removing last element:",listOfCountries)
print("Removed country:",removedCountry)

```


## 41. Explain split(), sub(), subn() methods of re module in Python.

## Answer 
* Pythonda stringləri dəyişməyin bir neçə yolu var. 

1. split() - bu method regex pattern'ə uygun olaraq verilmiş şərtə görə stringi bölür
2. sub() - bu methodda 2 parametr verilir, biri textdə dəyişmək istədiyiniz hissədir. Digəri isə dəyişmək istədiyiniz hissəyə nə qoymaq istəyirsiz.
3. subn() - bu method da eyni sub methodu kimi işləyir, eyni zamanda nə qədər dəyişiklik edibsə onun sayın da göstərir.


## 42. Which of the following is an invalid statement?

a) abc = 1,000,000
b) a b c = 1000 2000 3000
c) a,b,c = 1000, 2000, 3000
d) a_b_c = 1,000,000 
## Answer

* Cavab B-dir. Çünki a və d bəndində abc variable'i təyin olunub və içində tuple var. c bəndində isə 3 variable təyin olunub və hərəsinə bir value verilib.


## 43. What is the output of the following?

```py
try: 
    if '1' != 1: 
        raise
```
## Answer

* Try catch'siz işləmədiyinə görə bu kod səhvdir, heç bir nəticə verməyəcək.



## 44. Explain Inheritance in Python with an example.

* Inheritance (varislik) bizə kodun təkrar istifadəsini təmin edir, proqram yaratmaq və saxlamağı asanlaşdırır. Bir class'a digər class'ın bütün atributlarını, metodlarını əldə etməyə kömək edir. Bu isə bizə eyni xüsusiyyətlərə sahib bir çox class'ı sadəcə bir dəfə yazaraq, digərləri ilə overwrite (üzərinə yazmaq) etməyə və ya yeni metod, atribut əlavə etməyə imkanı verir.

Python bir neçə fərqli tipdə inheritance'ı dəstəkləyir:

* Single Inheritance - bir class tək əsas class'dan inherit (miras) alır.
* Multi-level (çoxsəviyyəli) Inheritance - class A əsas class Base-dən inherit alır, həmçinin class B də class A-dan inherit alır.
* Hierarchical (ierarxik) inheritance – bir parent (valideyn) class'dan istənilən sayda child (uşaq) class inherit ala bilər.
* Multiple Inheritance - bir child class birdən çox parent class'dan inherit ala bilər.
* Hybrid Inheritance - iki və ya daha çox inheritance növünün birləşməsidir.




  












