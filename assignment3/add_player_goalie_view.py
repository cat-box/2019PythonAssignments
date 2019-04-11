import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import *
import json

class AddPlayerGoalieView(tk.Frame):
    """ Popup Window """

    TYPE_GOALIE = 'goalie'

    def __init__(self, parent, close_popup_callback, add_player_callback):
        """ Initializer """

        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)

        self._close_popup_callback = close_popup_callback
        self._add_player_callback = add_player_callback

        self._fields_u = ['First Name', 'Last Name', 'Height (cm)', 'Weight (lbs)', 'Jersey Number', 'Date of Birth (mmm dd, yyyy)', 'Year Joined', 'Shots Against', 'Goals Against', 'Goals Saved', 'Games Played', 'Games Won', 'Games Lost']
        self._fields = ['fname', 'lname', 'height', 'weight', 'jersey_num', 'date_birth', 'year_joined', 'shots_against', 'goals_against','goals_saved', 'games_played', 'games_won', 'games_lost']

        self._create_widgets()

    def _create_widgets(self):
        """ Creates widgets """

        self._entries = []

        self._title = tk.Label(self, text="Add Goalie", font=20)
        self._title.grid(row=0, padx=20)

        for i, field in enumerate(self._fields_u, 1):
            self._field = tk.Label(self, text=field)
            self._field.grid(row=i)
            self._ent = tk.Entry(self)
            self._ent.grid(row=i, column=1, padx=20)

            self._entries.append(self._ent)

            # self._entries[self._fields[i-1]] = self._ent

        tk.Button(self, text="Cancel", command=self._close_popup_callback).grid(row=14, column=0, pady=5)

        tk.Button(self, text="Submit", command=self.add_player).grid(row=14, column=1, pady=5)

    def add_player(self):
        self._values = {}

        for i, entry in enumerate(self._entries, 0):
            value = entry.get()
            self._values[self._fields[i]] = value

        self._values['player_type'] = self.TYPE_GOALIE
        player_string = self._add_player_callback(self._values)

        if player_string is not None:
            self._message = tkMessageBox.showinfo("Sucess", "Player successfully added! :D")
            self._close_popup_callback()
        else:
            self._message = tkMessageBox.showinfo("Error", "Player was not added :c")
            self._close_popup_callback()
