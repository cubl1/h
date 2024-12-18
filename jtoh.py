import time
import multiprocessing

def read_info(name):
    with open(name, "r") as file:
        all_data = list(map(str, file.read().split("\n")))

filenames = [f'./file {number}.txt' for number in range(1, 5)]

starter = time.time()
for i in filenames:
    read_info(i)
ender = time.time()
print(ender - starter)

if __name__ == '__main__':
    starter = time.time()
    for i in filenames:
        process = multiprocessing.Process(target=read_info, args=(i, ))
        process.start()
    ender = time.time()
    print(ender - starter)