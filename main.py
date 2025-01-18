from moviepy import VideoFileClip, CompositeVideoClip, vfx, afx, concatenate_videoclips
import os

def add_fade_transition(list, output_path):

    videos = []

    for idx, file in enumerate(list):
        videos.append(VideoFileClip(file))
        videos[idx] = videos[idx].with_effects([vfx.FadeOut(0.25),afx.AudioFadeOut(0.25)])

    final_clip = concatenate_videoclips(videos)
    final_clip.write_videofile(output_path) 
    print(f"Output video saved to {output_path}")

list = [f for f in os.listdir(".") if f.endswith(".MP4")]

print(list)

add_fade_transition(list, "output.mp4")