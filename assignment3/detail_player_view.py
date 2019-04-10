import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import *
import json


class DetailPlayerView(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback, player_details):
        """ Initializer """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2, padx=30)

        self._close_popup_callback = close_popup_callback

        self._player_details = player_details

        self._create_widgets()

    def _create_widgets(self):
        """ Creates widgets """

        i = 1

        self._title = tk.Label(self, text="Player Details", font=20)
        self._title.grid(row=0, padx=20, columnspan=2)

        for key, value in self._player_details.items():
            self._field = tk.Label(self, text=key, font=('TkDefaultFont', 9, 'bold'))
            self._field.grid(row=i, column=0, sticky="W", pady=3, padx=10)

            self._field2 = tk.Label(self, text=value)
            self._field2.grid(row=i, column=1, sticky="W")

            i+=1

        tk.Button(self, text="Exit", command=self._close_popup_callback).grid(
            row=16, column=0, pady=5, columnspan=2)
