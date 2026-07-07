import streamlit as st
import random
import time
# ----------------- 1. OMNITOOLS CONFIG -----------------
# We use layout="wide" to give us more screen space!
st.set_page_config(page_title="OmniTools", page_icon="🛠️", layout="wide")
# This creates the permanent navigation sidebar on the left
st.sidebar.title("🛠️ OmniTools")
st.sidebar.write("Welcome to your ultimate utility suite.")
tool_selection = st.sidebar.radio(
    "Select a Tool:", ["Typing Speed Test", "Password Manager", "PDF Converter"])
# =======================================================
# ----------------- 2. TYPING SPEED TEST ----------------
# =======================================================
if tool_selection == "Typing Speed Test":
    st.title("⌨️ Typing Speed Test")
    st.write("Test your typing speed and accuracy in real-time.")

    # 1. The data pools
    import string
    import json

    letters = list(string.ascii_lowercase + string.digits +
                   "!@#$%^&*()_+-=[]{}|;':,.<>/?`~ ")
    words = ["apple", "banana", "table", "chair", "mountain", "river", "ocean", "space", "rocket", "planet", "orbit", "galaxy", "universe", "telescope", "computer", "keyboard", "mouse", "screen", "window", "door",
             "house", "building", "street", "city", "country", "world", "globe", "map", "compass", "north", "south", "east", "west", "up", "down", "left", "right", "front", "back", "top", "bottom", "inside", "outside", "near", "far", "close", "open", "shut", "lock", "key", "safe", "danger", "fast", "slow", "quick", "speedy", "rapid", "swift", "sudden", "abrupt", "gradual", "steady", "constant", "changing", "dynamic", "static", "still", "quiet", "loud", "noisy", "silent", "peaceful", "calm", "chaotic", "messy", "neat", "tidy", "clean", "dirty", "filthy", "spotless", "bright", "dark", "light", "heavy", "soft", "hard", "rough", "smooth", "sharp", "dull", "blunt", "pointed", "round", "square", "flat", "curved", "straight", "bent", "broken"]
    sentences = [

        "To be or not to be, that is the ultimate question.",
        "Sphinx of black quartz, judge my vow!",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Pack my box with five dozen liquor jugs.",
        "Artificial Intelligence is changing the world very quickly.",
        "The five boxing wizards jump quickly over the fence.",
        "Always remember to double-check your spelling and grammar.",
        "Programming is not about memorizing code; it is about solving problems.",
        "There is no place like home, especially after a long day.",
        "My favorite color is blue, but my sister prefers bright red.",
        "12345 is actually a terrible password for your email account.",
        "Water is essential for life, so remember to drink plenty of it.",
        "He quietly walked down the dark, mysterious hallway.",
        "Can you type this sentence perfectly without looking at the keyboard?",
        "The recipe calls for two cups of flour and one teaspoon of salt.",
        "Boredom is the feeling that everything is a waste of time.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "A completely random sentence can be surprisingly difficult to type quickly.",
        "Why did the chicken cross the road? To get to the other side, obviously!",
        "It was the best of times, it was the worst of times.",
        "Learning to code can be frustrating, but the reward is worth the effort.",
        "Zebras are famous for their black and white striped coats.",
        "The rusty old car struggled to climb up the steep, winding mountain road.",
        "Good programmers write code that humans can understand.",
        "Wait, did you remember to close your parenthesis at the end of that line?"
    ]
    # 2. Difficulty Selection
    difficulty = st.radio("Choose Difficulty:", [
                          "1. Easy (30 Letters)", "2. Medium (15 Words)", "3. Hard (10 Sentences)"])
    if 'test_active' not in st.session_state:
        st.session_state.test_active = False

    def start_test():
        st.session_state.test_active = True
        if "Easy" in difficulty:
            st.session_state.pool = letters
            st.session_state.target_count = 30
        elif "Medium" in difficulty:
            st.session_state.pool = words
            st.session_state.target_count = 15
        else:
            st.session_state.pool = sentences
            st.session_state.target_count = 10
    if not st.session_state.test_active:
        st.button("Start Typing Test", on_click=start_test, type="primary")
    else:
        st.info("Click anywhere in the box below and start typing!")

        # --- THE JAVASCRIPT "BLACK BOX" HACK ---
        import streamlit.components.v1 as components

        # We pass the pool and target count directly into the JS engine!
        pool_json = json.dumps(st.session_state.pool)
        target_count = st.session_state.target_count

        js_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{ font-family: 'Inter', sans-serif; color: #333; }}
            .sentence {{ font-size: 24px; letter-spacing: 1px; margin-bottom: 20px; user-select: none; }}
            .correct {{ color: #0047AB; font-weight: bold; }}
            .current {{ text-decoration: underline; font-weight: bold; color: #ff007f; background-color: #ffe6f2; }}
            #stats {{ font-size: 20px; font-weight: bold; color: #0047AB; line-height: 1.5; }}
            #progress {{ font-size: 16px; color: #666; margin-bottom: 10px; font-weight: bold; }}
        </style>
        </head>
        <body>
            <div id="progress">Loading...</div>
            <div id="textDisplay" class="sentence"></div>
            <div id="stats"></div>
            
            <script>
                const pool = {pool_json};
                const targetCount = {target_count};
                
                let currentTarget = pool[Math.floor(Math.random() * pool.length)];
                let currentIndex = 0;
                let roundsCompleted = 0;
                
                let startTime = null;
                let totalCharactersTyped = 0;
                let errors = 0;
                
                const display = document.getElementById("textDisplay");
                const stats = document.getElementById("stats");
                const progress = document.getElementById("progress");
                
                function render() {{
                    progress.innerText = `Round: ${{roundsCompleted + 1}} / ${{targetCount}}`;
                    
                    let html = "";
                    for (let i = 0; i < currentTarget.length; i++) {{
                        if (i < currentIndex) {{
                            html += `<span class="correct">${{currentTarget[i]}}</span>`;
                        }} else if (i === currentIndex) {{
                            html += `<span class="current">${{currentTarget[i]}}</span>`;
                        }} else {{
                            html += `<span>${{currentTarget[i]}}</span>`;
                        }}
                    }}
                    display.innerHTML = html;
                }}
                
                window.addEventListener("keydown", function(e) {{
                    if (roundsCompleted >= targetCount) return; // Test is over
                    
                    // Disable Backspace
                    if (e.key === "Backspace") {{
                        e.preventDefault(); 
                        return;
                    }}
                    
                    // Ignore shift, control, etc.
                    if (e.key.length > 1) return; 
                    
                    // Start timer on first keystroke
                    if (startTime === null) startTime = new Date().getTime();
                    
                    // Check if they typed the correct letter
                    if (e.key === currentTarget[currentIndex]) {{
                        currentIndex++;
                        totalCharactersTyped++;
                    }} else {{
                        errors++; // Track mistakes for accuracy
                    }}
                    
                    // Check if they finished the current word/sentence
                    if (currentIndex === currentTarget.length) {{
                        roundsCompleted++;
                        
                        if (roundsCompleted === targetCount) {{
                            // TEST COMPLETE!
                            let endTime = new Date().getTime();
                            let elapsedSeconds = (endTime - startTime) / 1000;
                            let wpm = (totalCharactersTyped / 5) / (elapsedSeconds / 60);
                            let accuracy = (totalCharactersTyped / (totalCharactersTyped + errors)) * 100;
                            
                            progress.innerText = "Test Complete!";
                            display.innerHTML = "";
                            stats.innerHTML = `🎉 Perfect! <br> 🚀 Speed: ${{wpm.toFixed(2)}} WPM <br> 🎯 Accuracy: ${{accuracy.toFixed(2)}}%`;
                            return;
                        }} else {{
                            // Load next word/sentence
                            currentTarget = pool[Math.floor(Math.random() * pool.length)];
                            currentIndex = 0;
                        }}
                    }}
                    
                    render();
                }});
                
                render();
            </script>
        </body>
        </html>
        """
        components.html(js_code, height=300)

        if st.button("End Test / Change Difficulty", type="primary"):
            st.session_state.test_active = False
            st.rerun()
# =======================================================
# ----------------- 3. PASSWORD MANAGER -----------------
# =======================================================
elif tool_selection == "Password Manager":
    st.title("🔒 Password Manager")
    st.write(
        "This is a placeholder for your Capstone project! You can build the logic here.")
    st.info("Status: Under Construction")
# =======================================================
# ----------------- 4. PDF CONVERTER --------------------
# =======================================================
else:
    st.title("📄 PDF Converter")
    st.write("Merge, split, and convert your PDF files effortlessly.")
    st.info("Status: Under Construction")
