'''
A standard divide and conquer algorithm for mergesort

input format
============
12 11 13 5 6 7
==============
'''

arr = list(map(int, input().split(" ")))

def merge(a,b):
	l = []
	while a and b:
		if a[0] < b[0]:
			l.append(a.pop(0))
		else:
			l.append(b.pop(0))
	return l + a + b


def merge_sort(l, h):
	mid = int((h+l)/2)
	if l < h:
		# print(arr[l: h])
		low = merge_sort(l, mid)
		high = merge_sort(mid+1, h)
		return merge(low, high)
	# print(arr, l)
	return [arr[l]]
print(merge_sort(0, len(arr)-1))