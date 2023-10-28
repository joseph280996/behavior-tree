# Assumptions made

1. The nodes of the tree are assumed created in the top-down left-right order from the given behavior tree.
2. For priority nodes, I'm assuming that its children are instantiated in order (i.e. from left to right) which allows id field to be in ascending order so I can use that as the metric for priority ranking.
3. For Dock task, I'll make an unrealistic assumption that the moment the Romba dock, it will automatically charge the battery to 100%
4. I'm going to make the assumption that the battery level is going to drop every 2 seconds.
5. In the assignment statements, it states that tasks (besides DONE GENERAL and DONE SPOT) don't need to be implemented, I'll assume that all tasks functionality are implemented except the mentioned tasks and the moving to the next spot functionality in reality is going to be implemented.
6. I'll make the assumption that the only time the clean floor fails is when there is nothing else to clean. 
7. In this implementation, I'll also assume that the parameters stored in the Blackboard is going to be changed only at the beginning of the the program. And the BT is going to execute based on this initial state to the end of the program.
8. The condition to terminate the program is once the BT has done its valuation and executed all the tasks as required. So I'm assuming the testing procedure will require restarting the program for every test scenarios.
