import os
import sys
import wave
import numpy
import pygame
import ffmpeg
from pygame.locals import *
from scipy.fftpack import dct


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS or _MEIPASS2
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class AudioVisualizer:
    def __init__(self):
        self.NUMBER = 30
        self.HEIGHT = 600
        self.WIDTH = 40
        self.FPS = 10
        self.file_name = None
        self.status = '< Drop Audio File Here >'
        self.fpsclock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.NUMBER * self.WIDTH, 50 + self.HEIGHT])
        icon = pygame.image.load(resource_path('logo.png'))
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Musync')
        self.my_font = pygame.font.SysFont('Times', 18)
        self.num = None
        self.wave_data = None
        self.framerate = None
        self.nframes = None
        self.total_playtime = 0


    def load_and_convert_audio(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            ffmpeg.input(self.file_name).output('output.wav').overwrite_output().run()
        except Exception as e:
            print(f"Error Converting Audio File: {e}")
            sys.exit(1)


    def play_audio(self):
        try:
            pygame.mixer.music.load(resource_path("output.wav"))
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent()
            pygame.mixer.music.set_volume(10)
            self.status = "playing"
        except pygame.error as e:
            print(f"Error Loading Audio File: {e}")
            sys.exit(1)


    def read_audio_file(self):
        try:
            f = wave.open("output.wav", 'rb')
            params = f.getparams()
            nchannels, sampwidth, self.framerate, self.nframes = params[:4]
            str_data = f.readframes(self.nframes)
            f.close()
            wave_data = numpy.fromstring(str_data, dtype=numpy.short)
            wave_data.shape = -1, 2
            self.wave_data = wave_data.T
            self.num = self.nframes
        except wave.Error as e:
            print(f"Error Reading Audio File: {e}")
            sys.exit(1)


    def Visualizer(self, nums):
        num = int(nums)
        h = abs(dct(self.wave_data[0][self.nframes - num:self.nframes - num + self.NUMBER]))
        h = [min(self.HEIGHT, int(i ** (1 / 2.5) * self.HEIGHT / 100)) for i in h]
        self.draw_bars(h)


    def vis(self):
        if self.status == "stopped":
            self.num = self.nframes
            return
        elif self.status == "paused":
            self.Visualizer(self.num)
        else:
            if self.framerate is not None:
                self.num -= self.framerate / self.FPS
                if self.num > 0:
                    self.Visualizer(self.num)


    def get_time(self):
        seconds = max(0, self.total_playtime + pygame.mixer.music.get_pos() / 1000)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        hms = ("%02d:%02d:%02d" % (h, m, s))
        return hms
    

    def controller(self, key):
        print(key)
        if self.status == "stopped":
            if key == K_RETURN:
                pygame.mixer_music.play()
                self.status = "playing"
        elif self.status == "paused":
            if key == K_RETURN:
                pygame.mixer_music.stop()
                self.status = "stopped"
            elif key == K_SPACE:
                pygame.mixer.music.unpause()
                self.status = "playing"
        elif self.status == "playing":
            t = pygame.mixer.music.get_pos() / 1000 + self.total_playtime
            if key == K_RETURN:
                pygame.mixer.music.stop()
                self.status = "stopped"
            elif key == K_SPACE:
                pygame.mixer.music.pause()
                self.status = "paused"
            elif key == K_LEFT:
                t = max(0, t - 5)
                self.total_playtime = t
                pygame.mixer.music.stop()
                pygame.mixer.music.play(0, t)
                self.num = self.nframes - t * self.framerate
            elif key == K_RIGHT:
                t = min(self.nframes / self.framerate, t + 5)
                self.total_playtime = t
                pygame.mixer.music.stop()
                pygame.mixer.music.play(0, t)
                self.num = self.nframes - t * self.framerate


    def draw_bars(self, h):
        bars = []
        for i, value in enumerate(h):
            color = pygame.Color(0, 0, 0)
            h = i * (360 / self.NUMBER) + 180
            color.hsla = ((h - 360) if h > 360 else h, 100, 50, 100)
            bars.append([i * self.WIDTH, 50 + self.HEIGHT - value, self.WIDTH - 1, value, color])
        for i in bars:
            pygame.draw.rect(self.screen, i[4], i[:4], 0)


    def run(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN:
                        self.controller(event.key)
                    elif event.type == pygame.DROPFILE:
                        self.file_name = event.file
                        if not self.file_name.lower().endswith(('.wav', '.mp3', '.ogg', '.flac', '.opus', 'm4a', '.raw')):
                            self.status = "Error: Not an Audio File"
                        else:
                            pygame.mixer.music.stop()
                            self.status = "stopped"
                            self.load_and_convert_audio()
                            self.play_audio()
                            self.read_audio_file()

                if self.num is not None and self.num <= 0:
                    self.status = "stopped"

                display_text = self.status
                text_surface = self.my_font.render(display_text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.NUMBER * self.WIDTH / 2, 50 + self.HEIGHT / 2))
                self.screen.fill((0, 0, 0))
                self.screen.blit(text_surface, text_rect)

                if self.file_name is not None and self.status != "Error: Not an Audio File":
                    file_name = os.path.basename(self.file_name)
                    display_text = f"NOW PLAYING : {file_name}"
                    name = self.my_font.render(display_text, True, (255, 255, 255))
                    info = self.my_font.render(self.status.upper() + "" + self.get_time(), True, (255, 255, 255))
                    self.screen.blit(name, (0, 0))
                    self.screen.blit(info, (0, 18))
                    self.vis()

                self.fpsclock.tick(self.FPS)
                pygame.display.update(pygame.Rect(0, 0, self.NUMBER * self.WIDTH, 50 + self.HEIGHT))

def main():
    pygame.init()
    pygame.mixer.init()
    visualizer = AudioVisualizer()
    visualizer.run()

if __name__ == "__main__":
    main()