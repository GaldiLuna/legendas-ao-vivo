import cv2
import moviepy as mp
import speech_recognition as sr
from pydub import AudioSegment
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os

# Função para extrair áudio do vídeo
def extrair_audio(video_path, audio_path="audio.wav"):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

# Função para transcrever o áudio em pedaços
def transcrever_audio(audio_path, chunk_duration=5000):
    audio = AudioSegment.from_wav(audio_path)
    recognizer = sr.Recognizer()
    transcricoes = []

    for i in range(0, len(audio), chunk_duration):
        chunk = audio[i:i+chunk_duration]
        chunk.export("temp.wav", format="wav")

        with sr.AudioFile("temp.wav") as source:
            audio_data = recognizer.record(source)
            try:
                texto = recognizer.recognize_google(audio_data, language='pt-BR')
            except sr.UnknownValueError:
                texto = ""
        transcricoes.append(texto)
    os.remove("temp.wav")
    return transcricoes

# Função para mostrar o vídeo com legendas (UTF-8 suportado)
def reproduzir_video_com_legenda(video_path, legendas):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    legenda_idx = 0
    chunk_frames = int(fps * 5)  # 5 segundos de legenda

    frame_count = 0

    # Carregar fonte compatível com UTF-8 (ajuste o caminho se necessário)
    fonte = ImageFont.truetype("arial.ttf", 32)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if legenda_idx < len(legendas):
            legenda = legendas[legenda_idx]

            # Converter frame para Pillow
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(frame_pil)
            draw.text((50, 450), legenda, font=fonte, fill=(255, 255, 255))

            # Voltar para OpenCV
            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

        cv2.imshow("Vídeo com Legenda", frame)

        if frame_count % chunk_frames == 0 and frame_count != 0:
            legenda_idx += 1

        frame_count += 1

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Função principal
def legenda_automatica(video_path):
    print("Extraindo áudio...")
    audio_path = extrair_audio(video_path)

    print("Transcrevendo áudio...")
    legendas = transcrever_audio(audio_path)

    print("Reproduzindo vídeo com legendas...")
    reproduzir_video_com_legenda(video_path, legendas)

# Exemplo de uso
if __name__ == "__main__":
    video_entrada = "exemplo_video.mp4"  # substitua pelo seu vídeo
    legenda_automatica(video_entrada)
