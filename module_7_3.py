class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self.words_dict = {}

    def find(self,word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, mode='r', encoding='utf8') as file:
                words = file.read().split()
                self.words_dict[file_name] = words
        return self.words_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


