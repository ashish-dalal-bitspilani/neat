class Solution:

    def __init__(self, problem):
        self.problem = problem
        print(f"This is a working solution for the problem : {self.problem}")

    @staticmethod
    def longest_binary_gap(n: int)-> int:
        binary_num =  format(n, 'b')
        binary_gaps = []
        length = 0
        for i in range(len(str(binary_num))):
            if str(binary_num)[i] == '1':
                binary_gaps.append(length)
                length = 0
                continue
            else:
                length += 1
        print(binary_gaps)
        return max(binary_gaps)

if __name__ == "__main__":
    solution = Solution("longestBinaryGap")
    print(solution.longest_binary_gap(9))#2
    print(solution.longest_binary_gap(529))#4
    print(solution.longest_binary_gap(20))#1
    print(solution.longest_binary_gap(15))#0
    print(solution.longest_binary_gap(32))#0
    print(solution.longest_binary_gap(1041))#5