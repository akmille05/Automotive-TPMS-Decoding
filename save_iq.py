import os
import time
import numpy as np


def save_raw_iq(raw_buffers, folder="captures"):
    """
    Save raw HackRF IQ bytes into a .raw file.

    raw_buffers:
        A list containing byte buffers collected by the callback.

    folder:
        The directory where captures will be stored.
    """

    # Create the captures folder if it does not already exist.
    os.makedirs(folder, exist_ok=True)

    # Use the current time so every capture has a different filename.
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        folder,
        f"capture_315MHz_{timestamp}.raw"
    )

    # Open the file in binary write mode.
    with open(filename, "wb") as file:
        # Write each captured buffer in the order it arrived.
        for raw_buffer in raw_buffers:
            file.write(raw_buffer)

    print(f"Saved IQ capture: {filename}")

    # Return the filename in case another file needs it.
    return filename