from translate import Translator
translator = Translator(to_lang="ja")

#First ensure you can properly open file, then translate the file to Japanese and create a new document containing translated text
try:
    with open('text_to_translate.txt', mode = 'r') as original:
        translation = translator.translate(original.read())
        with open('translated_text.txt', mode = 'w') as new:
            new.write(translation)
except IOError:
    print('Wrong path my guy')

#Test to ensure translated file open correctly and contains translated text
with open('translated_text.txt') as translated:
    print(translated.read())
