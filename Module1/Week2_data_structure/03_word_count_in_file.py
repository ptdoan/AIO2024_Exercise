# Exercise3_count_word_in_file

# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
# path = 'P1_data.txt'

def preprocess_text(sentence):
  sentence = sentence.lower()
  sentence = sentence.strip()
  sentence = sentence.replace(',', '')
  sentence = sentence.replace('.', '')
  word = sentence.split()
  return word

#sentence = 'I love AI. AI    is not easy.'
#preprocess_text(sentence)

def count_word(file_path):
  counter = {}
  with open(file_path, 'r') as f:
    sentences = f.readlines()
  for sentence in sentences:
    words = preprocess_text(sentence)
    for word in words:
      if word in counter:
        counter[word] += 1
      else:
        counter[word] = 1
  return counter

#result = count_word('/content/P1_data.txt')
result = count_word('/Module1/Week2_data_structure/P1_data.txt')
assert result['who'] == 3
print (result['man'])