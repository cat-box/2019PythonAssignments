import tkinter as tk


class Page2View(tk.Frame):
    """ Page 2 """

    def __init__(self, parent, submit_callback, get_players_callback):
        """ Initialize Page 2 """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._submit_callback = submit_callback
        self._get_players_callback = get_players_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 2 """
        self._title = tk.Label(self, text="Team", font=20)
        self._title.grid(row=1, padx=20)

        self._listbox = tk.Listbox(self)
        self._listbox.grid(row=2)

        self._refresh_button = tk.Button(
            self, text="Refresh", command=self._submit_callback)
        self._refresh_button.grid(row=3)

    def get_form_data(self):
        return { "fname":  "" }

    def refresh(self):
        self._listbox.destroy()
        self._listbox = tk.Listbox(self)
        self._listbox.grid(row=2)

        self._get_players_callback()


    def set_form_data(self, players_list):
        self._listbox.delete(0, tk.END)

        # self.refresh()

        for player in players_list:
            self._listbox.insert(tk.END, '%s %s' % (player['fname'], player['lname']))



