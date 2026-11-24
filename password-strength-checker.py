import string
from colorama import Fore,Style,init 

init(autoreset=True)

#Load comman password dataset
def load_common_passwords(file_path):
  try:
    with open(file_path,"r", encoding="utf-8",errors="ignore") as f:
      return set(line.strip() for line in f)
  except FileNotFoundError:
    print(colorama.Fore.Red +"[!] Passwoed dataset file not found")
    exit()
common_passwords=load_common_passwords("rockyou.txt")

password = input(Fore.CYAN +"Enter your passwords:")
print("/n" + Fore.YELLOW + "Passwords Analysis")
print("-"*30)

#chech common password list
if password in common_passwords:
  print(Fore.RED +"[!] This password exits in a common password dataset! ")
  print(Fore.RED +"Estimated Time to crack: Instantly!!")
  exit()

score=0
charset_size=0

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

#length check
if len(password) >=8:
  score+=1
  print(Fore.GREEN +"[+] Good password length ")
if any(c.islower for c in password):
  charset_size +=len(lowercase)

if any(c.isupper for c in password):
  score+= 1
  charset_size +=len(uppercase)
  print(Fore.GREEN +"[+] Contains Uppercase Characters")


if any(c.isdigit() for c in password):
  score+=1
  charset_size +=len(digits)
  print(Fore.GREEN +"[+] Contains numbers")

if any(c in symbols for c in password):
  score+=1
  charset_size +=len(symbols)
  print(Fore.GREEN +"[+] Contains special characters")

if charset_size==0:
  charset_size = 26

#calculate combinations
combinations = charset_size **len(password)

#Assume attacker guesses per second
guesses_per_second = 1_000_000_000

second = combinations / guesses_per_second

def convert_time(seconds):
  minutes = seconds/60
  hours = minutes/60
  days = hours/24
  years = days/365

  if seconds < 60:
    return f"{seconds: 2f}seconds"
  elif minutes < 60:
      return f"{seconds: 2f}minutes"
  elif hours < 24:
    return f"{seconds: 2f}hours"
  elif days < 365:
    return f"{seconds: 2f}days"
  else:
    return f"{years: 2f}years"

print("\n" + Fore.YELLOW + "Strength Result")
print("-"*30)
if score <=1:
  print(Fore.RED +"Weak Password")
elif score == 2:
  print(Fore.YELLOW + "Medium Password")
elif score == 3:
  print(Fore.BLUE + "Strong Password")
else:
  print(Fore.GREEN + "Very Strong Password" )

print(Fore.MAGENTA + f"/n Estimated time to crack: {convert_time(second)}")
