# Exercise3_count_word_in_file
def preprocess_text(sentence):
  sentence = sentence.lower()
  sentence = sentence.strip()
  sentence = sentence.replace(',', '')
  sentence = sentence.replace('.', '')
  word = sentence.split()
  return word

sentence = 'I love AI. AI    is not easy.'
preprocess_text(sentence)



# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

path = 'P1_data.txt'
with open(path, 'r') as f:
  sentences = f.readlines()
type(sentences)

sentences[:len(sentences)]

counter = {}
for sentence in sentences:
  words = preprocess_text(sentence)
  for word in words:
    if word in counter:
      counter[word] += 1
    else:
      counter[word] = 1

print(counter)