def sumIntervals(intervals):
    sum = 0
    for i in range(len(intervals)):
        if not intervals[i]:
            continue
        for j in range(i+1, len(intervals)):
            if not intervals[j]:
                continue
            if (intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]):
                intervals[i] = None
                break
            elif (intervals[i][0] >= intervals[j][0] and intervals[i][0] <= intervals[j][1]):
                intervals[i] = [intervals[j][1], intervals[i][1]]
            elif (intervals[i][1] <= intervals[j][1] and intervals[i][1] >= intervals[j][0]):
                intervals[i] = [intervals[i][0], intervals[j][0]]
            elif (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]):
                intervals[j] = None

    for i in intervals:
        if i:
            sum += i[1] - i[0]
    return sum

print(sumIntervals([
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ))