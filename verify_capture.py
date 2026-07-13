#Verifies that the save_iq file correctly saves the IQ data to a .raw file

import numpy as np

#open file
filename = "captures/capture_315MHz_20260713_095238.raw"

#read file
raw_samples = np.fromfile(filename, dtype=np.int8)

#prints only the first 20 values so it doesn't go on forever
print(raw_samples[:20])

#how many bytes are in the file (should be around 4,300,00)
print(len(raw_samples))

#separate I and Q
i_samples = raw_samples[0::2]
q_samples = raw_samples[1::2]

#build copmplex IQ samples
iq = i_samples.astype(np.float32) + 1j * q_samples.astype(np.float32)
print(iq[:10])