
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.core.window import Window

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # Dibujar la imagen de fondo adaptada a la pantalla
        with self.canvas.before:
            self.rect = Rectangle(source="portada.png", pos=self.pos, size=Window.size)
        
        # Actualizar fondo si cambia el tamaño de pantalla
        self.bind(pos=self._update_rect, size=self._update_rect)

        self.spacing = 10
        self.padding = 20
        self.cols = 2

        # Campos de texto y etiquetas
        self.add_widget(Label(text="First Name: ", font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=180))
        self.name = TextInput(text='Jorge', multiline=False, font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=220)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: ", font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=180))
        self.lastName = TextInput(text='Pérez Reyes', multiline=False, font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=220)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email: ", font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=180))
        self.email = TextInput(text='j_perez_reyes@hotmail.com', multiline=False, font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=220)
        self.add_widget(self.email) 

        # Botones
        self.add_widget(Button(text='OK', font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=180, on_press=self.submit)) 
        self.add_widget(Button(text='EXIT', font_size=20, size_hint_y=None, height=50, size_hint_x=None, width=180, on_release=self.close_app)) 
        
        self.frase = TextInput(text="Yo: ", multiline=True, font_size=15, size_hint_y=None, height=135, size_hint_x=None, width=220)
        self.add_widget(self.frase)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def submit(self, obj):
        if self.name.text == 'Jorge': 
            self.frase.text = "A mi me pertenecen ese rostro y es cuerpo, porque Jehová me los a regalado a mi, soy el dueño de ellos."
        else: 
            self.frase.text = "Cada vez que ves a esa mujer en tu mente, te estas viendo a ti mismo, porque tu seras esa mujer en carne y hueso, con ese mismo rostro fisico... Es promesa de Jehová"

    def close_app(self, obj):
        App.get_running_app().stop()

class PERSONAL_PROGRAMApp(App):
    title = "* * * * *P-r-u-e-b-a* * * *"
    def build(self):
        return MyGrid() 

if __name__ == "__main__":
    PERSONAL_PROGRAMApp().run()