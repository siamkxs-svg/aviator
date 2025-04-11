import streamlit as st

# Prediction logic
def predict_next_round(crash_list, window=5):
    if len(crash_list) < window:
        return "Need at least {} crash values.".format(window), None

    recent = crash_list[-window:]
    low_crashes = sum(1 for c in recent if c < 1.5)
    high_crashes = sum(1 for c in recent if c > 5)

    if low_crashes >= 4:
        prediction = "High crash expected (2x+)"
        cashout = 2.0
    elif high_crashes >= 3:
        prediction = "Low crash likely (<2x)"
        cashout = 1.3
    else:
        prediction = "Stable pattern – moderate risk"
        cashout = 1.5

    return prediction, cashout

# Streamlit UI
st.set_page_config(page_title="Aviator Probability-Based Predictor", layout="centered")
st.title("🌏 Aviator Probability-Based Predictor")

st.markdown("""
Enter your latest Aviator crash multipliers below (most recent last).
Example: `1.22, 1.35, 1.10, 1.40, 1.25`
""")

user_input = st.text_input("Crash values (comma-separated):")

if user_input:
    try:
        crash_values = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        prediction, cashout = predict_next_round(crash_values)

        st.markdown("### 🔢 Recent Crashes: ")
        st.write(crash_values[-5:])

        if cashout:
            st.success(f"Prediction: {prediction}")
            st.info(f"Recommended Cashout Target: {cashout}x")
        else:
            st.warning(prediction)

    except ValueError:
        st.error("Please enter valid numbers separated by commas.")

st.markdown("---")
st.caption("This is a statistical tool, not a guaranteed predictor. Use responsibly.")
