# import streamlit as st
# import pandas as pd
# import requests
#
#
# def main():
#     st.title("Candidate Evaluation Dashboard")
#
#     # File uploader widget
#     uploaded_file = st.file_uploader("Upload a CSV file with candidate data", type=["csv"])
#
#     candidate_data = {}
#     if uploaded_file is not None:
#         # Read the CSV file without headers
#         df = pd.read_csv(uploaded_file, header=None)
#
#         # Ensure there are enough rows in the CSV
#         if df.shape[0] >= 30:
#             # Extract values from the second column
#             values = df[1].tolist()
#
#             # Map CSV values to form fields
#             form_fields = [
#                 'Full Name', 'DOB', 'Gender', 'Nationality', 'Languages Preferred',
#                 'Phone Number', 'Email Address', 'Permanent Address', 'Religion',
#                 'Caste/Community', 'Ethnicity', 'Education Level', 'Previous Occupations',
#                 'Political Base', 'Highest Degree Obtained', 'Field of Study',
#                 'Educational Institutions Attended', 'Certifications/Other Qualifications',
#                 'Current Occupation', 'Years of Experience in Leadership',
#                 'Political Party Affiliation', 'Previous Political Positions Held',
#                 'Major Political Achievements', 'Political Ideology/Core Belief',
#                 'Political Movements Involvement', 'Key Areas of Focus',
#                 'Primary Vision for the Country/Region', 'Short-term Goals',
#                 'Long-term Goals', 'Involvement in Social/Community Projects',
#                 'Awards and Recognitions', 'Twitter', 'Facebook', 'Instagram',
#                 'Other Social Media Handles'
#             ]
#
#             if len(values) >= len(form_fields):
#                 # Populate candidate_data
#                 for field, value in zip(form_fields, values):
#                     candidate_data[field] = value
#
#                 # Ensure multi-value fields are properly split
#                 multi_value_fields = [
#                     'Languages Preferred', 'Previous Occupations', 'Educational Institutions Attended',
#                     'Certifications/Other Qualifications', 'Previous Political Positions Held',
#                     'Major Political Achievements', 'Political Ideology/Core Belief',
#                     'Political Movements Involvement', 'Key Areas of Focus',
#                     'Primary Vision for the Country/Region', 'Short-term Goals', 'Long-term Goals',
#                     'Involvement in Social/Community Projects', 'Awards and Recognitions', 'Other Social Media Handles'
#                 ]
#                 for field in multi_value_fields:
#                     if field in candidate_data:
#                         candidate_data[field] = candidate_data[field].split(", ")
#
#     # Input fields
#     candidate_data['Full Name'] = st.text_input("Full Name", value=candidate_data.get("Full Name", ""))
#     candidate_data['DOB'] = st.text_input("Date of Birth", value=candidate_data.get("DOB", ""))
#     candidate_data['Gender'] = st.selectbox("Gender", ["Male", "Female"],
#                                             index=["Male", "Female"].index(candidate_data.get("Gender", "Male")))
#     candidate_data['Nationality'] = st.text_input("Nationality", value=candidate_data.get("Nationality", ""))
#     candidate_data['Languages Preferred'] = st.text_input("Languages Preferred (comma-separated)",
#                                                           value=", ".join(
#                                                               candidate_data.get("Languages Preferred", [])))
#     candidate_data['Phone Number'] = st.text_input("Phone Number", value=candidate_data.get("Phone Number", ""))
#     candidate_data['Email Address'] = st.text_input("Email Address", value=candidate_data.get("Email Address", ""))
#     candidate_data['Permanent Address'] = st.text_input("Permanent Address",
#                                                         value=candidate_data.get("Permanent Address", ""))
#     candidate_data['Religion'] = st.text_input("Religion", value=candidate_data.get("Religion", ""))
#     candidate_data['Caste/Community'] = st.text_input("Caste/Community",
#                                                       value=candidate_data.get("Caste/Community", ""))
#     candidate_data['Ethnicity'] = st.text_input("Ethnicity", value=candidate_data.get("Ethnicity", ""))
#     candidate_data['Education Level'] = st.text_input("Education Level",
#                                                       value=candidate_data.get("Education Level", ""))
#     candidate_data['Previous Occupations'] = st.text_input("Previous Occupations (comma-separated)",
#                                                            value=", ".join(
#                                                                candidate_data.get("Previous Occupations", [])))
#     candidate_data['Political Base'] = st.text_input("Political Base", value=candidate_data.get("Political Base", ""))
#     candidate_data['Highest Degree Obtained'] = st.text_input("Highest Degree Obtained",
#                                                               value=candidate_data.get("Highest Degree Obtained", ""))
#     candidate_data['Field of Study'] = st.text_input("Field of Study", value=candidate_data.get("Field of Study", ""))
#     candidate_data['Educational Institutions Attended'] = st.text_input(
#         "Educational Institutions Attended (comma-separated)",
#         value=", ".join(candidate_data.get("Educational Institutions Attended", [])))
#     candidate_data['Certifications/Other Qualifications'] = st.text_input(
#         "Certifications/Other Qualifications (comma-separated)",
#         value=", ".join(candidate_data.get("Certifications/Other Qualifications", [])))
#     candidate_data['Current Occupation'] = st.text_input("Current Occupation",
#                                                          value=candidate_data.get("Current Occupation", ""))
#     candidate_data['Years of Experience in Leadership'] = st.text_input("Years of Experience in Leadership",
#                                                                         value=candidate_data.get(
#                                                                             "Years of Experience in Leadership", ""))
#     candidate_data['Political Party Affiliation'] = st.text_input("Political Party Affiliation",
#                                                                   value=candidate_data.get(
#                                                                       "Political Party Affiliation", ""))
#     candidate_data['Previous Political Positions Held'] = st.text_input(
#         "Previous Political Positions Held (comma-separated)",
#         value=", ".join(candidate_data.get("Previous Political Positions Held", [])))
#     candidate_data['Major Political Achievements'] = st.text_input("Major Political Achievements (comma-separated)",
#                                                                    value=", ".join(candidate_data.get(
#                                                                        "Major Political Achievements", [])))
#     candidate_data['Political Ideology/Core Belief'] = st.text_input("Political Ideology/Core Belief (comma-separated)",
#                                                                      value=", ".join(candidate_data.get(
#                                                                          "Political Ideology/Core Belief", [])))
#     candidate_data['Political Movements Involvement'] = st.text_input(
#         "Political Movements Involvement (comma-separated)",
#         value=", ".join(candidate_data.get("Political Movements Involvement", [])))
#     candidate_data['Key Areas of Focus'] = st.text_input("Key Areas of Focus (comma-separated)",
#                                                          value=", ".join(candidate_data.get("Key Areas of Focus", [])))
#     candidate_data['Primary Vision for the Country/Region'] = st.text_input(
#         "Primary Vision for the Country/Region (comma-separated)",
#         value=", ".join(candidate_data.get("Primary Vision for the Country/Region", [])))
#     candidate_data['Short-term Goals'] = st.text_input("Short-term Goals (comma-separated)",
#                                                        value=", ".join(candidate_data.get("Short-term Goals", [])))
#     candidate_data['Long-term Goals'] = st.text_input("Long-term Goals (comma-separated)",
#                                                       value=", ".join(candidate_data.get("Long-term Goals", [])))
#     candidate_data['Involvement in Social/Community Projects'] = st.text_input(
#         "Involvement in Social/Community Projects (comma-separated)",
#         value=", ".join(candidate_data.get("Involvement in Social/Community Projects", [])))
#     candidate_data['Awards and Recognitions'] = st.text_input("Awards and Recognitions (comma-separated)",
#                                                               value=", ".join(
#                                                                   candidate_data.get("Awards and Recognitions", [])))
#     candidate_data['Twitter'] = st.text_input("Twitter Handle", value=candidate_data.get("Twitter", ""))
#     candidate_data['Facebook'] = st.text_input("Facebook Handle", value=candidate_data.get("Facebook", ""))
#     candidate_data['Instagram'] = st.text_input("Instagram Handle", value=candidate_data.get("Instagram", ""))
#     candidate_data['Other Social Media Handles'] = st.text_input("Other Social Media Handles (comma-separated)",
#                                                                  value=", ".join(
#                                                                      candidate_data.get("Other Social Media Handles",
#                                                                                         [])))
#
#     if st.button("Submit"):
#         response = requests.post('http://127.0.0.1:5000/predict', json={'candidate_data': candidate_data})
#         result = response.json()
#
#         st.write("Raw Response:", result)
#
#         if result:
#             st.write(f"Division: {result.get('division', 'N/A')}")
#             st.write("PESTEL Scores:")
#             for key, value in result.get('pestel_scores', {}).items():
#                 st.write(f"{key}: {value}")
#
#             st.write(f"Demographic Alignment Score: {result.get('demographic_alignment_score', 'N/A')}")
#             st.write(f"Community Engagement Score: {result.get('community_engagement_score', 'N/A')}")
#             st.write(f"Support Index: {result.get('support_index', 'N/A')}")
#         else:
#             st.error("No data returned from the backend.")
#
#
# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import requests

