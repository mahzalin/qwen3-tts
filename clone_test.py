import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"

REFERENCE_AUDIO = "my_voice.wav"

# دقیقا متنی که در فایل صوتی Reference گفته شده است
REFERENCE_TEXT = """
Hello, my name is Niloofar.
I'm testing an AI voice cloning model.
"""

# متنی که می‌خواهید مدل با صدای Clone شده تولید کند
TEXT_TO_GENERATE = """
Welcome to Nil AI Labs.
This is a test of my cloned voice.
"""

print("Loading Qwen3-TTS model...")

model = Qwen3TTSModel.from_pretrained(
    MODEL_NAME,
    device_map="cpu",
    dtype=torch.float32,
)

print("Model loaded.")

print("Generating speech...")

wavs, sr = model.generate_voice_clone(
    text=TEXT_TO_GENERATE,
    language="English",
    ref_audio=REFERENCE_AUDIO,
    ref_text=REFERENCE_TEXT,
)

output_file = "output_voice_clone.wav"

sf.write(
    output_file,
    wavs[0],
    sr,
)

print(f"Done! Output saved to: {output_file}")
