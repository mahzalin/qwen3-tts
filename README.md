# 🎙️ Qwen3-TTS Voice Cloning

یک پروژه ساده و کاربردی برای **Clone کردن صدای خودتان با استفاده از Qwen3-TTS**.

در این پروژه یاد می‌گیرید چطور یک نمونه از صدای خودتان را به مدل بدهید، سپس یک متن جدید وارد کنید و یک فایل صوتی جدید با صدایی مشابه صدای نمونه تولید کنید.

> 🎥 این پروژه همراه با آموزش ویدئویی در کانال **Nil AI Labs** ساخته شده است.
لینک کانال:
https://youtube.com/@nilailabs
---

## ✨ این پروژه چه کاری انجام می‌دهد؟

روند کار به این صورت است:

```text
🎙️ صدای شما
      +
📝 متن همان صدای ضبط‌شده
      ↓
🤖 Qwen3-TTS
      +
📝 متن جدید
      ↓
🔊 صدای تولیدشده
```

برای مثال، فرض کنید فایل صوتی شما این جمله را دارد:

> Hello, my name is Niloofar. I'm testing an AI voice cloning model.

حالا می‌توانید یک متن کاملاً جدید مثل:

> Welcome to Nil AI Labs. This is a test of my cloned voice.

به مدل بدهید و Qwen3-TTS آن را با صدایی مشابه نمونه صوتی تولید کند.

---

## 📌 Features

* 🎙️ Voice Cloning
* 📝 تبدیل متن جدید به گفتار
* 💻 اجرای محلی روی سیستم
* 🔊 تولید فایل صوتی WAV
* 🤖 استفاده از Qwen3-TTS
* 🆓 بدون نیاز به سرویس آنلاین برای اجرای مدل
* 📦 نصب و اجرای ساده با `uv`

---

# 🛠️ Requirements

برای اجرای این پروژه به موارد زیر نیاز دارید:

* Python 3.11
* `uv`
* Qwen3-TTS
* یک فایل صوتی از صدای خودتان
* اتصال اینترنت برای دانلود اولیه مدل
* فضای کافی برای فایل‌های مدل

> ⚠️ اولین اجرای مدل ممکن است به دلیل دانلود فایل‌های مدل زمان ببرد.

---

# 💻 سیستم‌عامل

مراحل این README بر اساس اجرای پروژه روی **macOS / Linux** نوشته شده‌اند.

اگر از Windows استفاده می‌کنید، بعضی از دستورات مربوط به فعال‌سازی محیط مجازی ممکن است متفاوت باشند.

---

# 📁 Project Structure

ساختار پروژه به صورت زیر است:

```text
qwen3-tts-voice-cloning/
│
├── .venv/
├── clone_test.py
├── README.md
└── my_voice.wav
```

### توضیح فایل‌ها

* `clone_test.py` — کد اصلی Voice Cloning
* `README.md` — راهنمای نصب و استفاده
* `my_voice.wav` — نمونه صدای کاربر
* `.venv/` — محیط مجازی Python

> ⚠️ فایل صوتی شخصی خودتان را در یک Repository عمومی GitHub قرار ندهید.

---

# 🚀 Installation

## 1. نصب uv

اگر از macOS و Homebrew استفاده می‌کنید، ابتدا `uv` را نصب کنید:

```bash
brew install uv
```

برای بررسی نصب:

```bash
uv --version
```

اگر نسخه `uv` نمایش داده شد، نصب با موفقیت انجام شده است.

---

## 2. نصب Python 3.11

برای نصب Python 3.11 با استفاده از `uv`:

```bash
uv python install 3.11
```

---

## 3. ساخت Virtual Environment

ابتدا وارد پوشه پروژه شوید:

```bash
cd qwen3-tts-voice-cloning
```

سپس یک محیط مجازی با Python 3.11 ایجاد کنید:

```bash
uv venv .venv --python 3.11
```

---

## 4. فعال کردن Virtual Environment

در macOS / Linux:

```bash
source .venv/bin/activate
```

بعد نسخه Python را بررسی کنید:

```bash
python --version
```

باید چیزی شبیه این مشاهده کنید:

```text
Python 3.11.x
```

---

# 📦 نصب Qwen3-TTS

حالا Qwen3-TTS را نصب کنید:

