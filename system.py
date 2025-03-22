# Main simulation code for the model

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
from agent import Agent, Project
from parameters import EFFICIENCY, FIXED_DAYS, FIXED_NUM_TASKS, COLLABORATION_OVERHEAD_FACTOR, MIN_DEVELOPERS, MAX_DEVELOPERS, MIN_TESTERS, MAX_TESTERS


class System:
    def __init__(self):
        self.results = [] # list of results for different combinations
        self.agents = [] # list of agents

    def create_agents(self, num_devs, num_testers):
        for i in range(num_devs):
            level = random.choice(list(EFFICIENCY.keys())) # Randomly assigning efficiency to developers
            self.agents.append(Agent(f"Dev_{i}", level, "Developer"))
        for i in range(num_testers):
            self.agents.append(Agent(f"Tester_{i}", "Mid", "Tester")) # experience level for testers hard coded for now, this can be extended to test complex situations

    # Function to generate the impact of having a specified number of resources in the project
    @staticmethod
    def calculate_collaboration_overhead(num_agents):
        return min(COLLABORATION_OVERHEAD_FACTOR * num_agents, 1.0)

    # Main simulation for a project
    def run_simulation(self, num_devs, num_testers, num_tasks, days):
        project = Project(num_tasks) # Define a project
        self.create_agents(num_devs, num_testers) # create the agents for the model
        total_effort = 0

        # activity per day
        for day in range(days):
            # randomly assign some agents on leave and impact of attrition
            for agent in self.agents:
                agent.take_leave()
                agent.attrition_check()

            active_agents = [a for a in self.agents if a.active and not a.on_leave] # agents working per day
            overhead_factor = 1 - self.calculate_collaboration_overhead(len(active_agents)) # impact of overhead

            # work by agents on tasks
            for task in project.tasks:
                if task.completion_time > 0:
                    for agent in active_agents:
                        if agent.work_on_task(task):
                            task.completion_time *= overhead_factor # impact of overhead_factor on time required to complete the task
                            total_effort += EFFICIENCY[agent.experience_level]


            if project.check_completion():
                return day + 1, total_effort, len(active_agents)

        return days, total_effort, len(active_agents)

    def run_model(self):
        dev_range = range(MIN_DEVELOPERS, MAX_DEVELOPERS) # Range of developers we have
        tester_range = range(MIN_TESTERS, MAX_TESTERS) # Range of testers we have

        # Running model for different combinations of developers and testers in the project
        for num_devs in dev_range:
            for num_testers in tester_range:
                completion_time, total_effort, active_agents = self.run_simulation(num_devs, num_testers, FIXED_NUM_TASKS, FIXED_DAYS)
                self.results.append((num_devs, num_testers, completion_time, total_effort, active_agents)) # storing the results in our list
                self.agents = [] # reset the agents list for each iteration

    # Plotting the results
    def plot_results(self):
        df = pd.DataFrame(self.results, columns=["Developers", "Testers", "Completion Time", "Total Effort", "Active Agents"])

        # Plot to analyse Completion Time vs Developers and Testers
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x="Developers", y="Completion Time", hue="Testers", marker='o')
        plt.title("Completion Time vs Developers and Testers")
        plt.xlabel("Number of Developers")
        plt.ylabel("Completion Time (Days)")
        plt.legend(title="Testers")
        plt.grid(True)
        plt.show()
        plt.savefig("completion_time_vs_developers_and_testers.png")
        plt.close()

        # Plot to analyse Total Effort vs Developers and Testers
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x="Developers", y="Total Effort", hue="Testers", marker='o')
        plt.title("Total Effort vs Developers and Testers")
        plt.xlabel("Number of Developers")
        plt.ylabel("Total Effort")
        plt.legend(title="Testers")
        plt.grid(True)
        plt.show()
        plt.savefig("total_effort_vs_developers_and_testers.png")
        plt.close()

        # Plot to analyse Resource Utilization vs Completion Time
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=df, x="Completion Time", y="Active Agents", hue="Developers", size="Testers", sizes=(20, 200))
        plt.title("Resource Utilization vs Completion Time")
        plt.xlabel("Completion Time (Days)")
        plt.ylabel("Active Agents")
        plt.legend(title="Developers")
        plt.grid(True)
        plt.show()
        plt.savefig("resource_utilization_vs_completion_time.png")
        plt.close()

    def run_system(self):
        if __name__ == "__main__":
            self.run_model()
            self.plot_results()


system = System()
system.run_system()