import sys, os, time, subprocess
import questionary

from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich.text import Text
from rich.table import Table

## Global Variables

ascii_logo = r"""
   _____                         _____ _          _ _   
  |  __ \                       / ____| |        | | |  
  | |__) |___  ___ ___  _ __   | (___ | |__   ___| | |  
  |  _  // _ \/ __/ _ \| '_ \   \___ \| '_ \ / _ \ | |  
  | | \ \  __/ (_| (_) | | | |  ____) | | | |  __/ | |  
  |_|  \_\___|\___\___/|_| |_| |_____/|_| |_|\___|_|_|  
"""
CONSOLE = Console()
MENU_LOGO = Panel(ascii_logo, title="ReconShell", subtitle="by Luk", style="red1")
BASE_DIR = Path(__file__).parent
DOMAIN_SCRIPT = BASE_DIR / "scripts" / "domain_search.sh"

## Utils

def loading_animation(CONSOLE, message_style="Loading", delay_char=0.12, delay_dot=0.6, num_dots=3):
    styled_message_text = Text.from_markup(message_style, style=None)

    for char_segment in styled_message_text:
        CONSOLE.print(char_segment, end="")
        CONSOLE.file.flush()
        time.sleep(delay_char)

    for _ in range(num_dots):
        CONSOLE.print(".", end="")
        CONSOLE.file.flush()
        time.sleep(delay_dot)

    CONSOLE.print()

def clean_screen():
	if(os.name == "nt"):
        	os.system("cls")
	else:
        	os.system("clear")

	CONSOLE.print(Align.left(MENU_LOGO))


## Options Methods

def run_domain_search(url: str):
	cmd = ["/bin/bash", str(DOMAIN_SCRIPT), url]
	proc = subprocess.run(cmd, capture_output=True, text=True)

	if(proc.returncode != 0):
		err = proc.stderr.strip() or f"Código de retorno: {proc.returncode}."
		return [], err

	rows = []
	for line in proc.stdout.splitlines():
		line = line.strip()
		if not line:
			continue

		parts = line.split("\t", 1)

		if len(parts) != 2:
			parts = line.split(None, 1)

			if len(parts) != 2:
				continue

		ip, domain = parts[0].strip(), parts[1].strip()
		rows.append((ip, domain))

	return rows, None

def show_domain_results(url:str, rows):
	clean_screen()
	table = Table(title=f"Domains in {url}", show_lines=False)
	table.add_column("IP", style="red1")
	table.add_column("Domain", style ="cyan1")

	for ip, domain in rows:
		table.add_row(ip, domain)
	CONSOLE.print(table)

## Application

clean_screen()
loading_animation(CONSOLE, message_style="[red1]Loading[/red1]", delay_char=0.08, delay_dot=0.15)
time.sleep(1)
clean_screen()

choice = questionary.select(
	"Select a option:",
	choices=[
		"Domain Search",
		"Exit"
	]
).ask()


if choice == "Domain Search":
	clean_screen()
	url = Prompt.ask("[dark_slate_gray2]URL[/]")
	clean_screen()

	CONSOLE.print("[dark_slate_gray2]\nRunning Domain Search...[/]")

	rows, err = run_domain_search(url)

	if err:
		CONSOLE.print(f"[red1]Error:[/] {err}")

	elif not rows:
		CONSOLE.print("[yellow]No domain searched.[/]")

	else:
		show_domain_results(url, rows)

elif choice == "Exit":
	CONSOLE.print("[dark_slate_gray2]\tSaindo...[/]")
