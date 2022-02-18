from wordleWords import *
words = getWordleAns()
pAns=[match[0]+match[1] for match in words if "der" in match and not "i" in match and not "o" in match and not "u" in match]
print(pAns)