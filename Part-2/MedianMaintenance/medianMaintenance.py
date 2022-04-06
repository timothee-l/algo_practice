import heapq as hq

with open('input.txt', 'r') as read_obj:
    Numbers = list(map(int, read_obj.readlines()))


def push(n):
    # Add n to low heap if n smaller than largest value of small heap.
    # Add n to high heap otherwise
    if n < -lowHeap[0]:
        hq.heappush(lowHeap, -n)
    else:
        hq.heappush(highHeap, n)


def rebalance():
    imbalance = len(highHeap) - len(lowHeap)
    if imbalance <= -2:
        # lowHeap too small
        hq.heappush(highHeap, -hq.heappop(lowHeap))
    elif imbalance >= 2:
        # highHeap too small
        hq.heappush(lowHeap, -hq.heappop(highHeap))


def findMedian():
    if len(lowHeap) >= len(highHeap):
        return -lowHeap[0]
    else:
        return highHeap[0]


# Initialization

lowHeap = []  # Extract Max (values reversed)
highHeap = []  # Extract Min

sumOfMedians = Numbers[0]
lowHeap.append(-Numbers.pop(0))

# Main loop

for number in Numbers:
    push(int(number))
    rebalance()
    sumOfMedians += findMedian()

print(sumOfMedians % 10000)
