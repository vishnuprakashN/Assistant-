import pvcheetah
import pvporcupine
import struct
import pyaudio

porcupine = pvporcupine.create(
        access_key = "6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==",
        keyword_paths=['/home/ubuntu/tommy_voice/hey_tommy.ppn']
                )

CHUNK = porcupine.frame_length
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = porcupine.sample_rate

cheetah = pvcheetah.create(access_key='6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==')

p = pyaudio.PyAudio()

stream = p.open(format =FORMAT,
                channels = CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("start recording")

frames = []

while True:
    data = stream.read(CHUNK,exception_on_overflow = False)
    audio_frame = struct.unpack_from('h' * CHUNK,data)
    keyword_index = porcupine.process(audio_frame)
    if keyword_index ==0:
        print("hey tommy")
        partial_transcript, is_endpoint = cheetah.process(audio_frame)
        if is_endpoint:
            final_transcript = cheetah.flush()
            print(final_transcript)

