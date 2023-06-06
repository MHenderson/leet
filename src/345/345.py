s = "ab@a"
expected = "aba@"

result = []
vowels = []

for i in range(len(s)):
    if(s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]):
        vowels.append(s[i])
        result.append("@")
    else:
        result.append(s[i])

vowels.reverse()

for v in vowels:
    for i in range(len(result)):
        if(result[i]=="@"):
            result[i]=v
            break

print(''.join(result))
