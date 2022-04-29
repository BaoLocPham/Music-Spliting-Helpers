import os
from pydub import *

def split_song_to_sequences(file_path,in_dir="./full_songs/", out_dir="./sequences/", chunk_length=10):
    song = AudioSegment.from_mp3(os.path.join(in_dir,file_path))
    file_name = file_path.split(".mp3")[0]
    # pydub does things in milliseconds
    chunk_length_in_milliseconds = chunk_length * 1000
    second = 1000
    print(f"{file_path} is {song.duration_seconds} seconds long")

    for i in range(0, int(song.duration_seconds)//chunk_length):
        song_sequence = song[(i*10)*second:(i*10)*second+chunk_length_in_milliseconds]

        song_sequence = song_sequence.fade_in(2000).fade_out(2000)

        export_sequence(song_sequence, f"{out_dir}/{file_name}_{i}_s.mp3")

def export_sequence(song_sequence, file_name, format="mp3"):
    song_sequence.export(file_name, format=format)