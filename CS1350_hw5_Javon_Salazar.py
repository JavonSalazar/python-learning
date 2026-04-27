# Homework 4
# Name: Javon Salazar
# Date: 3/20/26
#Description: This homework covers over Polymorphism and abstract classes, Class methods and static methods, Operator overloading and magic methods.

#Problem 1: Employee Payroll System
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def pay_stub(self):
        pay = self.calculate_pay()
        return f"{self.name} (ID: {self.employee_id}): ${pay:.2f}"

    @staticmethod
    def validate_positive(value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive!")
        return True


class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.validate_positive(annual_salary, "annual_salary")
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 24

    def description(self):
        return f"Salaried: {self.name}"


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.validate_positive(hourly_rate, "hourly_rate")
        self.validate_positive(hours_worked, "hours_worked")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            overtime = self.hours_worked - 40
            return (40 * self.hourly_rate) + (overtime * self.hourly_rate * 1.5)

    def description(self):
        return f"Hourly: {self.name}"


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)

        self.validate_positive(base_salary, "base_salary")
        self.validate_positive(sales, "sales")
        self.validate_positive(commission_rate, "commission_rate")

        if commission_rate > 1.0:
            raise ValueError("commission_rate must be positive!")

        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_pay(self):
        return self.base_salary + (self.sales * self.commission_rate)

    def description(self):
        return f"Commission: {self.name}"


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self.employees)

    def print_all_stubs(self):
        for emp in self.employees:
            print(emp.pay_stub())



if __name__ == "__main__":
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)

    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.description()}")

    print("\nPay Stubs:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.pay_stub()}")

    payroll = Payroll()
    payroll.add_employee(alice)
    payroll.add_employee(bob)
    payroll.add_employee(carol)

    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")

    print("\nTesting validation:")
    try:
        bad = SalariedEmployee("Bad", "E999", -50000)
    except ValueError as e:
        print(f"  Caught: {e}")

    try:
        bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
    except ValueError as e:
        print(f"  Caught: {e}")
        

#Problem 2: Music Libary
class Song:
    total_songs = 0

    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        Song.total_songs += 1

    def display(self):
        return f"{self.title} - {self.artist} ({self.format_duration(self.duration_seconds)})"

    @classmethod
    def from_string(cls, s):
        title, artist, duration = s.split(" | ")
        seconds = cls.parse_duration(duration)
        return cls(title, artist, seconds)

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @staticmethod
    def format_duration(seconds):
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes}:{sec:02d}"

    @staticmethod
    def parse_duration(duration_str):
        minutes, seconds = map(int, duration_str.split(":"))
        return minutes * 60 + seconds


class Playlist:
    total_playlists = 0

    def __init__(self, name):
        Playlist.total_playlists += 1
        self.name = name
        self.playlist_id = f"PL_{Playlist.total_playlists:03d}"
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration_seconds for song in self.songs)

    def display(self):
        return f"Playlist: {self.name} ({len(self.songs)} songs, {Song.format_duration(self.total_duration())})"

    @classmethod
    def get_total_playlists(cls):
        return cls.total_playlists


class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name, song_strings):
        playlist = Playlist(name)
        for s in song_strings:
            playlist.add_song(Song.from_string(s))
        return playlist

    @staticmethod
    def format_library_report(playlists):
        report = "=== LIBRARY REPORT ===\n"

        for playlist in playlists:
            report += f"Playlist: {playlist.name}\n"
            for i, song in enumerate(playlist.songs, start=1):
                report += f"  {i}. {song.display()}\n"
            report += f"  Duration: {Song.format_duration(playlist.total_duration())}\n\n"

        report += f"Total Songs: {Song.get_total_songs()}\n"
        report += "======================"
        return report

#Problem 3: GradeBook
class GradeBook:
    def __init__(self, course_name):
        self.course_name = course_name
        self.grades = {}

    # --- Display ---
    def __str__(self):
        return f"GradeBook: {self.course_name} ({len(self.grades)} students)"

    def __repr__(self):
        return f"GradeBook('{self.course_name}')"

    # --- Container Protocol ---
    def __len__(self):
        return len(self.grades)

    def __getitem__(self, student):
        if student not in self.grades:
            raise KeyError(student)
        return self.grades[student]

    def __setitem__(self, student, grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.grades[student] = grade

    def __contains__(self, student):
        return student in self.grades

    def __iter__(self):
        return iter(self.grades)

    def __bool__(self):
        return len(self.grades) > 0

    # --- Property ---
    @property
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    # --- Arithmetic ---
    def __add__(self, other):
        new_gb = GradeBook(f"{self.course_name} + {other.course_name}")

        # copy current
        for student, grade in self.grades.items():
            new_gb[student] = grade

        # merge other
        for student, grade in other.grades.items():
            if student in new_gb:
                new_gb[student] = max(new_gb[student], grade)
            else:
                new_gb[student] = grade

        return new_gb

    def __iadd__(self, other):
        for student, grade in other.grades.items():
            if student in self.grades:
                self.grades[student] = max(self.grades[student], grade)
            else:
                self.grades[student] = grade
        return self

    def __mul__(self, factor):
        new_gb = GradeBook(f"{self.course_name} (curved)")
        for student, grade in self.grades.items():
            new_grade = min(grade * factor, 100)
            new_gb[student] = new_grade
        return new_gb

    # --- Comparison ---
    def __eq__(self, other):
        return abs(self.average - other.average) < 0.01

    def __lt__(self, other):
        return self.average < other.average

    def __le__(self, other):
        return self.average <= other.average