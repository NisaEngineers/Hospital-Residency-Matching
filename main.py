def residency_match(students_preferences, hospitals_preferences, hospital_capacities):
    """
    Implements a many-to-one stable matching algorithm (Gale–Shapley variant).
    Each student proposes to hospitals based on their preference list.
    Hospitals accept students based on their own preferences and capacity.
    """
    unmatched_students = list(students_preferences.keys())  # All students start unmatched
    proposals = {student: [] for student in students_preferences}  # Track proposals made
    final_matches = {hospital: [] for hospital in hospitals_preferences}  # Hospital → list of matched students

    while unmatched_students:
        student = unmatched_students[0]  # Pick the first unmatched student

        # Student proposes to hospitals in order of preference
        for hospital in students_preferences[student]:
            if hospital not in proposals[student]:
                proposals[student].append(hospital)

                current_matches = final_matches[hospital]
                capacity = hospital_capacities[hospital]

                if len(current_matches) < capacity:
                    # Hospital has room — accept student
                    final_matches[hospital].append(student)
                    unmatched_students.pop(0)
                else:
                    # Hospital is full — check if it prefers this student over someone already matched
                    ranked_students = hospitals_preferences[hospital]
                    least_preferred = max(current_matches, key=lambda s: ranked_students.index(s))

                    if ranked_students.index(student) < ranked_students.index(least_preferred):
                        # Replace least preferred student
                        final_matches[hospital].remove(least_preferred)
                        final_matches[hospital].append(student)
                        unmatched_students.pop(0)
                        unmatched_students.append(least_preferred)  # Requeue the replaced student
                break  # Move to next student

    return final_matches



# Medical students and their hospital preferences
students = {
    'Dr. Ayesha': ['Apollo Hospital', 'GreenLife Hospital'],
    'Dr. Rafi': ['GreenLife Hospital', 'Apollo Hospital'],
    'Dr. Tanvir': ['Apollo Hospital', 'GreenLife Hospital']
}

# Hospitals and their preferences for students
hospitals = {
    'Apollo Hospital': ['Dr. Ayesha', 'Dr. Tanvir', 'Dr. Rafi'],
    'GreenLife Hospital': ['Dr. Rafi', 'Dr. Ayesha', 'Dr. Tanvir']
}

# Hospital capacity (number of residency slots)
capacities = {
    'Apollo Hospital': 2,
    'GreenLife Hospital': 1
}

# Run the matching algorithm
match_results = residency_match(students, hospitals, capacities)

# Display results
for hospital, matched_students in match_results.items():
    print(f"{hospital} matched with: {', '.join(matched_students)}")

