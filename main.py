import sys
import os
import time

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.text import Text

def loading_animation(console, message_style="Loading", delay_char=0.12, delay_dot=0.6, num_dots=3):
    styled_message_text = Text.from_markup(message_style, style=None)

    for char_segment in styled_message_text:
        console.print(char_segment, end="")
        console.file.flush()
        time.sleep(delay_char)

    for _ in range(num_dots):
        console.print(".", end="")
        console.file.flush()
        time.sleep(delay_dot)

    console.print()

def clean_screen():
    time.sleep(1)
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clean_screen()

console = Console()
ascii_logo = r"""
   _____                         _____ _          _ _   
  |  __ \                       / ____| |        | | |  
  | |__) |___  ___ ___  _ __   | (___ | |__   ___| | |  
  |  _  // _ \/ __/ _ \| '_ \   \___ \| '_ \ / _ \ | |  
  | | \ \  __/ (_| (_) | | | |  ____) | | | |  __/ | |  
  |_|  \_\___|\___\___/|_| |_| |_____/|_| |_|\___|_|_|  

           >@+                                 )@(    
          #+*++*+^*^^^^+~==----~=<<)))))((((((]]((>   
       %@@[)<(<()((<(<))))<*+*^<))(((((<()(()((]]]>   
        ({)(((]([((((]]]][@@[[[[[[}}}][}{%%#{#}[]]-   
      -(@%#@@##(@%%@@%)<<<%#}#@@@((((((((((((}((]]    
     .>]%@@@@@@@@@@@@[<<<[[(]]]((][+                  
          )@@@@@@@@@@))  [@(     )                    
          *@@@@@@@@@@@^   *@     +                    
          @@@@@@@@@@()[*        (*                    
         #@@@@@@@@@>-                                 
        }@@@@]>@@@}<                                  
       ]@@@@@+=}@@(>                                  
       @@@@@@@@@@#]                                   
      =@@@@@@@@@@(+                                   
      +@@@@%]@@@})                                    
      ^@@@@@@@@@{]-                                   
"""

logo_panel = Panel(ascii_logo, title="ReconShell", subtitle="by Luk", style="cyan1")
console.print(Align.left(logo_panel))
loading_animation(console, message_style="[red1]Loading[/red1]", delay_char=0.08, delay_dot=0.15)

panel_width = 30
menu = """
[1] Domain Search
[0] Sair
"""

menu_panel = Panel(menu, subtitle="Menu", style="dark_slate_gray2", width=panel_width)
clean_screen()
console.print(Align.left(menu_panel))

time.sleep(3)
choice = Prompt.ask("[dark_slate_gray2]Selecione uma opção[/]", choices=["1", "0"])

if choice == "1":
	clean_screen()
	url = Prompt.ask("[dark_slate_gray2]URL: [/]")
	console.print("[dark_slate_gray2]\nIniciando Domain Search...[/]")
elif choice == "0":
	console.print("[dark_slate_gray2]\tSaindo...[/]")
