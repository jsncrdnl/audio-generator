from gtts import gTTS
from pydub import AudioSegment
import os
import re

# Input text file containing one sentence per line
INPUT_FILE = "input.txt"
OUTPUT_FOLDER = "audios"

# Ensure output directory exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Function to clean filenames (remove invalid characters for Windows)
def sanitize_filename(text):
    return re.sub(r'[<>:"/\\|?*]', '_', text)[:100]  # Limit filename length

# Read sentences from the input file
try:
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        texts = [line.strip() for line in file if line.strip()]  # Remove empty lines
except FileNotFoundError:
    print(f"❌ Error: File '{INPUT_FILE}' not found!")
    exit(1)

# Process each sentence
for index, text in enumerate(texts):
    print(f"🔹 Generating audio {index + 1}: {text}")

    # Sanitize filename
    safe_filename = sanitize_filename(text) + ".mp3"
    output_file = os.path.join(OUTPUT_FOLDER, f'{index}_{safe_filename}')

    # Convert text to speech
    tts = gTTS(text, lang="fr")
    temp_file = os.path.join(OUTPUT_FOLDER, f"temp_{index}.mp3")
    tts.save(temp_file)

    # Add 1s silence
    voice = AudioSegment.from_mp3(temp_file)
    silence = AudioSegment.silent(duration=1000)
    final_audio = silence + voice

    # Save final audio file
    final_audio.export(output_file, format="mp3")

    # Remove temporary file
    os.remove(temp_file)

print("✅ All audio files have been generated successfully!")
