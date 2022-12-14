Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

	for num in numbers:
		if num > 500:
			break
		elif num < 151 and num % 5 == 0:
			print(num)

Q26. What is a string? How can we declare string in Python?
Ans: String datatype in Python is used to store character or text data.It is also a default datatype in python.
  It can be declared using :
- Single quotes: 'Bhavesh'
- Double quotes: "Bhavesh"
- Triple quotes: ''' Bhavesh '''

Q27. How can we access the string using its index?
Ans : By providing index no. or range of index numbers.

    str = 'Data Engineer'
    print(str[0:4]) -> 'Data'
    print(str[ : : -1]) -> 'reenignE ataD'

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

ANS:   print(string[9:])

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

ANS:    print(string[ :-8:-1])

Q30. Reverse the string given in the above question.

ANS:    print(string[ : :-1])

Q31. How can you delete entire string at once?

ANS:    del string

Q32. What is escape sequence?
ANS: Escape sequence ( \ ) is used to treat the special character as a part of string to avoid the errors. 
      e.g. string = "Im a\" Data \" Engineer"

Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```

Ans:    print("'iNeuron's Big Data Course'")
    # or
    print('\'iNeuron\'s Big Data Course\'')

Q34. What is a list in Python?
Ans: List in python is a sequential datatype. It is used to store different types of data in a sequential manner.

Q35. How can you create a list in Python?

Ans    sample_list = [1, 'Hi', True, 4.5]

Q36. How can we access the elements in a list?
Ans : By using index.

    list = [1, 'Hi', True, 4.5]
    list[0] -> 1
    list[1] -> 'Hi'
    list[-1] -> 4.5

Q37. Write a code to access the word "iNeuron" from the given list.
```
 list = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 
Ans: print(list[4][2])

Q38. Take a list as an input from the user and find the length of the list.

	
Ans:    input_list = input('Enter , separated list items:').split(',')
        print(input_list)
    
   
Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```

Ans:    list.insert(3, 'Big')
    # Output -> ["Welcome", "to", "Data", "Big", "course"]
   
Q40. What is a tuple? How is it different from list?
Ans  1.Tuple is another type of sequential datatype. We can store different types of data inside it.
     2.The difference between Tuple & List is
       -List is mutable & Tuple is immutable.

Q41. How can you create a tuple in Python

Ans	# Using () brackets
	tup1 = (1, 2, 'Big', 'Data', 2.0)

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
Ans  We cannot add data after creating the Tuple as tuples are immutable.To update the tuple, the only way is to overwrite the entire tuple with required changes.

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
Ans : We can combine two tuples using + operator.

	tup1 = (1,2,3,4)
	tup2 = (5,6,7,8)
	combined_tuple = tup1 + tup2
	print(combined_tuple)

Q44. Take a tuple as an input and print the count of elements in it.

Ans:	tup1 = eval(input('Enter the tuple elements:'))
	print('Length of the tuple is:', len(tup1))

Q45. What are sets in Python?
Ans : Set is a data type in pyton which is collection of unique elements. It is not indexed.

Q46. How can you create a set?

Ans:	s1 = {1, 2, 3}
	
	
Q47. Create a set and add "iNeuron" in your set.

Ans:	s1 = {'Big', 'Data', 'Engineer'}
	s1.add('iNeuron')

Q48. Try to add multiple values using add() function.
Ans : We cannot add multiple values using add() function.

Q49. How is update() different from add()?
Ans: update() function can add multiple elements in a set if iterable items like list, tuple, string or another set is providied to it as an argument.

Q50. What is clear() in sets?
Ans: It is used to delete all elements in set & make it empty.

Q51. What is frozen set?
Ans :  Frozen set is datatype in Pyton. It is similar to set except it is immutable.

Q52. How is frozen set different from set?
Ans: Set is mutable while frozen set is immutable.

Q53. What is union() in sets? Explain via code.
Ans  union() in set is used to combine the elements of two different sets.

	s1 = {'Big', 'Data', 'Engineer'}
	s2 = {1, 2, 3}
	print(s1.union(s2))
	# Output -> {1, 2, 3, 'Data', 'Engineer', 'Big'}

Q54. What is intersection() in sets? Explain via code.
Ans: intersection() in sets is used to get only those elements which are present in both the sets.

	s1 = {'Data', 'Engineer', 'Software', 'Developer'}
	s2 = {'Software', 'Engineer', 'Data', 'Science'}
	print(s1.intersection(s2))
	# Output -> {'Data', 'Software', 'Engineer'}

Q55. What is dictionary in Python?
Ans : dictionary data type in Python is used to store data in the form of key-value pairs.

Q56. How is dictionary different from all other data structures.
Ans : dictionary stores data in key-value pair. While most of the sequential data types use indexes to access data dictionary uses keys.

Q57. How can we declare a dictionary in Python?

Ans:	# Empty dictionary
	dict1 = dict()
	dict2 = {}
	
	# Dictionary with elements
	dict3 = {'name':'Bhavesh', 'age':26, 'city':'Durg'}

Q58. What will the output of the following?
```
 var = {}
 print(type(var))
