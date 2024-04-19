#Aufgabe 2a
def encode_text(text, key):
  def shift_char(char, key):
      if char.isalpha():
          ascii_offset = ord('A') if char.isupper() else ord('a')
          shifted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
          return shifted_char
      return char

  return "".join(shift_char(char, key) for char in text)

def main():
  import sys

  if len(sys.argv) < 2:
      print("Error: Please provide the text and key as command line arguments.")
      return

  text = sys.argv[1]
  key = int(sys.argv[2])

  encrypted_text = encode_text(text, key)
  decrypted_text = encode_text(encrypted_text, -key)

  print("Original Text:", text)
  print("Encrypted Text:", encrypted_text)
  print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
  main()

#Aufgabe2b
def string_histogram(text):
  histogram = {}

  for char in text:
      if char.isalpha():
          char_lower = char.lower()
          histogram[char_lower] = histogram.get(char_lower, 0) + 1

  return histogram
example_text = "Das ist ein Text"
result = string_histogram(example_text)
print(result)

#Aufgabe2c
def frequencies(histogram):
  total_letters = sum(histogram.values())
  probability_vector = [histogram.get(chr(ord('a') + i), 0) / total_letters for i in range(26)]
  return probability_vector

example_histogram = {'d': 1, 'a': 1, 's': 2, 'i': 2, 't': 3, 'e': 2, 'n': 1, 'x': 1}
result = frequencies(example_histogram)
print(result)

#Aufgabe2d
import string

def frequencies(histogram):
    total_letters = sum(histogram.values())
    probability_vector = [histogram.get(chr(ord('a') + i), 0) / total_letters for i in range(26)]
    return probability_vector

def crack_caesar(example_text, text):
    example_histogram = {}
    for char in example_text:
        if char.isalpha():
            char_lower = char.lower()
            example_histogram[char_lower] = example_histogram.get(char_lower, 0) + 1

    example_frequencies = frequencies(example_histogram)

    decrypted_texts = []

    for shift in range(26):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
                decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
            else:
                decrypted_text += char

        decrypted_histogram = {}
        for char in decrypted_text:
            if char.isalpha():
                char_lower = char.lower()
                decrypted_histogram[char_lower] = decrypted_histogram.get(char_lower, 0) + 1

        decrypted_frequencies = frequencies(decrypted_histogram)

        distance = sum(abs(a - b) for a, b in zip(example_frequencies, decrypted_frequencies))
        decrypted_texts.append((distance, decrypted_text))

    best_decryption = min(decrypted_texts, key=lambda x: x[0])[1]
    return best_decryption

example_text = "I know virtue is in thee, Brutus, as well as I know thy outward favor. Now, honor is the subject of my tale..."

encoded_text = "Reu jf zk zj. Wfi kyzj kzdv Z nzcc cvrmv pfl: Kf-dfiifn, zw pfl gcvrjv kf jgvrb nzky dv, Z nzcc tfdv yfdv kf pfl; fi, zw pfl nzcc, Tfdv yfdv kf dv, reu Z nzcc nrzk wfi pfl."

decrypted_text = crack_caesar(example_text, encoded_text)
print(decrypted_text)

#Klartext: And so it is. For this time I will leave you: To-morrow, if you please to speak with me, I will come home to you; or, if you will, Come home to me, and I will wait for you.