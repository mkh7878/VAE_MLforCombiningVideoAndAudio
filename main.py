
import os
import pyaudio
import numpy as np
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import math
from collections import deque

class ImageCarousel(App):
    def build(self):
        # Get the path to the image directory relative to the script
        image_dir = os.path.join(os.path.dirname(__file__), "BCinter200")

        # Get the list of image filenames in the directory
        image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
        image_files.sort()  # Sort the filenames alphabetically

        # Create a BoxLayout as the root widget
        self.root = BoxLayout(orientation='vertical')

        # Create an Image widget and add it to the root widget
        self.image = Image(allow_stretch=True, keep_ratio=False)
        self.root.add_widget(self.image)

        # Store the array of images
        self.images = image_files

        # Set up PyAudio
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True,
                                   frames_per_buffer=4096)  # Increased buffer size

        # Store the previous amplitude values with a queue
        self.amplitude_queue = deque(maxlen=20)  # Adjust the size as needed for desired lag

        # Schedule the image changes
        self.index = 0
        Clock.schedule_interval(self.update_image, 1 / 30)  # Output rate of 30 times per second

        return self.root

    def update_image(self, dt):
        # Read audio input and calculate amplitude
        try:
            data = np.frombuffer(self.stream.read(4096), dtype=np.float32)  # Increased buffer size
            amplitude = np.mean(np.abs(data)) * 1000  # Multiply by 1000 for scaling

            # Round up the amplitude to the nearest whole number
            amplitude = math.ceil(amplitude)

            # Add the current amplitude to the queue
            self.amplitude_queue.append(amplitude)

            # Check if the queue is full
            if len(self.amplitude_queue) == self.amplitude_queue.maxlen:
                # Get the average amplitude from the queue
                avg_amplitude = sum(self.amplitude_queue) / len(self.amplitude_queue)

                # Get the index of the image based on the rounded average amplitude
                index = round(avg_amplitude) % len(self.images)

                # Load and display the appropriate image
                image_dir = os.path.join(os.path.dirname(__file__), "BCinter200")
                image_file = self.images[index]
                self.image.source = os.path.join(image_dir, image_file)
                self.image.reload()

        except IOError as e:
            print("Error:", str(e))

    def on_start(self):
        # Start the PyAudio stream
        self.stream.start_stream()

    def on_stop(self):
        # Stop and close the PyAudio stream
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

if __name__ == "__main__":
    ImageCarousel().run()

