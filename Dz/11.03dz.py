s = "I am learning Python. hello WORLD!"
h1 = s.find("h")
h2 = s.rfind("h")
s1 = s[:h1+1] + s[h1+1:h2][::-1] + s[h2:]
print(s1)