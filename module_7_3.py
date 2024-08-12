import os


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            if os.path.isfile(file_name):
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        for p in punctuation:
                            line = line.replace(p, '')
                        words.extend(line.split()) # Разбиваем строку на слова
                    all_words[file_name] = words  # Добавляем в словарь значение
            else:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)  # Получаем первую позицию слова
            else:
                result[file_name] = 0  # Если слово не найдено, возвращаем 0
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Счетчик количества слов
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
