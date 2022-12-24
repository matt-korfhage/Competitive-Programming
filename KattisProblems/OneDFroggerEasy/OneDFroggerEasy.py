class OneDFroggerEasy:

    def determineH(self, inputs, squares) -> tuple:
        return self.__determineHRecursive(inputs[0], inputs[1], inputs[2], 0, squares, set())

    def __determineHRecursive(self, n, s, m, i, squares, visited: set) -> tuple:
        if s < 1:
            return 'left', i
        elif s > n:
            return 'right', i
        elif squares[s-1] == m:
            return 'magic', i
        elif visited.__contains__(s):
            return 'cycle', i
        else:
            visited.add(s)
            return self.__determineHRecursive(n, s+squares[s-1], m, i+1, squares, visited)


nsm = input().split(" ")
nsm = [eval(x) for x in nsm]
tiles = input().split(" ")
tiles = [eval(y) for y in tiles]
solution = OneDFroggerEasy()
results = solution.determineH(nsm, tiles)
print(results[0])
print(results[1])
