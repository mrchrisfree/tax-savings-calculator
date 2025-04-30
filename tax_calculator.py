import streamlit as st

import streamlit as st

def calculate_savings(current_software_cost, num_returns, avg_return_fee, years, one_time_cost=989, max_annual_fee=750):
    # Current tax software cost over time
    total_current_cost = (current_software_cost + (num_returns * avg_return_fee)) * years
    
    # Tomahawk Tax cost over time
    total_tomahawk_cost = one_time_cost + min(num_returns * avg_return_fee, max_annual_fee) * years
    
    # Savings
    savings = total_current_cost - total_tomahawk_cost
    return total_current_cost, total_tomahawk_cost, savings

# Streamlit UI
st.title("Tomahawk Tax Savings Calculator!")
st.write("Compare your current tax software expenses with Tomahawk Tax and see how much you can save!")

st.write("Just insert your personalized numbers below...")


# User Inputs
current_software_cost = st.number_input("How much do you pay yearly for your current tax software? ($)", min_value=0, value=2000)
num_returns = st.number_input("How many returns do you file per year?", min_value=0, value=300)
avg_return_fee = st.number_input("Average cost per return filing? ($)", min_value=0, value=5)
years = st.number_input("How many years do you plan to continue your tax business?", min_value=1, value=5)

if st.button("Calculate Savings"):
    total_current, total_tomahawk, savings = calculate_savings(current_software_cost, num_returns, avg_return_fee, years)
    
    st.subheader("Your Savings Breakdown")
    st.write(f"**Total cost with your current software:** ${total_current:,.2f}")
    st.write(f"**Total cost with Tomahawk Tax:** ${total_tomahawk:,.2f}")
    st.write(f"**Total savings over {years} years:** ${savings:,.2f}")
    
    if savings > 0:
        st.success(f"You could save **${savings:,.2f}** over {years} years by switching to Tomahawk Tax!")
    else:
        st.info("Your costs might be similar, but Tomahawk Tax offers a **one-time purchase** and cost stability!")

st.write("Interested in big time savings with Tomahawk Tax? [Click here](https://join.tomahawktax.com/start-saving-and-growing-today) to learn more and schedule a free demo!")
