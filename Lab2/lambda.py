

ls=[1,2,3,4]
tuped=tuple(map(lambda a:a,ls))
tuped=tuple(ls)
tuped=tuple([i for i in ls])
tuped=[(lambda x:x**2 - x)(x) for x in ls]
print(tuped)