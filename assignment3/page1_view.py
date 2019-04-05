import tkinter as tk


class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, submit_callback, get_players_callback, add_player_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        self._submit_callback = submit_callback
        self._get_players_callback = get_players_callback
        self._add_player_callback = add_player_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        self._title = tk.Label(self, text="Team", font=20)
        self._title.grid(row=1, padx=20)

        self._listbox = tk.Listbox(self)
        self._listbox.grid(row=2)

        self._listbox.insert(tk.END, "This is item 1")
        self._listbox.insert(tk.END, "This is item 2")

        self._refresh_button = tk.Button(self, text="Refresh", command=self.refresh)
        self._refresh_button.grid(row=3)

        self._add_player = tk.Button(self, text="Add", command=lambda:self._add_player_callback("forward"))
        self._add_player.grid(row=5)



    def get_form_data(self):
        return { "fname" : "" }


    def refresh(self):
        # if self._listbox is not None:
        self._listbox.destroy()
        self._listbox = tk.Listbox(self)
        self._listbox.grid(row=2)

        self._get_players_callback()


    def set_form_data(self, players_list):
        self._listbox.delete(0, tk.END)
        
        # self.refresh()

        for player in players_list:
            self._listbox.insert(tk.END, '%s %s' % (player['fname'], player['lname']))

