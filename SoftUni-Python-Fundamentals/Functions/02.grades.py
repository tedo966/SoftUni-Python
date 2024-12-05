grade_data = float(input())
def grade_status(grade):
    if grade <= 2.99:
        return "Fail"
    elif grade <= 3.49:
        return "Poor"
    elif grade <= 4.49:
        return "Good"
    elif grade <= 5.49:
        return "Very Good"
    elif grade <= 6:
        return "Excellent"
print(grade_status(grade_data))