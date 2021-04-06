import numpy as np
import glob, pyaudio, os
from time import sleep
from datetime import datetime
CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
result=[]
while True:
    result.clear()
    for video in glob.glob('*.dav'):
        print(video)
        os.system(f'start {video}')
        sleep(5)
        for i in range(int(10*3200/1024)):
            data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
            peak=np.average(np.abs(data))*2
            bars="#"*int(50*peak/2**16)
            result_two = len("%04d %05d %s"%(i,peak,bars))
            data = datetime.now().strftime('%H:%M:%S')
            cov = os.path.splitext(video)
            result.append(result_two)
            bath = cov[0]
            bath = str(bath)
        del(result[0:25])
        print(result)
        if 12 in result or 13 in result:
            pass
        else:
            with open("result.log", "a") as lg:
                lg.write(f' SEM AUDIO  - {bath.upper()} - {data}\n')
stream.stop_stream()
stream.close()
p.terminate()