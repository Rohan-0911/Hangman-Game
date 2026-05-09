#  Project Title: HANGMAN GAME
#  Created By: CSE(AIML)-E Group No.3
#  Description: A Hangman game for terminal.

import random
import time
import colorama
from rich import print
from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich import box

# Reseting colors
colorama.init(autoreset=True)

# Console Configuration
console = Console()

#ASCII Art

TITLE_ART = """
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

GAME_OVER_ART = """
  ____                         ___                 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
"""

VICTORY_ART = """
 __      __ _      _                     _ 
 \ \    / /(_)    | |                   | |
  \ \  / /  _  ___| |_ ___  _ __ _   _  | |
   \ \/ /  | |/ __| __/ _ \| '__| | | | | |
    \  /   | | (__| || (_) | |  | |_| | |_|
     \/    |_|\___|\__\___/|_|   \__, | (_)
                                  __/ |    
                                 |___/     
"""

# Word List

words = [
    # Simple Words
    "shirt", "table", "mango", "house", "water",
    "apple", "bread", "chair", "plant", "music",
    "phone", "watch", "shoes", "bottle", "glass",
    "train", "plane", "truck", "cycle", "motor",
    # Nature
    "river", "ocean", "cloud", "storm", "grass",
    "trees", "flower", "beach", "stone", "light"
]

# Rules List
rules_list = [
    "1. You need to guess a five letter word.",
    "2. You need to guess a single letter at a time.",
    "3. You have 6 lives total.",
    "4. You will lose 1 live for 1 incorrect guess.",
    "5. Special characters and numbers are not allowed.",
    "6. Have fun and try to beat your high score!",
    "7. ALL THE BEST!"
]

# Valid input characters
valid_input = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]

# Functions

def print_separator_full():
    """
    Prints a full screen visual separator line.
    """
    print("\n" + "="*163 + "\n")

def print_separator_short():
    """
    Prints a short visual separator line.
    """
    print("\n" + "="*60 + "\n")

def type_effect(text, color="white"):
    """
    Prints one character at a time.
    """
    style = f"bold {color}"
    for char in text:
        console.print(char, end="", style=style)
        time.sleep(0.05) # Speed
    print()

def show_loading_bar():
    """
    Shows a loading bar.
    """
    console.print("[yellow]Initializing Game Engine...[/]")
    time.sleep(0.5)
    with console.status("[bold green]Loading Assets...[/]"):
        time.sleep(1.5)
    console.print("[bold green]Ready![/]\n")
    time.sleep(0.5)

def show_rules():
    """
    Displays the rules.
    """

    # Create table
    table = Table(title="OFFICIAL GAME RULES", box=box.ROUNDED, style="yellow")
    
    # Add columns
    table.add_column("Rule No.", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")

    # Add rows
    for index, rule in enumerate(rules_list):
        table.add_row(str(index+1), rule)
    
    # Print table
    console.print(table)

    console.input("\n[bold green]Press Enter to Start Game...[/]")

    print_separator_full()

def display_secret_word(display):
    """
    Display the characters guessed by player.
    """
    console = Console(height=5)

    layout = Layout()

    layout.split_column(
        Layout(name="display", size=5)
    )

    layout["display"].update(
        Panel.fit(f"\n[bold cyan]  {" ".join(display)}  ", title="Secret Word", border_style="cyan", box=box.HEAVY)
    )

    layout.size = 5

    console.print(layout)

# Main Game

def start():
    """
    The main game logic.
    """
    
    #Get a random word
    random_num = random.randrange(0, len(words))
    
    random_word = words[random_num]
    
    # List to store attempts
    attempts = []
    wrong_attempts = [] 
    
    # Create the display
    display = ["_"] * len(random_word)
    
    # Set lives
    tot_lives = 6
        
    #Header
    console.print(Panel(Align.center("\n[bold magenta]ULTIMATE HANGMAN[/]\n"), style="magenta", box = box.HEAVY))

    display_secret_word(display)
            
    lives_display = "❤️ " * tot_lives + "💀 " * (6 - tot_lives)
    print(f"\nLives: {lives_display}")

    print_separator_short()

    # Main game loop

    while tot_lives > 0:

        # Take input from player
        letter = console.input("[bold yellow]Guess a letter: [/]").lower()
        
        # Valid input check
        if letter not in valid_input:
            console.print("[bold red]Invalid Input! Please enter a single letter (a-z).[/]\n")
            console.input("[italic]Press Enter to retry...[/]")

            print_separator_short()

        # Previously guessed or not check
        elif letter in attempts:
            console.print(f"[bold orange3]You already guessed '{letter.upper()}'. Try another one.[/]\n")

            display_secret_word(display)
            
            lives_display = "❤️ " * tot_lives + "💀 " * (6 - tot_lives)
            print(f"\nLives: {lives_display}")
        
            print(f"Wrong Guesses: {', '.join(wrong_attempts)}")
        
            console.input("\n[italic]Press Enter to retry...[/]")

            print_separator_short()

        # Wrong guessed previously or not check
        elif letter.upper() in wrong_attempts:
            console.print(f"[bold orange3]You already tried '{letter.upper()}'![/]\n")

            display_secret_word(display)
            
            lives_display = "❤️ " * tot_lives + "💀 " * (6 - tot_lives)
            print(f"\nLives: {lives_display}")
        
            print(f"Wrong Guesses: {', '.join(wrong_attempts)}")
        
            console.input("\n[italic]Press Enter to retry...[/]")

            print_separator_short()

        # Is guess correct check
        elif letter in random_word:
                        
            # Loop to find position and occurence of guessed letter in random word
            initial_pos = 0
            found_count = 0
            
            for char in random_word:
                if char == letter:
                    display[initial_pos] = letter.upper()
                    attempts.append(letter)
                    found_count += 1
                initial_pos += 1

            console.print("[bold green]Congratulations you guessed it right!🎉🎉")
            console.print(f"[lightgreen]{letter.upper()} is present in word\n")

            display_secret_word(display)

            lives_display = "❤️ " * tot_lives + "💀 " * (6 - tot_lives)
            print(f"\nLives: {lives_display}")
        
            print(f"Wrong Guesses: {', '.join(wrong_attempts)}")

            print_separator_short()
            
            # Check Win Condition
            if "_" not in display:
                print_separator_full()
                
                # Show Victory ASCII Art
                console.print(Panel(Align.center(f"[bold green]{VICTORY_ART}[/]"), style="green"))
                
                console.print(Panel(Align.center(f"\n\nThe word was: [bold white]{random_word.upper()}[/]"), style="green"))
                console.input("\n[bold green]Press Enter to return to menu...[/]")
                break

        else:
            # Wrong Guess
            console.print(f"[bold red]Missed it! '{letter.upper()}' is not in the word.[/]\n")
            
            # Reduce lives
            tot_lives -= 1

            # Wrong Attempts
            wrong_attempts.append(letter.upper())

            display_secret_word(display)

            lives_display = "❤️ " * tot_lives + "💀 " * (6 - tot_lives)
            print(f"\nLives: {lives_display}")
        
            print(f"Wrong Guesses: {', '.join(wrong_attempts)}")

            if tot_lives==0:
                pass
            
            else:
                console.input("\n[italic]Press Enter to continue...[/]")
                print_separator_short()

    # Loss Condition Check
    if tot_lives == 0:
        print_separator_full()
        
        # Show Game Over ASCII Art
        console.print(Panel(Align.center(f"[bold red]{GAME_OVER_ART}[/]"), style="red"))
        
        console.print(Panel(Align.center(f"\n\nThe word was: [bold white]{random_word.upper()}[/]"), style="red"))
        console.input("\n[bold red]Press Enter to return to menu...[/]")

# Game Start

while True:
    # No more clearing here! Just a nice separator.
    print_separator_full()
        
    # Print the massive ASCII Title
    console.print(Panel(Align.center(f"[bold cyan]{TITLE_ART}[/]"), style="cyan"))
        
    console.print(Panel(Align.center("[bold yellow]Welcome to Hangman[/]"), style="yellow"))
        
    # Menu Options
    console.print("\n[1] View Rules & Start Game")
    console.print("[2] Start Game")
    console.print("[3] Exit")
        
    choice = console.input("\n[bold cyan]Select Option: [/]")
    
    print_separator_full()

    if choice == "1":
        show_rules()
        show_loading_bar()
        start()
            
    elif choice == "2":
        show_loading_bar()
        start()
            
    elif choice == "3":
        console.print("\n[bold green]Thanks for playing! Goodbye![/]")
        break
            
    else:
        console.print("\n[bold red]Invalid Selection![/]")
        time.sleep(1)