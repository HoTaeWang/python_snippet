from collections import deque
# Create a deque
t_deque = deque()
# Add elements to the deque
t_deque.append("Harry")  # Add to the right 
t_deque.append("Ron")    # Add to the right     
t_deque.append("Hermione")  # Add to the right
# Add to the left   
t_deque.appendleft("Draco")  # Add to the left
# Add to the left
t_deque.appendleft("Neville")  # Add to the left    
# Display the deque
print("Deque after adding elements:")   
print(t_deque)  # Output: deque(['Neville', 'Draco', 'Harry', 'Ron', 'Hermione'])
# Remove elements from the deque
t_deque.pop()  # Remove from the right
t_deque.popleft()  # Remove from the left
# Display the deque
print("Deque after removing elements:")
print(t_deque)  # Output: deque(['Draco', 'Harry', 'Ron'])
# Access elements in the deque
print("First element:", t_deque[0])  # Output: First element: Draco
print("Last element:", t_deque[-1])  # Output: Last element: Ron
# Check if the deque is empty
print("Is deque empty?", len(t_deque) == 0)  # Output: Is deque empty? False
# Get the length of the deque
print("Length of deque:", len(t_deque))  # Output: Length of deque: 3
# Clear the deque
t_deque.clear() # Clear the deque
# Display the deque
print("Deque after clearing:", t_deque)  # Output: Deque after clearing: deque([])
