from moviepy.editor import VideoFileClip

def ExtraerAudio(video_path):
    
    video_clip = VideoFileClip(video_path)

    audio_clip = video_clip.audio

    audio_clip.write_audiofile("audio_its_my_life.mp3")

    video_clip.close()
    audio_clip.close()

ExtraerAudio(r"PONER_RUTA DONDE ESTA TU ARCHIVO")