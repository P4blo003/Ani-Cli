# -*- coding: utf-8 -*-


"""
*******************************************************************************************
    Sript name: console.py
    Project: Ani-Cli
    Author: Pablo González García
    Date: 2025-07-28
    Description: Contains utility functions for printing formatted messages and data to
        the console. Provides custom print functions for various output styles. 
    Copyright (c) 2025 Pablo González García
    Licencia: MIT License. See the LICENCE file in the project root.
*******************************************************************************************
"""


# ---- MODULO ---- #
# Librerías estándar:
import shutil
# Librerías internas:

# Librerías externas:


# ---- PARAMS ---- #
__prompt__:str = "ani-cli"


# ---- FUNCTIONS ---- #
def print_header(splitter:str, title:str) -> None:
    """
    Prints program header into the console terminal.

    Args:
        splitter (str): Splitter for the header.
        title (str): Title for the header.
    """
    # Gets terminal sizes.
    cols:int = shutil.get_terminal_size().columns
    spacing:int = (cols - len(title)) // 2

    # Print the header.
    print(f"\n{splitter*cols}")
    print(f"{" "*spacing}{title}")
    print(f"{splitter*cols}\n")

def get_input() -> str:
    """
    Prints terminal prompt and returns the input.
    """
    # Print the prompt and gets the input.
    user_input:str = input(f"{__prompt__}: ")
    
    # Returns the user input.
    return user_input