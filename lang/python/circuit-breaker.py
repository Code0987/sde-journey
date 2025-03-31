import time
import functools

class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=5, success_threshold=1):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold
        
        self.failure_count = 0
        self.success_count = 0
        self.state = "CLOSED"
        self.last_failure_time = None
    
    def reset(self):
        """Resets the circuit breaker to the closed state."""
        self.failure_count = 0
        self.success_count = 0
        self.state = "CLOSED"
    
    def open_circuit(self):
        """Opens the circuit breaker."""
        self.state = "OPEN"
        self.last_failure_time = time.time()
    
    def half_open_circuit(self):
        """Moves the circuit breaker to the half-open state."""
        self.state = "HALF-OPEN"
    
    def is_open(self):
        """Returns whether the circuit breaker is open or not."""
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                # Move to half-open after the timeout expires
                self.half_open_circuit()
            return True
        return False
    
    def call(self, func):
        """Decorator to apply the circuit breaker logic to a function."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.state == "OPEN" and self.is_open():
                print("Circuit is in HALF-OPEN state, allowing limited calls")
            elif self.state == "OPEN":
                print("Circuit is OPEN, blocking requests.")
                raise Exception("Circuit is OPEN. Request blocked.")
            
            try:
                result = func(*args, **kwargs)
                
                if self.state == "HALF-OPEN":
                    self.success_count += 1
                    if self.success_count >= self.success_threshold:
                        print("Circuit is now CLOSED after successful attempts")
                        self.reset()
                
                return result
            except Exception as e:
                print(f"Function failed: {e}")
                
                self.failure_count += 1
                if self.failure_count >= self.failure_threshold:
                    print("Failure threshold reached. Circuit is now OPEN.")
                    self.open_circuit()
                raise
        
        return wrapper

# Example Usage
breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=10, success_threshold=2)

@breaker.call
def potentially_unstable_service():
    if time.time() % 2 == 0:
        raise Exception("Simulated service failure")
    return "Service success"

# Simulate multiple requests
for i in range(10):
    try:
        result = potentially_unstable_service()
        print(f"Request {i+1}: {result}")
    except Exception as e:
        print(f"Request {i+1} failed: {e}")
    time.sleep(1)
