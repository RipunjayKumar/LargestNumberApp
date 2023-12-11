import streamlit as st


def is_valid_number(num):
  """
  Checks if the input is a valid number.
  """
  try:
    float(num)
    return True
  except ValueError:
    return False


def find_largest(num1, num2, num3):
  """
  Finds the largest number among three input numbers.
  """
  try:
    largest = max(num1, num2, num3)
    return largest
  except TypeError:
    return "Invalid input. Please enter valid numbers."


st.title("Find the Largest Number!")

# User inputs for three numbers
num1 = st.text_input("Enter the first number: ")
num2 = st.text_input("Enter the second number: ")
num3 = st.text_input("Enter the third number: ")

# Validate user inputs
if not all(is_valid_number(num) for num in [num1, num2, num3]):
  st.error("Invalid input. Please enter valid numbers.")
else:
  # Convert input strings to floats
  num1, num2, num3 = [float(num) for num in [num1, num2, num3]]

  # Button to trigger calculation
  if st.button("Find Largest"):
    # Call the function to find the largest number
    largest_number = find_largest(num1, num2, num3)

    # Display the result based on the output type
    if isinstance(largest_number, str):
      st.error(largest_number)
    else:
      st.write(f"The largest number is: {largest_number}")

# Additional information
st.markdown("""
This app allows you to find the largest number among three given numbers. It accepts both positive and negative values, as well as decimal numbers.

Please enter valid numbers. You will be notified if any invalid input is detected.
""")
