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
            self._field = tk.Label(self, text=key)
            self._field.grid(row=i, column=0, sticky="W", pady=3, padx=10)

            self._field2 = tk.Label(self, text=value)
            self._field2.grid(row=i, column=1, sticky="W")

            i+=1

        tk.Button(self, text="Exit", command=self._close_popup_callback).grid(
            row=16, column=0, pady=5, columnspan=2)

    def update_player(self):
        self._values = {}
        self._field_check = 1

        for i, entry in enumerate(self._entries, 0):
            value = entry.get()
            self._values[self._fields[i]] = value
            if value == '':
                self._field_check = 0
                break

        if self._field_check == 0:
            self._message = messagebox.showinfo("Error", "Missing fields")
        else:
            self._values['player_type'] = self.TYPE_GOALIE

            player_string = self._update_player_callback(
                self._player_details['id'], self._values)

            if player_string is not None:
                self._message = messagebox.showinfo(
                    "Sucess", "Player successfully updated! :D")
                self._close_popup_callback()
            else:
                self._message = messagebox.showinfo(
                    "Error", "Player was not updated :c")
                self._close_popup_callback()
