import cv2
import numpy as np
import random

def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image


frame_size = (3840, 2160)
frame_rate = 25

video = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, frame_size)


white_frame = create_blank(frame_size[0], frame_size[1], rgb_color=(255, 255, 255))
black_frame = create_blank(frame_size[0], frame_size[1], rgb_color=(0, 0, 0))


frame_conf = {
              "white":{
                        "count_min":0.5,
                        "count_max":3,
                        "frame":white_frame
                        },
              "black":{
                        "count_min":0.5,
                        "count_max":5,
                        "frame":black_frame
                        },
              }




number_of_frames = 500
current_frame = 0
frames_from_swich = 0
current_colour = "white"

while number_of_frames > current_frame:

    frame = frame_conf[current_colour]

    count = random.randint(int(frame["count_min"]), int(frame["count_max"]))

    if count < frames_from_swich:

        if current_colour == "white":
            current_colour = "black"
        else:
            current_colour = "white"

        frames_from_swich = 0

    video.write(frame["frame"])



    frames_from_swich += 1
    current_frame += 1
    print(current_frame, current_colour, frames_from_swich)


video.release()

print("done")

