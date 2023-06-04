high_scores = [78, 56, 67, 90, 87, 92, 80]
high_scores.sort(reverse=True)

print("5 điểm cao nhất:")
for score in high_scores[:5]:
    print(score)