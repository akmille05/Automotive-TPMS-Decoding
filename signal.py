# Gets the signal
# capture the burst
# save burst to file 
from python_hackrf import pyhackrf
import numpy as np
import time

CENTER_FREQ = 315_000_000
SAMPLE_RATE = 2_000_000

LNA_GAIN = 32
VGA_GAIN = 20

def rx_callback(device, buffer, buffer_length, valid_length):
    raw_bytes = bytes(buffer[:valid_length])

    samples = np.frombuffer(raw_bytes, dtype=np.int8)

    i_samples = samples[0::2] #collects I values
    q_samples = samples[1::2] #collects Q values

    iq = i_samples.astype(np.float32) + 1j * q_samples.astype(np.float32) #combines them into complex IQ samples

    amplitude = np.mean(np.abs(iq)) #collects strength of each signal and averages them to get the overall amplitude of the signal

    print("Amplitude:", amplitude)

    return 0 #tells the hackrf to keep recieving

def main():
    pyhackrf.pyhackrf_init()

    sdr = pyhackrf.pyhackrf_open()

    sdr.pyhackrf_set_freq(CENTER_FREQ)
    sdr.pyhackrf_set_sample_rate(SAMPLE_RATE)

    sdr.pyhackrf_set_lna_gain(LNA_GAIN)
    sdr.pyhackrf_set_vga_gain(VGA_GAIN)
    sdr.pyhackrf_set_amp_enable(False)

    sdr.set_rx_callback(rx_callback)

    sdr.pyhackrf_start_rx()

    try:
        while sdr.pyhackrf_is_streaming():
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Stopped by user.")

    finally:
        sdr.pyhackrf_stop_rx()
        sdr.pyhackrf_close()
        pyhackrf.pyhackrf_exit()

if __name__ == "__main__":
    main()