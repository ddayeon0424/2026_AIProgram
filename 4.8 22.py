aset = {1, 2, 3, 4}
bset = {2, 4, 6, 7}

cset = aset.union(bset)
cset = aset | bset


cset = aset & bset
cset = aset.intersection(best)
cset = bset & aset
cset = bset.intersection(aset)

print(cset)
