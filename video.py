def play_video(filename):
    try:
        with open(filename, "rb") as f:
            video_data = f.read()
        print("Відео відтворено (умовно):", filename)
    except FileNotFoundError:
        print("Файл відео не знайдено.")
