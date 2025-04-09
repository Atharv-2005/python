sentence=input("Enter string")
words=sentence.lower().split()
counts={}
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1

print("word counts: ")
for word, count in counts.items():
    print(f"{word}:{count}")

