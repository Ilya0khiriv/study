from collections import OrderedDict




def reqst():
# Requests нужен для запроса данных из интернета с возможностей передачи параметров в URL и использования логина и пароля
    import requests
    r = requests.get('https://google.com')

    # find word some word and count it

    print(len(r.text))

    count = 0

    word = "google"

    for i in range(len(r.text)):
        final_word = str("")
        if r.text[i] == word[0]:
            final_word += word[0]
            pos_word = 0
            pos_tet = i

            while True:
                pos_word += 1
                pos_tet += 1

                if final_word == word:
                    count += 1
                    break


                if pos_word in range(len(word)):
                    try:
                        char_word_ = word[pos_word]
                        char_txt_ = r.text[pos_tet]
                    except:
                        break
                else: break

                if char_word_ == char_txt_:
                    final_word += char_txt_

    print(count)

def pnds():
    import pandas as pd
    group = pd.read_excel('5.xlsx')
    # get names from the table

    names = []
    i = -1
    while True: # show only names that are in the first column and pass it to a list
        try:
            i += 1
            name = str(group.iloc[i,0])
            if name != "nan": names.append(name)
        except Exception as exc:
            print(f"Reached an Error {exc}")
            break
    print(names)

def nmpy():
    import numpy
    arr = numpy.array([1, 2, 3, 4, 5, 6])
    new_arr = []
    for a in arr:
        try:
            new_arr.append(numpy.sin(a - a**(1/2)) ** (1/9) - 1)
        except:
            pass
    return new_arr

def mpl(r):
    import matplotlib.pyplot as plt
    # Plot some numbers:
    plt.plot(r)
    plt.title("Lal")
    # Display the plot:
    plt.show()

def pllw():
    from PIL import Image
    from PIL import ImageEnhance

    with Image.open("sample.png") as im:
        enh = ImageEnhance.Contrast(im)
        io = enh.enhance(100)
        io.thumbnail((100, 100))
        io.save("sample.webp")



if __name__ == "__main__":
    # reqst() # помогает быстро и легко обратить к данным вебсайта
    # pnds() # помогает трансформировать сохранение на компьютер данные в операбельные словари и листы
    # r = nmpy() #помогает использовать сложные матекатические фнукции, которых нет в питоне с оптимизацией на кокретное железо
    # mpl(r) # визуализирует математические даннные
    # pllw() # дает возможность редактирвать изображения в больших колличествах и автоматизировать этот процесс

