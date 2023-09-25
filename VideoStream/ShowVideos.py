import vlc
import os
import time

# VLC player 
player = vlc.MediaPlayer()

# Videos folder
video_folder = '/home/pi/Sherr/Videos'  

# Get videos
videos = [f for f in os.listdir(video_folder) if f.endswith(('.mov', '.mp4'))]

for video in videos:

  # Set media
  media = vlc.Media(os.path.join(video_folder, video))

  # Play video
  player.set_media(media)
  player.play()

 # Wait until it finishes
  time.sleep(0.5)
  length_milliseconds = player.get_length()
  length = length_milliseconds / 1000
  time.sleep(length)

  # Reset player
  player.stop()
