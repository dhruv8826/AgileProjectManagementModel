# Probabilities-
# - of a resource to take a leave on any given day of work
LEAVE_PROBABILITY = 0.1
# - of a resource to leave the project in between
ATTRITION_PROBABILITY = 0.02

# Efficiency of resources based on their experience, broadly classified into 3 categories
EFFICIENCY = {'Junior': 1, 'Mid': 2, 'Senior': 3}

# Collaboration overhead: Negative impact of too many resources working ona task, as more is not always good
COLLABORATION_OVERHEAD_FACTOR = 0.05

# Simulation with-
# - fixed days
FIXED_DAYS = 30
# - fixed no of tasks
FIXED_NUM_TASKS = 20
# - range of developers
MIN_DEVELOPERS = 3
MAX_DEVELOPERS = 11
# - range of testers
MIN_TESTERS = 1
MAX_TESTERS = 6
# - range of task complexity
MIN_COMPLEXITY = 5
MAX_COMPLEXITY = 20