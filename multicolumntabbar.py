# source:
# https://forum.sublimetext.com/t/multi-line-tabbar-for-st2/12978/5
#
# instructions:
# - copy the code into a file named multicolumntabbar.py
# - put this file into the Packages/User folder (go there by clicking Preferences -> Browse Packages).
# - then it works

from collections import defaultdict

import sublime_plugin

enabled_map = defaultdict(lambda: True)

#modify this parameter to configure height of tab rows
#bar_height = 0.025
bar_height = 0.07

class MultiColumnTabBarCommand(sublime_plugin.EventListener):
    def on_activated(self, view):        
        id_ = view.window().id()
        if not enabled_map[id_]:
            return
        window = view.window()
        group, _ = window.get_view_index(view)
        if group == 0:
            window.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, bar_height, bar_height*2, 1.0],"cells": [[0, 2, 1, 3],[0, 0, 1, 1],[0, 1, 1, 2]]})
        elif group == 1:
            window.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, bar_height, bar_height*2, 1.0],"cells": [[0, 0, 1, 1],[0, 2, 1, 3],[0, 1, 1, 2]]})
        elif group == 2:
            window.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, bar_height, bar_height*2, 1.0],"cells": [[0, 0, 1, 1],[0, 1, 1, 2],[0, 2, 1, 3]]})
              
                        
class ToggleMultiColLayoutCommand(sublime_plugin.WindowCommand):
    def run(self):
        id_ = self.window.id()
        enabled_map[id_] ^= True
        if enabled_map[id_]:
            print("Multi Column switch enabled")
        else:
            print("Multi Column switch disabled")
           
            
class DisableMultiColLayoutCommand(sublime_plugin.WindowCommand):
    def run(self):
        id_ = self.window.id()
        enabled_map[id_] = False
        print("Multi Column switch disabled")


class EnableMultiColLayoutCommand(sublime_plugin.WindowCommand):
    def run(self):
        id_ = self.window.id()
        enabled_map[id_] = True
        print("Multi Column switch enabled")


class ResetLayoutCommand(sublime_plugin.WindowCommand):
    def run(self):
        id_ = self.window.id()
        enabled_map[id_] = False
        self.window.run_command("set_layout",{"cols": [0.0 ,1],"rows": [0.0, 1.0],"cells": [[0, 0, 1, 1]]})
        print("Multi Column disabled and layout reset to standard")
