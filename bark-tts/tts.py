from bark import SAMPLE_RATE, generate_audio, preload_models
import scipy

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
    Ich habe heute im Internet nach einer guten Text-to-Speech-Lösung gesucht.
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
scipy.io.wavfile.write("bark_out.wav", rate=SAMPLE_RATE, data=audio_array)