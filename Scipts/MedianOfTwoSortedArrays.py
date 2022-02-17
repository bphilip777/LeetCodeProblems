import math

def findMedianSortedArrays(nums1:list, nums2:list)-> float:
    # Two Binary Search Algorithms Solution
    if len(nums1) > len(nums2):  # Make x larger or equal to y
        x, y = nums2, nums1
    else:
        x, y = nums1, nums2
    lx, ly = len(x), len(y)
    mid = (lx + ly) // 2  # Find the midpoint after adding the length of both arrays
    isEven = (lx + ly) % 2 == 0
    l, h = 0, lx - 1  # Find left and right of x array

    while True:
        cx = (h + l) // 2  # Find midpoint of x array
        cy = mid - cx - 2  # Find midpoint of y array -
        print(mid, cx, cy)
        # grab right and left values of center
        xmin = x[cx] if cx >= 0 else - math.inf
        xmax = x[cx + 1] if cx + 1 < lx else math.inf
        ymin = y[cy] if cy >= 0 else - math.inf
        ymax = y[cy + 1] if cy + 1 < ly else math.inf

        if xmin <= ymax and ymin <= xmax:
            if isEven:  # even case
                return (max(xmin, ymin) + min(xmax, ymax)) / 2
            else:  # Odd - median is the minimum of xmax and ymax
                return min(xmax, ymax)
        elif xmin > ymax:
            h = cx - 1  # values in array x is larger than values in array y, shift cx left
        else:
            l = cx + 1  # values in array x is smaller than values in array y, shift cx right


nums1 = [1, 2, 3]
nums2 = [4, 5]
val = findMedianSortedArrays(nums1, nums2)
print(val)
