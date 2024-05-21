import datetime
import time

class Music:
    def __init__(self, title, duration, artist, year):
        self.title = title
        self.duration = duration
        self.artist = artist
        self.year = year
        self.playing = False
        self.start_time = None
        self.time_played = 0
        self.end = False

    def play(self):
        if self.playing:
            print(f"Трек '{self.title}' уже воспроизводится.")
        else:
            print(f"Сейчас играет - '{self.title}'. Исполнитель: {self.artist} ({self.year}г.)")
            self.playing = True
            self.start_time = datetime.datetime.now()
        while self.time_played < self.duration:
            time.sleep(1)
            self.time_played += 1
            if not self.playing:
                break
        if self.time_played >= self.duration:
            print(f"Трек '{self.title}' завершен.")
            self.playing = False
            self.end = True
        else:
            print(f"Трек '{self.title}' на паузе.")

    def pause(self):
        if self.playing:
            if not self.end:
                print(f"Трек '{self.title}' на паузе.")
                self.playing = False
                self.time_played += (datetime.datetime.now() - self.start_time).seconds
            else:
                print(f"Трек '{self.title}' уже завершен.")
        else:
            print(f"Сейчас этот трек не играет.")

    def resume(self):
        if self.playing:
            print(f"Трек '{self.title}' уже воспроизводится.")
        else:
            if self.end:
                print(f"Трек '{self.title}' уже завершен.")
            else:
                print(f"Включаем трек '{self.title}'")
                self.playing = True
            self.start_time = datetime.datetime.now()
        while self.time_played < self.duration:
            time.sleep(1) # Имитируем секунду воспроизведения
            self.time_played += 1
            if not self.playing:
                break
            if self.time_played >= self.duration:
                print(f"Трек '{self.title}' завершен.")
                self.playing = False
                self.end = True
            else:
                print(f"Трек '{self.title}' на паузе.")

class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def play_all_tracks(self):
        print(f"Воспроизведение альбома '{self.title}' исполнителя {self.artist} ({self.year})...")
        for track in self.tracks:
            track.play()

# Пример использования:
track1 = Music("Violet", '3:38', "SEREBRO", 2024)
track2 = Music("Runaway baby 2", '2:28', "Bruno Mars", 2010)

album.add_track(track1)
album.add_track(track2)

# Воспроизведение всех треков альбома
album.play_all_tracks()

# Пауза и возобновление воспроизведения трека
track1.pause()
track1.resume()



