# =======================================================
# ----------------- 1. TYPING SPEED TEST ----------------
# =======================================================
import random
import string
import time
import streamlit as st
from utils import render_icon_html

# --- SEO METADATA ---
st.set_page_config(
    page_title="Free WPM Typing Speed Test | Ad-Free Benchmark | OmniTools",
    page_icon="⌨️",
    layout="wide",
)

top_bar1, top_bar2 = st.columns([6, 1])
with top_bar1:
  img_html = render_icon_html(
      "typing_icon.png",
      "typing_speed_icon_1788371582708.jpg",
      size=65,
      glow_color="rgba(255, 51, 153, 0.4)",
  )
  st.markdown(
      f"""
    <div style="display: flex; gap: 16px; align-items: center;">
        {img_html}
        <div>
            <h2 style="margin: 0; color: #f8fafc;">Typing Speed Test</h2>
            <div style="color: #94a3b8; font-size: 0.95rem;">Test your typing speed and accuracy in real-time.</div>
        </div>
    </div>
    """,
      unsafe_allow_html=True,
  )
with top_bar2:
  st.page_link("omnitools_app.py", label="🏠 Back", use_container_width=True)

st.divider()

# Word pools
letters = list(
    string.ascii_lowercase + string.digits + "!@#$%^&*()_+-=[]{}|;':,.<>/?`~ "
)
words = [
    "apple",
    "banana",
    "table",
    "chair",
    "mountain",
    "river",
    "ocean",
    "space",
    "rocket",
    "planet",
    "orbit",
    "galaxy",
    "universe",
    "telescope",
    "computer",
    "keyboard",
    "mouse",
    "screen",
    "window",
    "door",
    "house",
    "building",
    "street",
    "city",
    "country",
    "world",
    "globe",
    "map",
    "compass",
    "north",
    "south",
    "east",
    "west",
    "up",
    "down",
    "left",
    "right",
    "front",
    "back",
    "top",
    "bottom",
    "inside",
    "outside",
    "near",
    "far",
    "close",
    "open",
    "shut",
    "lock",
    "key",
    "safe",
    "danger",
    "fast",
    "slow",
    "quick",
    "speedy",
    "rapid",
    "swift",
    "sudden",
    "abrupt",
    "gradual",
    "steady",
    "constant",
    "changing",
    "dynamic",
    "static",
    "still",
    "quiet",
    "loud",
    "noisy",
    "silent",
    "peaceful",
    "calm",
    "chaotic",
    "messy",
    "neat",
    "tidy",
    "clean",
    "dirty",
    "filthy",
    "spotless",
    "bright",
    "dark",
    "light",
    "heavy",
    "soft",
    "hard",
    "rough",
    "smooth",
    "sharp",
    "dull",
    "blunt",
    "pointed",
    "round",
    "square",
    "flat",
    "curved",
    "straight",
    "bent",
    "broken",
]
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump!",
    "Sphinx of black quartz, judge my vow.",
    "Two driven jocks help fax my big quiz.",
    "Five quacking zephyrs jolt my wax bed.",
    "The five boxing wizards jump quickly.",
    "Bright vixens jump; dozy fowl quack.",
    "A wizard's job is to vex chumps quickly in fog.",
    "Watch Jeopardy, Alex Trebek's fun TV quiz game.",
    "By Jove, my quick study of lexicography won a prize.",
    (
        "Programming is not about memorizing code; it is about solving"
        " problems."
    ),
    "Artificial Intelligence is changing the world very quickly.",
    (
        "The internet is a vast network that connects computers all over the"
        " world."
    ),
    "Cybersecurity is the practice of protecting systems, networks, and programs.",
    (
        "Software engineering is the systematic application of engineering"
        " approaches."
    ),
    "Cloud computing provides on-demand availability of computer system resources.",
    "Python is an interpreted, high-level and general-purpose programming language.",
]
paragraphs = [
    (
        "The morning sun cast a gentle golden glow across the quiet streets as"
        " the city slowly woke up. A cool breeze carried the sweet aroma of"
        " freshly brewed coffee from the corner bakery, welcoming early"
        " morning commuters on their way to work."
    ),
    (
        "Consistency is the secret ingredient behind mastering any new skill"
        " in life. When you dedicate even ten minutes each day to focused"
        " practice, the compound effect over months and years produces"
        " remarkable results that talent alone cannot achieve."
    ),
    (
        "Reading books is one of the most rewarding habits you can develop. It"
        " allows you to travel across different eras, explore distant worlds,"
        " and experience the thoughts of great minds throughout history, all"
        " from the comfort of your favorite armchair."
    ),
    (
        "The ocean covers more than seventy percent of our planet and remains"
        " one of the least explored frontiers on Earth. Beneath its shimmering"
        " surface lie vast underwater mountain ranges, deep trenches, and"
        " countless mysterious creatures that have never seen sunlight."
    ),
    (
        "In the modern digital era, learning how to type quickly and accurately"
        " is an essential superpower. It allows your thoughts to flow"
        " seamlessly onto the screen without interruption, boosting both your"
        " productivity and creative expression."
    ),
    (
        "Clean code is like well-written prose; it is intuitive, easy to"
        " understand, and pleasant to maintain over time. Great software"
        " engineers do not just write code for machines to execute, but for"
        " fellow developers to read and improve."
    ),
    (
        "Coding is equal parts logic and creativity. Whether building a simple"
        " calculator, designing an interactive game, or training a machine"
        " learning model, programming gives you the power to bring abstract"
        " ideas into tangible reality."
    ),
    (
        "Master the art of finishing what you start. While starting new"
        " projects is exciting, the true satisfaction and growth come from"
        " pushing through the messy middle and bringing your work across the"
        " finish line."
    ),
]

