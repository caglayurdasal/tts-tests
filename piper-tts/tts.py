# pip install piper-tts (version 1.2.0 is used in tests)
# pip install setuptools wheel tts -U
# pip install pip setuptools wheel -U
import wave
from piper.voice import PiperVoice

model = "/home/wasp/Dev/tts-tests/piper-tts/voices_DE/thorsten-emotional/de_DE-thorsten_emotional-medium.onnx"
# model= "/home/wasp/Dev/tts-tests/piper-tts/voices_DE/thorsten-high/de_DE-thorsten-high.onnx"
# model = "/home/wasp/Dev/tts-tests/piper-tts/voices_DE/thorsten-medium/de_DE-thorsten-medium.onnx"
# model = "/home/wasp/Dev/tts-tests/piper-tts/voices_DE/eva/de_DE-eva_k-x_low.onnx"
# model = "/home/wasp/Dev/tts-tests/piper-tts/voices_DE/kerstin/de_DE-kerstin-low.onnx"
# model = "/home/wasp/Dev/tts-tests/piper-tts/voices_DE/ramona/de_DE-ramona-low.onnx"

voice = PiperVoice.load(model)
text = 'Die Augen der 56 Triathletinnen waren gebannt auf die Seine gerichtet. Zwischen dem Grand Palais und dem Invalidendom warteten die Athletinnen am Pont Alexandre III auf den Startschuss. "On your marks", auf die Plätze, schallte es aus den Lautsprechern am Rande des französischen Flusses, der tagelang für Diskussionen gesorgt hatte. Pünktlich mit dem Startsignal sprangen dann alle Athletinnen ins Wasser - die Triathlon-Wettbewerbe der Frauen bei den Olympischen Spielen in Paris konnten dank einer verbesserten Wasserqualität der Seine beginnen.'

wav_file = wave.open("thorsten-emotional.wav", "w")
# wav_file = wave.open("thorsten-high.wav", "w")
# wav_file = wave.open("thorsten-medium.wav", "w")
# wav_file = wave.open("eva-low.wav", "w")
# wav_file = wave.open("kerstin-low.wav", "w")
# wav_file = wave.open("ramona-low.wav", "w")


audio = voice.synthesize(text, wav_file)
