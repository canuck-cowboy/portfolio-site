"""
Note 1: to run the app
    > Terminal: streamlit run main.py
"""

# Import necessary libraries
import streamlit as st  # Main library used to build Streamlit apps
from pathlib import Path  # Helps manage file paths across different operating systems
import base64

# Configure the web page:
# - page_title sets the title shown in the browser tab
# - page_icon sets the favicon (small icon in the browser tab)
st.set_page_config(
    page_title="Gareth Nassar | Network Admin",
    page_icon="🤠"  # Network emoji as icon
)

# Define file paths relative to this script's directory
# This ensures file references remain valid if the app is moved
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
profile_pic_path = current_dir / 'assets' / 'profile-pic.png'  # Profile picture file path
resume_path = current_dir / 'assets' / 'resume.pdf'            # Resume PDF file path

# Read the resume PDF file into memory so it can be downloaded by users
with open(resume_path, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

# Create two columns to layout the profile section side-by-side
col1, col2 = st.columns(2, gap='small')

# Left column: display the profile image with ripple effect
with col1:
    with open(profile_pic_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        @keyframes ripple {{
            0% {{ transform: scale(1) skew(0deg, 0deg); }}
            25% {{ transform: scale(1.05, 0.95) skew(1.5deg, -1.5deg); }}
            50% {{ transform: scale(1) skew(0deg, 0deg); }}
            75% {{ transform: scale(1.05, 0.95) skew(-1.5deg, 1.5deg); }}
            100% {{ transform: scale(1) skew(0deg, 0deg); }}
        }}

        .ripple-image {{
            width: 230px;
            animation: ripple 1.5s infinite ease-in-out;
            border-radius: 12px;
        }}
        </style>

        <img class="ripple-image" src="data:image/png;base64,{encoded_image}" />
        """,
        unsafe_allow_html=True
    )

# Right column: display my name, job title, and a button to download my resume
with col2:
    st.title('Gareth Nassar', anchor=False)  # Main heading with anchor links disabled
    st.write('Network & System Administrator')  # Job title below the name

    # Button that allows downloading the resume PDF file
    st.download_button(
        label='📄 Resume',         # Button label with emoji
        data=PDFbyte,             # PDF file content loaded earlier
        file_name=resume_path.name,  # Name the file will have when downloaded
        mime='application/pdf'    # File type so the browser knows it's a PDF
    )
st.write("#####")
# Write a personal introduction about my passion for networking
st.write("""
For me, networking isn't just a vocation—it's a way of seeing the world. 
From configuring my first home Wi-Fi router to helping neighbors troubleshoot their internet issues, I've always been drawn to the flow of data and the systems that connect us. 

I approach every project with the same passion and precision, whether it's optimizing enterprise networks or securing local systems. 
Networking isn't just what I do—it's who I am.
""")

# Add vertical spacing with an empty Markdown header (level 3)
st.markdown("###")

# === SKILLS SECTION ===
st.header("🧠 Skills", anchor=False)  # Section header without anchor links

# Define skill categories and associated proficiency levels (0-100 scale)
skills = {
    "🔧 Networking": {
        "Network Monitoring": 95,
        "Network Troubleshooting": 85,
        "Network Design": 80,
        "Network Security": 75,
        "Network Automation": 85,
        "Wireless Networking": 70,
        "Routing & Switching": 90
    },
    "🖥️ Systems Administration": {
        "Active Directory": 95,
        "Server Administration": 85,
        "Cloud Computing": 80,
        "Backup & Disaster Recovery": 80,
        "Virtualization": 60,
        "Patch Management": 75,
        "Database Administration": 90
    },
    "🔐 Security": {
        "Firewall Configuration": 90,
        "VPNs & Remote Access Security": 85,
        "Intrusion Detection & Prevention Systems": 65,
        "Network Access Control": 85,
        "SEIM": 60,
        "Cryptography & PKI": 60,
        "Penetration Testing": 50,
    },
    "💻 Programming & Scripting": {
        "Python": 98,
        "Netmiko": 85,
        "SQL": 95,
        "Shell Scripting": 65,
        "Configuration as Code": 50,
        "Java": 90,
        "C++": 60,
    },
    "🧰 Tools & Utilities": {
        "Cisco Packet Tracer": 98,
        "Wireshark": 96,
        "SolarWinds": 80,
        "Nagios": 65,
        "Nmap": 73,
        "Ansible": 80,
        "PRTG": 65,
    }
}


# Create tabs for each skill category
tabs = st.tabs(list(skills.keys()))

# Display each skill with a progress bar representing proficiency level
for i, category in enumerate(skills.keys()):
    with tabs[i]:
        for skill, level in skills[category].items():
            st.write(f"**{skill}**")  # Skill name in bold
            st.progress(level)         # Progress bar for skill level

# Add another horizontal divider line
st.markdown("---")
# === WHAT I CAN DO SECTION ===
st.header("🛠️ What I Can Do", anchor=False)

# List of tasks and capabilities I perform in my role
st.write("""
- Design, configure and secure business networks from scratch  
- Troubleshoot network and system outages with speed and precision  
- Automate infrastructure tasks with Python, PowerShell and Ansible  
- Perform basic penetration testing to identify and report  vulnerabilities    
- Explain complex technical issues clearly to non-technical users
""")

# Add a horizontal divider line
st.markdown("---")

# === NETWORKING TIPS SECTION ===
st.header("💡 My Networking Tips", anchor=False)

# List of important networking tips I follow and recommend
tips = [
    "Document everything. Predictability starts with records.",
    "Automate to worry less and do more.",
    "Keep networks simple and scalable.",
    "Monitor traffic to spot issues early.",
    "Think like an attacker. Anticipate weaknesses and close gaps before they’re exploited."
]

# Display each tip inside a blue info box for emphasis
for tip in tips:
    st.info(f"{tip}")

# Add another horizontal divider line
st.markdown("---")

# === MY MOTTO SECTION ===
st.header("💬 Signature Quote", anchor=False)

# Display personal motto in a styled blockquote
st.markdown(
    """
    <blockquote style="font-size:1.4em; font-style:italic; color:#444; border-left:4px solid #ccc; padding-left:1em;">
    “Every good Network Admin should be part scientist, part artist, and part detective.”<br>
    <span style="font-size:0.9em; color:#666;">— Gareth Nassar, 2023</span>
    </blockquote>
    """,
    unsafe_allow_html=True
)


# Horizontal divider
st.markdown("---")

# === CERTIFICATION SECTION ===
# Simple Markdown heading for my certification
st.markdown("### 🎖️ CompTIA Network+", unsafe_allow_html=True)

# Horizontal divider
st.markdown("---")

# === CONTACT FOOTER ===
# Small text with contact email and LinkedIn profile link
st.caption("📬 Contact: garethnassar@gmail.com | [LinkedIn](https://www.linkedin.com/in/canuckcowboy/) | [GitHub](https://github.com/canuck-cowboy)")
