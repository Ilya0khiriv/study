import requests as rq
import logging


class Create_log():
    def __init__(self, name, file, level=logging.INFO):
        self.__file = file
        self.__level = level
        self.__name = name

        self.__log = logging.getLogger(self.__name)
        self.__log.setLevel(self.__level)
        fh = logging.FileHandler(self.__file, 'w', 'utf-8')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.__log.addHandler(fh)

    def info(self, msg): self.__log.info(msg)

    def err(self, msg): self.__log.error(msg)

    def warn(self, msg): self.__log.warning(msg)


log_ok = Create_log("accessible", "success_responses.log")
log_bad = Create_log("no_access", "bad_responses.log")
log_blocked = Create_log("blocked_access", "block_responses.log")

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3).status_code
        if 200 == response: log_ok.info(f"{site} returned {response}")
        else: log_bad.warn(f"{site} returned {response}")

    except:
        log_blocked.err(f"{site} is blocked")
