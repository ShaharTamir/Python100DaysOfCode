'''
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. 
When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines
to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
This is to try and simulate the coordinates on a real map.

Your job is to write a program that allows you to mark a square
on the map using a two-digit system. 
The first digit is the vertical column number and the 
second digit is the horizontal row number.
'''

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

map[int(position[1]) - 1][int(position[0]) - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")