def util(x,y):
    ans = {}
    ans['greatestPairSum'] = max(x["maxVal"]+y["maxVal"],max(x['greatestPairSum'], y['greatestPairSum']))
    ans['maxVal'] = max(x['maxVal'], y['maxVal'])
    return ans

def constructSegmentTree(arr,ss,se,si,st):
    if ss==se:
        st[si] = {'maxVal': arr[ss], 'greatestPairSum': 0}
        return st[si]

    mid = ss + (se-ss)//2
    st[si] = util(constructSegmentTree(arr,ss,mid,si*2+1,st),constructSegmentTree(arr,mid+1,se,si*2+2,st))
    return st[si]

def query(ss,se,qs,qe,index,st):

    if qs<=se and qe>=se:
        return st[index]

    if se < qs or ss > qe:
        return {'maxVal':-1,'greatestPairSum': -1}

    mid = ss + (se-ss)//2
    return util(query(ss, mid, qs, qe, 2 * index + 1, st), query(mid + 1, se, qs, qe, 2 * index + 2, st))

def operation(arr,n,qs,qe):
    st = [{} for _ in range(4*n)]

    constructSegmentTree(arr,0,n-1,0,st)
    print(st)
    ans = query(0, n - 1, qs, qe, 0, st)

    print(ans['greatestPairSum'])


arr = [1, 3, 2, 7, 9, 11]
n = len(arr)

L, R = 2,3

operation(arr, n, L, R)
