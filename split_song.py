import os
from helpers import split_song_to_sequences

if __name__ == '__main__':
    # Load the song
    filenames = next(os.walk("./full_songs/"))[2]

    for filename in filenames:
        split_song_to_sequences(filename, out_dir="./sequences/", chunk_length=10)

    # # Save the chunks
    # for i, chunk in enumerate(chunks):
    #     chunk.export("chunk{0}.mp3".format(i), format="mp3")