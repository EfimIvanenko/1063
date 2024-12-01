class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = file_names

    def get_all_words(self):
        """Возвращает словарь со словами из каждого файла."""
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()

                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        """Возвращает словарь с позициями первого вхождения слова в каждом файле."""
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            try:
                result[file_name] = words.index(word) + 1
            except ValueError:
                result[file_name] = None
        return result

    def count(self, word):
        """Возвращает словарь с количеством вхождений слова в каждом файле."""
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


if __name__ == "__main__":
    with open('test_file.txt', 'w', encoding='utf-8') as file:
        file.write(
            "It's a text for task Найти везде,\n"
            "Используйте его для самопроверки.\n"
            "Успехов в решении задачи!\n"
            "text text text\n"
        )

    finder2 = WordsFinder('test_file.txt')

    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
