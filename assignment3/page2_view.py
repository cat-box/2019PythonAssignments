import tkinter as tk
from tkinter import W, E, messagebox as tkMessageBox
import re
import json

class Page2View(tk.Frame):
    """ Page 2 """

    TYPE_GOALIE = "goalie"

    def __init__(self, parent, get_players_callback, get_player_detail_callback, add_player_callback, delete_player_callback, update_player_callback, display_details_callback):
        """ Initialize Page 2 """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        
        self._get_players_callback = get_players_callback
        self._get_player_detail_callback = get_player_detail_callback
        self._add_player_callback = add_player_callback
        self._delete_player_callback = delete_player_callback
        self._update_player_callback = update_player_callback
        self._display_details_callback = display_details_callback

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

        self._delete_player = tk.Button(self, text="Delete", command=self.delete_player)
        self._delete_player.grid(row=6)

        self._update_player = tk.Button(self, text="Update", command=self.update_player)
        self._update_player.grid(row=7)

    def refresh(self):
        self._listbox.destroy()
        self._listbox = tk.Listbox(self, width=35)
        self._listbox.grid(row=2, sticky=W)

        self._get_players_callback(self.TYPE_GOALIE)

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
        self._display_details_callback(details)

    def delete_player(self):
        player_id = self.get_id()

        if tkMessageBox.askyesno('Verify', 'Really delete?'):
            status_code = self._delete_player_callback(player_id)
            if status_code == 200:
                self._message = tkMessageBox.showinfo("Sucess", "Player successfully deleted! :D")
            else:
                self._message = tkMessageBox.showinfo("Error", "Player was not deleted! :c")
            self.refresh()

    def update_player(self):
        player_id = self.get_id()
        player_detail = self._get_player_detail_callback(player_id)
        self._update_player_callback(player_detail)
        self.refresh()