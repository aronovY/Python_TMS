from collections import Counter


doc_text = open('/Users/user/Desktop/Python/text.txt', 'r')
word_list = doc_text.read().split()
words = []
text = doc_text.read()
lst = text.split()
print(Counter(lst).most_common(10))
