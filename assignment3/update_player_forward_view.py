import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import *
import json

class UpdatePlayerForwardView(tk.Frame):
    """ Popup Window """

    TYPE_FORWARD = 'forward'

    def __init__(self, parent, close_popup_callback, update_player_callback, player_details):
        """ Initializer """

        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)

        self._close_popup_callback = close_popup_callback
        self._update_player_callback = update_player_callback

        self._fields_u = ['First Name', 'Last Name', 'Height (cm)', 'Weight (lbs)', 'Jersey Number', 'Date of Birth (mmm dd, yyyy)', 'Year Joined', 'Zone', 'Shooting Hand', 'Goals', 'Assists', 'Total Shots']
        self._fields = ['fname', 'lname', 'height', 'weight', 'jersey_num', 'date_birth', 'year_joined', 'zone', 'shooting_hand','goals', 'assists', 'total_shots']
        self._player_details = player_details

        self._create_widgets()

    def _create_widgets(self):
        """ Creates widgets """

        self._entries = []

        self._title = tk.Label(self, text="Update Forward", font=20)
        self._title.grid(row=0, padx=20)

        for i, field in enumerate(self._fields_u, 1):
            self._field = tk.Label(self, text=field)
            self._field.grid(row=i)

            default_text = self._player_details[self._fields[i-1]]
            self._ent = tk.Entry(self)
            self._ent.insert(i-1, default_text)
            self._ent.grid(row=i, column=1, padx=20)

            self._entries.append(self._ent)

        tk.Button(self, text="Cancel", command=self._close_popup_callback).grid(row=14, column=0, pady=5)

        tk.Button(self, text="Update", command=self.update_player).grid(row=14, column=1, pady=5)

    def update_player(self):
        self._values = {}

        for i, entry in enumerate(self._entries, 0):
            value = entry.get()
            self._values[self._fields[i]] = value

        self._values['player_type'] = self.TYPE_FORWARD
        player_string = self._update_player_callback(self._player_details['id'], self._values)

        if player_string is not None:
            self._message = messagebox.showinfo("Sucess", "Player successfully updated! :D")
            self._close_popup_callback()
        else:
            self._message = messagebox.showinfo("Error", "Player was not updated :c")
            self._close_popup_callback()
