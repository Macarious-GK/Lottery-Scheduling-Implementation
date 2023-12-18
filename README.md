# Lottery-Scheduling-Implementation
 # Lottery Scheduler

## Overview
This Python script simulates a lottery scheduler using classes and methods. The lottery scheduler randomly selects a winning ticket among different processes based on their allocated percentages.

## Classes

- **`task`:** 
  - Represents a process with a name, percentage allocation, and a ticket list.

- **`Lotery_scheduler`:** 
  - Manages the lottery scheduling process by adding processes and their ticket allocations.

## Usage

1. **Creating Processes:**
    Instantiate the `task` class to create processes.
    ```python
    P_1 = task('Coping Process', 5, [])  # 50% of Total tickets number
    ```

2. **Initializing Scheduler:**
    Initialize the `Lotery_scheduler` class with the total number of tickets.
    ```python
    S = Lotery_scheduler(10)  # Total tickets number
    S.Adding_Process(P_1)
    ```

3. **Run Scheduler:**
    Run the scheduler using `Run_scheduler` to get the winning process based on ticket allocation.
   first we disrupte the tickets among the process then run the scheduler to pick one lucky number.
    ```python
    S.Ticket_disruption()
    S.Run_scheduler()
    ```

5. **Testing:**
    Simulate and test the scheduler by running it multiple times.
   Creating empty list to append all the process in order to count the how many times process run and find the persentage of CPU usage..
    ```python
    L = []
    for i in range(100):
        L.append(S.Run_scheduler())
    print(f"Coping Process: {round((L.count('Coping Process')/100)*100,2)}%, Gamming: {round((L.count('Gamming')/100)*100,2)}% Downloading: {round((L.count('Downloading')/100)*100,2)}%")
    ```

## Testing
The code includes a test section that simulates the scheduler's functionality by running it 100 times and calculating the percentage of wins for each process.


