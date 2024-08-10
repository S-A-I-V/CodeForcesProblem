'''
city has n houses


'''
n, m = map(int, input().split())
tasks = list(map(int, input().split()))

currposi = 1
tcounter = 0
for task in tasks:
    if task >= currposi:
        tcounter += task - currposi
    else:
        tcounter += n - currposi + task
    currposi = task

print(tcounter)
