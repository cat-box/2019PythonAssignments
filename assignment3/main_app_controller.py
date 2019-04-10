#!/usr/bin/env python3

import tkinter as tk
from top_navbar_view import TopNavbarView
from page1_view import Page1View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from add_player_forward_view import AddPlayerForwardView
from add_player_goalie_view import AddPlayerGoalieView
from update_player_forward_view import UpdatePlayerForwardView
from update_player_goalie_view import UpdatePlayerGoalieView
from detail_player_view import DetailPlayerView
import requests
import json

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    TYPE_FORWARD = "forward"
    TYPE_GOALIE = "goalie"

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback)
        self._page1 = Page1View(self, self._get_players_of_type, self._get_player, self._page_add_callback, self._delete_player, self._page_update_callback, self._display_details)
        self._page2 = Page2View(self, self._get_players_of_type, self._get_player, self._page_add_callback, self._delete_player, self._page_update_callback, self._display_details)
        self._bottom_navbar = BottomNavbarView(self, self._quit_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)
        self._curr_page = TopNavbarView.PAGE1
        # Hide Page 2 by default
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

        self._get_players_of_type(self.TYPE_FORWARD)
        self._get_players_of_type(self.TYPE_GOALIE)

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

        self._get_players_of_type(self.TYPE_FORWARD)
        self._get_players_of_type(self.TYPE_GOALIE)

    def _close_popup_callback(self):
        self._popup_win.destroy()

    def _page_add_callback(self, player_type):
        self._popup_win = tk.Toplevel()
        self._popup_win.title('Add Player')

        if player_type == self.TYPE_FORWARD:
            self._popup = AddPlayerForwardView(self._popup_win, self._close_popup_callback, self._add_player)
        elif player_type == self.TYPE_GOALIE:
            self._popup = AddPlayerGoalieView(self._popup_win, self._close_popup_callback, self._add_player)
        else:
            return

    def _page_update_callback(self, player_data):
        self._popup_win = tk.Toplevel()
        self._popup_win.title('Update Player')

        player_type = player_data['player_type']
        
        if player_type == self.TYPE_FORWARD:
            self._popup = UpdatePlayerForwardView(self._popup_win, self._close_popup_callback, self._update_player, player_data)
        elif player_type == self.TYPE_GOALIE:
            self._popup = UpdatePlayerGoalieView(self._popup_win, self._close_popup_callback, self._update_player, player_data)

    def _quit_callback(self):
        self.quit()

    def _get_player(self, player_id):
        response = requests.get("http://127.0.0.1:5000/team/players/%s" % player_id) 

        if response.status_code is 200:
            return response.json()
            

    def _display_details(self, player_detail):
        self._popup_win = tk.Toplevel()
        self._popup_win.title('Player Detail')
        self._popup = DetailPlayerView(self._popup_win, self._close_popup_callback, player_detail)


    def _get_players_of_type(self, player_type):
        response = requests.get("http://127.0.0.1:5000/team/players/all/%s" % player_type)

        if response.status_code is 200:
            if player_type == self.TYPE_FORWARD:
                self._page1.set_form_data(response.json())
            elif player_type == self.TYPE_GOALIE:
                self._page2.set_form_data(response.json())

    def _add_player(self, player_data):
        response = requests.post("http://127.0.0.1:5000/team/players", json = player_data)

        if response.status_code is 200:
            self._page1.refresh()
            self._page2.refresh()
            return response.text
        
        return None

    def _delete_player(self, player_id):
        response = requests.delete("http://127.0.0.1:5000/team/players/%s" % player_id)

        if response.status_code is 200:
            self._page1.refresh()
            self._page2.refresh()
        return response.status_code

    def _update_player(self, player_id, player_data):
        response = requests.put("http://127.0.0.1:5000/team/players/%s" % player_id, json = player_data)

        if response.status_code is 200:
            self._page1.refresh()
            self._page2.refresh()
        return response.status_code


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Roster")
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
