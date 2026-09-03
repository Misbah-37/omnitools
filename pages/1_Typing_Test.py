# =======================================================
# ----------------- 1. TYPING SPEED TEST ----------------
# =======================================================
import json
import string
import streamlit as st
import streamlit.components.v1 as components
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
)

if "test_active" not in st.session_state:
  st.session_state.test_active = False


def start_test():
  st.session_state.test_active = True
  if "Easy" in difficulty:
    st.session_state.pool = letters
    st.session_state.target_count = 30
  elif "Medium" in difficulty:
    st.session_state.pool = words
    st.session_state.target_count = 15
  elif "Hard" in difficulty:
    st.session_state.pool = sentences
    st.session_state.target_count = 10
  else:
    st.session_state.pool = paragraphs
    st.session_state.target_count = 1


if not st.session_state.test_active:
  st.button("Start Typing Test", on_click=start_test, type="primary")
else:
  pool_json = json.dumps(st.session_state.pool)
  target_count = st.session_state.target_count

  js_template = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body { font-family: 'Inter', sans-serif; color: #e2e8f0; background: transparent; margin: 0; padding: 10px; }
        .sentence { font-size: 20px; line-height: 1.6; letter-spacing: 0.5px; margin-bottom: 20px; user-select: none; word-wrap: break-word; }
        .correct { color: #00d2ff; font-weight: bold; text-shadow: 0 0 8px rgba(0,210,255,0.4); }
        .current { text-decoration: underline; font-weight: bold; color: #ff3399; background-color: rgba(255, 51, 153, 0.2); border-radius: 3px; padding: 0 2px; }
        #stats { font-size: 20px; font-weight: bold; color: #00d2ff; line-height: 1.6; }
        #progress { font-size: 15px; color: #94a3b8; margin-bottom: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
        .typing-input {
            width: 100%;
            padding: 12px 16px;
            font-size: 18px;
            background: #1e293b;
            color: #f8fafc;
            border: 2px solid #00d2ff;
            border-radius: 8px;
            outline: none;
            box-sizing: border-box;
            margin-bottom: 15px;
        }
    </style>
    </head>
    <body>
        <div id="progress">Loading...</div>
        <div id="textDisplay" class="sentence"></div>
        <input type="text" id="typingInput" class="typing-input" placeholder="Tap here and start typing..." autocomplete="off" autocapitalize="off" spellcheck="false" />
        <div id="stats"></div>
        <script>
            const pool = __POOL_JSON__;
            const targetCount = __TARGET_COUNT__;
            let currentTarget = pool[Math.floor(Math.random() * pool.length)];
            let roundsCompleted = 0;
            let startTime = null;
            let totalCharactersTyped = 0;
            let errors = 0;
            
            const display = document.getElementById("textDisplay");
            const stats = document.getElementById("stats");
            const progress = document.getElementById("progress");
            const inputField = document.getElementById("typingInput");
            
            inputField.focus();
            
            function render() {
                progress.innerText = "Round: " + (roundsCompleted + 1) + " / " + targetCount;
                const typedText = inputField.value;
                let html = "";
                
                for (let i = 0; i < currentTarget.length; i++) {
                    if (i < typedText.length) {
                        if (typedText[i] === currentTarget[i]) {
                            html += '<span class="correct">' + currentTarget[i] + '</span>';
                        } else {
                            html += '<span class="current" style="color: #ef4444; background: rgba(239,68,68,0.2);">' + currentTarget[i] + '</span>';
                        }
                    } else if (i === typedText.length) {
                        html += '<span class="current">' + currentTarget[i] + '</span>';
                    } else {
                        html += '<span>' + currentTarget[i] + '</span>';
                    }
                }
                display.innerHTML = html;
            }
            
            inputField.addEventListener("input", function(e) {
                if (roundsCompleted >= targetCount) return;
                
                const typedText = inputField.value;
                if (startTime === null && typedText.length > 0) {
                    startTime = new Date().getTime();
                }
                
                let currentErrors = 0;
                for (let i = 0; i < typedText.length; i++) {
                    if (i < currentTarget.length) {
                        if (typedText[i] !== currentTarget[i]) currentErrors++;
                    } else {
                        currentErrors++;
                    }
                }
                errors = currentErrors;
                
                if (typedText === currentTarget) {
                    roundsCompleted++;
                    totalCharactersTyped += currentTarget.length;
                    inputField.value = "";
                    
                    if (roundsCompleted === targetCount) {
                        let endTime = new Date().getTime();
                        let elapsedSeconds = (endTime - startTime) / 1000;
                        let wpm = (totalCharactersTyped / 5) / (elapsedSeconds / 60);
                        let accuracy = (totalCharactersTyped / (totalCharactersTyped + errors)) * 100;
                        progress.innerText = "✨ Test Complete!";
                        display.innerHTML = "";
                        inputField.style.display = "none";
                        stats.innerHTML = "🎉 Perfect! <br> 🚀 Speed: " + wpm.toFixed(2) + " WPM <br> 🎯 Accuracy: " + accuracy.toFixed(2) + "%";
                        return;
                    } else {
                        currentTarget = pool[Math.floor(Math.random() * pool.length)];
                    }
                }
                render();
            });
            
            render();
        </script>
    </body>
    </html>
    """

  # Safely inject python variables without f-string brace conflicts
  js_code = (
      js_template.replace("__POOL_JSON__", pool_json)
      .replace("__TARGET_COUNT__", str(target_count))
  )
  components.html(js_code, height=380)

  if st.button("End Test / Change Difficulty", type="primary"):
    st.session_state.test_active = False
    st.rerun()
