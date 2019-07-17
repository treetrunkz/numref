
multi3_list=[]
count = 0

while count < 4:
  user_num = int(input('Enter a number that is divisible by three: '))
  if user_num % 3 == 0:
    multi3_list.append(user_num)
    count += 1
  else:
    print('This input is erroneous!')
print('Congrats! you have done it!')
print(multi3_list)


enclist=[]
word = input('Enter the word you want to encrypt now.')
enclist.append(word)


def encrypt(word):
  return word[1:]+word[0]

text = input('enter a word: ')
print(text,"encrypted is",encrypt(text))


def encrypt(text):
    return text[1:]+text[0]

word = input("Enter a word:")
print(word,"encrypted is",encrypt(word))



'''
file_in = open('elevations.csv')
contents = file_in.readlines()
file_in.close()

#delete first line + column headers
del context[0]
print('The number of locations in the file is,',len(contents))

print(contents)

scount=0
max_height=-1000
for item in countents:
  parts = item.strip().split(',')
  location = parts[0]
  height = parts[2]
  if location[0] == 'S':
    scount+=1
  if height > max_height:
    max_height = height
'''
