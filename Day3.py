# arr = [12,56,78,34,45,67,89]
# arr.sort(reverse=True)
# arr.sort()
# print(arr)
# print(min(arr))
# print(max(arr))
# print(sum(arr))

# msg = 'I love Python.'
# lst = msg.split()
# lst.reverse()
# s = str(lst)
# print(s)
# print(type(s))
# print(s[1])
# s = ' '.join(lst)
# print(s)

# st = input('Enter the string: ')
# s = st.split()
# print(len(s))

# s = 'abc123'
# print(s.isdigit())
# print(s.isalpha())
# print(s.isalnum())

# num = int(input('Enter the number: '))
# if num % 2 != 0:
#       print('number is odd')
#       print('Done')
      
# else:
#       print('number is even')
      
# print('Khatam Tata Bye Bye')



# n = int(input('Enter the number: '))

# if n>10:
#       print('greater than 10')
# elif n == 10:
#       print('equal to 10')
# else:
#       print('less than 10')



# col = input('Enter the Color: ')
# s = col.upper()
# if s == 'RED':
#       print('Stop')
# elif s == 'YELLOW':
#       print('Wait')
# elif s == 'Green':
#       print('Go')
# else:
#       print('Invalid Color')


# vowels = 'aeiou' #['a','e','i','o','u']
# char = input('Enter the character: ')
# print(char in vowels)

# digit = '1234567890'
# num = input('Enter the number: ')
# print(num in digit)

vowels = 'aeiou'
char = input('Enter the character: ')
if char in vowels:
      print('Vowel')
else:
     print('Consonant')


special = '!@#$%^&*()'
char = input('Enter the character: ')
print(char in special)#

alnum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
char = input('Enter the character: ')
print(char in alnum)


