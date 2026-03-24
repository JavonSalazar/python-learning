#Problem 1: Word Analyzer
import string

def analyze_text(text):
    clean = ''.join(c.lower() if c.isalpha() or c == ' ' else '' for c in text)
    words = clean.split()

    word_counts = {}
    for w in words:
        word_counts[w] = word_counts.get(w, 0) + 1

    most_common = max(word_counts, key=word_counts.get)

    unique_count = sum(1 for v in word_counts.values() if v == 1)

    return {
        "word_counts": word_counts,
        "most_common": most_common,
        "unique_count": unique_count
    }

#Problem 2: Roster
class Roster:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = set()

    def enroll(self, name):
        self.students.add(name)

    def drop(self, name):
        self.students.discard(name)

    def is_enrolled(self, name):
        return name in self.students


def common_students(r1, r2):
    return r1.students & r2.students


def exclusive_students(r1, r2):
    return r1.students ^ r2.students


def print_report(rosters):
    for r in rosters:
        print(f"{r.course_name}: {len(r.students)} students")

    common = set.intersection(*(r.students for r in rosters))
    print("Enrolled in all courses:", common)