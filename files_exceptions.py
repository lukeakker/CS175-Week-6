# -*- coding: utf-8 -*-
"""files_exceptions

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O9TbE_M5oye9BkTA81rbg7X_AlYZqrLM
"""

##In class excercise
def main():

  coffee_file = open('coffee.txt', 'w')

  coffee_file.write("Hello\n")
  coffee_file.write("Hello\n")
  coffee_file.write("Hello\n")

  coffee_file.close()



if __name__ == '__main__':
  main()

#Lucas Vandenakker
#CS 175
#Files and Exceptions

number_file1 = open('numbers.txt', 'w')

number_file1.write("74\n")
number_file1.write("63\n")
number_file1.write("82\n")

number_file1.close()

number_file = open('numbers.txt', 'r')
nums = []
sum = 0

for i in number_file:

    temp = int(i)
    nums.append(temp)
    sum += temp

number_file.close()

print("The list of nums are:", nums)
print("The total is:", sum)

#Lucas Vandenakker
#CS 175
#Average From Input File

def main():

  mainfile = 'numbers.txt'

  listOfNums = openFile(mainfile)

  average = avgNums(listOfNums)

  printing(average)

def openFile(file):

  try:
    newFile = open(file, 'r')

    try:
      numbers = getInput(newFile)

    except ValueError:
      print("ValueError: Could not convert line to int")

  except IOError:
    print("IOError: Could not read file")

  return numbers




def getInput(tempFile):

  nums =[]

  for i in tempFile:
    nums.append(int(i))


  return nums

def avgNums(tempList):

  tempAvg = 0

  for x in tempList:

    tempAvg+=x

  return tempAvg / len(tempList)

def printing(averageTemp):
  print("The average of your numbers is: ", averageTemp)




if __name__ == '__main__':
  main()

#Lucas Vandenakker
#CS-175
#Try-Catch
search_term = "sam"

try:
  with open('numbers.txt', 'r') as file:
    content = file.read()

    if search_term not in content:
        raise Exception(f"'{search_term}' was not found in the file.")

except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")

except IsADirectoryError:
    print(f"Error: The path '{file}' is a directory, not a file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")