x = list()
x.append('1')
dir(x)

print(x)

# split() function
## string.split()
## string.split
split on specific character
split a string into a list default on space


 test string as following example

 ``['abc,', 'so', 'abc.split,', 'and', 'this', 'returns', 'a', 'list'] ``

 ``test_string = ' abc, so abc.split, and this returns a list'
 test_list = test_string.split()``
 ***
# Dictionary

`` dict = {} `` is key value structure

list.keys()

list.value()
## Multiple for-loop
```
for aaa, bbb in jjj.items()
   print(aaa, bbb)
```
  ***
## Chapter 10
### Tuples
``tuples = () ``   
string and tuples are immutable
Tuples are comparable.

- `item() can return tuple`

- `sorted(list/tuple, reverse = True)` can order the tuples according to **key / values**.

- The tuple can be sorted by flipped.
#### example:
![MGmnC2](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/uPic/MGmnC2.png?token=AJ7JITGRYVMREP4XCJX7OS27N55YA)
#### Short version of the example
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/1601147113349-20200926200512.png?token=AJ7JITC4JUNZCRJKF3CWVXC7N6ISM)

# Ch11
## Regular expression
## 11.3
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200927102024.png?token=AJ7JITFSMKQLHRZ4T7YC2627OBMZK)

- `import re` import the regular expression library
- `re.search('Rex', string)` similiar to find()
- `re.findall('Rex', string)` similar to find() combining with slicing

- ``"."`` is any character.
- `*` (asterisk) is any number of character.
- `+` >= 1 time.
- `\S` match non-whitespace character.

## 11.2
- `re.findall('reg', string)` find all the possible matches

- `[0-9]+` to find one or more digits.

- `[AIEOU]` and `[aeiou]` are different, rex is **case sensitive**.
- `()` it starts to extract the string in bracket.
- `[]` not everything but XXX.
-`\` _escape character_ e.g. `\$`,

## Warning of Greedy Matching
`"*" and "+"` are very pushy that can match as much as the programme could match
## non-greedy Matching
`?` __(zero or more times)__ is able to solve this outcome.

### example of matching email
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200927103832.png?token=AJ7JITGJOYO5H3KQ47W7T5C7OBO5M)

```
(\S+@\S+)
```
