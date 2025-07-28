#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
*******************************************************************************************
    Sript name: main.py
    Project: Ani-Cli
    Author: Pablo González García
    Date: 2025-07-28
    Description: Main entry point for Ani-Cli project. Handles the core functionality,
        for searching listing episodes, and downloading anime content from various
        sources.
    Copyright (c) 2025 Pablo González García
    Licencia: MIT License. See the LICENCE file in the project root.
*******************************************************************************************
"""


# ---- MODULO ---- #
# Librerías estándar:

# Librerías internas:

# Librerías externas:
from common import console
from common import web


# ---- MAIN ---- #
if __name__ == "__main__":
    
    # Try-Except to manage exceptions.
    try:

        # Print program header.
        console.print_header(splitter='=', title='Ani-Cli')

        # Infinit loop for user inputs.
        while (True):
            # Gets the user input.
            user_input:str = console.get_input()
    
    # If Ctrl+C detected.
    except KeyboardInterrupt:
        # Print line jump.
        print()
        # Prints information.
        console.print_message(msg="Ctrl+C detected. Finishing program ...", type=console.MSG_TYPE.INFO)

    # If error detected.
    except Exception as e:
        # Print line jump.
        print()
        # Prints information.
        console.print_message(msg=str(e), type=console.MSG_TYPE.ERROR)