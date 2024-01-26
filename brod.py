
import os
import streamlit as st
import sqlite3

UPLOADS_DIR = "uploads"  # Directory to store uploaded files

def create_table():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_message(user, message):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (user, message) VALUES (?, ?)", (user, message))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user, message FROM messages")
    messages = cursor.fetchall()
    conn.close()
    return messages

def save_uploaded_file(uploaded_file):
    file_path = os.path.join(UPLOADS_DIR, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getvalue())
    return file_path

def upload_files():
    file_types = ["js", "html", "css", "java", "rs", "py", "png", "jpg", "c", "cpp", "db", "csv", "txt", "xlsx", "xls", "ppt"]
    uploaded_files = st.file_uploader("Submit Files or Directories to Admin", type=file_types, accept_multiple_files=True, key="file_uploader")

    if uploaded_files:
        for uploaded_file in uploaded_files:
            

            # Save the uploaded file to internal storage
            file_path = save_uploaded_file(uploaded_file)

            



def main():
    st.title("")

    # Create table if it doesn't exist
    create_table()

    # Create uploads directory if it doesn't exist
    os.makedirs(UPLOADS_DIR, exist_ok=True)

    # Get user input for the key
    key_input = st.empty()
    key = key_input.text_input("Enter the key:")

    if key == "yiam_" or key == "Hind@1":
        show_dashboard()
        key_input.empty()
        show_chat_interface(key)
    elif key != "":
        st.warning("Invalid key. Please try again.")

def show_dashboard():
    st.subheader("")
    upload_files()

def show_chat_interface(user_key):
    user_input = st.text_input("Type your message here:", key="user_input")

    if user_input:
        insert_message(user_key, user_input)

    messages = get_messages()
    st.subheader("Chat History")
    for user, message in messages:
        if user == "admin_key":
            st.text(f"Admin: {message}")
        else:
            st.text(f"User: {message}")

if __name__ == "__main__":
    main()
