import sys
def rep(f, old, new, count=1):
    s=open(f).read()
    n=s.count(old)
    if n!=count:
        print("!! MISMATCH",f,n,old[:50]); return
    open(f,'w').write(s.replace(old,new))
