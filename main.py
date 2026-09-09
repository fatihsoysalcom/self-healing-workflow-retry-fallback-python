import random
import time

MAX_RETRIES = 3
FLAKY_SERVICE_SUCCESS_RATE = 0.6 # 60% chance of success for the primary service

def simulate_flaky_service_call(task_name):
    """
    Simulates a call to an external service that might fail due to transient issues.
    """
    # Simulate network latency or processing time
    time.sleep(0.2) 
    if random.random() < FLAKY_SERVICE_SUCCESS_RATE:
        print(f"  ✅ Primary service for '{task_name}' successful.")
        return True
    else:
        print(f"  ❌ Primary service for '{task_name}' FAILED.")
        return False

def perform_fallback_action(task_name):
    """
    Simulates a 'self-healing' fallback action when the primary service fails
    after all retries. This could be sending a notification, using a backup API,
    or logging for manual review, ensuring business continuity.
    """
    print(f"  🔄 Initiating fallback action for '{task_name}'...")
    # Simulate some processing for the fallback
    time.sleep(0.5)
    # For demonstration, assume fallback usually succeeds. In a real system,
    # the fallback itself could also potentially fail.
    print(f"  ✅ Fallback action for '{task_name}' completed. (e.g., Notified admin, logged to error queue)")
    return True

def execute_self_healing_task(task_id):
    """
    Attempts to execute a critical task with self-healing capabilities:
    retries on transient failures and a fallback action for persistent issues.
    """
    task_name = f"Workflow Step {task_id}"
    print(f"\n--- Executing {task_name} ---")
    
    # --- Error Detection and Retry Mechanism ---
    # This loop attempts the primary task multiple times to overcome transient errors.
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"  Attempt {attempt}/{MAX_RETRIES} for primary service...")
        if simulate_flaky_service_call(task_name):
            print(f"🎉 {task_name} successfully completed after {attempt} attempt(s).")
            return True # Task succeeded
        else:
            if attempt < MAX_RETRIES:
                print(f"  Primary service failed. Retrying {task_name} in 1 second...")
                time.sleep(1)
            else:
                print(f"  All {MAX_RETRIES} primary service attempts for {task_name} failed.")
    
    # --- Self-Healing Fallback Action ---
    # If all primary retries fail, a predefined fallback action is triggered
    # to recover or mitigate the failure autonomously.
    print(f"  Primary service exhausted all retries. Attempting self-healing fallback...")
    if perform_fallback_action(task_name):
        print(f"✅ {task_name} completed via fallback mechanism. Business continuity maintained.")
        return True # Task succeeded via fallback
    else:
        # If even fallback fails, then manual intervention is truly needed.
        print(f"❌ Fallback for {task_name} also failed. Manual intervention required to resolve.")
        return False # Task ultimately failed

if __name__ == "__main__":
    print("--- Simulating n8n-like Self-Healing Workflow Steps ---")
    print(f"Configuration:")
    print(f"  Primary service success rate: {FLAKY_SERVICE_SUCCESS_RATE*100}%")
    print(f"  Max retries for primary service: {MAX_RETRIES}")

    # Run multiple tasks to demonstrate different scenarios (success, retry-success, fallback-success, ultimate-failure)
    # Due to randomness, you might need to run it a few times to see all scenarios.
    execute_self_healing_task(101) # Example 1
    execute_self_healing_task(102) # Example 2
    execute_self_healing_task(103) # Example 3
    execute_self_healing_task(104) # Example 4
    
    print("\n--- Simulation Complete ---")
    print("Run the script multiple times to observe different outcomes due to randomness.")
