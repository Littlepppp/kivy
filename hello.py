import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self):
        # call grid layout constructor
        super().__init__()
        # set columns
        self.cols = 2
        # add widgets
        self.add_widget(Label(text="Name: "))
        # add input box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=True)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=True)
        self.add_widget(self.color)

        self.submit = Button(text="Submit")
        self.submit.on_press = self.press
        # self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f"{name}-{pizza}-{color}")

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()