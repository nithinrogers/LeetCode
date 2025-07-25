class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            current_points, skip_count = questions[i]
            solve_points = current_points
            next_available = i + skip_count + 1  
            if next_available < n:  
                solve_points += dp[next_available]
            skip_points = dp[i + 1]
            dp[i] = max(solve_points, skip_points)
        return dp[0]
