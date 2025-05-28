import streamlit as st

# Page setup
st.set_page_config(page_title="For Subha 💖", page_icon="🌸", layout="centered")

# Title and intro
st.title("💖 Just For You, Subha 💖")
st.markdown("## A little surprise, just because you're special ✨")
st.write("You bring joy into my life just by being in it. I don’t need a reason to celebrate you!")

# Image uploader (optional)
uploaded_file = st.file_uploader("Upload your favorite photo 💫 (Optional)", type=["jpg", "png"])
if uploaded_file:
    from PIL import Image
    image = Image.open(uploaded_file)
    st.image(image, caption="You are my favorite view 💕", use_column_width=True)
else:
    st.info("No photo uploaded yet. Still, you're always in my heart 💖")

# Music section
st.markdown("### A song that reminds me of you 🎵")
st.video("https://www.youtube.com/watch?v=450p7goxZqg")  # Example: "Until I Found You"

# Personal love note
st.markdown("---")
st.markdown("### 💌 A Little Note:")
st.success("I don’t need a special occasion to remind you how much you mean to me. I’m lucky to have you, Subha. ❤️")

# Fun animation
st.balloons()
