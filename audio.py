def process_audio(filename):
    try:
        with open(filename, "rb") as f:
            audio_data = f.read()
        print("Аудіо оброблено (умовно):", filename)
    except Exception as e:
        print("Виникла помилка при обробці аудіо:", e)
