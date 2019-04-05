import tkinter as tk
from tkinter import messagebox as tkMessageBox

class AddPlayerForwardView(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback):
        """ Initializer """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)

        self._close_popup_callback = close_popup_callback

        self._fields = ['First Name', 'Last Name', 'Height (cm)', 'Weight (lbs)', 'Jersey Number', 'Date of Birth (mmm dd, yyyy)', 'Year Joined', 'Zone', 'Shooting Hand', 'Goals', 'Assists', 'Total Shots']

        self._create_widgets()


    def _create_widgets(self):
        """ Creates widgets """

        print(len(self._fields))

        self._entries = []

        self._title = tk.Label(self, text="Add Player", font=20)
        self._title.grid(row=0, padx=20)

        for i, field in enumerate(self._fields, 1):
            self._field = tk.Label(self, text=field)
            self._field.grid(row=i)
            self._ent = tk.Entry(self)
            self._ent.grid(row=i, column=1, padx=20)

            self._entries.append((field, self._ent))

        tk.Button(self, text="Close", command=self._close_popup_callback).grid(row=13, column=1)
