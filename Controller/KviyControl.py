from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Line

from KivyVehicles import Rovers 

class MyApp(App):
    def build(self):
        self.rover_list = Rovers()
        self.rover_list.InitRovers()

        main_layout = FloatLayout()

        # Add the canvas with grid lines

        #combobox = TextInput(hint_text='Available Rovers')
        #main_layout.add_widget(combobox)
           
        title_label = Label(text='Available Rovers', size_hint=(1, None), height=30)
        main_layout.add_widget(title_label)

        self.rover_spinner = Spinner(
            text='Select Rover',
            values=[rover.Name for rover in self.rover_list.get_rovers()],  # Assuming you have a list of rover objects named 'rovers'
            size_hint=(None, None),
            width=200,
            height=30,
            pos_hint={'x': 0.05, 'top': 0.95}
        )
        main_layout.add_widget(self.rover_spinner)


        # Add other widgets to the left layout
  

        disconnect_button = Button(text='Disconnect', size_hint=(None, None), width=200, height=30, pos_hint={'x': 0.05, 'top': 0.9})
        main_layout.add_widget(disconnect_button)
  
                # Create a container for video display
        #video_container = FloatLayout()
        #video_container.add_widget(Label(text='Video Display'))

       # main_layout.add_widget(video_container)
        

        up_button = Button(text='Up')
        down_button = Button(text='Down')
        left_button = Button(text='Left')
        right_button = Button(text='Right')
        #camera_controls.add_widget(up_button)
        #camera_controls.add_widget(down_button)
       # camera_controls.add_widget(left_button)
       # camera_controls.add_widget(right_button)
       # layout.add_widget(camera_controls)
        
        message_list = Label(text='Messages')
        main_layout.add_widget(message_list)
        # Add more widgets...
        
        return main_layout
    
    def connect_to_rover(self, instance):
        rover_name = instance.text
        selected_rover = None

        for rover in self.rover_list.get_rovers():
            if rover.Name == rover_name:
                selected_rover = rover
                break

        if selected_rover:
            # Here you can implement your logic to connect to the selected rover
            # For example, you can launch a new screen or dialog for rover control
            print(f"Connecting to {selected_rover.Name} with IP: {selected_rover.IPAddress}")


if __name__ == '__main__':
    MyApp().run()
