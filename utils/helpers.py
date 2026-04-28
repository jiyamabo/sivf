# grading scheme as at 2024-06-30 (spring 2024): latest update at a college

def letter_grade_fall2024(grades):
    grade_ranges = [
        (93, 'A+'),
        (85, 'A'),
        (80, 'A-'),
        (77, 'B+'),
        (74, 'B'),
        (70, 'B-'),
        (67, 'C+'),
        (64, 'C'),
        (60, 'C-'),
        (55, 'D+'),
        (50, 'D'),
        (0, 'F')
    ]

    for min_grade, letter in grade_ranges:
        if grades >= min_grade:
            return letter


def letter_grade_spring2024(grades):
    grade_ranges = [
        (93.9, 'A+'),
        (87, 'A'),
        (80, 'A-'),
        (77, 'B+'),
        (74, 'B'),
        (70, 'B-'),
        (67, 'C+'),
        (64, 'C'),
        (60, 'C-'),
        (57, 'D+'),
        (50, 'D'),
        (0, 'F')
    ]

    for min_grade, letter in grade_ranges:
        if grades >= min_grade:
            return letter


