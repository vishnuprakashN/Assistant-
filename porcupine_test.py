#! /usr/bin/env python3
import struct
import pyaudio
import pvporcupine

porcupine = None
pa = None
audio_stream = None

try:
    porcupine = pvporcupine.create(
            access_key='6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==', 
            keywords=['picovoice', 'blueberry'])

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
                    rate=16000,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=512)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Hotword Detected")
finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
            pa.terminate()
