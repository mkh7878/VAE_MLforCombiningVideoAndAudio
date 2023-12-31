# Final Project: #
### VAE Machine Learning model to combine and relate video and audio ###

This is the Coding 3 Final Project Submission for my MsC in creative computing at UAL.

[Youtube video with breif explanation and demonstration.](https://youtu.be/iFEo42yb-hs)

For my project I created a VAE model in order to do unsupervised machine learning. My idea is to train the model on each frame of a short film, then create a video that is controlled by a song.
I ended up creating an application that uses the images generated by the ML model to react to live audio. 

The code with in-depth descriptions is linked below: 

[Part 1](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/Images/Coding3-MaeHorak-WFM-Part1.ipynb)

[Part 2](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/main/Coding3-MaeHorak-WFM-Part2.ipynb)

[Application For Live Music Performance](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/main/main.py)

![WFM screenshot](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/frame_3712.png)

# Datasets #

The dataset I used for the first test of my ML model was over 5k images that were frames from a short film from my company [Off Hand Co](https://www.offhandco.com/) called "Works for Me". I chose to do only 10 epochs and a batch size of 20 simply because I wanted to not waste time incase the project didn't work. The latent dim was 10.

For the second set of training data I inputted just a single scene from a short film I made called "Bat Country". I hoped that doing just one scene would make the output images a bit more similar and cohesive, as my intention was that they seem to be blending and moving together. 

Once the dataset was trained, I exported the decoder for further use.

# Experimenting with Dataset 1 #

I experimented with generating random latent vectors and was able to successfully produce images. The below image is produced with a randomised latent vector.

![random latent vector generation](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/image_6870.png)

I then made some GIFs using ranomised latent vectors just to see what combining the images might look like.

![gif](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/Images/gif_0.gif?raw=true)

# Mapping Latent Vector using the Amplitude values of a song # 

Then I uploaded a song I've recorded and used the python librosa library to find values of amplitude (loudness) of the music. Because librosa gives the amplitude 22,050x a second, I saved every 735th value so I would have 30 per second. [Then I exported these amplitude values into a csv file.](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/Images/updated_amplitude.csv) Below is a graph of the amplitude throughout the song using the 30 values per second.

![graph](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/download%20(1).png)

Now I used the values from the CSV file to feed into the decoder. The idea was basically to see what the ML model "decided" was important and the patterns it found in the images, and then to use the values (scaled to the range of latent vector) to generate new images which I would make into a new video. I hoped that the images would change as the song gets louder, and that certainly did seem to happen in some ways. I want to use a different dataset of a different film I made and adjust the settings to see what results I get.

[![video link](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/Screenshot%202023-06-13%20at%2011.48.30%20am.png)](https://www.youtube.com/watch?v=iHyoilV8OI0)
[Link to Youtube Video](https://www.youtube.com/watch?v=iHyoilV8OI0)

# Using Dataset 2 to create Application # 

Next, I trained the ML model on a scene from a short film called "Bat Country". I extracted 4179 frames at 200x100px which seemed to be a manageable size while still outputting a cool result. This time I trained the model on 25 epochs, a batch size of 10 and the latent dim was 100.

![Bat Country Screenshot](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/frame1722.jpg)

I created the a video using the same song and same code as the first dataset, just to see if there were any significant differences. Below is a gif generated.

![gif](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/Images/gif_4.gif?raw=true)

Nothing particularly interesting happened so I moved on to working on an application which used pyaudio to extract live data from the computer's microphone. 

I wanted 2 specific things from my application: 

1. That the output was a video that reacted to live audio.
2. That the frames of the output had interpolation between them to make the transition seem smooth. 

For this I decided not to generate the images in real time, but to sort through the images, interpolate so that I could seamlessly blend them together. I randomly selected 600 images, then sorted them from lightest to darkest. Then I interpolated 4x between each images and saved them all in order.

Next, I used pyaudio in order to control which image is shown. The program takes the audio value, scales it, and then displays whichever image is indexed at that value! 

![app working](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/Screenshot%202023-06-14%20at%2011.04.52%20pm.png)

[Video Link](https://www.youtube.com/watch?v=iFEo42yb-hs)

I added a lag that stores 20 values in a queue and then averages them together in order to make the images give the impression of seamlessly blending together. I was really pleased with how reactive this was, and think that it could have cool applications in live performance.


# Help Writing Code # 

To write this code I used chatGPT to assist with the machine learning model and training/exporting it. The video and sound manipulation was done using some straightforward python libraries. 

These include:
[Librosa](https://pypi.org/project/librosa/)
[OpenCV](https://docs.opencv.org/4.x/d1/dfb/intro.html)
[NumPy](https://numpy.org/)
[Pillow](https://python-pillow.org/)
[Pandas](https://pandas.pydata.org/)
For the application I used
[Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)
[Kivy](https://kivy.org/)

The code I wrote using the help of [chatGPT](https://chat.openai.com/), sometimes asking it line-by-line how to do things. I had to break down this project into small and simple steps in order for ChatGPT to be useful.


