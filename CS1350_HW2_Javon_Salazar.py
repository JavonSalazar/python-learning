# Homework 2
# Name: Javon Salazar
# Date: 2/2/26
#Description: 

# Problem 1: Movie Rating Analyzer

print("\n=== Problem 1: Movie Rating Analyzer ===")
ratings = {
    "Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
    "Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
    "Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
    "Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
    "Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}

print("=== User Statistics ===")

# Part A: User statistics
for user, movies in ratings.items():
    num_movies = len(movies)
    avg_rating = sum(movies.values()) / num_movies
    favorite_movie = max(movies, key=movies.get)
    favorite_score = movies[favorite_movie]

    print(f"{user}: {num_movies} movies, avg rating: {avg_rating:.2f}, "
          f"favorite: {favorite_movie} ({favorite_score})")

# Part B: Movie statistics
movie_stats = {}

for user, movies in ratings.items():
    for movie, score in movies.items():
        if movie not in movie_stats:
            movie_stats[movie] = {"ratings": []}
        movie_stats[movie]["ratings"].append(score)

# This calculates the average and count
for movie in movie_stats:
    scores = movie_stats[movie]["ratings"]
    movie_stats[movie]["avg"] = sum(scores) / len(scores)
    movie_stats[movie]["count"] = len(scores)
    
print("\n=== Movie Statistics ===")

# This sorts by the average going down
sorted_movies = sorted(movie_stats.items(),
                       key=lambda x: x[1]["avg"],
                       reverse=True)

for movie, stats in sorted_movies:
    print(f"{movie}: {stats['avg']:.2f} avg ({stats['count']} reviews)")

# Part C : Recommends movies with an average >= 4.0
print("\n=== Recommendations ===")
recommended_movies = {m for m, s in movie_stats.items() if s["avg"] >= 4.0}
print("Movies with avg >= 4.0:", recommended_movies)

# This will print out the recommendations for Alice
alice_movies = set(ratings["Alice"].keys())
alice_recommendations = recommended_movies - alice_movies
print("Recommendations for Alice:", alice_recommendations)


# Problem 2: Sales Data Transformer

print("\n=== Problem 2: Sales Data Transformer ===")
sales_records = [
    {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5, "region": "North"},
    {"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50, "region": "North"},
    {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8, "region": "South"},
    {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20, "region": "South"},
    {"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3, "region": "South"},
    {"product": "Keyboard", "category": "Electronics", "price": 75, "quantity": 30, "region": "North"},
    {"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5, "region": "North"},
    {"product": "Monitor", "category": "Electronics", "price": 300, "quantity": 12, "region": "South"},
]
# Part A: Comprehensions
print("\n=== Part A: Comprehensions ===")

# Finds the price for each product
product_prices = {r["product"]: r["price"] for r in sales_records}
print("Product prices:", product_prices)

# Takes only products with price > 100
expensive_products = {p: price for p, price in product_prices.items() if price > 100}
print("Expensive products (>$100):", expensive_products)

# Makes the item Premium or Standard 
price_category = {p: ("Premium" if price >= 300 else "Standard")
                  for p, price in product_prices.items()}
print("Price categories:", price_category)

# Part B: Aggregations
print("\n=== Part B: Aggregations ===")
total_by_category = {}
total_by_region = {}
quantity_by_product = {}

for record in sales_records:
    revenue = record["price"] * record["quantity"]
    # Takes the total revenue per category
    total_by_category[record["category"]] = \
        total_by_category.get(record["category"], 0) + revenue
    # Takes the total revenue per region
    total_by_region[record["region"]] = \
        total_by_region.get(record["region"], 0) + revenue
    # Takes the total quanity sold per product
    quantity_by_product[record["product"]] = \
        quantity_by_product.get(record["product"], 0) + record["quantity"]

print("Revenue by category:", total_by_category)
print("Revenue by region:", total_by_region)
print("Quantity by product:", quantity_by_product)


# Problem 3: Course Registration System
print("\n=== Problem 3: Course Registration System ===")
registrations = {
    "Alice": {"CS101", "CS201", "MATH101"},
    "Bob": {"CS101", "MATH101", "PHYS101"},
    "Carol": {"CS201", "CS301", "MATH201"},
    "Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
    "Eve": {"CS301", "MATH201", "MATH301"}
}

prerequisites = {
    "CS101": set(),
    "CS201": {"CS101"},
    "CS301": {"CS201"},
    "MATH101": set(),
    "MATH201": {"MATH101"},
    "MATH301": {"MATH201"},
    "PHYS101": {"MATH101"}
}

# Part A: Set Operations
print("\n=== Part A: Set Operations ===")

# 1 Finds all unique courses with at least one student and sets a union
all_courses = set().union(*registrations.values())
print("All courses with enrollment:", all_courses)

# 2 Finds a class all studens have a intersection
common_courses = set.intersection(*registrations.values())
print("Courses ALL students share:", common_courses)

# 3 Finds courses only Alice is taking
other_students = set().union(*(v for k, v in registrations.items() if k != "Alice"))
only_alice = registrations["Alice"] - other_students
print("Courses ONLY Alice takes:", only_alice)

# 4 Finds students in any CS courses
students_in_cs = {student for student, courses in registrations.items()
                  if any(course.startswith("CS") for course in courses)}
print("Students in CS courses:", students_in_cs)

# Part B: Prerequisite Check
print("\n=== Part B: Prerequisite Check ===")

# Finds and prints if a student's registration is valid if not prints what they are missing
for student, courses in registrations.items():
    valid = True
    missing_info = []

    for course in courses:
        required = prerequisites[course]
        missing = required - courses
        if missing:
            valid = False
            missing_info.append((course, required, missing))

    if valid:
        print(f"{student}: VALID")
    else:
        print(f"{student}: INVALID - Missing prerequisites:")
        for course, required, missing in missing_info:
            print(f"  {course} requires {required} but missing: {missing}")

# Part C: Enrollment Analysis
print("\n=== Part C: Enrollment Analysis ===")

# 1 Finds students who are "overloaded" taking 4+ courses
overloaded = {s for s, c in registrations.items() if len(c) >= 4}
print("Overloaded students (4+ courses):", overloaded)

# 2 Finds all Math courses being taken by anyone
math_courses = {course for courses in registrations.values()
                for course in courses if course.startswith("MATH")}
print("All MATH courses enrolled:", math_courses)

# 3 Finds pairs of identical schedules
found_pair = False
students = list(registrations.keys())

for i in range(len(students)):
    for j in range(i+1, len(students)):
        if registrations[students[i]] == registrations[students[j]]:
            print("Identical schedules:", students[i], "and", students[j])
            found_pair = True

if not found_pair:
    print("Students with identical schedules: None found")

# 4 Calculates enrollment count and find under enrolled courses
enrollment_count = {}

for courses in registrations.values():
    for course in courses:
        enrollment_count[course] = enrollment_count.get(course, 0) + 1

print("\nEnrollment per course:")
for course, count in enrollment_count.items():
    print(f"  {course}: {count} students")

under_enrolled = {course for course, count in enrollment_count.items() if count < 3}
print("\nUnder-enrolled courses (<3 students):", under_enrolled)

