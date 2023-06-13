# Final Project: #
### VAE Machine Learning model to combine and relate video and audio ###

This is the Coding 3 Final Project Submission for my MsC in creative computing at UAL.

For my project I created a VAE model in order to do unsupervised machine learning. My idea is to train the model on each frame of a short film, then create a new video that is controlled by a song.

The code with in-depth descriptions is linked below: 

[Part 1](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/Images/Coding3-MaeHorak-WFM-Part1.ipynb)
[Part 2](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/main/Coding3-MaeHorak-WFM-Part2.ipynb)

![WFM screenshot](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/frame_3712.png)

The dataset I used for this ML model was over 5k images that were frames from a short film from my company [Off Hand Co](https://www.offhandco.com/) called "Works for Me".

Once the dataset was trained, I exported the decoder for further use.

I experimented with generating random latent vectors and was able to successfully produce images. The below image is produced with a randomised latent vector.

![random latent vector generation](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/image_6870.png)

Then I uploaded a song I've recorded and used the python librosa library to find values of amplitude (loudness) of the music. Because librosa gives the amplitude 22,050x a second, I saved every 735th value so I would have 30 per second. [Then I exported these amplitude values into a csv file.](https://github.com/mkh7878/VAE_MLforCombiningVideoAndAudio/blob/Images/updated_amplitude.csv) Below is a graph of the amplitude throughout the song using the 30 values per second.

![graph](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/download%20(1).png)

Now I used the values from the CSV file to feed into the decoder. The idea was basically to see what the ML model "decided" was important and the patterns it found in the images, and then to use the values (scaled to the range of latent vector) to generate new images which I would make into a new video. I hoped that the images would change as the song gets louder, and that certainly did seem to happen in some ways. I want to use a different dataset of a different film I made and adjust the settings to see what results I get.

[![video link](https://raw.githubusercontent.com/mkh7878/VAE_MLforCombiningVideoAndAudio/Images/Screenshot%202023-06-13%20at%2011.48.30%20am.png)](https://www.youtube.com/watch?v=iHyoilV8OI0)
[Link to Youtube Video](https://www.youtube.com/watch?v=iHyoilV8OI0)

To write this code I used chatGPT to assist with the machine learning model and training/exporting it. The video and sound manipulation was done using some straightforward python libraries. 

These include:
[Librosa](https://pypi.org/project/librosa/)
[OpenCV](https://docs.opencv.org/4.x/d1/dfb/intro.html)
[NumPy](https://numpy.org/)
[Pillow](https://python-pillow.org/)
[Pandas](https://pandas.pydata.org/)

The code I wrote using the help of chatGPT, sometimes asking it line-by-line how to do things. I had to break down this project into small and simple steps in order for ChatGPT to be useful.


