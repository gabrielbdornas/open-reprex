import whisper
from pathlib import Path

path = Path(__file__).parent
audio_name = 'automate_web.mp4' # mudar nome do audio
transcript = path / 'transcript.txt'
audio = path / 'arquivos' / audio_name

# import ipdb; ipdb.set_trace(context=10)

model = whisper.load_model('small')
result = model.transcribe(str(audio),
                          language="pt",
                          fp16=False,
                          verbose=True,
                          patience=2,
                          beam_size=5,
                          )
print(result["text"])
# transcript.write_text(result["text"], encoding='utf-8')
