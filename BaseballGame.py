# You are keeping the scores for a baseball game with strange rules. At the beginning of the game,
# you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply
# to the record and is one of the following:
#
#     An integer x.
#         Record a new score of x.
#     '+'.
#         Record a new score that is the sum of the previous two scores.
#     'D'.
#         Record a new score that is the double of the previous score.
#     'C'.
#         Invalidate the previous score, removing it from the record.
#
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and
# that all operations are valid.

class Solution(object):
    def calpoints(self, ops: list[str]) -> int:
        stack = []

        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])  # somando os dois últimos números que aparecerem
                # (and keeping track of them for the two other operators)
            elif op == "D":
                stack.append(2 * stack[-1])  # multiplicando eles
            elif op == "C":
                stack.pop()
            else:  # vai ser um número ou uma string que será convertida em número (int)
                stack.append(int(op))

        return sum(stack)

# O(n)
