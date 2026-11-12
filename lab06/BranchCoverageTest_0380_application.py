import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


@pytest.mark.parametrize("marks, expected", [
    (95, "S"), (85, "A"), (75, "B"),
    (65, "C"), (55, "D"), (45, "E"), (20, "F")
])
def test_all_grade_branches(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_invalid_grade_branches(marks):
    with pytest.raises(ValueError):
        letter_grade(marks)


def test_final_marks_valid_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_valid_with_project():
    assert final_marks(30, 50, True) == 85


def test_final_marks_project_cap():
    assert final_marks(40, 60, True) == 100


@pytest.mark.parametrize("internal, external", [
    (41, 50), (30, 61)
])
def test_invalid_final_marks_branches(internal, external):
    with pytest.raises(ValueError):
        final_marks(internal, external, False)


def test_exam_fees_blocked():
    assert exam_eligibility(90, False, True) == "blocked"


def test_exam_attendance_eligible():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_medical_eligible():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_medical_condition_false():
    assert exam_eligibility(70, True, False) == "detained"


def test_exam_attendance_below_medical_threshold():
    assert exam_eligibility(60, True, True) == "detained"
