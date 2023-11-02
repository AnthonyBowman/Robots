from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
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
  
        # Create floated video container
        video_container = FloatLayout()  
        video_container.size = (510, 360)
        video_container.pos = (140, 40)

        def add_border(widget):
            with widget.canvas:
                Color(1, 1, 1, 1) 
                Line(rectangle=(widget.x, widget.y, widget.width, widget.height)) 

        # Add border
        add_border(video_container)
        main_layout.add_widget(video_container)

        # Create side camera control panel 
        camera_controls = BoxLayout(orientation='vertical', size=(100,video_container.height))
        camera_controls.size_hint = (None, None)
        camera_controls.pos = (video_container.x + video_container.width, video_container.y)
        
        up_button = Button(text='Up')
        down_button = Button(text='Down')
        east_button = Button(text='Left')
        west_button = Button(text='Right')

        camera_controls.add_widget(up_button)
        camera_controls.add_widget(down_button)
        camera_controls.add_widget(east_button)
        camera_controls.add_widget(west_button)

        # Add both widgets to main layout
        main_layout.add_widget(camera_controls)
        
        # Create left side rover control panel 
        rover_controls = BoxLayout(orientation='vertical', size=(100,video_container.height))
        rover_controls.size_hint = (None, None)
        rover_controls.pos = (video_container.x - 100, video_container.y)
        
        forward_button = Button(text='Forward')
        back_button = Button(text='Back')
        left_button = Button(text='Left')
        right_button = Button(text='Right')

        rover_controls.add_widget(forward_button)
        rover_controls.add_widget(back_button)
        rover_controls.add_widget(left_button)
        rover_controls.add_widget(right_button)

        main_layout.add_widget(rover_controls)
        
        # Create a container for video display
#        video_container = FloatLayout(size_hint=(None,None), size=(320, 240), pos=(100,100))
#        add_border(video_container)
#        video_container.add_widget(Label(text='Video Display'))               
#        main_layout.add_widget(video_container)
        
#        camera_controls = BoxLayout(orientation='vertical', size_hint_x=None, width=100)
        #camera_controls.size_hint = (None, None)
        #camera_controls.size = (50, 100)
        #camera_controls.pos = (500, 500) # x, y 
        # Position controls on right side 
 #       camera_controls.pos = (video_container.width, 0) 
      
  #      up_button = Button(text='Up')
  #      down_button = Button(text='Down')
  
  #      camera_controls.add_widget(up_button)
  #      camera_controls.add_widget(down_button)

  #      main_layout.add_widget(camera_controls)
        
        #message_list = Label(text='Messages')
        #main_layout.add_widget(message_list)
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
