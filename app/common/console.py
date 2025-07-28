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
from enum import Enum
# Librerías internas:

# Librerías externas:


# ---- ENUMS ---- #
class MSG_TYPE(Enum):
    # Message types.
    NORMAL  = 0,
    ERROR   = 1,
    INFO    = 2,
    CORRECT = 3


# ---- PARAMS ---- #
__prompt__:str  = "ani-cli"

# Text colors:
__red__:str     = '\033[31m'
__green__:str   = '\033[32m'
__blue__:str    = '\033[34m'
__reset__:str   = '\033[0m'


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

def print_message(msg:str, type:MSG_TYPE=MSG_TYPE.NORMAL) -> None:
    """
    Prints program message.

    Args:
        msg (str): Program message.
        type (MSG_TYPE): Message type.
    """
    # Generates the message tag.
    tag:str = "Normal"
    # Sets the tag by the message type.
    match (type):
        case MSG_TYPE.ERROR:
            tag = f"{__red__}ERROR{__reset__}"
        case MSG_TYPE.INFO:
            tag = f"{__blue__}INFO{__reset__}"
        case MSG_TYPE.CORRECT:
            tag = f"{__green__}OK{__reset__}"

    # Prints the message.
    print(f"[{tag}] -> {msg}")

def get_input() -> str:
    """
    Prints terminal prompt and returns the input.
    """
    # Print the prompt and gets the input.
    user_input:str = input(f"{__prompt__}: ")
    
    # Returns the user input.
    return user_input