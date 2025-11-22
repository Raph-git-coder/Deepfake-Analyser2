import streamlit as st
from datetime import date
import random

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="A Letter to the One I Love",
    page_icon="🌸",
    layout="centered"
)

# ------------------------------------------------------
# ENHANCED CSS (No URL images, clean text-only style)
# ------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Marcellus&display=swap');

body {
    background: linear-gradient(180deg, #fff8f4, #ffe9e4);
}

/* Handwritten poetic font */
.poem {
    font-family: 'Great Vibes', cursive;
    font-size: 36px;
    line-height: 1.65;
    text-align: center;
    padding: 20px 15px;
    background: linear-gradient(90deg, #ff7b9c, #d45a9f, #ff9f7f, #ff7b9c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Elegant title */
.title {
    font-family: 'Marcellus', serif;
    font-size: 38px;
    color: #d04e61;
    text-align: center;
}

/* Soft fade-in */
.fade {
    animation: fadeIn 2s ease forwards;
    opacity: 0;
}
@keyframes fadeIn {
    to { opacity: 1; }
}

/* Flower burst (text symbols only) */
.flower-burst {
    animation: bloom 1.5s ease forwards;
    opacity: 0;
    font-size: 36px;
    position: fixed;
}
@keyframes bloom {
    0% { transform: scale(0.3); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# TITLE
# ------------------------------------------------------
st.markdown("<div class='title fade'>🌸 A Birthday Letter for My Love 🌸 💞 </div>", unsafe_allow_html=True)
st.write("")

# ------------------------------------------------------
# NAME INPUT
# ------------------------------------------------------
name = st.text_input("Please enter your name:")

# ------------------------------------------------------
# POEM
# ------------------------------------------------------
poem = """
My dearest {name},  

On this gentle day,  
the whole world seems to glow—  
as if morning itself softened its light  
just to honor your existence.  

There is a quiet magic about you,  
the kind that turns breath into poetry  
and moments into warmth.  

Your presence is a soft miracle,  
your heart a lantern that never dims.  

If tenderness had a shape,  
it would be your name.  

If love had a color,  
it would be the light you carry.  

On your birthday,  
I wish you joys that unfold like petals,  
softly, beautifully,  
in their own perfect time.  

You are loved far beyond measure.  

Happy Birthday,
My beautiful soul,
    Love U 💕.
"""

# ------------------------------------------------------
# REVEAL FLOWERS + MESSAGE (TEXT SYMBOLS ONLY)
# ------------------------------------------------------
if name.strip():
    st.write("")
    if st.button("💌 Reveal My Birthday Message"):

        # Poem
        st.markdown(f"<div class='poem fade'>{poem.format(name=name)}</div>", unsafe_allow_html=True)

        # Signature
        st.markdown(
            """
            <div class='fade' style='text-align:center; margin-top:20px;'>
                <span style='font-family:Great Vibes; font-size:60px; color:#d4426d;'>
                    With Love ♥❀
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("💞Love you Forever💞")

# ------------------------------------------------------
# FOOTER
# ------------------------------------------------------
st.write("---")
st.caption(f"Made with love • {date.today().strftime('%B %d, %Y')}")





