import librosa
import numpy as np

def calculate_snr(signal_wav_with_noise, signal_wav_without_noise):
  """Calculates the SNR of the main voice with noise and the main voice without noise.

  Args:
    signal_wav_with_noise: The path to the main voice WAV file with noise.
    signal_wav_without_noise: The path to the main voice WAV file without noise.

  Returns:
    The SNR in decibels.
  """

  # Load the main voice WAV file with noise.
  signal_with_noise, sample_rate = librosa.load(signal_wav_with_noise)

  # Load the main voice WAV file without noise.
  signal_without_noise, sample_rate = librosa.load(signal_wav_without_noise)

  # Extract the signal from each WAV file.
  signal_with_noise_stft = librosa.core.stft(signal_with_noise)
  signal_without_noise_stft = librosa.core.stft(signal_without_noise)

  # Calculate the power of the signal and the noise in each WAV file.
  signal_with_noise_power = np.sum(signal_with_noise_stft ** 2)
  signal_without_noise_power = np.sum(signal_without_noise_stft ** 2)

  # Calculate the SNR in decibels.
  snr_db = 10 * np.log10(signal_without_noise_power / signal_with_noise_power)

  return snr_db

# Example usage:

# signal_wav_with_noise = "noiseyTestAudio.wav"
# signal_wav_without_noise = "noiseyTestAudio (enhanced).wav"

# snr_db = calculate_snr(signal_wav_with_noise, signal_wav_without_noise)

# print(snr_db)
