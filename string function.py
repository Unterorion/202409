sent = "Python is the best choice."
lett = 't'
count = "number of a letter: %s" % sent.count(lett)
print(count)

find = "the first place of a letter: %s" % sent.find(lett)
print(find)

idx = "the first index of a letter: %s" % sent.index(lett)
print(idx)

join = ",".join(sent)
print(join)

upper = sent.upper()
print(upper)

lower = sent.lower()
print(lower)

sent2 = " "*10 + sent + " "*10
print(sent2)
print(sent2.lstrip())
print(sent2.rstrip())
print(sent2.strip())

print(sent.replace("Python", "Java"))

list_sent = sent.split()
print(list_sent)
comma = ",".join(list_sent)
print(comma)
print(comma.split(","))
