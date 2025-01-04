import random
import matplotlib.pyplot as plt
import pandas as pd

# Function to simulate dice rolls and calculate probabilities
def simulate_dice_rolls(num_rolls):
    results = [0] * 13  # Initialize counts for sums from 0 to 12 (index 0 and 1 will not be used)

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        results[roll_sum] += 1

    probabilities = [count / num_rolls for count in results]
    return probabilities[2:]  # Return probabilities for sums 2 to 12

# Analytical probabilities for sums from 2 to 12
analytical_probs = [
    1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36
]

# Simulate dice rolls
num_rolls = 1000000  # Adjust this number for a large simulation
simulated_probs = simulate_dice_rolls(num_rolls)

# Create a DataFrame for comparison
sums = list(range(2, 13))
data = {
    "Sum": sums,
    "Analytical Probability": analytical_probs,
    "Simulated Probability": simulated_probs
}
df = pd.DataFrame(data)

# Display the DataFrame
df["Difference"] = abs(df["Analytical Probability"] - df["Simulated Probability"])
print(df)

# Plot the probabilities
plt.figure(figsize=(10, 6))
plt.plot(sums, analytical_probs, marker="o", label="Analytical Probability")
plt.plot(sums, simulated_probs, marker="x", label="Simulated Probability")
plt.title("Comparison of Analytical and Simulated Probabilities")
plt.xlabel("Sum of Dice Rolls")
plt.ylabel("Probability")
plt.legend()
plt.grid()
plt.show()

