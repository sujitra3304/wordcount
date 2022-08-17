"""Count words in file."""

file = open("twain.txt")

letter_count = {}

for line in file:
    line = line.rstrip()
    word = line.split(" ")
    for i in word:

      letter_count[i] = letter_count.get(i, 0) + 1


for word, count in letter_count.items():
    print(f"{word} {count}")

    

# def count_char(str):
#   letter_count = {}

#   for i in str:
#     letter_count[i] = letter_count.get(i, 0) + 1

#   return letter_count