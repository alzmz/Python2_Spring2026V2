# review python chapters 3 - 8]

average = float(input('Enter average:')) 
while average < 0 or average > 100:
    if average == -999:
        print ('Exit the program')
        break
    else:
        average = float(input('Enter average (0-100):'))
if average != -999:
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        print(f'average - {average:.2f}\tfinal grade = {letter_grade}')

 # just learnt the difference between ising if and elif in this code, elif is relational, if is a stand alone, edit and run to see.
# need to research later - f" Average {average:<10.2f}
#conditional if 
hours = 55
hourly_rate =  20.50
pay = (hours - 40) * 1.5 * hourly_rate + 40 * hourly_rate if hours > 40 else hours * hourly_rate
print(f'\nPay = {pay:.1f}')

#random number 
import random 
#from random import randint, random, randrange
random.seed(12345)
rand_num = random.randint(1,100)
rand_num1 = random.randrange(1,100)
print (F'\nRandom number generated:{rand_num}')
#generate random character
ch = chr(random.randint(ord('A'),ord('Z')))
print(f'Random charater is:{ch}')
#str functions
num = input('Enter a number:')
while not num.isdigit(): #num.isalpha():
    print('Enter a number only')
    num = input('Enter a number:')
print(f'The number entered:{num}')
#check for vowel
sentence = input('Enter a sentence:')
vowels = 'aeiou'
count = 0 
for ch in sentence.lower():
    if ch in vowels:
        count += 1
print(f'Total vowels:{count}')
vowelless = [ch for ch in sentence.lower() if ch not in vowels]
print(f'The sentence without vowels:{vowelless}\n')
vowelless_Str = ''.join(vowelless)
print(vowelless_Str)
#global variable
glb_num = 10 
print(f'id:{id(glb_num)},value:{glb_num}')
def modify_global():
    """ modify global variable """
    global glb_num
    local = glb_num + 10
    print(f'id:{id(glb_num)},value:{glb_num}, local:{local}')
modify_global()
#unpacking
def  make_sandwich(*ingredients):
    """ make sandwich unpacking the ingreients"""
    for ingredients in ingredients:
        print(f'Addding {ingredients} to the sandwich')
    print(f'your sandwich is ready!')
make_sandwich('ham','cheese','lettuce','tomato')
#prime number
def is_prime(num):
    """ check of the num passed in is a prime number """
    if num <= 1:
        return False
    for i in range(2,num // 2 + 1):
        if num % 2 == 0:
            return False
    return True
number = int(input('Enter a number:'))
if is_prime(number):
    print(f'{number} is a prime')
else:
    print(f'{number}is not a prime') 
#check palindrome
def is_palindrome(s):
    """ check if the string s is palindrome """
    return s==[::-1]
word = input('Enter a word:')
if is_palindrome(word):
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome')






















#list
numbers = [10,50,20,40,30]
print(f'umbers:{numbers}')
print(f'Sum of numbers:{sum(numbers)}')
print(f'Max value of numbers:{max(numbers)}')
print(f'Min value of numbers:{min(numbers)}')
print(f'Index of max value of numbers:{numbers.index(max(numbers))}')
print(f'Index value of min numbers:{numbers.index(min(numbers))}')
print(f'Reversed numbers:{numbers[::-1]}')
ordered_numbers = sorted(numbers)
print(f'Order list: {ordered_numbers}')
# matrix - two-dimensional list
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
matrix_sum = 0 
for row in matrix:
    for col in row:
        matrix_sum += col
print(f'The matrix sum:{matrix_sum}')

#row sums
row_sums = [sum(row) for row in matrix]
print(f'row sums:{row_sums}')

# column sum
col_sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
print(f'col sums: {col_sums}')

#flatten the matrix
flattened = [col for row in matrix for col in row]
print(f'Flattened matrix:{flattened}')

# write a function for row sum and col sum she said sm about using a loop for it - take home assignment 