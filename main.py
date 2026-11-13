import streamlit as st
import random

# Page title
st.title("🪨 Rock, Paper, Scissors")

st.write("Choose your move and play against the computer!")

# Store the possible choices
choices = ["👊", "✋", "✌️"]

# Create score variables
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# Player chooses
player_choice = st.radio(
    "Choose your move:",
    choices,
    horizontal=True
)

# Play button
if st.button("🎮 Play"):

    # Computer chooses randomly
    computer_choice = random.choice(choices)

    st.write("### Your choice:", player_choice)
    st.write("### Computer choice:", computer_choice)

    # An empty box we can keep rewriting, like a mini screen
    computer_decision_box = st.empty()
 
    # Flip through random moves, getting slower each time
    for i in range(20):
        flicker = random.choice(choices)
        computer_box.write(f"### Computer is thinking... {flicker}")
        time.sleep(0.08 + i * 0.02)  # starts fast, slows down
 
    # Stop on the real answer
    computer_decision_box.write(f"### Computer choice: {computer_choice}")
 

    # Decide the winner
    if player_choice == computer_choice:
        st.info("🤝 It's a draw!")

    elif (
        (player_choice == "👊" and computer_choice == "✌️")
        or
        (player_choice == "✋" and computer_choice == "👊")
        or
        (player_choice == "✌️" and computer_choice == "✋")
    ):
        st.success("🎉 You win!")
        st.session_state.player_score += 1

    else:
        st.error("😢 Computer wins!")
        st.session_state.computer_score += 1

# Display score
st.divider()

st.subheader("🏆 Score Board")

col1, col2 = st.columns(2)

with col1:
    st.metric("You", st.session_state.player_score)

with col2:
    st.metric("Computer", st.session_state.computer_score)

# Reset button
if st.button("🔄 Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.rerun()
