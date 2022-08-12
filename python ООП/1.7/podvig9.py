class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        v = Video()
        cls.videos.append((video))

    @classmethod
    def play(cls, video_indx):
        Video.play(cls.videos[video_indx])


v1 = Video()
v2 = Video()
Video.create(v1, 'Python')
Video.create(v2, 'Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)