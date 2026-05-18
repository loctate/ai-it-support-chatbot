import streamlit as st

st.title("AI IT Support Chatbot")

user_input = st.text_input(
    "Describe your IT issue:"
)

if st.button("Get Solution"):

    issue = user_input.lower()

    if "wifi" in issue:
        answer = """
1. Restart your router and modem
2. Forget and reconnect the WiFi network
3. Run Windows Network Troubleshooter
4. Check IP configuration using ipconfig
5. Test another device on the same network
"""

    elif "printer" in issue:
        answer = """
1. Check printer power and cable connection
2. Restart the printer
3. Reinstall printer drivers
4. Verify printer is set as default
5. Restart Print Spooler service
"""

    elif "slow" in issue:
        answer = """
1. Restart the computer
2. Disable unnecessary startup applications
3. Check CPU and RAM usage
4. Scan for malware
5. Free up disk space
"""

    elif "overheating" in issue:
        answer = """
1. Clean laptop fan and air vents
2. Avoid blocking ventilation
3. Close unnecessary applications
4. Check CPU usage
5. Replace thermal paste if necessary
"""

    else:
        answer = """
1. Restart the device
2. Check system connections
3. Verify software updates
4. Review system logs
5. Contact IT support if issue continues
"""

    st.subheader("Troubleshooting Steps")
    st.write(answer)