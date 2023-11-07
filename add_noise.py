from pydub import AudioSegment
from pydub.playback import play
# from google.colab import drive

# drive.mount('/content/drive/')


# Load the main voice and noise audio files
main_voice = AudioSegment.from_file("/content/drive/MyDrive/story_chain/Noise reduction/TestAudio.wav", format="wav")
noise = AudioSegment.from_file("/content/drive/MyDrive/story_chain/Noise reduction/Conversation Sound Effects.mp3", format="mp3")

# Ensure that both audio tracks have the same duration (adjust if necessary)
if len(main_voice) > len(noise):
    main_voice = main_voice[:len(noise)]
else:
    noise = noise[:len(main_voice)]

# Combine the main voice with the noise
combined_audio = main_voice.overlay(noise)

# Export the combined audio to a new file
combined_audio.export("noiseyTestAudio.wav", format="wav")