difficulty = st.radio(
    "Choose Difficulty:",
    [
        "1. Easy (30 Letters)",
        "2. Medium (15 Words)",
        "3. Hard (10 Sentences)",
        "4. Expert (1 Paragraph)",
    ],
    horizontal=True,
)

# Initialize session state
if "test_started" not in st.session_state:
  st.session_state.test_started = False
if "target_text" not in st.session_state:
  st.session_state.target_text = ""
if "start_time" not in st.session_state:
  st.session_state.start_time = None


def init_game():
  st.session_state.test_started = True
  st.session_state.start_time = None
  if "Easy" in difficulty:
    st.session_state.target_text = "".join(random.choices(letters, k=30))
  elif "Medium" in difficulty:
    st.session_state.target_text = " ".join(random.choices(words, k=5))
  elif "Hard" in difficulty:
    st.session_state.target_text = random.choice(sentences)
  else:
    st.session_state.target_text = random.choice(paragraphs)


if not st.session_state.test_started:
  if st.button("🚀 Start Typing Test", type="primary"):
    init_game()
    st.rerun()
else:
  target = st.session_state.target_text

  st.markdown("### Type this text:")

  # Render colored target text directly using standard markdown/HTML for maximum clarity
  # Cyan = Correctly typed so far, Red = Mistake made at position, Gray = Upcoming
  user_input = st.session_state.get("user_typing_box", "")

  # Start timer on first keystroke
  if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

  # Build clear visual representation
  colored_html = "<div style='font-size: 22px; font-family: monospace; line-height: 1.8; background: #0f172a; padding: 20px; border-radius: 10px; border: 1px solid #334155; word-break: break-all;'>"
  for i, char in enumerate(target):
    if i < len(user_input):
      if user_input[i] == char:
        colored_html += (
            f"<span style='color: #00d2ff; font-weight: bold;'>{char}</span>"
        )
      else:
        colored_html += f"<span style='color: #ef4444; background: rgba(239, 68, 68, 0.3); font-weight: bold;'>{char}</span>"
    elif i == len(user_input):
      colored_html += (
          f"<span style='color: #fbbf24; background: rgba(251, 191, 36,"
          f" 0.3); border-bottom: 2px solid #fbbf24; font-weight:"
          f" bold;'>{char}</span>"
      )
    else:
      colored_html += f"<span style='color: #64748b;'>{char}</span>"
  colored_html += "</div>"

  st.markdown(colored_html, unsafe_allow_html=True)

  # Native text box that triggers mobile virtual keyboard instantly and reliably
  typed = st.text_input(
      "Type here:", key="user_typing_box", placeholder="Start typing here..."
  )

  # Check completion condition
  if typed == target:
    elapsed = time.time() - st.session_state.start_time if st.session_state.start_time else 1
    minutes = elapsed / 60
    words_count = len(target.split())
    wpm = int(words_count / minutes) if minutes > 0 else 0

    st.success(
        f"🎉 **Test Complete!** Speed: **{wpm} WPM** | Time:"
        f" **{elapsed:.2f}s**"
    )
    if st.button("Play Again"):
      st.session_state.test_started = False
      st.session_state.user_typing_box = ""
      st.rerun()

  col1, col2 = st.columns(2)
  with col1:
    if st.button("Reset / New Text"):
      init_game()
      st.rerun()
  with col2:
    if st.button("Change Difficulty"):
      st.session_state.test_started = False
      st.rerun()
