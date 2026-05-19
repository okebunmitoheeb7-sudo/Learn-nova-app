from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class TodoApp(App):

    def build(self):
        self.tasks = []

        self.layout = BoxLayout(orientation="vertical")

        self.input = TextInput(hint_text="Enter task", size_hint=(1, 0.2))
        self.layout.add_widget(self.input)

        add_btn = Button(text="Add Task", size_hint=(1, 0.2))
        add_btn.bind(on_press=self.add_task)
        self.layout.add_widget(add_btn)

        self.label = Label(text="No tasks yet", size_hint=(1, 0.6))
        self.layout.add_widget(self.label)

        return self.layout

    def add_task(self, instance):
        task = self.input.text
        if task != "":
            self.tasks.append(task)
            self.label.text = "\n".join(self.tasks)
            self.input.text = ""

TodoApp().run()