```bash
uv pip install -U qwen-tts
```

بعد از نصب، می‌توانید با دستور زیر بررسی کنید که پکیج به درستی نصب شده است:

```bash
python -c "import qwen_tts; print('Qwen3-TTS is working!')"
```

اگر پیام زیر نمایش داده شد:

```text
Qwen3-TTS is working!
```

یعنی نصب با موفقیت انجام شده است.

---

# 🎙️ آماده کردن Voice Sample

برای Voice Cloning به یک فایل صوتی از صدای خودتان نیاز دارید.

برای گرفتن نتیجه بهتر، پیشنهاد می‌شود فایل صوتی:

* صدای واضح داشته باشد.
* تا حد امکان نویز پس‌زمینه نداشته باشد.
* موسیقی پس‌زمینه نداشته باشد.
* Echo یا Reverb شدید نداشته باشد.
* فقط شامل صدای یک نفر باشد.
* با صدای طبیعی و واضح ضبط شده باشد.

فرمت پیشنهادی:

```text
WAV
```

برای مثال:

```text
my_voice.wav
```

فایل صوتی را در همان پوشه‌ای قرار دهید که `clone_test.py` قرار دارد.

---

# 📝 Reference Text چیست؟

علاوه بر فایل صوتی، باید متن چیزی که داخل فایل صوتی گفته‌اید را نیز در اختیار مدل قرار دهید.

برای مثال، اگر داخل `my_voice.wav` گفته‌اید:

```text
Hello, my name is Niloofar.
I'm testing an AI voice cloning model.
```

همین متن باید به عنوان `REFERENCE_TEXT` وارد شود.

> ⚠️ متن Reference باید با محتوای فایل صوتی مطابقت داشته باشد.

---

# 🧠 اجرای Voice Cloning

فایل زیر را باز کنید:

```text
clone_test.py
```

در این فایل سه بخش اصلی را باید متناسب با فایل و متن خودتان تغییر دهید.

---

## 1. فایل صوتی Reference

نام فایل صوتی خودتان را وارد کنید:

```python
REFERENCE_AUDIO = "my_voice.wav"
```

اگر نام فایل شما مثلاً `voice_sample.wav` است:

```python
REFERENCE_AUDIO = "voice_sample.wav"
```

---

## 2. متن Reference

متنی که دقیقاً در فایل صوتی گفته‌اید را وارد کنید:

```python
REFERENCE_TEXT = """
Hello, my name is Niloofar.
I'm testing an AI voice cloning model.
"""
```

---

## 3. متن جدید

حالا متنی را که می‌خواهید مدل با صدای Clone شده تولید کند، در `TEXT_TO_GENERATE` قرار دهید:

```python
TEXT_TO_GENERATE = """
Welcome to Nil AI Labs.
This is a test of my cloned voice.
"""
```

این متن لازم نیست همان متنی باشد که در فایل صوتی اولیه گفته‌اید.

---

# ▶️ اجرای پروژه

بعد از فعال کردن محیط مجازی و آماده کردن فایل صوتی، دستور زیر را اجرا کنید:

```bash
python clone_test.py
```

در اولین اجرا، مدل Qwen3-TTS دانلود و بارگذاری می‌شود.

ممکن است این مرحله نسبت به اجراهای بعدی زمان بیشتری ببرد.

---

# 🔊 Output

اگر اجرای برنامه با موفقیت انجام شود، فایل زیر ساخته خواهد شد:

```text
output_voice_clone.wav
```

این فایل، صدای تولیدشده توسط مدل است.

می‌توانید آن را با هر نرم‌افزار پخش فایل صوتی باز کنید.

---

# 🔄 تولید متن جدید

بعد از اینکه یک بار Voice Cloning را اجرا کردید، برای تولید جمله جدید نیازی نیست فایل صوتی Reference را دوباره ضبط کنید.

فقط مقدار زیر را تغییر دهید:

```python
TEXT_TO_GENERATE
```

برای مثال:

```python
TEXT_TO_GENERATE = """
Artificial intelligence is changing the way we create content.
"""
```

سپس دوباره اجرا کنید:

```bash
python clone_test.py
```

و فایل صوتی جدید تولید خواهد شد.

---

# 🧩 کد کامل

