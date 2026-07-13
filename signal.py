# Gets the signal
# capture the burst
# save burst to file 
from python_hackrf import pyhackrf
import numpy as np
import time
from save_iq import save_raw_iq

CENTER_FREQ = 315_000_000
SAMPLE_RATE = 2_000_000

LNA_GAIN = 32
VGA_GAIN = 20

noise_floor = None
triggered = False

SAVE_SECONDS = 1.0

captured_buffers = []
capture_start_time = None


def rx_callback(device, buffer, buffer_length, valid_length):
    raw_bytes = bytes(buffer[:valid_length])

    samples = np.frombuffer(raw_bytes, dtype=np.int8)

    i_samples = samples[0::2] #collects I values
    q_samples = samples[1::2] #collects Q values

    iq = i_samples.astype(np.float32) + 1j * q_samples.astype(np.float32) #combines them into complex IQ samples

    amplitude = np.mean(np.abs(iq)) #collects strength of each signal and averages them to get the overall amplitude of the signal

    global noise_floor
    global triggered

    global triggered, captured_buffers, capture_start_time

    if noise_floor is None:
        noise_floor = amplitude

    noise_floor = 0.99 * noise_floor + 0.01 * amplitude
    threshold = noise_floor * 3

    print("Amplitude:", amplitude, "Noise Floor:", noise_floor)

    if amplitude > threshold and not triggered: #checks for large jump in amplitude (signal strength)
        triggered = True
        capture_start_time = time.time()
        captured_buffers = [raw_bytes]
        print("\n" + "=" * 50)
        print("🚨 SIGNAL DETECTED! 🚨")
        print("=" * 50 + "\n")
    
    elif triggered:
        captured_buffers.append(raw_bytes)

        if time.time() - capture_start_time >= SAVE_SECONDS:
            save_raw_iq(captured_buffers)
            return -1

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