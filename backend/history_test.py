from database import get_history

history = get_history()

print("\nPrediction History:\n")

for row in history:
    print(row)