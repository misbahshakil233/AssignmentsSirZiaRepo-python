import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return round(weight / (height ** 2), 2)

def main():
    st.title("BMI Calculator")
    st.write("Check your Body Mass Index (BMI) and understand your health status.")

    weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI: {bmi}")

            if bmi < 18.5:
                st.warning("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese. Consider a healthier lifestyle.")
        else:
            st.error("Please enter a valid height.")

if __name__ == "__main__":
    main()