```
Ans: <class 'dict'>

Q59. How can we add an element in a dictionary?
	
Ans:	dict1 = dict()
	
	# Method 1
	dict1.update({'name':'Bhavesh'})
	
	# Method 2
	dict1['age'] = 25
	
	print(dict1)
	# Output -> {'name': 'Bhavesh', 'age': 25}

Q60. Create a dictionary and access all the values in that dictionary.
	
Ans:	dict1 = {'name':'Bhavesh', 'age':25, 'city':'Durg'}
	print(dict1.values())
	# Output -> dict_values(['Bhavesh', 23, 'Pune'])

Q61. Create a nested dictionary and access all the element in the inner dictionary.

Ans:	dict1 = {'name':'Bhavesh', 'age':25, 'city':'Durg', 'skills': {'language':'Python', 'database':'MySQL'}}
	print(dict1.get('skills'))
	# Output -> {'language':'Python', 'database':'MySQL'}

Q62. What is the use of get() function?
Ans : 1.get() function is used to get value corresponding to the key given as an argument.
      2.by using get () the output doesn't return any error.


Q63. What is the use of items() function?
Ans : items() function is used to get a list of key-value tuples of a dictionary

Q64. What is the use of pop() function?
Ans  pop() function is used to get value corresponding to the key given as an argument. It also deletes that key-value pair from dictionary.

Q65. What is the use of popitems() function?
Ans It removes the last item inserted from a dictionary.

Q66. What is the use of keys() function?
Ans keys() function is used to get all the keys from a dictionary.

Q67. What is the use of values() function?
Ans values() function is used to get all the values from a dictionary.

Q68. What are loops in Python?
Ans : Loops in Python are used to execute a block of code repeatedly until the condition is True.

Q69. How many type of loop are there in Python?
Ans : In Python there are two types of loops
       - for loop
       - while loop

Q70. What is the difference between for and while loops?
Ans : Mostly we use 'for loop' for a particular range and we use 'while loop' until a particular condition is True.

Q71. What is the use of continue statement?
Ans : continue statement is used to skip the current execution of the loop & move to the next iteration.

Q72. What is the use of break statement?
Ans : break statement is used to exit from the loop.

Q73. What is the use of pass statement?
Ans : pass statement is used to temporarily execute the program without the block of code which we have planned to develop in future.

Q74. What is the use of range() function?
Ans : range() function generates range of numbers which have been passed to it as an argument. 

Q75. How can you loop over a dictionary?
Ans : We can use items() function to loop through a dictionary.

	dict1 = {'name':'Bhavesh', 'age':25, 'city':'Durg', 'skills': {'language':'Python', 'database':'MySQL'}}
	for k,v in dict1.items():
	    print('Key:', k, 'Value:', v)

### Coding problems
Q76. Write a Python program to find the factorial of a given number.

	def fact(num):
	    result = 1
	    for n in range(2, num+1):
		result = result * n
	    return result

	input_number = int(input('Enter a number: '))
	factorial = fact(input_number)
	print('Factorial of', input_number, 'is', factorial)

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

	p = int(input('Enter principal amount: '))
	r = int(input('Enter annual interest rate: '))
	t = int(input('Enter time (in years): '))

	simple_interest = (p * r * t) / 100
	print('Simple interest:', simple_interest)

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

	p = int(input('Enter principal amount: '))
	r = int(input('Enter annual interest rate: '))
	t = int(input('Enter time (in years): '))

	compound_interest = p * (1 + r / 100) ** t
	print('Compound interest:', compound_interest)

Q79. Write a Python program to check if a number is prime or not.

	num = int(input('Enter a number: '))

	if num == 0 or num ==1:
		   print('The input number', num, 'is not a prime number')
	else:
		for n in range(2, num):
			if num % n == 0:
				print('The input number', num, 'is not a prime number')
				break
		else:
			print('The input number', num, 'is a prime number')

Q80. Write a Python program to check Armstrong Number.

	num = input('Enter a number: ')
	result = 0

	for n in num:
		result += int(n) ** 3

	if int(num) == result:
		print(num, 'is a Armstrong number')
	else:
		print(num, 'is not a Armstrong number')

Q81. Write a Python program to find the n-th Fibonacci Number.

	num = int(input('Enter a number: '))
	fibonacci = [0, 1]

	if num == 0:
	    print('The nth Fibonacci numbre is 0')
	elif num == 1:
	    print('The nth Fibonacci numbre is 1')
	else:
	    for n in range(2, num + 1):
		result = fibonacci[-1] + fibonacci[-2]
		fibonacci.append(result)
	    print('The nth Fibonacci numbre is', fibonacci[-1])

Q82. Write a Python program to interchange the first and last element in a list.

	lst = [1, 2, 3, 4, 5]
	lst[0], lst[-1] = lst[-1], lst[0]
	print(lst)
	# Output -> [5, 2, 3, 4, 1]

Q83. Write a Python program to swap two elements in a list.

	lst = [1, 2, 3, 4, 5]
	i1 = int(input('Enter 1st index to swap: '))
	i2 = int(input('Enter 2nd index to swap: '))
	lst[i1], lst[i2] = lst[i2], lst[i1]
	print(lst)

Q84. Write a Python program to find N largest element from a list.

	lst = [3, 5, 1, 2, 4]
	n = int(input('Enter the no. of largest numbers required: '))
	lst.sort(reverse=True)
	print(lst[0:n])

Q85. Write a Python program to find cumulative sum of a list.

	lst = [3, 5, 1, 2, 4]
	cumulative_sum = 0
	for i in range(len(lst)):
	    cumulative_sum += lst[i]
	    lst[i] = cumulative_sum

	print(lst)
	# Output -> [3, 8, 9, 11, 15]

Q86. Write a Python program to check if a string is palindrome or not.

	s = input('Enter a string: ')
	reverse_s = s[ : : -1]

	if s.upper() == reverse_s.upper():
	    print('The string is palindrome ')
	else:
	    print('The string is not palindrome ')

Q87. Write a Python program to remove i'th element from a string.

	s = input('Enter a string: ')
	i = int(input('Enter index of element to be removed: '))
	s = s[:i] + s[i+1:]
	print(s)

Q88. Write a Python program to check if a substring is present in a given string.

	s = input('Enter a string: ')
	substr = input('Enter sub string: ')
	if s.find(substr) == -1:
	    print('Substring not present')
	else:
	    print('Substring is present')

Q89. Write a Python program to find words which are greater than given length k.

	s = input('Enter a string: ')
	k = int(input('Enter desired length: '))

	lst = s.split()
	for word in lst:
	    if len(word) > k:
		print(word)

Q90. Write a Python program to extract unquire dictionary values.

	test_dict = {'my': [1, 8, 9, 6], 'big': [10, 11, 9, 1], 'data': [6, 12, 10, 6], 'dict': [5, 2, 1]}
	result = []
	for v in test_dict.values():
	    result += v
	print(list(set(result)))

Q91. Write a Python program to merge two dictionary.

	dict1 = {'a':1, 'b':2, 'c':3}
	dict2 = {'d':4, 'e':5, 'f':6}

	dict1.update(dict2)
	print(dict1)
	# Output -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```

