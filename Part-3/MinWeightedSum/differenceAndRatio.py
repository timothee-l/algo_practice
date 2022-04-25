import csv

scoreByDifference = False  # Score is difference wj - lj (else ratio wj / sj)

with open('input.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    scores = {}  # key = job id; value = score (or list of job ids if multiple)
    weights = {}  # key = job id; value = weight (to break score ties)
    lengths = {}  # key = job id; value = length (to compute completion time)
    firstRow = True
    for jobId, job in enumerate(reader):
        if firstRow:
            firstRow = False
            n = int(job[0])
        else:
            weight = int(job[0])
            length = int(job[1])
            if scoreByDifference:
                score = weight - length  # Score sj = wj - lj for job j
            else:  # score by ratio
                score = weight / length  # Score sj = wj / lj for job j
            scores[jobId] = score
            weights[jobId] = weight
            lengths[jobId] = length

sumWCT = 0  # Sum of weighted completion times
sumCT = 0  # Sum of completion times
CT = 0  # Completion time for current job
while scores:
    mx = max(scores.values())
    jobIds = [k for k, v in scores.items() if v == mx]
    # Higher scoring jobs first
    jobIds = sorted(jobIds, key=lambda ele: weights[ele], reverse=True)
    for jobId in jobIds:
        CT = CT + lengths[jobId]
        sumCT += CT
        WCT = CT * weights[jobId]
        sumWCT += WCT
        scores.pop(jobId)


print(sumWCT)
