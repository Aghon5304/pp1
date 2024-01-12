speeds = [48,47,54,50,42,68,39,46]
zle=list(filter(lambda n:n>50,speeds))
print(f"speeds too high: {zle}")