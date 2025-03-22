# Agent-Based Model for Agile Project Management

## Project Overview
This project implements an **Agent-Based Model (ABM)** to simulate agile project management scenarios. The model evaluates the optimal combination of resources to deliver a project within a fixed time while accounting for factors like experience levels, leaves, attrition, collaboration overhead, and productivity. 

## Objective
The primary goal is to determine the **best mix of developers and testers** to complete a fixed number of tasks within a specified time while minimizing resource utilization and effort.

## Features
- **Agents:** Developers and testers with varying experience levels (Junior, Mid, Senior).
- **Tasks:** Randomly generated with different complexity levels.
- **Project Management:** Simulates collaboration, task completion, and productivity.
- **Constraints:**
  - Leaves and attrition using probabilistic functions.
  - Collaboration overhead based on team size.
  - Efficiency impacted by experience level.
- **Visualization:** Generates insightful graphs to analyze completion time, total effort, and resource utilization.

## Simulation Parameters
- Fixed Days: **Number of days in which the Project is expected to be completed**
- Number of Tasks: **Count of tasks involved as single units of work**
- Number of Developers: **Range of number of developers that can be afforded**
- Number of Testers: **Range of number of testers that can be afforded**
- Leave Probability: **Probability for a resource to take leave on a given day**
- Attrition Probability: **Probability for a resource to leave the project in between**
- Efficiency Assumption Levels:
  - **Junior**: 1 unit/day
  - **Mid**: 2 units/day
  - **Senior**: 3 units/day

## How It Works
1. **Initialization:** Creates developers and testers with random experience levels.
2. **Simulation:** Runs day-by-day, where agents work on tasks.
3. **Task Progress:** Developers reduce task complexity, testers may find bugs.
4. **Collaboration Overhead:** Efficiency is reduced with larger team sizes.
5. **Completion Check:** The simulation tracks time, total effort, and active agents.

## Visualizations
- **Completion Time vs. Number of Developers and Testers**
- **Total Effort vs. Team Composition**
- **Resource Utilization vs. Completion Time**

## Project Structure
```
agile_project_management_model/
│
├── system.py          # Main simulation script
├── agent.py           # Defines agent classes and manages tasks and projects
├── parameters.py      # Constants and parameters
└── README.md          # Project documentation
```

## Requirements
- Python 3.8+
- Required Libraries: 
  ```bash
  pip install matplotlib seaborn pandas
  ```

## Run Instructions
1. Clone the repository.
   ```bash
   git clone <repository_url>
   cd agile_project_model
   ```
2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation.
   ```bash
   python system.py
   ```
4. Visualize results using the generated graphs.

## Conclusion
This agent-based model effectively demonstrates how agile project management can be optimized using simulations. The insights from the visualizations can be applied to real-world project planning to achieve better resource allocation and productivity.

## Future Enhancements
- Add more detailed metrics like bug fix time and rework.
- Implement more realistic scenarios with dynamic task generation.
- Introduce customizable agent behavior based on performance history.
- Extend this model to other working environments like construction sites, etc.

## Contact
For any queries or contributions, feel free to reach out!

