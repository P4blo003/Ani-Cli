# -*- coding: utf-8 -*-


"""
*******************************************************************************************
    Sript name: web.py
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
from .error import WebError
# Librerías externas:
import cloudscraper

from requests import Response
from cloudscraper import CloudScraper


# ---- FUNCTIONS ---- #
def get(url:str) -> Response:
    """
    Try gets response from the given URL.

    Args:
        url (str): Url to make the connection.
    Raises:
        WebError: In caso the response from the URL is not 200.
    """
    # Try-Except to manage exceptions.
    try:
        # Creates cloud scrapper.
        scrapper:CloudScraper = cloudscraper.create_scraper()

        # Gets the response and raises exception in case the status code is not 200.
        response:Response = scrapper.get(url=url)
        response.raise_for_status()

        # Returns the response.
        return response

    # If error detected.
    except Exception as e:
        # Raises exception.
        raise WebError(msg=f"Couldn't get response from [{url}].", status_code=response.status_code)