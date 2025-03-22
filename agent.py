# Defines agent classes and manages tasks and projects

import random
from parameters import LEAVE_PROBABILITY, ATTRITION_PROBABILITY, EFFICIENCY, MIN_COMPLEXITY, MAX_COMPLEXITY

class Agent:
    def __init__(self, agent_id, experience_level, role):
        self.agent_id = agent_id
        self.experience_level = experience_level
        self.role = role
        self.completed_tasks = 0
        self.on_leave = False # Default is set to False, but can be updated as per take_leave() logic
        self.active = True # By default, all are active, may leave the project later on

    # Agent works on the task until its completion
    def work_on_task(self, task):
        if not self.active or self.on_leave:
            return False
        efficiency = EFFICIENCY[self.experience_level]
        task.completion_time -= efficiency
        if task.completion_time <= 0:
            self.completed_tasks += 1
            return True
        return False

    # Function to put an agent on leave randomly in comparison to the LEAVE_PROBABILITY
    def take_leave(self):
        self.on_leave = random.random() < LEAVE_PROBABILITY

    # Function to set an agent to leave the project and stop contributing randomly in comparison to the ATTRITION_PROBABILITY
    def attrition_check(self):
        if random.random() < ATTRITION_PROBABILITY:
            self.active = False

# Task class defines an individual task
class Task:
    def __init__(self, complexity):
        self.complexity = complexity
        self.completion_time = complexity
        self.bugs = 0

# Project class defines the complete project which may have multiple tasks as its parts
class Project:
    def __init__(self, num_tasks):
        self.tasks = [Task(random.randint(MIN_COMPLEXITY, MAX_COMPLEXITY)) for _ in range(num_tasks)] # Complexity for each task assigned on random between the range defined
        self.completed_tasks = 0

    def check_completion(self):
        return all(task.completion_time <= 0 for task in self.tasks)