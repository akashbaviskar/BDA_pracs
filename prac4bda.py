from collections import defaultdict

# ------------------------
# MAP FUNCTION
# ------------------------
def mapper(lines):
    mapped = []

    for line in lines:
        name, marks = line.strip().split()
        marks = int(marks)

        # Assign grade
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"

        mapped.append((name, grade))  # (key, value)

    return mapped


# ------------------------
# SHUFFLE FUNCTION
# ------------------------
def shuffle(mapped_data):
    grouped = defaultdict(list)

    for name, grade in mapped_data:
        grouped[name].append(grade)

    return grouped


# ------------------------
# REDUCE FUNCTION
# ------------------------
def reducer(grouped_data):
    result = {}

    for name, grades in grouped_data.items():
        result[name] = grades

    return result


# ------------------------
# MAIN PROGRAM
# ------------------------
def main():
    # Sample file
    with open("students.txt", "w") as f:
        f.write("Rahul 92\nSneha 76\nAmit 65\nPooja 50\n")

    # Read file
    with open("students.txt", "r") as f:
        lines = f.readlines()

    # Map → Shuffle → Reduce
    mapped = mapper(lines)
    grouped = shuffle(mapped)
    result = reducer(grouped)

    # Display output
    print("Student Grades:")
    for name, grades in result.items():
        print(name, "->", grades)   # FIXED HERE


main()