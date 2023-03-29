import pvcheetah
import pyaudio
import struct

cheetah = pvcheetah.create(access_key = "6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==")


CHUNK = cheetah.frame_length
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = cheetah.sample_rate

p = pyaudio.PyAudio()

stream = p.open(format =FORMAT,
                channels =CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


print("start recording..")
seconds = 3

while True:
#for i in range(0, int(RATE /CHUNK * seconds)):
    data = stream.read(CHUNK,exception_on_overflow = False)
    audio_frame = struct.unpack_from('h' * CHUNK,data)
    partial_transcript, is_endpoint = cheetah.process(audio_frame)
    print(is_endpoint)
    if is_endpoint:
        final_transcript = cheetah.flush()
        break

    
#final_transcript = cheetah.flush()
print(final_transcript)
stream.close()
p.terminate()


