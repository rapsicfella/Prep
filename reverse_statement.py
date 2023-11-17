st = 'Acquia is a content management system built on top of Drupal'
words = st.split()
for i in range(len(words)//2):
    words[i], words[len(words) -1 -i] =  words[len(words) -1 -i], words[i]
res = " ".join(words)
print(res)
