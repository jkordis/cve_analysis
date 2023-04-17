import streamlit as st
import requests
import json
import pandas as pd

# Create a Streamlit interface
st.sidebar.title("CVE Lookup")
cve = st.sidebar.text_input("Enter CVE Number")

if st.sidebar.button("Submit"):
    if cve:
        # Add a loading bar
        with st.spinner("Searching for vulnerability details..."):
            # Send a GET request to the NVD API
            url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve}"
            response = requests.get(url)

            # Convert response to a dictionary
            data = json.loads(response.text)

            # Check if data has the expected structure
            if "result" in data and "CVE_Items" in data["result"] and data["result"]["CVE_Items"]:
                result = data["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]
                title = data["result"]["CVE_Items"][0]["cve"]["CVE_data_meta"]["ID"]
                cvss_score = result["cvssV2"]["baseScore"]
                st.write(f"Title: {title}")
                st.write(f"CVSS Score: {cvss_score}")
            else:
                st.write("No results found for the given CVE number.")
    else:
        st.write("Please enter a CVE number.")
