import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self, ):
        self.users = []
        self.videos = []
        self.current_user = ""

    def log_in(self, nickname, password):

        for user in self.users:
            if nickname in user.nickname:
                if hash(password) == user.password:
                    self.current_user = {}
                    self.current_user = nickname
                    return
        print("Incorrect credentials")

    def register(self, nickname, password, age):

        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        self.users.append(User(nickname, hash(password), age))
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = ""

    def add(self, *videos):
        for video in videos:
            self.videos.append(video)

    def get_videos(self, search_term):
        results = []
        for video in self.videos:
            if search_term.lower() in video.title.lower():
                results.append(video.title)
        return results

    def watch_video(self, video):

        def play(saved_video):
            timer = 0
            for i in range(saved_video):
                timer += 1
                print(timer, end=" ")
                time.sleep(1)
            print("Конец видео")

        if self.current_user == "":
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        age = 0
        for user in self.users:
            if self.current_user == user.nickname:
                age = user.age

        if age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for saved_video in self.videos:
            if video in saved_video.title:
                play(saved_video.duration)
                return

        print("Видео не найдено")


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
