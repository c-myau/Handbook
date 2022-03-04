import random
import statistics
import sys


#target metrics:
# 0% -> 0 + 558 = 558 EM
# 60% -> 50 + 558 = 608 EM
# 90% -> 100 + 558 = 658 EM
m_rolls = 10000000
def main():
    choice = [16, 19, 21, 23]
    cdict = {0:0, 20:0, 40:0, 60:0, 80:0, 100:0, 120:0, 140:0, 160:0, 180:0, 200:0, 220:0}
    for i in range(0, m_rolls):
        count = 0
        random.seed()
        for i in range(0, 5):
            roll = random.randint(1, 4)
            if roll == 4:
                count += random.choice(choice)
        for i in range(0, 5):
            roll = random.randint(1, 4)
            if roll == 4:
                count += random.choice(choice)
        cdict[round(count/20)*20] += 1
    print(cdict)
    for item in cdict:
        print(cdict[item]/m_rolls)
    # print(sum(clist)/len(clist))
    # print(statistics.pstdev(clist))
if __name__ == "__main__":
    sys.exit(main())
