from translate import Translator
# translates from file


def translate_file():
    text_file = "text.txt"
    try:
        with open(text_file, mode='r+') as my_file:
            t = my_file.read()
            translator = Translator(to_lang="no")
            translation = translator.translate(t)
            print(translation)
    except FileNotFoundError as e:
        print('check file path')

print(translate_file())