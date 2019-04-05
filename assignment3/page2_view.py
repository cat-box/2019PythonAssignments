import tkinter as tk
from tkinter import W, E
import re
import json

class Page2View(tk.Frame):
    """ Page 2 """

    def __init__(self, parent, submit_callback, get_players_callback, get_player_detail_callback, add_player_callback):
        """ Initialize Page 2 """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._submit_callback = submit_callback
        self._get_players_callback = get_players_callback
        self._get_player_detail_callback = get_player_detail_callback
        self._add_player_callback = add_player_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 2 """
        self._title = tk.Label(self, text="Team", font=20)
        self._title.grid(row=1, padx=20)

        self._listbox = tk.Listbox(self, width=35)
        self._listbox.grid(row=2, sticky=W)

        self._refresh_button = tk.Button(self, text="Refresh", command=self.refresh)
        self._refresh_button.grid(row=3)

        self._get_details = tk.Button(self, text="Details", command=self.get_data)
        self._get_details.grid(row=4)

        self._add_player = tk.Button(self, text="Add", command=lambda:self._add_player_callback("goalie"))
        self._add_player.grid(row=5)


    def get_form_data(self):
        return { "fname":  "" }

    def refresh(self):
        self._listbox.destroy()
        self._listbox = tk.Listbox(self, width=35)
        self._listbox.grid(row=2, sticky=W)

        self._get_players_callback()

    def get_id(self):
        selection = self._listbox.curselection()
        value = self._listbox.get(selection[0])
        p_id = re.findall(r"[0-9]", value)
        player_id = ''.join(p_id)
        return player_id

    def set_form_data(self, players_list):
        self._listbox.delete(0, tk.END)

        for player in players_list:
            self._listbox.insert(tk.END, '%s: %s %s' % (player['id'], player['fname'], player['lname']))

    def get_data(self):
        player_id = self.get_id()
        details = self._get_player_detail_callback(player_id)
        self.popupmsg(details, '%s: %s %s' % (details['id'], details['fname'], details['lname']))

    def popupmsg(self, message, player):
        popup = tk.Toplevel(self)
        popup.wm_title("Player Details")
        popup.tkraise(self)

        tk.Label(self, text=player, font=20)

        tk.Label(popup, text=json.dumps(message, indent=4), anchor=W, justify="left").pack(side="top", fill="x", pady=10)
        tk.Button(popup, text="OK", command = popup.destroy).pack()
        
