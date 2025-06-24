import streamlit as st

st.title("CORAM Physical Therapy: Elder Symptom Tracker")

st.write("""
This tool helps you track symptoms and receive preliminary guidance. 
It’s designed for older adults seeking support for common physical therapy issues.
""")

symptoms = st.multiselect(
    "Select your symptoms:",
    [
        "Lower back pain",
        "Knee pain",
        "Hip stiffness",
        "Shoulder discomfort",
        "Balance issues",
        "Muscle weakness",
        "Joint pain",
        "Limited mobility",
        "Foot numbness",
        "Post-surgery soreness"
    ]
)

diagnosis_hint = ""
if "Lower back pain" in symptoms and "Limited mobility" in symptoms:
    diagnosis_hint += "- Possible early spinal degeneration or disc issues.\n"
if "Balance issues" in symptoms and "Muscle weakness" in symptoms:
    diagnosis_hint += "- Suggests need for fall prevention therapy and strength training.\n"
if "Hip stiffness" in symptoms or "Knee pain" in symptoms:
    diagnosis_hint += "- Common in arthritis cases; consider joint mobility exercises.\n"
if "Shoulder discomfort" in symptoms and "Limited mobility" in symptoms:
    diagnosis_hint += "- May relate to frozen shoulder or rotator cuff injury.\n"
if "Foot numbness" in symptoms:
    diagnosis_hint += "- Could be a sign of neuropathy; medical evaluation recommended.\n"

if symptoms:
    st.subheader("Preliminary Suggestions")
    st.markdown(diagnosis_hint or "- No suggestions found. Please consult a licensed physical therapist.")
else:
    st.info("Please select at least one symptom to continue.")
