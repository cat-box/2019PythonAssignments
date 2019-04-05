#!/usr/bin/env python3

import tkinter as tk
from top_navbar_view import TopNavbarView
from page1_view import Page1View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from popup_view import PopupView
from add_player_forward_view import AddPlayerForwardView
from add_player_goalie_view import AddPlayerGoalieView
import requests
import json

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    TYPE_FORWARD = "forward"
    TYPE_GOALIE = "goalie"

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback, self._page_popup_callback)
        self._page1 = Page1View(self, self._page1_submit_callback, self._get_players_of_forward, self._page_add_callback)
        self._page2 = Page2View(self, self._page2_submit_callback, self._get_players_of_goalie, self._get_player, self._page_add_callback)
        self._bottom_navbar = BottomNavbarView(self, self._quit_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)
        self._curr_page = TopNavbarView.PAGE1
        # Hide Page 2 by default
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

        self._get_players_of_forward()
        self._get_players_of_goalie()

    def _page_callback(self):
        """ Handle Switching Between Pages """

        curr_page = self._top_navbar.curr_page.get()
        if (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE1):
            self._page1.grid_forget()
            self._page2.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE2
            
        elif (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE2):
            self._page2.grid_forget()
            self._page1.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE1

        self._get_players_of_forward()
        self._get_players_of_goalie()

    def _page_popup_callback(self):
        self._popup_win = tk.Toplevel()
        self._popup = PopupView(self._popup_win, self._close_popup_callback)

    def _close_popup_callback(self):
        self._popup_win.destroy()

    def _page_add_callback(self, player_type):
        self._popup_win = tk.Toplevel()
        if player_type == self.TYPE_FORWARD:
            self._popup = AddPlayerForwardView(self._popup_win, self._close_popup_callback)
        elif player_type == self.TYPE_GOALIE:
            self._popup = AddPlayerGoalieView(self._popup_win, self._close_popup_callback, self._add_player)
        else:
            return

    def _page1_submit_callback(self):
        print("Submit Page 1")
        print(self._page1.get_form_data())

    def _page2_submit_callback(self):
        print("Submit Page 2")
        print(self._page2.get_form_data())

    def _quit_callback(self):
        self.quit()

    def _get_player(self, player_id):
        print(player_id)
        response = requests.get("http://127.0.0.1:5000/team/players/%s" % player_id) 

        if response.status_code is 200:
            return(response.json())

    def _get_players_of_forward(self):
        response = requests.get("http://127.0.0.1:5000/team/players/all/forward")

        if response.status_code is 200:
            self._page1.set_form_data(response.json())

    def _get_players_of_goalie(self):
        response = requests.get("http://127.0.0.1:5000/team/players/all/goalie")

        if response.status_code is 200:
            self._page2.set_form_data(response.json())

    def _add_player(self, player_data):
        response = requests.post("http://127.0.0.1:5000/team/players", json = player_data)

        if response.status_code is 200:
            self._page2.refresh()
            return response.text
        
        return None



if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

