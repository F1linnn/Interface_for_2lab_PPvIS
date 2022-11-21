from main_window import MyMainApp
class Injector:
    def build(self):
        MyMainApp().run()

if __name__ == "__main__":
    injector = Injector()
    injector.build()
