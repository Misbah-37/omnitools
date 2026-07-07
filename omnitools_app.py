import streamlit as st
import random
import time

# ----------------- 1. OMNITOOLS CONFIG -----------------
# We use layout="wide" to give us more screen space!
st.set_page_config(page_title="OmniTools", page_icon="🛠️", layout="wide")

# This creates the permanent navigation sidebar on the left
st.sidebar.title("🛠️ OmniTools")
st.sidebar.write("Welcome to your ultimate utility suite.")
tool_selection = st.sidebar.radio("Select a Tool:", ["Typing Speed Test", "Password Manager", "PDF Converter"])


# =======================================================
# ----------------- 2. TYPING SPEED TEST ----------------
# =======================================================
if tool_selection == "Typing Speed Test":
    st.title("⌨️ Typing Speed Test")
    st.write("Test your typing speed and accuracy in real-time.")
    
    # 1. The data pools
    import string
    import json
    
    letters = list(string.ascii_lowercase + string.digits + "!@#$%^&*()_+-=[]{}|;':,.<>/?`~ ")
    words = ["apple", "banana", "table", "chair", "mountain", "river", "ocean", "space", "rocket", "planet",
             "orbit", "galaxy", "universe", "telescope", "computer", "keyboard", "mouse", "screen", "window", "door"]
    sentences = [
        "To be or not to be, that is the ultimate question.",
        "Sphinx of black quartz, judge my vow!",
        "Artificial Intelligence is changing the world very quickly.",
        "Programming is not about memorizing code; it is about solving problems."
    ]

    # 2. Difficulty Selection
    difficulty = st.radio("Choose Difficulty:", ["1. Easy (30 Letters)", "2. Medium (10 Words)", "3. Hard (5 Sentences)"])

    if 'test_active' not in st.session_state:
        st.session_state.test_active = False

    def start_test():
        st.session_state.test_active = True
        if "Easy" in difficulty:
            st.session_state.pool = letters
            st.session_state.target_count = 30
        elif "Medium" in difficulty:
            st.session_state.pool = words
            st.session_state.target_count = 10
        else:
            st.session_state.pool = sentences
            st.session_state.target_count = 5

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
    st.write("This is a placeholder for your Capstone project! You can build the logic here.")
    st.info("Status: Under Construction")


# =======================================================
# ----------------- 4. PDF CONVERTER --------------------
# =======================================================
else:
    st.title("📄 PDF Converter")
    st.write("Merge, split, and convert your PDF files effortlessly.")
    st.info("Status: Under Construction")
