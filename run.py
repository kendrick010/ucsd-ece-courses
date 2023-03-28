from ucsd_ece_courses import ECECatalog

catalog = ECECatalog()

# Get ECE 5 courage descriptions, try also 'ece 5', 'ece_5', '5', etc.
course = 'ece_5'
print(catalog.course_title(course))
print(catalog.course_credit(course))
print(catalog.course_summary(course))
print(catalog.course_prerequisite(course))

# Get all course numbers and titles
print(catalog.course_numbers)
print(catalog.course_titles)