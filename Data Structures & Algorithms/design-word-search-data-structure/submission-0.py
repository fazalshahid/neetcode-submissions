class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        isdot = '.' in word

        if not isdot:
            return word in self.words
        
        all_words = list(self.words)

        words = []
        for w in all_words:
            if len(word) != len(w):
                continue
            words.append(w)

        for w in words:
            sw = ''
            for i, ch in enumerate(w): 
                if word[i] == '.':
                    sw += '.'
                else:
                    sw += ch
            if sw == word:
                return True
        
        return False

        