Ans:	list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
	my_dict = dict(list)
	print(my_dict)
	# Output -> {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```

	lst = [9, 5, 6]
	result = []
	for num in lst:
		result.append((num, num**3))

	print(result)
	# Output -> [(9, 729), (5, 125), (6, 216)]

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```

	test_tuple1 = (7, 2)
	test_tuple2 = (7, 8)

	result = []
	for i in test_tuple1:
		for j in test_tuple2:
			result.append((i, j))        
			result.append((j, i))        

	print(result)
	# Output -> [(7, 7), (7, 7), (7, 8), (8, 7), (2, 7), (7, 2), (2, 8), (8, 2)]

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```

	lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)]

	def second_item(tup):
		return tup[1]

	lst.sort(key=second_item)
	print(lst)
	# Output -> [('Geeks', 8), ('for', 24), ('Geeks', 30)]

Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
	n = 5
	for i in range(1, n+1):
		print('* ' * i)
	
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

	n = 5
	for i in range(1, n+1):
		print(' ' * (n-i), '*' * i)

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

	n = 5
	for i in range(1, n+1):
		print(' ' * (n-i), '* ' * i)

Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

	n = 5
	for i in range(1, n+1):
		for j in range(1, i+1):
			print(j, end=' ')
		print()

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
```

	import string
	alpha = list(string.ascii_uppercase)
	n = 5
	for i in range(1, n+1):
		print((alpha[i-1] + ' ') * i)
		