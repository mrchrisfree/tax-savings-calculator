import streamlit as st

def calculate_savings(num_returns, competitor_fee, charge_per_return, overhead_costs):
    tomahawk_cost = 1000 + min(750, num_returns * (750 / num_returns))  # Tomahawk Tax pricing cap
    competitor_cost = num_returns * competitor_fee
    savings = competitor_cost - tomahawk_cost
    revenue = num_returns * charge_per_return
    net_profit_tomahawk = revenue - (tomahawk_cost + overhead_costs)
    net_profit_competitor = revenue - (competitor_cost + overhead_costs)
    return tomahawk_cost, competitor_cost, savings, net_profit_tomahawk, net_profit_competitor

st.title("🔢 Tax Prep Profit & Savings Calculator")
st.subheader("See how much you're overpaying for tax software—and how much more profit you could keep with Tomahawk Tax!")

# User inputs
num_returns = st.number_input("📌 Number of Returns Filed Per Year:", min_value=1, value=100)
competitor_fee = st.number_input("💰 Competitor Software's Per-Return Fee ($):", min_value=1, value=50)
charge_per_return = st.number_input("📊 How Much You Charge Per Return ($):", min_value=1, value=250)
overhead_costs = st.number_input("🏢 Your Annual Overhead Costs (Office, Marketing, etc.) ($):", min_value=0, value=5000)

if st.button("💡 Calculate My Savings & Profits"):
    tomahawk_cost, competitor_cost, savings, net_profit_tomahawk, net_profit_competitor = calculate_savings(
        num_returns, competitor_fee, charge_per_return, overhead_costs)
    
    st.success(f"✅ With Tomahawk Tax, your total software cost is: **${tomahawk_cost:,.2f}**")
    st.error(f"⚠️ With Competitor Software, your total cost is: **${competitor_cost:,.2f}**")
    st.info(f"💰 Your potential savings by switching: **${savings:,.2f} per year!**")
    
    st.subheader("📈 Your Profit Comparison:")
    st.write(f"**💵 Net Profit with Tomahawk Tax:** ${net_profit_tomahawk:,.2f}")
    st.write(f"**💸 Net Profit with Competitor Software:** ${net_profit_competitor:,.2f}")
    
    st.markdown("---")
    st.subheader("🚀 Want to See How Tomahawk Can Save You More?")
    st.markdown("[👉 Book a Free Demo Here](#)")
