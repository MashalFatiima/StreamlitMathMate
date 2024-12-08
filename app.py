import streamlit as st
import math

def scientific_calculator(operation, num1, num2=None):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif operation == 'Square Root':
        return math.sqrt(num1)
    elif operation == 'Exponentiation':
        return math.pow(num1, num2)
    elif operation == 'Sine':
        return math.sin(math.radians(num1))
    elif operation == 'Cosine':
        return math.cos(math.radians(num1))
    elif operation == 'Tangent':
        return math.tan(math.radians(num1))
    elif operation == 'Logarithm':
        return math.log10(num1)

st.title("Scientific Calculator")

operation = st.selectbox("Select Operation", ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Square Root', 'Exponentiation', 'Sine', 'Cosine', 'Tangent', 'Logarithm'])

num1 = st.number_input("Enter first number", step=1e-6, format="%.6f")

if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation']:
    num2 = st.number_input("Enter second number", step=1e-6, format="%.6f")
else:
    num2 = None

if st.button("Calculate"):
    if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation'] and num2 is not None:
        result = scientific_calculator(operation, num1, num2)
    else:
        result = scientific_calculator(operation, num1)

    st.write(f"Result: {result}")
