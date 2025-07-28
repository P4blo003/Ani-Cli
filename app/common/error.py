# -*- coding: utf-8 -*-


"""
*******************************************************************************************
    Sript name: error.py
    Project: Ani-Cli
    Author: Pablo González García
    Date: 2025-07-28
    Description: <description>
    Copyright (c) 2025 Pablo González García
    Licencia: MIT License. See the LICENCE file in the project root.
*******************************************************************************************
"""


# ---- MODULO ---- #
# Librerías estándar:

# Librerías internas:

# Librerías externas:


# ---- CLASES ---- #
class WebError(Exception):

    # -- Default methods -- #
    def __init__(self, msg:str, status_code:int) -> None:
        """
        Initializes the class properties.

        Args:
            msg (str): Msg of the exception.
            status_code (int): Status code of the web response.
        """
        self.__msg:str = msg
        self.__status_code:int = status_code
    
    def __repr__(self) -> str:
        """
        Returns the string format of the error.

        Returns:
            str: String format.
        """
        # Generates the string.
        str_fmt:str = f"({self.__status_code}): {self.__msg}"

        # Returns the string.
        return str_fmt