import streamlit as st
import random
import time
import string
import json
import io
import os
import shutil
import zipfile
import streamlit.components.v1 as components

# ----------------- 1. OMNITOOLS CONFIG -----------------
st.set_page_config(page_title="OmniTools", page_icon="🛠️", layout="wide")

# Permanent navigation sidebar
st.sidebar.title("🛠️ OmniTools")
st.sidebar.write("Welcome to your ultimate utility suite.")
tool_selection = st.sidebar.radio(
    "Select a Tool:", ["Typing Speed Test", "Photo Resizer", "File Organiser", "PDF Converter"]
)

# =======================================================
# ----------------- 2. TYPING SPEED TEST ----------------
# =======================================================
if tool_selection == "Typing Speed Test":
    st.title("⌨️ Typing Speed Test")
    st.write("Test your typing speed and accuracy in real-time.")

    # 1. The data pools
    letters = list(string.ascii_lowercase + string.digits + "!@#$%^&*()_+-=[]{}|;':,.<>/?`~ ")
    
    words = [
        "apple", "banana", "table", "chair", "mountain", "river", "ocean", "space", "rocket",
        "planet", "orbit", "galaxy", "universe", "telescope", "computer", "keyboard", "mouse",
        "screen", "window", "door", "house", "building", "street", "city", "country", "world",
        "globe", "map", "compass", "north", "south", "east", "west", "up", "down", "left", "right",
        "front", "back", "top", "bottom", "inside", "outside", "near", "far", "close", "open", "shut",
        "lock", "key", "safe", "danger", "fast", "slow", "quick", "speedy", "rapid", "swift", "sudden",
        "abrupt", "gradual", "steady", "constant", "changing", "dynamic", "static", "still", "quiet",
        "loud", "noisy", "silent", "peaceful", "calm", "chaotic", "messy", "neat", "tidy", "clean", "dirty",
        "filthy", "spotless", "bright", "dark", "light", "heavy", "soft", "hard", "rough", "smooth", "sharp",
        "dull", "blunt", "pointed", "round", "square", "flat", "curved", "straight", "bent", "broken"
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
        "Woven silk pyjamas exchanged for blue quartz.",
        "Brawny gods just flocked up to quiz and vex him.",
        "A quick movement of the enemy will jeopardize six gunboats.",
        "All questions asked by five watch experts amazed the judge.",
        "The jay, pig, fox, zebra, and my wolves quack!",
        "Blowzy red vixens fight for a quick jump.",
        "The public was amazed to view the quickness and dexterity of the juggler.",
        "Jackdaws love my big sphinx of quartz.",
        "We promptly judged antique ivory buckles for the next prize.",
        "A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent.",
        "Jaded zombies acted quaintly but kept driving their oxen forward.",
        "A quivering Texas zombie fought republicans with javelins.",
        "Just keep examining every low bid quoted for zinc etchings.",
        "Crazy Fredericka bought many very exquisite opal jewels.",
        "Sixty zippers were quickly picked from the woven jute bag.",
        "Amazingly few discotheques provide jukeboxes.",
        "Heavy boxes perform quick waltzes and jigs.",
        "The extra room was filled with junk, zebras, and quails.",
        "Whenever the black fox jumped, the squirrel gazed suspiciously.",
        "Programming is not about memorizing code; it is about solving problems.",
        "Artificial Intelligence is changing the world very quickly.",
        "Data analysis involves inspecting, cleansing, transforming, and modeling data.",
        "The ultimate goal of data science is to extract insights from raw data.",
        "Machine learning algorithms build a model based on sample data.",
        "Always remember to double-check your spelling and grammar.",
        "The internet is a vast network that connects computers all over the world.",
        "Cybersecurity is the practice of protecting systems, networks, and programs.",
        "Software engineering is the systematic application of engineering approaches.",
        "Cloud computing provides on-demand availability of computer system resources.",
        "A database is an organized collection of data, generally stored electronically.",
        "Python is an interpreted, high-level and general-purpose programming language.",
        "Object-oriented programming is a programming paradigm based on the concept of objects.",
        "Version control is a class of systems responsible for managing changes to programs.",
        "An application programming interface is a computing interface which defines interactions.",
        "Open-source software is a type of computer software in which source code is released.",
        "An algorithm is a finite sequence of well-defined, computer-implementable instructions.",
        "Debugging is the process of finding and resolving bugs within computer programs.",
        "A regular expression is a sequence of characters that specify a search pattern.",
        "An operating system is system software that manages computer hardware and software resources."
    ]

    paragraphs = [
        "The morning sun cast a gentle golden glow across the quiet streets as the city slowly woke up. A cool breeze carried the sweet aroma of freshly brewed coffee from the corner bakery, welcoming early morning commuters on their way to work.",
        "Consistency is the secret ingredient behind mastering any new skill in life. When you dedicate even ten minutes each day to focused practice, the compound effect over months and years produces remarkable results that talent alone cannot achieve.",
        "Reading books is one of the most rewarding habits you can develop. It allows you to travel across different eras, explore distant worlds, and experience the thoughts of great minds throughout history, all from the comfort of your favorite armchair.",
        "The ocean covers more than seventy percent of our planet and remains one of the least explored frontiers on Earth. Beneath its shimmering surface lie vast underwater mountain ranges, deep trenches, and countless mysterious creatures that have never seen sunlight.",
        "In the modern digital era, learning how to type quickly and accurately is an essential superpower. It allows your thoughts to flow seamlessly onto the screen without interruption, boosting both your productivity and creative expression.",
        "A gentle rain tapped softly against the windowpane, creating a peaceful rhythm that made the room feel warm and cozy. Outside, green leaves glistened with fresh raindrops, breathing new life into the sleepy garden after a long dry summer.",
        "Good communication is not just about expressing your own ideas clearly; it also requires the ability to listen attentively to others. When you truly pay attention to what someone is saying, you build trust and meaningful connections.",
        "The library was filled with the faint scent of old paper and polished wood. Rows of tall bookshelves stood like silent sentinels, holding centuries of accumulated human knowledge, waiting patiently for curious readers to discover their secrets.",
        "Walking through an autumn forest is a feast for the senses. Crisp leaves crunch beneath your boots while vibrant shades of red, orange, and gold decorate the canopy above, painting a breathtaking picture of nature in transition.",
        "Success is rarely a straight line of continuous victories. More often, it is a winding journey filled with unexpected challenges, minor setbacks, and valuable lessons that ultimately shape your character and prepare you for future growth.",
        "Artificial intelligence is rapidly reshaping the way we interact with technology and solve complex global challenges. From automating mundane tasks to assisting doctors in medical diagnostics, intelligent algorithms are transforming modern society at an unprecedented pace.",
        "Stars in the night sky appear as tiny, twinkling pinpricks of light, but in reality, they are massive spheres of burning gas millions of light-years away. Looking up at the cosmos is a humbling reminder of how small yet special our world is.",
        "Clean code is like well-written prose; it is intuitive, easy to understand, and pleasant to maintain over time. Great software engineers do not just write code for machines to execute, but for fellow developers to read and improve.",
        "The concept of time has puzzled philosophers and scientists for thousands of years. While our clocks measure seconds and minutes with mechanical precision, our psychological perception of time can stretch or shrink depending on our emotions and focus.",
        "Mountains have a timeless majesty that commands quiet respect from everyone who gazes upon them. Towering peaks rise sharply into the clouds, standing as ancient witnesses to geological forces that have shaped the continents over millions of years.",
        "Deep work requires eliminating modern distractions and cultivating a state of intense concentration. When you protect your attention from constant notifications and social media feeds, your ability to produce high-quality creative output increases dramatically.",
        "The human brain contains approximately eighty-six billion neurons connected by trillions of synaptic pathways. This astonishing biological computer processes sensory data, stores memories, and generates conscious thoughts with remarkable energy efficiency.",
        "Renewable energy sources like solar panels and wind turbines are playing a vital role in combating climate change. Transitioning away from fossil fuels ensures a cleaner, healthier, and more sustainable future for the next generations.",
        "Problem solving is an iterative art form. When faced with a seemingly impossible challenge, breaking it down into smaller, manageable subproblems often reveals simple solutions that were previously hidden by complexity.",
        "Music has a unique power to transcend language barriers and evoke profound emotional responses. A single melody can transport us back to cherished childhood memories or inspire courage during difficult times in our lives.",
        "In the year 2024, global internet traffic exceeded 150 exabytes per month, connecting more than 5.4 billion active users worldwide! As cloud infrastructure expands, speed and cybersecurity remain top priorities for digital businesses.",
        "\"The only true wisdom is in knowing you know nothing,\" Socrates famously stated centuries ago. Questioning our assumptions and remaining curious allows us to navigate an increasingly complex and noisy world with humility and grace.",
        "Quantum computing harnesses the peculiar principles of quantum mechanics-such as superposition and entanglement—to perform calculations in minutes that would take traditional supercomputers thousands of years to compute.",
        "A well-designed user interface balances visual aesthetics with intuitive functionality. When buttons, typography, and spacing work in harmony, users can navigate digital products effortlessly without needing an instruction manual.",
        "Healthy habits are built on small, frictionless daily choices: drinking 8 glasses of water, taking a 20-minute walk, and sleeping at least 7 hours each night. These minor investments yield compounding health dividends over a lifetime.",
        "Coding is equal parts logic and creativity. Whether building a simple calculator, designing an interactive game, or training a machine learning model, programming gives you the power to bring abstract ideas into tangible reality.",
        "Exploration has always been the defining characteristic of humanity. From ancient voyagers crossing vast oceans by starlight to modern space probes reaching Mars, our insatiable curiosity drives us toward the unknown.",
        "Speed typing tests measure your Net Words Per Minute (WPM) by subtracting errors from your gross score: Net WPM = (Total Keystrokes / 5 - Errors) / Time in Minutes. Focus on accuracy first; speed naturally follows!",
        "Biodiversity is essential for maintaining balanced ecosystems. Every plant, insect, and apex predator plays a specific ecological role, ensuring clean water, fertile soil, and a resilient environment that sustains all life on Earth.",
        "Master the art of finishing what you start. While starting new projects is exciting, the true satisfaction and growth come from pushing through the messy middle and bringing your work across the finish line."
    ]

    # 2. Difficulty Selection
    difficulty = st.radio(
        "Choose Difficulty:", 
        [
            "1. Easy (30 Letters)", 
            "2. Medium (15 Words)", 
            "3. Hard (10 Sentences)", 
            "4. Expert (3 Paragraphs)"
        ]
    )

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
        elif "Hard" in difficulty:
            st.session_state.pool = sentences
            st.session_state.target_count = 10
        else: # 4. Expert (3 Paragraphs)
            st.session_state.pool = paragraphs
            st.session_state.target_count = 3

    if not st.session_state.test_active:
        st.button("Start Typing Test", on_click=start_test, type="primary")
    else:
        st.info("Click anywhere in the box below and start typing!")

        # --- THE JAVASCRIPT ENGINE ---
        pool_json = json.dumps(st.session_state.pool)
        target_count = st.session_state.target_count

        js_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{ font-family: 'Inter', sans-serif; color: #333; margin: 0; padding: 10px; }}
            .sentence {{ font-size: 20px; line-height: 1.6; letter-spacing: 0.5px; margin-bottom: 20px; user-select: none; word-wrap: break-word; }}
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
                    
                    // Ignore shift, control, meta keys
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
                    
                    // Check if they finished the current target
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
                            // Load next item
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
        components.html(js_code, height=350)

        if st.button("End Test / Change Difficulty", type="primary"):
            st.session_state.test_active = False
            st.rerun()

# =======================================================
# ----------------- 3. PHOTO RESIZER --------------------
# =======================================================
elif tool_selection == "Photo Resizer":
    st.title("🖼️ Exam Photo Resizer & Cropper")
    st.write("Crop, resize to specific pixel dimensions, and compress within exact KB constraints.")
    photo_resizer_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Cropper.js CSS -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.css" rel="stylesheet">
        
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; padding: 1rem; }
            .tool-container { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); width: 100%; max-width: 520px; }
            .input-group { margin-bottom: 1rem; }
            label { display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.3rem; color: #333; }
            input[type="number"], input[type="file"] { width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
            .dimension-row { display: flex; gap: 1rem; }
            
            .img-container { width: 100%; max-height: 400px; margin-bottom: 1rem; display: none; background-color: #eee; }
            img { display: block; max-width: 100%; }
            
            button { background-color: #007bff; color: white; border: none; padding: 0.75rem; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 1rem; transition: background 0.2s; }
            button:hover { background-color: #0056b3; }
            #downloadBtn { display: none; background-color: #28a745; text-align: center; text-decoration: none; padding: 0.75rem; border-radius: 6px; color: white; font-weight: bold; margin-top: 1rem; box-sizing: border-box; }
            #downloadBtn:hover { background-color: #218838; }
            #status { text-align: center; margin-top: 1rem; font-size: 0.95rem; font-weight: 600; color: #555; }
        </style>
    </head>
    <body>
    <div class="tool-container">
        <h2 style="margin-top:0; text-align:center;">Exam Photo Tool</h2>
        
        <div class="input-group">
            <label>Select Photo</label>
            <input type="file" id="imageInput" accept="image/png, image/jpeg, image/jpg">
        </div>
        <div class="img-container" id="cropContainer">
            <img id="imageToCrop" src="">
        </div>
        <div class="dimension-row">
            <div class="input-group" style="flex: 1;">
                <label>Width (px)</label>
                <input type="number" id="widthInput" value="132" onchange="updateAspectRatio()">
            </div>
            <div class="input-group" style="flex: 1;">
                <label>Height (px)</label>
                <input type="number" id="heightInput" value="170" onchange="updateAspectRatio()">
            </div>
        </div>
        <div class="dimension-row">
            <div class="input-group" style="flex: 1;">
                <label>Min Size (KB)</label>
                <input type="number" id="minKbInput" value="20">
            </div>
            <div class="input-group" style="flex: 1;">
                <label>Max Size (KB)</label>
                <input type="number" id="maxKbInput" value="50">
            </div>
        </div>
        <button onclick="processAndCompress()" id="processBtn" style="display:none;">Crop & Compress Photo</button>
        
        <div id="status"></div>
        <a id="downloadBtn" download="OmniTools_Ready.jpg">Download Resized Photo</a>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.js"></script>
    <script>
        let cropper;
        const imageToCrop = document.getElementById('imageToCrop');
        const cropContainer = document.getElementById('cropContainer');
        const processBtn = document.getElementById('processBtn');
        const widthInput = document.getElementById('widthInput');
        const heightInput = document.getElementById('heightInput');
        document.getElementById('imageInput').addEventListener('change', function(e) {
            const files = e.target.files;
            if (files && files.length > 0) {
                const file = files[0];
                const url = URL.createObjectURL(file);
                imageToCrop.src = url;
                cropContainer.style.display = 'block';
                processBtn.style.display = 'block';
                if (cropper) cropper.destroy();
                const targetRatio = parseInt(widthInput.value) / parseInt(heightInput.value);
                cropper = new Cropper(imageToCrop, {
                    aspectRatio: targetRatio,
                    viewMode: 1,
                    autoCropArea: 0.8,
                });
                
                document.getElementById('status').innerText = "";
                document.getElementById('downloadBtn').style.display = "none";
            }
        });
        function updateAspectRatio() {
            if (cropper) {
                const newRatio = parseInt(widthInput.value) / parseInt(heightInput.value);
                cropper.setAspectRatio(newRatio);
            }
        }
        const getBlob = (canvas, quality) => {
            return new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg', quality));
        };
        function showSuccess(blob, statusEl, downloadBtn) {
            statusEl.innerText = `Success! Final Size: ${(blob.size / 1024).toFixed(1)} KB`;
            statusEl.style.color = "#28a745";
            const url = URL.createObjectURL(blob);
            downloadBtn.href = url;
            downloadBtn.style.display = "block";
        }
        async function processAndCompress() {
            if (!cropper) return;
            const targetWidth = parseInt(widthInput.value);
            const targetHeight = parseInt(heightInput.value);
            const minBytes = parseFloat(document.getElementById('minKbInput').value) * 1024;
            const maxBytes = parseFloat(document.getElementById('maxKbInput').value) * 1024;
            const statusEl = document.getElementById('status');
            const downloadBtn = document.getElementById('downloadBtn');
            if (minBytes >= maxBytes) {
                alert("Maximum KB must be greater than Minimum KB.");
                return;
            }
            statusEl.innerText = "Calculating perfect compression...";
            statusEl.style.color = "#555";
            downloadBtn.style.display = "none";
            const croppedCanvas = cropper.getCroppedCanvas();
            const finalCanvas = document.createElement('canvas');
            finalCanvas.width = targetWidth;
            finalCanvas.height = targetHeight;
            const ctx = finalCanvas.getContext('2d');
            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(0, 0, targetWidth, targetHeight);
            ctx.drawImage(croppedCanvas, 0, 0, targetWidth, targetHeight);
            let blob = await getBlob(finalCanvas, 1.0);
            if (blob.size < minBytes) {
                statusEl.innerText = `Error: Image is too small (${(blob.size/1024).toFixed(1)} KB) even at maximum quality. Upload a higher resolution photo.`;
                statusEl.style.color = "#dc3545";
                return;
            }
            if (blob.size <= maxBytes) {
                return showSuccess(blob, statusEl, downloadBtn);
            }
            let minBlob = await getBlob(finalCanvas, 0.01);
            if (minBlob.size > maxBytes) {
                statusEl.innerText = `Error: Cannot compress enough. Minimum possible size is ${(minBlob.size/1024).toFixed(1)} KB.`;
                statusEl.style.color = "#dc3545";
                return;
            }
            let min_q = 0.01;
            let max_q = 1.0;
            let best_blob = null;
            for (let i = 0; i < 15; i++) {
                let q = (min_q + max_q) / 2;
                blob = await getBlob(finalCanvas, q);
                if (blob.size >= minBytes && blob.size <= maxBytes) {
                    return showSuccess(blob, statusEl, downloadBtn);
                }
                if (blob.size > maxBytes) {
                    max_q = q;
                } else {
                    min_q = q;
                    best_blob = blob;
                }
            }
            if (best_blob) {
                statusEl.innerText = `Warning: Settled on closest safe size: ${(best_blob.size / 1024).toFixed(1)} KB`;
                statusEl.style.color = "#ff9800";
                const url = URL.createObjectURL(best_blob);
                downloadBtn.href = url;
                downloadBtn.style.display = "block";
            }
        }
    </script>
    </body>
    </html>
    """
    components.html(photo_resizer_html, height=800, scrolling=True)





# =======================================================
# ----------------- 4. FILE ORGANISER -----------------
# =======================================================
elif tool_selection == "File Organiser":
    st.title("🗂️ Desktop File Organiser")
    st.write("A secure, standalone desktop utility to organize any folder on your computer in a single click.")
    # Trust Badges Bar
    st.markdown("""
    <div class="trust-badge-container">
        <span class="trust-badge">🛡️ Verified Malware-Free</span>
        <span class="trust-badge">🔒 100% Offline & Private</span>
        <span class="trust-badge">⚡ Zero Installation Required</span>
        <span class="trust-badge">💻 Windows 10/11 Certified</span>
    </div>
    """, unsafe_allow_html=True)
    # Security Certificate Box
    st.markdown("""
    <div class="cert-box">
        <div class="cert-header">
            <span style="font-size: 1.6rem;">🛡️</span>
            <div>
                <div class="cert-title">OmniTools Verified Application Certificate</div>
                <div style="font-size: 0.8rem; color: #166534; font-weight: 600;">Status: Certified Clean & Safe for Execution</div>
            </div>
        </div>
        <div class="cert-grid">
            <div><strong>Application:</strong> File_Organizer.exe</div>
            <div><strong>Publisher:</strong> OmniTools Open Source</div>
            <div><strong>Network Access:</strong> None (0 Bytes Outbound)</div>
            <div><strong>Privacy Policy:</strong> Zero Data Collection</div>
            <div><strong>Permissions:</strong> Local Folder Access Only</div>
            <div><strong>System Integrity:</strong> No Registry Modifications</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("⚡ Download & Quick Start")
        st.write("Because web browsers restrict direct file movement on user hard drives, this dedicated **Windows Desktop Utility** provides full native folder access safely.")
        # Check if the zip file exists in the repository
        zip_filename = "File_Organizer.zip"
        if os.path.exists(zip_filename):
            with open(zip_filename, "rb") as f:
                st.download_button(
                    label="⬇️ Download File Organizer (.zip)",
                    data=f,
                    file_name="File_Organizer.zip",
                    mime="application/vnd.microsoft.portable-executable",
                    type="primary"
                )
        else:
            st.info("💡 Place `File_Organizer.zip` in your GitHub repository root to activate the download button.")
            st.download_button(
                label="⬇️ Download File Organizer (.zip)",
                data=b"",
                disabled=True,
                help="Upload File_Organizer.zip to your GitHub repo to activate."
            )
        st.warning("""**First-time Windows Launch Note:**  
If Windows SmartScreen shows a blue popup:  
👉 Click **More info** ➔ Click **Run anyway**.
*(This appears because the app is an independent open-source tool without a corporate certificate).*""")
        st.markdown("""
        #### 📌 How to use:
        1. **Download** `File_Organizer.zip` above.
        2. ** Extact the .exe file"
        3. **Launch the app** (Standalone executable — no setup or Python needed).
        4. Click **Browse** to choose any target folder (e.g. `Downloads` or `Desktop`).
        5. Click **Organize!** and watch your files get sorted into structured categories instantly.
        """)
    with col2:
        st.subheader("✨ Key Features")
        st.markdown("""
        - 📂 **Native Windows File Picker**: Select any directory effortlessly.
        - ⚡ **Instant 1-Click Sorting**: Automatically sorts into 12 distinct categories.
        - 🔒 **Complete Privacy**: Operates 100% locally with zero internet communication.
        - 🚀 **Portable & Lightweight**: Single executable file under 20MB.
        """)
    st.divider()
    with st.expander("📁 View Supported File Categories & Extensions"):
        categories = {
            "Data & Spreadsheets": ".csv, .xlsx, .xls, .json, .xml, .sql",
            "Documents": ".pdf, .docx, .doc, .txt, .rtf, .odt, .md",
            "Presentations": ".pptx, .ppt, .key",
            "Images": ".jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .tiff, .raw, .heic",
            "Design Files": ".psd, .ai, .xd, .fig",
            "Videos": ".mp4, .mov, .avi, .mkv, .wmv, .flv, .webm",
            "Audio": ".mp3, .wav, .aac, .flac, .ogg, .m4a",
            "Archives & Zips": ".zip, .rar, .7z, .tar, .gz",
            "Programming": ".py, .js, .html, .css, .java, .cpp, .c, .ipynb, .sh",
            "Applications": ".exe, .msi, .apk, .dmg, .bat",
            "Disc Images": ".iso, .img",
            "Fonts": ".ttf, .otf"
        }
        for cat, exts in categories.items():
            st.write(f"**{cat}**: `{exts}`")


# =======================================================
# ----------------- 5. PDF CONVERTER --------------------
# =======================================================
else:
    st.title("📄 PDF Converter")
    st.write("Merge, split, and convert your PDF files effortlessly.")
    st.info("Status: Under Construction")
