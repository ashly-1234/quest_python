# Program to accept number of lines of the Triangle and draw the inverted Trianlge:
# * * * *
#   * * *
#     * *
#       *

number_of_lines = int(input('Enter number of lines of the Triangle: '))


for i in range (number_of_lines, 0, -1):
    print((number_of_lines-i) * ' ' + i * '*')    