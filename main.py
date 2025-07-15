from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt

console = Console()

ascii_logo = """
   _____                         _____ _          _ _ 
  |  __ \                       / ____| |        | | |
  | |__) |___  ___ ___  _ __   | (___ | |__   ___| | |
  |  _  // _ \/ __/ _ \| '_ \   \___ \| '_ \ / _ \ | |
  | | \ \  __/ (_| (_) | | | |  ____) | | | |  __/ | |
  |_|  \_\___|\___\___/|_| |_| |_____/|_| |_|\___|_|_|
"""

logo_panel = Panel(ascii_logo, title="ReconShell", subtitle="by Luk", style="green")
console.print(Align.center(logo_panel))

panel_width = 60

menu = """
[1] Domain Search
[0] Sair
"""

menu_panel = Panel(menu, subtitle="Menu", style="green", width=panel_width)
console.print(Align.center(menu_panel))

choice = Prompt.ask("[green]Selecione uma opção[/]", choices=["1", "0"])

if choice == "1":
	console.print("[yellow]\tIniciando Domain Search...[/]")
elif choice == "0":
	console.print("[yellow]\tSaindo...[/]")
