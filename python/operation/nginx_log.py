"""nginx access.log 分析."""

from collections import Counter

ips = []
c = Counter()
d = {}
with open('access.log') as f:
    for line in f:
        line_list=line.split()
        ips.append((line_list[0]))
        c[line_list[6]] += 1
        http_code = line_list[8]
        d.setdefault(http_code, 0)
        d[http_code] += 1


sum_requests = 0
error_requests = 0
for key, val in d.items():
    try:
        if int(key) >= 400:
            error_requests += val
        sum_requests += val
    except ValueError:
        print(key,val)
print("sum requests is", sum_requests)

print('error rate: {0: .2f}%' .format(error_requests * 100.0 / sum_requests))
print("PV is {0}".format(len(ips)))
print("PV is {0}".format(len(set(ips))))
print("Popular resources: {0} " .format(c .most_common(10)))
