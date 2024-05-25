import time

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    pass

class UrTube:

    def __init__(self,):
        self.users = {}
        self.videos = {}
        self.current_user = ""

    def log_in(self, login):
        self.current_user = ""
        self.current_user = login

    def register(self, nickname, password, age):
        if nickname in self.users.keys():
            print(f"Пользователь {nickname} уже существует")

        self.users.update({nickname: [hash(password), age]})
        self.log_in(nickname)

    def log_out(self):
        self.current_user = ""

    def add(self, *video):
        for i in video:
            self.videos.update({i.title: [i.duration, i.time_now, i.adult_mode]})

    def get_videos(self, search_term):
        results = []
        for i in self.videos.keys():
            if search_term.lower() in i.lower():
                results.append(i)
        return results

    def watch_video(self, video):

        if self.current_user == "":
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        elif self.users[self.current_user][1] < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        if video not in self.videos.keys():
            print("Видео не существует")
            return


        timer = 0
        for i in range(self.videos[video][0]):
            timer += 1
            print(timer, end = " ")
            time.sleep(1)
        print("Конец видео")





if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    ur.add(v1, v2)

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    ur.watch_video('Лучший язык программирования 2024 года!')