def main():
    st.title("Candidate Evaluation Dashboard")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a CSV file with candidate data", type=["csv"])

    candidate_data = {}
    if uploaded_file is not None:
        # Read the CSV file without headers
        df = pd.read_csv(uploaded_file, header=None)

        # Ensure there are enough rows in the CSV
        if df.shape[0] >= 30:
            # Extract values from the second column
            values = df[1].tolist()

            # Map CSV values to form fields
            form_fields = [
                'Full Name', 'DOB', 'Gender', 'Nationality', 'Languages Preferred',
                'Phone Number', 'Email Address', 'Permanent Address', 'Religion',
                'Caste/Community', 'Ethnicity', 'Education Level', 'Previous Occupations',
                'Political Base', 'Highest Degree Obtained', 'Field of Study',
                'Educational Institutions Attended', 'Certifications/Other Qualifications',
                'Current Occupation', 'Years of Experience in Leadership',
                'Political Party Affiliation', 'Previous Political Positions Held',
                'Major Political Achievements', 'Political Ideology/Core Belief',
                'Political Movements Involvement', 'Key Areas of Focus',
                'Primary Vision for the Country/Region', 'Short-term Goals',
                'Long-term Goals', 'Involvement in Social/Community Projects',
                'Awards and Recognitions', 'Twitter', 'Facebook', 'Instagram',
                'Other Social Media Handles'
            ]

            if len(values) >= len(form_fields):
                # Populate candidate_data
                for field, value in zip(form_fields, values):
                    candidate_data[field] = value

                # Ensure multi-value fields are properly split
                multi_value_fields = [
                    'Languages Preferred', 'Previous Occupations', 'Educational Institutions Attended',
                    'Certifications/Other Qualifications', 'Previous Political Positions Held',
                    'Major Political Achievements', 'Political Ideology/Core Belief',
                    'Political Movements Involvement', 'Key Areas of Focus',
                    'Primary Vision for the Country/Region', 'Short-term Goals', 'Long-term Goals',
                    'Involvement in Social/Community Projects', 'Awards and Recognitions', 'Other Social Media Handles'
                ]
                for field in multi_value_fields:
                    if field in candidate_data:
                        candidate_data[field] = candidate_data[field].split(", ")

    # Input fields
    candidate_data['Full Name'] = st.text_input("Full Name", value=candidate_data.get("Full Name", ""))
    candidate_data['DOB'] = st.text_input("Date of Birth", value=candidate_data.get("DOB", ""))
    candidate_data['Gender'] = st.selectbox("Gender", ["Male", "Female"],
                                            index=["Male", "Female"].index(candidate_data.get("Gender", "Male")))
    candidate_data['Nationality'] = st.text_input("Nationality", value=candidate_data.get("Nationality", ""))
    candidate_data['Languages Preferred'] = st.text_input("Languages Preferred (comma-separated)",
                                                          value=", ".join(
                                                              candidate_data.get("Languages Preferred", [])))
    candidate_data['Phone Number'] = st.text_input("Phone Number", value=candidate_data.get("Phone Number", ""))
    candidate_data['Email Address'] = st.text_input("Email Address", value=candidate_data.get("Email Address", ""))
    candidate_data['Permanent Address'] = st.text_input("Permanent Address",
                                                        value=candidate_data.get("Permanent Address", ""))
    candidate_data['Religion'] = st.text_input("Religion", value=candidate_data.get("Religion", ""))
    candidate_data['Caste/Community'] = st.text_input("Caste/Community",
                                                      value=candidate_data.get("Caste/Community", ""))
    candidate_data['Ethnicity'] = st.text_input("Ethnicity", value=candidate_data.get("Ethnicity", ""))
    candidate_data['Education Level'] = st.text_input("Education Level",
                                                      value=candidate_data.get("Education Level", ""))
    candidate_data['Previous Occupations'] = st.text_input("Previous Occupations (comma-separated)",
                                                           value=", ".join(
                                                               candidate_data.get("Previous Occupations", [])))
    candidate_data['Political Base'] = st.text_input("Political Base", value=candidate_data.get("Political Base", ""))
    candidate_data['Highest Degree Obtained'] = st.text_input("Highest Degree Obtained",
                                                              value=candidate_data.get("Highest Degree Obtained", ""))
    candidate_data['Field of Study'] = st.text_input("Field of Study", value=candidate_data.get("Field of Study", ""))
    candidate_data['Educational Institutions Attended'] = st.text_input(
        "Educational Institutions Attended (comma-separated)",
        value=", ".join(candidate_data.get("Educational Institutions Attended", [])))
    candidate_data['Certifications/Other Qualifications'] = st.text_input(
        "Certifications/Other Qualifications (comma-separated)",
        value=", ".join(candidate_data.get("Certifications/Other Qualifications", [])))
    candidate_data['Current Occupation'] = st.text_input("Current Occupation",
                                                         value=candidate_data.get("Current Occupation", ""))
    candidate_data['Years of Experience in Leadership'] = st.text_input("Years of Experience in Leadership",
                                                                        value=candidate_data.get(
                                                                            "Years of Experience in Leadership", ""))
    candidate_data['Political Party Affiliation'] = st.text_input("Political Party Affiliation",
                                                                  value=candidate_data.get(
                                                                      "Political Party Affiliation", ""))
    candidate_data['Previous Political Positions Held'] = st.text_input(
        "Previous Political Positions Held (comma-separated)",
        value=", ".join(candidate_data.get("Previous Political Positions Held", [])))
    candidate_data['Major Political Achievements'] = st.text_input("Major Political Achievements (comma-separated)",
                                                                   value=", ".join(candidate_data.get(
                                                                       "Major Political Achievements", [])))
    candidate_data['Political Ideology/Core Belief'] = st.text_input("Political Ideology/Core Belief (comma-separated)",
                                                                     value=", ".join(candidate_data.get(
                                                                         "Political Ideology/Core Belief", [])))
    candidate_data['Political Movements Involvement'] = st.text_input(
        "Political Movements Involvement (comma-separated)",
        value=", ".join(candidate_data.get("Political Movements Involvement", [])))
    candidate_data['Key Areas of Focus'] = st.text_input("Key Areas of Focus (comma-separated)",
                                                         value=", ".join(candidate_data.get("Key Areas of Focus", [])))
    candidate_data['Primary Vision for the Country/Region'] = st.text_input(
        "Primary Vision for the Country/Region (comma-separated)",
        value=", ".join(candidate_data.get("Primary Vision for the Country/Region", [])))
    candidate_data['Short-term Goals'] = st.text_input("Short-term Goals (comma-separated)",
                                                       value=", ".join(candidate_data.get("Short-term Goals", [])))
    candidate_data['Long-term Goals'] = st.text_input("Long-term Goals (comma-separated)",
                                                      value=", ".join(candidate_data.get("Long-term Goals", [])))
    candidate_data['Involvement in Social/Community Projects'] = st.text_input(
        "Involvement in Social/Community Projects (comma-separated)",
        value=", ".join(candidate_data.get("Involvement in Social/Community Projects", [])))
    candidate_data['Awards and Recognitions'] = st.text_input("Awards and Recognitions (comma-separated)",
                                                              value=", ".join(
                                                                  candidate_data.get("Awards and Recognitions", [])))
    candidate_data['Twitter'] = st.text_input("Twitter Handle", value=candidate_data.get("Twitter", ""))
    candidate_data['Facebook'] = st.text_input("Facebook Handle", value=candidate_data.get("Facebook", ""))
    candidate_data['Instagram'] = st.text_input("Instagram Handle", value=candidate_data.get("Instagram", ""))
    candidate_data['Other Social Media Handles'] = st.text_input("Other Social Media Handles (comma-separated)",
                                                                 value=", ".join(
                                                                     candidate_data.get("Other Social Media Handles",
                                                                                        [])))

    if st.button("Submit"):
        response = requests.post('https://model-backend-m5jp.onrender.com/predict', json={'candidate_data': candidate_data})
        result = response.json()

        if result:
            st.write("Final Support Index Score:")
            st.metric("Final SI Score", round(result.get('final_si_score', 0), 2))

            # Iterate over each division to display their respective scores
            # Iterate over each division to display their respective scores
            for division, division_data in result.get('division_scores', {}).items():
                st.subheader(f"Division: {division}")

                # PESTEL Scores
                st.write("**PESTEL Scores**")
                pestel_scores = division_data.get('pestel_scores', {})
                cols = st.columns(3)
                cols[0].metric("Political", pestel_scores.get('Political', 'N/A'))
                cols[0].metric("Economic", pestel_scores.get('Economic', 'N/A'))
                cols[0].metric("Social", pestel_scores.get('Social', 'N/A'))
                cols[1].metric("Technological", pestel_scores.get('Technological', 'N/A'))
                cols[1].metric("Environmental", pestel_scores.get('Environmental', 'N/A'))
                cols[1].metric("Legal", pestel_scores.get('Legal', 'N/A'))

                # Other scores
                st.write("**Other Scores**")
                st.metric("Demographic Alignment", division_data.get('demographic_alignment_score', 'N/A'))
                st.metric("Community Engagement", division_data.get('community_engagement_score', 'N/A'))
                st.metric("Support Index", division_data.get('support_index', 'N/A'))


if __name__ == "__main__":
    main()
