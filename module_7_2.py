def custom_write(file_name, strings):
    #create a file
    with open(file_name, "w", encoding="utf-8") as file:
        pass

    lines = {}
    # open for read and write at the same time
    with open(file_name, "r+", encoding="utf-8") as file:
        line = 0
        for string in strings:
            line += 1
            file.read()
            symbol = file.tell()

            lines.update({
                (line, symbol): string
            })

            file.write(string + "\n ")

        return lines




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
