import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


@pytest.mark.parametrize("marks, expected", [
    (95, "S"),
    (85, "A"),
    (75, "B"),
    (65, "C"),
    (55, "D"),
    (45, "E"),
    (20, "F")
])
def test_letter_grade_all_grades(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_letter_grade_invalid_marks(marks):
    with pytest.raises(ValueError):
        letter_grade(marks)


def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_with_project():
    assert final_marks(30, 50, True) == 85


def test_final_marks_capped_at_100():
    assert final_marks(40, 60, True) == 100


@pytest.mark.parametrize("internal, external", [
    (41, 50),
    (30, 61)
])
def test_final_marks_invalid(internal, external):
    with pytest.raises(ValueError):
        final_marks(internal, external, False)


def test_exam_eligible_by_attendance():
    assert exam_eligibility(80, True, False) == "eligible"


def test_exam_eligible_with_medical():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_detained():
    assert exam_eligibility(60, True, False) == "detained"


def test_exam_blocked_due_to_fees():
    assert exam_eligibility(90, False, True) == "blocked"
