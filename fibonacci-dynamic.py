# Dynamic fibonacci implementation
# Time complexity: O(n)
# Space complexity: O(n)


def fibonacci(n, memo={}):
    if(n<=2):
        return 1
    if(n in memo):
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]


print(fibonacci(7))