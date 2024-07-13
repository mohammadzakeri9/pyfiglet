import pyfiglet
from termcolor2 import colored

valid_colors = ("red", "green", "blue", "cyan", "yellow", "magenta","black","white")

def print_art(color, message):
   if color not in valid_colors:
    message2 = ("color not exsit in valid !")
    print(message2)
    color = "white"
     
   ascii_art = pyfiglet.figlet_format(message)
   ascii_art = colored(ascii_art, color=color)
   print(ascii_art)


message = input("what would you like to print ? : ")
color = input("what color ? : ")

print_art(color,message)
