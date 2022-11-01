from base64 import b85encode
from colorama import Fore, init; init()
import os
from sys import argv
import random

seed=random.randint(-9**9, -1)

try: name=argv[1]
except:
	clear=lambda: os.system('cls && title Python Obfuscator by LALOL' if os.name == 'nt' else 'clear')
	clear()
	print(f'{Fore.CYAN}Enter file for obfuscation: {Fore.YELLOW}', end='', flush=True)
	name=input()
	clear()
try: f=open(name, 'r', encoding='utf-8')
except:
	print(Fore.RED+'File was not found!')
	exit()
numbers=[]
for i in f.read():
	numbers.append(ord(i)+seed)
numbers_string='['
for i in numbers:
	numbers_string+=f'{i},'
numbers_string+=']'
useless1=''
useless2=''
for i in range(5):
	useless1+=f'a={numbers_string};'
	useless2+=f'b={numbers_string};'
script=f'''{useless1}exec("a=''\\nfor i in {numbers_string}:a+=chr(i-{seed});{useless2}\\n{useless2}eval(compile(a, '', 'exec'))");{useless1}'''
code=b85encode(script.encode()).decode()
file=open(f'{name.replace(".py", "")}_Obfuscated.py', 'w', encoding='utf-8')
file.write(f'''# https://github.com/Its-LALOL/Python-Obfuscator\nexec(__import__('base64').b85decode('{code}'))''')
file.close()
print(f'{Fore.GREEN}Successfully obfuscated in {Fore.CYAN}{name.replace(".py", "")}_Obusfacted.py{Fore.CYAN}{Fore.GREEN}!')