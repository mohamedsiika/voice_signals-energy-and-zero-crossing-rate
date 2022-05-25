from recorder import recording
from fileread import read

# here to record a voice
def new_record():
    recorder=recording()
    recorder.start_recording()

def plotting_the_wave():
    file=read()
    print(file.E)
    file.plot_energy()
    file.plot_ZCR()






plotting_the_wave()
