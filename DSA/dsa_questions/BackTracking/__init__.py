"""Back tracking is algorithm technique in which all possible findings all solutions matching constraint.
It is also called brute force algorithm.

Complexity ranges from O(K^N) to O(N!)

Pseudocode:

    void FIND_SOLUTIONS( parameters):
        if (valid solution):
            store the solution
            Return

        for (all choice):
            if (valid choice):
                APPLY (choice)
                FIND_SOLUTIONS (parameters)
                BACKTRACK (remove choice)
        Return

"""