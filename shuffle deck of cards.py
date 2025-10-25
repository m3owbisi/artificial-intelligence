import random
deck=[f"{r} of {s}" for s in ['hearts','diamonds','clubs','spades'] for r in ['2','3','4','5','6','7','8','9','10','jack','queen','king','ace']]
random.shuffle(deck)
print("Shuffled deck:\n"+"\n".join(deck))
