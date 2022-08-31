from queue import PriorityQueue

n = int(input())
cards = PriorityQueue()
for i in range(n):
    cards.put(int(input()))

ans = 0
while True:
    item = cards.get()
    if cards.empty():
        print(ans)
        break
    item2 = cards.get()
    ans+= item+item2
    cards.put(item+item2)