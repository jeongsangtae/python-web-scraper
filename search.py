import subprocess

words = ["좀비", '일루미나티', '그레이', 'CIA']

new_words = []

for i in range(len(words)):
  for j in range(len(words)):
    if i != j:
      new_words.append(f"{words[i]} {words[j]}")
print(new_words)

for w in new_words:
  subprocess.Popen(f"start chrome /new-tab https://www.google.com/search?q={w}", shell = True)