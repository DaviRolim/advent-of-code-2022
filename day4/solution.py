def expand_sections(elf_range):
    elf_start, elf_end = [int(n) for n in elf_range.split('-')]
    elf_sections_expanded = set(range(elf_start, elf_end + 1))
    return elf_sections_expanded

# Condition for solution 1
def is_fully_contained(assignments_elf1, assignments_elf2):
    return assignments_elf1 <= assignments_elf2 or assignments_elf2 <= assignments_elf1

# Condition for solution 2
def has_intersection(set1, set2):
    return len(set1.intersection(set2)) > 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    overlapping_assignments = 0
    for line in lines:
        line = line.strip()
        assignment1, assignment2 = line.split(',')
        assignment1_set = expand_sections(assignment1)
        assignment2_set = expand_sections(assignment2)
        # Solution 1
        # if is_fully_contained(assignment1_set, assignment2_set): 
        # end solution 1
        # Solution 2
        if has_intersection(assignment1_set, assignment2_set): 
            overlapping_assignments += 1
print(overlapping_assignments)

