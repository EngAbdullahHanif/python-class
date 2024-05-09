# Divide and Conquer

## Definition

Divide and Conquer is a problem-solving strategy where a complex problem is broken down into smaller, more manageable subproblems. These subproblems are solved independently, and their solutions are then combined to solve the original problem.

## How it Works

1. **Divide**: The problem is divided into smaller subproblems that are similar to the original problem but simpler in nature.
2. **Conquer**: Each subproblem is recursively solved. If a subproblem is simple enough to be solved directly, it is solved using a base case condition.
3. **Combine**: The solutions to the subproblems are combined to obtain the solution to the original problem.

# Recursive

## Definition

Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. It involves breaking down a problem into smaller instances of the same problem until a base case is reached, upon which the function returns a result.

## How it Works

1. **Base Case**: The recursion terminates when a base case is reached. The base case defines the simplest instance of the problem that can be solved directly without further recursion.
2. **Recursive Step**: The function calls itself with modified parameters to solve smaller instances of the problem. Each recursive call reduces the problem size, moving closer to the base case.
3. **Iteration**: The recursive calls continue until the base case is reached, at which point the function returns a result. The results from each recursive call are combined to obtain the final result.
