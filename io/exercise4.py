with open("kku2.txt", "a") as writer:
     newlines = "Motto: วิทยา จริยา ปัญญา\n" \
                "Motto in English: Knowledge, Virtues, Wisdom"
     writer.writelines(newlines)

with open("kku2.txt", "r") as reader:
     for line in reader:
         print(line, end="")
