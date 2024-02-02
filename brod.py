
import streamlit as st
import sqlite3

# Function to create a table for storing messages if it doesn't exist
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

def main():
    st.title("")

    # Create table if it doesn't exist
    create_table()

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

def show_chat_interface(user_key):
    # Get user input for chat
    user_input = st.text_input("Type your message here:", key="user_input")

    if user_input:
        # Store message in the database
        insert_message(user_key, user_input)

    # Display stored messages
    messages = get_messages()
    st.subheader("Chat History")
    for user, message in messages:
        if user == "admin_key":
            st.text(f"Admin: {message}")
        else:
            st.text(f"User: {message}")

if __name__ == "__main__":
    main()
