import vlc
import time
import os

# Create VLC player
player = vlc.MediaPlayer()

# Image folder
image_folder = '/home/pi/Sherr/Images'  

# Get images
images = [f for f in os.listdir(image_folder) if f.endswith(('.jpg','.jpeg','.png'))]

for image in images:

  # Set media
  media = vlc.Media(os.path.join(image_folder, image))

  # Play media
  player.set_media(media)
  player.toggle_fullscreen()

  player.play()

  # Wait before next
  time.sleep(5) 

  # Reset player
  player.stop()
