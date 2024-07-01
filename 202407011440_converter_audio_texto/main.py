import whisper
from pathlib import Path

path = Path(__file__).parent
audio_name = 'audio.mp3' # mudar nome do audio
transcript = path / 'transcript.txt'
audio = path / 'arquivos' / audio_name

model = whisper.load_model('small')
result = model.transcribe(audio,
                          language="pt",
                          fp16=False,
                          verbose=True,
                          patience=2,
                          beam_size=5,
                          )
print(result["text"])
transcript.write_text(result["text"], encoding='utf-8')
