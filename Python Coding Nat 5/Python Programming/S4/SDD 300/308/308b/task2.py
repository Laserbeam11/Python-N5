header = "=" * 68
subheader = "-" * 68
scores = []

print(f"\n{subheader}\n")

print("test scores")
for i in range(5):
    score = int(input(f"enter score for test {i + 1}: "))
    scores.append(score)
    if i == 0:
        total = score
    elif i > 0:
        total += score

    print(f"total score after test {i + 1}: {round(total, 2)}")
    print()