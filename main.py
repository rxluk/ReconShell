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

panel = Panel(ascii_logo, title="ReconShell", subtitle="by Luk", style="bold green")

console.print(Align.center(panel))

menu = """
[1] Domain Search
[0] Sair
"""
console.print(Align.center(Panel(menu, title="Menu", style="bold cyan")))

choice = Prompt.ask("[bold yellow]Selecione uma opção[/]", choices=["1", "0"])

if choice == "1":
	console.print("[bold green] Iniciando Domain Search...[/]")
elif choice == "0":
	console.print("[bold red]Saindo...[/]")
