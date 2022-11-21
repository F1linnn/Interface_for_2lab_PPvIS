from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from Screens import *

Config.set('graphics', 'resizable', '0')

Builder.load_file("my.kv")


class MyMainApp(App):
    Window.clearcolor = (.67,.73,.89,1)
    def build(self):
        self.title="Main Window"
        Window.size = (450, 600)
        sm = ScreenManager()
        sm.add_widget(LogIn(name='LogIn'))
        sm.add_widget(NewProfile(name='NewProfile'))
        sm.add_widget(Main_menu(name='main_menu'))
        sm.add_widget(Profile(name='profile'))
        sm.add_widget(Dohod(name='dohod'))
        sm.add_widget(Rashod(name='rashod'))
        sm.add_widget(Menu_dop(name='dop_menu'))
        # sm.add_widget(FindTeamForPlayer(name='find_team_player'))
        # sm.add_widget(MobileCoachForPlayer(name='coach_player'))
        # sm.add_widget(MobileCoachForCoach(name = 'coach_coach'))
        # sm.add_widget(FindTeamForCoach(name='find_team_coach'))
        return sm
