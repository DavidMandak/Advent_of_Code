import time

line = open("2019/Inputs/input08.txt").read()[:-1]

t = time.time()
size = 25*6
layers = [line[i:i+size] for i in range(0, len(line), size)]
least = (None, None)
for i in range(len(layers)):
    count = layers[i].count("0")
    if least[0] is None or count < least[0]:
        least = (count, i)
most = layers[least[1]]
print(most.count("1")*most.count("2"))
print(time.time()-t)
