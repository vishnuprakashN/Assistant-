import pvporcupine
import pyaudio

porcupine = pvporcupine.create(
  access_key='6rUtqqqPW84yy+2ouTmCs5Wmfkmv1QIxDjUXzN8WUDR1b9MxUKhi3w==', keywords=['picovoice', 'bumblebee']
)

sample_rate = porcupine.frame_length
frame_length =  porcupine.sample_rate


print(sample_rate)
print(frame_length)

pa = pyaudio.PyAudio()

audio_stream = pa.open(
        rate=frame_length,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=sample_rate)