کد اصلی پروژه در فایل `clone_test.py` قرار دارد:

```python
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
```

---

# ⚠️ نکات مهم برای کیفیت بهتر

کیفیت Voice Cloning فقط به مدل بستگی ندارد. کیفیت فایل Reference نیز اهمیت زیادی دارد.

برای نتیجه بهتر:

### 🎙️ صدای تمیز

از یک recording واضح و با نویز کم استفاده کنید.

### 🔇 بدون موسیقی

موسیقی یا صدای پس‌زمینه می‌تواند روی نتیجه تأثیر بگذارد.

### 🗣️ یک گوینده

فایل Reference بهتر است فقط شامل صدای یک نفر باشد.

### 📝 متن صحیح

`REFERENCE_TEXT` باید با چیزی که در فایل صوتی گفته شده مطابقت داشته باشد.

### 🔊 صدای طبیعی

نمونه صوتی را با لحن طبیعی و بدون تغییرات شدید در صدا ضبط کنید.

---

# 🐛 Troubleshooting

## Python نسخه اشتباه را نشان می‌دهد

ابتدا Virtual Environment را فعال کنید:

```bash
source .venv/bin/activate
```

سپس:

```bash
python --version
```

مطمئن شوید Python 3.11 استفاده می‌شود.

---

## فایل صوتی پیدا نمی‌شود

بررسی کنید نام فایل در کد دقیقاً با فایل موجود در پوشه یکسان باشد:

```python
REFERENCE_AUDIO = "my_voice.wav"
```

همچنین مطمئن شوید فایل صوتی در همان پوشه `clone_test.py` قرار دارد.

---

## کیفیت خروجی مناسب نیست

موارد زیر را بررسی کنید:

* کیفیت فایل Reference
* وجود نویز
* وجود Echo یا Reverb
* وجود موسیقی پس‌زمینه
* واضح بودن صدای گوینده
* درست بودن `REFERENCE_TEXT`

---

## اجرای اول طولانی است

در اولین اجرا، فایل‌های مدل باید دانلود شوند و مدل روی سیستم بارگذاری شود.

بنابراین اجرای اول ممکن است نسبت به اجراهای بعدی زمان بیشتری نیاز داشته باشد.

---

## هشدار مربوط به `flash-attn`

ممکن است هنگام اجرای مدل هشداری مشابه زیر مشاهده کنید:

```text
Warning: flash-attn is not installed.
```

این پیام به معنی خراب بودن نصب Qwen3-TTS نیست.

در این پروژه از مسیر معمول PyTorch استفاده می‌شود و نبودن `flash-attn` لزوماً مانع اجرای مدل نمی‌شود.

---

# 🔐 استفاده مسئولانه

از Voice Cloning برای صدای خودتان یا صدایی که اجازه استفاده از آن را دارید استفاده کنید.

از این فناوری برای جعل هویت، فریب افراد، جعل صدای دیگران یا تولید محتوای گمراه‌کننده با صدای افراد بدون رضایت آن‌ها استفاده نکنید.

---

# 🎥 آموزش ویدئویی

اگر می‌خواهید تمام مراحل را به صورت تصویری و قدم‌به‌قدم ببینید، آموزش کامل این پروژه را در کانال YouTube من مشاهده کنید:

## Nil AI Labs

در این آموزش از نصب محیط Python تا تولید اولین فایل صوتی Clone شده، تمام مراحل به صورت عملی انجام می‌شود.

🔗 **YouTube Tutorial:**
`YOUR_YOUTUBE_VIDEO_LINK`

---

# 📚 تکنولوژی‌های استفاده‌شده

* [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)
* [PyTorch](https://pytorch.org/)
* Python
* uv
* SoundFile

---

# ⭐ Support

اگر این پروژه برایتان مفید بود، می‌توانید Repository را ⭐ **Star** کنید.

برای آموزش مدل‌ها و ابزارهای جدید هوش مصنوعی و یادگیری نحوه استفاده عملی از آن‌ها، کانال **Nil AI Labs** را دنبال کنید.

---

## 📄 License

این Repository شامل کد آموزشی این پروژه است.

لطفاً برای استفاده از خود مدل Qwen3-TTS، شرایط و مجوز مدل را در منابع رسمی Qwen بررسی کنید.
