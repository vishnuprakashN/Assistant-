import pyaudio
import pvporcupine
import struct

porcupine = pvporcupine.create(
        access_key = "6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==",
        keyword_paths=['hey_tommy.ppn']
                )

def get_next_audio_frame():
    py_audio = pyaudio.PyAudio()

    audio_stream = py_audio.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    pcm = audio_stream.read(porcupine.frame_length)
    audio_frame = struct.unpack_from("h" * porcupine.frame_length, pcm)
    return audio_frame

 

while True:
    audio_frame = get_next_audio_frame()
    keyword_index = porcupine.process(audio_frame)
    if keyword_index == 0:
        print("hey tommy")
    










