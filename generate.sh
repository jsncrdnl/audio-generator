mkdir audios
docker build -t tts-generator .
docker run --rm -v./audios:/app/audios -v ./input.txt:/app/input.txt tts-generator