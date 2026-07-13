import pandas as pd


# ============================================================
# 1. Load Dataset
# ============================================================

def load_data():
    """Load student dataset."""
    return pd.read_csv("./data/students.csv")


# ============================================================
# 2. Data Cleaning
# ============================================================

def clean_data(student):
    """Clean the dataset."""

    print("\nMissing Values:")
    print(student.isna().sum())

    print("\nDuplicate Rows:")
    print(student.duplicated().sum())

    student = student.drop_duplicates()

    return student


# ============================================================
# 3. Feature Engineering
# ============================================================

def grading(n):
    if n >= 90:
        return "A+"
    elif n >= 80:
        return "A"
    elif n >= 70:
        return "B"
    elif n >= 60:
        return "C"
    elif n >= 50:
        return "D"
    else:
        return "F"


def calculate_result(n):
    if n >= 40:
        return "Pass"
    return "Fail"


def feature_engineering(student):
    """Create new columns."""

    student["Total"] = (
        student["Math"]
        + student["Physics"]
        + student["Chemistry"]
        + student["English"]
    )

    student["Average"] = student["Total"] / 4

    student["Percentage"] = (student["Total"] / 400) * 100

    student["Grade"] = student["Percentage"].apply(grading)

    student["Result"] = student["Percentage"].apply(calculate_result)

    return student


# ============================================================
# 4. Filtering
# ============================================================

def filtering(student):
    """Filter different student groups."""

    return {
        "cse": student[student["Branch"] == "CSE"],

        "it": student[student["Branch"] == "IT"],

        "topstudent": student[student["Percentage"] > 90],

        "failedstudent": student[student["Result"] == "Fail"],

        "lowattendance": student[student["Attendance"] < 75],

        "csetop": student[
            (student["Branch"] == "CSE")
            & (student["Percentage"] > 85)
        ],
    }


# ============================================================
# 5. Sorting
# ============================================================

def sorting(student):
    """Sort dataset."""

    return {
        "top_10": student.sort_values(
            by="Percentage",
            ascending=False
        ),

        "below_10": student.sort_values(
            by="Percentage"
        ),

        "high_attendance": student.sort_values(
            by="Attendance",
            ascending=False
        ),

        "low_attendance": student.sort_values(
            by="Attendance"
        ),
    }


# ============================================================
# 6. GroupBy Analysis
# ============================================================

def groupby_analysis(student):
    """Perform groupby analysis."""

    top = student.groupby("Branch")["Percentage"].idxmax()

    return {

        "average_percentage_by_branches":
        student.groupby("Branch")["Percentage"].mean(),

        "average_attendance_by_branches":
        student.groupby("Branch")["Attendance"].mean(),

        "total_student_per_branch":
        student.groupby("Branch")["Student_ID"].count(),

        "highest_percent_per_branch":
        student.groupby("Branch")["Percentage"].max(),

        "lowest_percent_per_branch":
        student.groupby("Branch")["Percentage"].min(),

        "branch_summary":
        student.groupby("Branch")["Percentage"].agg(
            ["mean", "max", "min", "count"]
        ),

        "topper_per_branch":
        student.loc[top],
    }


# ============================================================
# 7. Statistics
# ============================================================

def statistics(student):
    """Generate descriptive statistics."""

    columns = [
        "Math",
        "Physics",
        "Chemistry",
        "English",
        "Percentage",
    ]

    return {

        "description":
        student.describe(),

        "mean":
        student[columns].mean(),

        "median":
        student[columns].median(),

        "mode":
        student[columns].mode(),

        "std":
        student[columns].std(),

        "variance":
        student[columns].var(),

        "correlation":
        student[columns].corr(),

        "branch_count":
        student["Branch"].value_counts(),

        "grade_count":
        student["Grade"].value_counts(),
    }


# ============================================================
# 8. Export Reports
# ============================================================

def export_reports(student, filtered, sorted_data, groupby_result):
    """Export analysis reports."""

    student.to_csv(
        "./output/student_analysis.csv",
        index=False
    )

    student.to_csv(
        "./output/students_cleaned.csv",
        index=False
    )

    sorted_data["top_10"].head(10).to_csv(
        "./output/top_10_students.csv",
        index=False
    )

    sorted_data["below_10"].head(10).to_csv(
        "./output/bottom_10_students.csv",
        index=False
    )

    filtered["failedstudent"].to_csv(
        "./output/failed_students.csv",
        index=False
    )

    filtered["lowattendance"].to_csv(
        "./output/low_attendance_students.csv",
        index=False
    )

    filtered["csetop"].to_csv(
        "./output/cse_top_students.csv",
        index=False
    )

    groupby_result["branch_summary"].to_csv(
        "./output/branch_summary.csv"
    )

    groupby_result["topper_per_branch"].to_csv(
        "./output/branch_toppers.csv",
        index=False
    )

    print("\n✅ All reports exported successfully!")


# ============================================================
# Main
# ============================================================

def main():

    student = load_data()

    student = clean_data(student)

    student = feature_engineering(student)

    filtered = filtering(student)

    sorted_data = sorting(student)

    groupby_result = groupby_analysis(student)

    stats = statistics(student)

    print("\nBranch Distribution:")
    print(stats["branch_count"])

    print("\nGrade Distribution:")
    print(stats["grade_count"])

    export_reports(
        student,
        filtered,
        sorted_data,
        groupby_result,
    )


if __name__ == "__main__":
    main()