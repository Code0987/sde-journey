from time import time, sleep

class SlidingWindowRateLimiter:
    def __init__(self, window_size: int, max_requests: int):
        """
        Initializes the sliding window rate limiter.

        :param window_size: Duration of the sliding window (in seconds).
        :param max_requests: Maximum number of allowed requests within the window.
        """
        now = time()
        self.window_size = window_size
        self.window = now // window_size  # Current window (integer part of division)
        self.n_previous_requests = 0  # Requests in the previous window
        self.n_requests = 0  # Requests in the current window
        self.max_requests = max_requests  # Maximum allowed requests in a window

    def allow_request(self) -> bool:
        """
        Determines if a new request can be allowed under the current rate limit.

        :return: True if the request is allowed, otherwise False.
        """
        now = time()
        current_window = now // self.window_size  # Determine which window we are in

        # If we have moved to a new window, shift the request count
        if current_window != self.window:
            self.n_previous_requests = self.n_requests  # Move current count to previous
            self.n_requests = 0  # Reset current request count for the new window
            self.window = current_window  # Update window to the current one

        # Calculate total requests in the sliding window (previous + current)
        elapsed_time_in_current_window = now % self.window_size
        weight = 1 - (elapsed_time_in_current_window / self.window_size)  # Fraction of the previous window's impact
        total_requests = (weight * self.n_previous_requests) + self.n_requests

        if total_requests < self.max_requests:
            # Allow request if under limit
            self.n_requests += 1
            return True
        else:
            # Deny request if over limit
            return False

# Example usage
rate_limiter = SlidingWindowRateLimiter(window_size=5, max_requests=2)

for i in range(100):
    if rate_limiter.allow_request():
        print(f"Request {i+1} allowed at {time()}")
    else:
        print(f"Request {i+1} denied at {time()}")
    sleep(1)
