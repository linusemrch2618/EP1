print(f"| {'d':^2s} | {'b':^6s} |")
for i in range(1, 51):
    if i%2==0:
        print(f"| {i:>2d} | {i:>06b} |")
