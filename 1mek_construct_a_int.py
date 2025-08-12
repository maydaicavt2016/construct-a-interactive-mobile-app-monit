# Import necessary libraries
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import platform
import psutil
import time

# Define the App class
class InteractiveMobileAppMonitor(App):
    def build(self):
        # Set the window size
        Window.size = (400, 600)

        # Create the main layout
        self.layout = BoxLayout(orientation='vertical')

        # Add a label to display the device information
        self.device_info_label = Label(text=f"Device: {platform.machine()}", font_size=20)
        self.layout.add_widget(self.device_info_label)

        # Add a label to display the CPU usage
        self.cpu_usage_label = Label(text="CPU Usage: 0.0%", font_size=20)
        self.layout.add_widget(self.cpu_usage_label)

        # Add a label to display the memory usage
        self.memory_usage_label = Label(text="Memory Usage: 0.0%", font_size=20)
        self.layout.add_widget(self.memory_usage_label)

        # Add a button to update the CPU and memory usage
        self.update_button = Button(text="Update", font_size=20)
        self.update_button.bind(on_press=self.update_usage)
        self.layout.add_widget(self.update_button)

        # Return the layout
        return self.layout

    def update_usage(self, instance):
        # Get the CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Get the memory usage
        memory_usage = psutil.virtual_memory().percent

        # Update the labels
        self.cpu_usage_label.text = f"CPU Usage: {cpu_usage}%"
        self.memory_usage_label.text = f"Memory Usage: {memory_usage}%"

# Run the App
if __name__ == "__main__":
    InteractiveMobileAppMonitor().run()