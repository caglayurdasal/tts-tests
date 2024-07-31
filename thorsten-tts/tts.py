from TTS.api import TTS


tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC")

tts.tts_to_file(text="Hallo! Ich heiße Amica. Ich bin ein Robot.", file_path="thorsten-tacotron2-DDC_1.wav")
tts.tts_to_file(text="Ich habe heute im Internet nach einer guten Text-to-Speech-Lösung gesucht.", file_path="thorsten-tacotron2-DDC_2.wav")

# some errors/warnings
# raise Exception(" [!] No espeak backend found. Install espeak-ng or espeak to your system.")
#   > sudo apt-get install espeak
