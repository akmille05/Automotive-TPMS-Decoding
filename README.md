# Automotive TPMS Live Signal Processing

A Python-based Software Defined Radio (SDR) application that receives and processes live Tire Pressure Monitoring System (TPMS) transmissions using a HackRF One. The project captures RF signals in real time, analyzes them using digital signal processing (DSP) techniques, decodes TPMS packets, and displays vehicle sensor information.

---

## Overview

This project demonstrates the complete signal processing pipeline for decoding TPMS transmissions from automotive tire pressure sensors. Using a HackRF One connected to a Linux system, the application captures raw IQ samples, filters and demodulates the signal, detects TPMS packets, and extracts sensor data such as sensor IDs and tire pressure information.

This project is intended for educational and research purposes to demonstrate SDR concepts, RF signal analysis, and digital signal processing.

---

## Features

- Connects to a HackRF One on Linux
- Captures live RF IQ samples
- Tunes to configurable TPMS frequencies
- Performs Fast Fourier Transform (FFT) analysis
- Displays the live RF spectrum
- Applies digital filtering
  - Low-pass
  - High-pass
  - Band-pass
  - Band-stop
- Demodulates TPMS signals
- Detects TPMS packets
- Decodes TPMS message fields
- Displays decoded sensor information in real time
- Modular Python design for future protocol support

---

## Project Structure

```
.
├── tpms_decoding_simulation.py # Runs simulation of car frequencies for testing
├── signal.py               # Calls the HackRF and determines if signal is detected
├── dsp_demodulation.py     # Signal demodulation (AM and FM)
├── signal_processing.py    # Runs FFT and filters the data and makes display of data
├── decodesignal.py         # TPMS packet decoder
├── main.py                 # Main application
├── README.md
```

---

## Requirements

### Hardware

- HackRF One
- TPMS sensors (for testing)
- Linux computer

### Software

- Python 3.10+
- libhackrf
- python_hackrf
- NumPy
- SciPy
- Matplotlib

Install dependencies:

```bash
pip install numpy scipy matplotlib python_hackrf
```

Install HackRF utilities:

```bash
sudo apt install hackrf
```

---

## Signal Processing Pipeline

```
HackRF One
      │
      ▼
Capture IQ Samples
      │
      ▼
Fast Fourier Transform (FFT)
      │
      ▼
Spectrum Analysis
      │
      ▼
Digital Filtering
      │
      ▼
Signal Demodulation
      │
      ▼
Packet Detection
      │
      ▼
TPMS Packet Decoder
      │
      ▼
Decoded Tire Sensor Data
```

---

## Usage

Connect the HackRF One and run:

```bash
python signal.py
```

The application will:

1. Connect to the HackRF
2. Configure the desired center frequency
3. Capture live IQ samples
4. Display the frequency spectrum
5. Filter and demodulate the received signal
6. Detect TPMS packets
7. Decode and display sensor information

---

## Example Output

```
==========================================
 Automotive TPMS Live Signal Processor
==========================================

Center Frequency : 315.0 MHz
Sample Rate      : 10 MSPS

Receiving IQ Samples...

Packet Detected

Sensor ID : 4A91F203
Pressure  : 34 psi
Temperature : 29 °C
Battery Status : Good
```

---

## Signal Processing

### Fast Fourier Transform (FFT)

The FFT converts captured IQ samples from the time domain into the frequency domain, allowing the RF spectrum to be visualized and analyzed.

### Digital Filtering

Frequency-domain filters isolate the desired TPMS transmission while reducing unwanted signals and noise.

Supported filters include:

- Low-pass
- High-pass
- Band-pass
- Band-stop

### Demodulation

The filtered RF signal is demodulated to recover the digital bitstream transmitted by the TPMS sensor.

### Packet Decoding

The decoded bitstream is parsed according to the TPMS protocol to extract useful information, such as:

- Sensor ID
- Tire pressure
- Temperature
- Battery status
- Checksum/CRC validation (if implemented)

---

## Future Improvements

- Live waterfall display
- Automatic TPMS frequency detection
- Support for multiple TPMS protocols
- Real-time packet logging
- CSV export of decoded data
- Graphical user interface (GUI)
- Vehicle sensor history
- Automatic CRC validation
- Multiple SDR support

---
