from collections import deque

strength_required = [int(x) for x in input().split()]
accuracy_needed = deque(int(x) for x in input().split())

GOAL_SCORE = 100
scored_goals = 0

while strength_required and accuracy_needed:
    current_strength = strength_required[-1]
    current_accuracy = accuracy_needed[0]
    sum_of_str_acc = current_strength + current_accuracy
    if sum_of_str_acc == GOAL_SCORE:
        scored_goals += 1
        strength_required.pop()
        accuracy_needed.popleft()
    elif sum_of_str_acc < GOAL_SCORE:
        if current_strength < current_accuracy:
            strength_required.pop()
        elif current_strength > current_accuracy:
            accuracy_needed.popleft()
        elif current_accuracy == current_strength:
            strength_required.pop()
            strength_required.append(sum_of_str_acc)
            accuracy_needed.popleft()
    elif sum_of_str_acc > GOAL_SCORE:
        current_strength -= 10
        strength_required[-1] = current_strength
        accuracy_needed.append(current_accuracy)
        accuracy_needed.popleft()
if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 0 < 3:
    print("Paul failed to make a hat-trick.")

if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")

if any(strength_required):
    print(f"Strength values left: {', '.join(map(str, strength_required))}")
if any(accuracy_needed):
    print(f"Accuracy values left: {', '.join(map(str, accuracy_needed))}")

