import bisect
import sys

haystack = [1, 4, 5, 6, 7, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)
        offset = position * "  |"
        print(f"{needle:2} @ {position:2}   {offset} {needle:<2}")

if __name__ == '__main__':
    if sys.argv[-1] == "left":
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print("DEMO:", bisect_fn.__name__)
    print("haystack ->", " ".join(f"{n:2}" for n in haystack))
    demo(bisect_fn)