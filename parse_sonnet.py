sonnet_text = open("sonnet.txt").read()

#print(sonnet_text)

sonnet_list = sonnet_text.split()

sonnet_list = [word.lower() for word in sonnet_list]
sonnet_list.sort()

print(sonnet_list)
