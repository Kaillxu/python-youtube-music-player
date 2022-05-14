import os
import pafy 
import vlc 
import time
import random
import re, requests, subprocess, urllib.parse, urllib.request
import os
import threading


# CHECKING SYSTEM -- IF IT'S FIRST TIME LAUNCH --> INSTALL NEEDED LIBS

bashCommand = "pip install python-vlc | pip install pafy | pip install youtube_dl | pip install requests | pip install thread6"

with open('settings.txt','r+') as f:
    for data in f:
        
        if data == "is_first_time=1":
            os.system(bashCommand)

            with open('settings.txt','w+') as file_data_not_first_time_anymore:
                file_data_not_first_time_anymore.write("is_first_time=0")
        
        elif data != "is_first_time=1" and data != "is_first_time=0":
            print("settings.txt file do not exist, is empty or contain wrong informations, creating another one...\n")
            with open('settings.txt','w+') as file:
                file.write("is_first_time=1")
                print("everything is setup, please restart")
                file.close()

    f.close()

# PLAYER CLASS

class mp3Player:

    def launch(self, choice):
        self.t1 = threading.Thread(target=self.play, args=(choice,))
        self.t1.start()
        self.t2 = threading.Thread(target=self.ask_volume)
        self.t2.start()
    
    def ask_volume(self):
        while True:
            ask = int(input("\r"))
            self.media.audio_set_volume(ask)


    # WILL GET YOUTUBE VIDEO URL FROM TITLE

    def query(self, name):

        self.query_string = urllib.parse.urlencode({"search_query": name})
        self.formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + self.query_string)
        self.search_results = re.findall(r"watch\?v=(\S{11})", self.formatUrl.read().decode())
        self.audio = pafy.new("https://www.youtube.com/watch?v=" + "{}".format(self.search_results[0]))
        self.audiolink = self.audio.getbestaudio()
        return (self.audiolink, self.audio)

    # PLAY THE MUSIC FROM THE URL GOTTEN WITH 'QUERY'

    def play(self, name):

        # PLAYING SYSTEM

        self.query_result = self.query(name)
        self.media = vlc.MediaPlayer(self.query_result[0].url)  
        self.media.play()

        self.progress_bar()

    def progress_bar(self):
        # PROGRESS BAR

        self.duration_minute = self.query_result[1].length // 60
        self.duration_seconds = self.query_result[1].length % 60

        self.progress = 0
        self.percent = 1/self.query_result[1].length*100
        self.time_done = 0
        self.minutes_done = 0
        self.seconds_done = 0

        for i in range(self.query_result[1].length):
            time.sleep(1)

            self.seconds_done += 1

            self.progress += self.percent

            if self.seconds_done == 60:
                self.minutes_done += 1
                self.seconds_done = 0
            
            if len(str(self.minutes_done)) < 2:
                self.minutes_done = "0" + str(self.minutes_done)



            if self.progress > 10 and self.progress < 20:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■▢▢▢▢▢▢▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 20 and self.progress < 30:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■▢▢▢▢▢▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 30 and self.progress < 40:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■▢▢▢▢▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 40 and self.progress < 50:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■▢▢▢▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 50 and self.progress < 60:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■■▢▢▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 60 and self.progress < 70:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■■■▢▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 70 and self.progress < 80:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■■■■▢▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 80 and self.progress < 90:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■■■■■▢▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 90 and self.progress < 100:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■■■■■■▢ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)

            elif self.progress > 100:
                
                print(f'\r{self.minutes_done}:{self.seconds_done} ■■■■■■■■■■ {str(self.duration_minute)}:{str(self.duration_seconds)}    |    Volume ? ', end = '')
                self.minutes_done = int(self.minutes_done)
                print('\n')




choice = str(input('Name of the song ? '))
mp3Player().launch(choice)
