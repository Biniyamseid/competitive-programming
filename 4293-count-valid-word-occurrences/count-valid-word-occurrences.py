class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        words = s.split(" ")
        # print(words)
        correct_words = []
        for word in words:
            if "-" in word:
                if "--" in word:
                    splits = word.split("--")
                    for w in splits:
                        if w and  w[0]=="-":
                            w = w[1:]
                        if w and w[-1]=="-":
                            w = w[:-1]
                        if w:
                            correct_words.append(w)
                    # correct_words.extend(splits)
                else:
                    if word[0]=="-":
                        word = word[1:]
                    if word and word[-1]=="-":
                        word = word[:-1]
                    if word:
                        correct_words.append(word)
            else:
                correct_words.append(word)
        ans =[]
        # print(correct_words)
        counter = Counter(correct_words)
        for query in queries:
            ans.append(counter[query])
        return ans
            
        