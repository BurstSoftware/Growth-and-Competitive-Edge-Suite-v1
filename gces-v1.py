import streamlit as st
import qrcode
from PIL import Image
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page configuration
st.set_page_config(page_title="Growth & Competitive Edge Suite", layout="wide")

# Sidebar for navigation
st.sidebar.title("Growth Suite")
tool = st.sidebar.selectbox("Select Tool", [
    "AI Advertising Writer",
    "Business Marketing Checklist",
    "Competitive Analysis Dashboard",
    "Static QR Code Generator",
    "Tool, Business, and Service Finder"
])

# Main title
st.title("Growth & Competitive Edge Suite")
st.markdown("A SaaS platform to accelerate business growth and outpace competitors.")

# Tool 1: AI Advertising Writer
if tool == "AI Advertising Writer":
    st.header("AI Advertising Writer")
    st.write("Generate targeted ad content to drive customer acquisition.")
    
    # Input fields
    product_name = st.text_input("Product/Service Name", "Your Product")
    target_audience = st.text_input("Target Audience", "e.g., Young Professionals")
    key_benefit = st.text_input("Key Benefit", "e.g., Save Time")
    
    if st.button("Generate Ad Copy"):
        # Simulated AI-generated ad copy (replace with actual AI model in production)
        ad_copy = f"🚀 Discover {product_name}! {key_benefit} for {target_audience}. Act now and transform your future! #Growth"
        st.success("Generated Ad Copy:")
        st.write(ad_copy)
        st.info("SaaS Feature: Analyze campaign performance and suggest optimizations (coming soon).")

# Tool 2: Business Marketing Checklist
elif tool == "Business Marketing Checklist":
    st.header("Business Marketing Checklist")
    st.write("Ensure a comprehensive marketing strategy with actionable tasks.")
    
    # Sample checklist (can be integrated with analytics in SaaS)
    checklist = {
        "Define Target Audience": False,
        "Set Campaign Goals": False,
        "Create Ad Content": False,
        "Choose Marketing Channels": False,
        "Track KPIs": False,
        "Optimize Campaigns": False
    }
    
    st.subheader("Marketing Tasks")
    for task, checked in checklist.items():
        checklist[task] = st.checkbox(task, value=checked)
    
    if st.button("Save Checklist"):
        st.success("Checklist saved!")
        st.info("SaaS Feature: Integrate with analytics to track KPIs for each task (coming soon).")

# Tool 3: Competitive Analysis Dashboard
elif tool == "Competitive Analysis Dashboard":
    st.header("Competitive Analysis Dashboard")
    st.write("Gain insights into competitors’ pricing, marketing, and offerings.")
    
    # Simulated competitor data (replace with web scraping or API in production)
    competitors = {
        "Competitor": ["Competitor A", "Competitor B", "Competitor C"],
        "Pricing": [99, 149, 79],
        "Market Share": [40, 35, 25],
        "Ad Spend": [5000, 7000, 3000]
    }
    df = pd.DataFrame(competitors)
    
    # Display data table
    st.subheader("Competitor Data")
    st.dataframe(df)
    
    # Visualizations
    st.subheader("Competitor Insights")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Pricing Comparison")
        fig, ax = plt.subplots()
        sns.barplot(x="Competitor", y="Pricing", data=df, ax=ax)
        st.pyplot(fig)
    
    with col2:
        st.write("Market Share")
        fig, ax = plt.subplots()
        df.plot(kind="pie", y="Market Share", labels=df["Competitor"], autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)
    
    st.info("SaaS Feature: Pull real-time data from web scraping or X posts (coming soon).")

# Tool 4: Static QR Code Generator
elif tool == "Static QR Code Generator":
    st.header("Static QR Code Generator")
    st.write("Link marketing campaigns to digital assets.")
    
    # Input URL
    url = st.text_input("Enter URL for QR Code", "https://example.com")
    
    if st.button("Generate QR Code"):
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        
        # Save and display QR code
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")
        st.image(img_buffer, caption="Generated QR Code")
        
        # Download option
        st.download_button(
            label="Download QR Code",
            data=img_buffer.getvalue(),
            file_name="qr_code.png",
            mime="image/png"
        )
        st.info("SaaS Feature: A/B testing for QR code destinations (coming soon).")

# Tool 5: Tool, Business, and Service Finder
elif tool == "Tool, Business, and Service Finder":
    st.header("Tool, Business, and Service Finder")
    st.write("Find vendors or tools to act on competitive insights.")
    
    # Simulated vendor database (replace with real database in production)
    vendors = {
        "Name": ["Vendor A", "Vendor B", "Vendor C"],
        "Service": ["Supplier", "Marketing Tool", "Analytics Platform"],
        "Rating": [4.5, 4.0, 4.8]
    }
    df_vendors = pd.DataFrame(vendors)
    
    # Search functionality
    search_term = st.text_input("Search for a service (e.g., Supplier, Marketing Tool)", "")
    if search_term:
        filtered_vendors = df_vendors[df_vendors["Service"].str.contains(search_term, case=False)]
        st.dataframe(filtered_vendors)
    else:
        st.dataframe(df_vendors)
    
    st.info("SaaS Feature: Searchable database with reviews and ratings (coming soon).")

# Footer
st.markdown("---")
st.markdown("**Growth & Competitive Edge Suite** - A SaaS platform for businesses to outpace competitors with data-driven strategies.")
st.markdown("Future Features: Automation, real-time competitor data, and integrated analytics.")
