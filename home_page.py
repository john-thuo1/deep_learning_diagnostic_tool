import streamlit as st

def main():
    # Set page config
    st.set_page_config(page_title="Image Diagnostic Tool", page_icon=":microscope:")

    # Page Style
    st.write(
        """
        <style>
        .title {
            font-size: 36px;
            font-family: "Times New Roman", serif;
        }
        .header {
            font-size: 15px;
            font-family: "Times New Roman", serif;
        }
        .content {
            font-size: 12px;
            font-family: "Times New Roman", serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Steps
    
    st.title("Image Diagnostic Tool")
    st.write("Follow the steps below to use the tool:")

    st.header("Step 1: Select the type of Disease")
    st.write("Choose from Pneumonia, Breast Cancer, or Tuberculosis")

    st.header("Step 2: Upload Patient's X-Ray Image")
    st.write("Note that this Image must be of type png or jpeg.")

    st.header("Step 3: Click 'See Results' to see results")

    st.header("Step 4: Double Check the results")
    st.write('Use your medical expertise. If the results draw the same conclusions, then send to the patient.')

    st.header("Step 5: click 'Share Results' to send the results to the Patient")
    st.write("This will prompt you to enter patient's phone number.")

if __name__ == "__main__":
    main()
