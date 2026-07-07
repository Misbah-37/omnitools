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
    words = ["apple", "banana", "table", "chair", "mountain", "river", "ocean", "space", "rocket",
             "planet", "orbit", "galaxy", "universe", "telescope", "computer", "keyboard", "mouse",
             "screen", "window", "door", "house", "building", "street", "city", "country", "world",
             "globe", "map", "compass", "north", "south", "east", "west", "up", "down", "left", "right",
             "front", "back", "top", "bottom", "inside", "outside", "near", "far", "close", "open", "shut",
             "lock", "key", "safe", "danger", "fast", "slow", "quick", "speedy", "rapid", "swift", "sudden",
             "abrupt", "gradual", "steady", "constant", "changing", "dynamic", "static", "still", "quiet",
             "loud", "noisy", "silent", "peaceful", "calm", "chaotic", "messy", "neat", "tidy", "clean", "dirty",
             "filthy", "spotless", "bright", "dark", "light", "heavy", "soft", "hard", "rough", "smooth", "sharp",
             "dull", "blunt", "pointed", "round", "square", "flat", "curved", "straight", "bent", "broken"]
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
        "Sex-charged fop blew my junk TV quiz.",
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
        "Sympathizing would fix Quaker objectives.",
        "The extra room was filled with junk, zebras, and quails.",
        "Whenever the black fox jumped, the squirrel gazed suspiciously.",
        "My girl wove six dozen plaid jackets before she quit.",
        "Six big devils from Japan quickly forgot how to waltz.",
        "The lazy major was fixing Cupid's broken quiver.",
        "A very bad quack might jinx zippy fowls.",
        "Few quips galvanized the mock jury box.",
        "Quick zephyrs blow, vexing daft Jim.",
        "John quickly extemporized five tow bags.",
        "The explorer was frozen in his big kayak just after making queer discoveries.",
        "A large fawn jumped quickly over white zinc boxes.",
        "Fifty-four joyful kids quickly gave up their prize.",
        "The crazy fox jumped over the white fence and ran away quickly.",
        "Many big zebras were killed by the quick, jumping fox.",
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
        "Web development is the work involved in developing a website for the internet.",
        "HTML is the standard markup language for documents designed to be displayed.",
        "Cascading Style Sheets is a style sheet language used for describing presentation.",
        "JavaScript is a programming language that conforms to the ECMAScript specification.",
        "Python is an interpreted, high-level and general-purpose programming language.",
        "Object-oriented programming is a programming paradigm based on the concept of objects.",
        "Version control is a class of systems responsible for managing changes to programs.",
        "An application programming interface is a computing interface which defines interactions.",
        "Open-source software is a type of computer software in which source code is released.",
        "An algorithm is a finite sequence of well-defined, computer-implementable instructions.",
        "Debugging is the process of finding and resolving bugs within computer programs.",
        "A graphical user interface allows users to interact with electronic devices.",
        "User experience design is the process of enhancing user satisfaction.",
        "Agile software development comprises various approaches to software development.",
        "A variable is a storage location paired with an associated symbolic name.",
        "Syntax refers to the rules that specify the correct combined sequence of symbols.",
        "A framework is an abstraction in which software providing generic functionality can be selectively changed.",
        "An integrated development environment is a software application that provides comprehensive facilities.",
        "Continuous integration is the practice of merging all developers' working copies.",
        "A compiler is a computer program that translates computer code written in one language.",
        "Recursion occurs when a thing is defined in terms of itself or of its type.",
        "A data structure is a data organization, management, and storage format.",
        "An array is a data structure consisting of a collection of elements.",
        "A linked list is a linear collection of data elements whose order is not given.",
        "A hash table is a data structure that implements an associative array abstract data type.",
        "A binary tree is a tree data structure in which each node has at most two children.",
        "Dynamic programming is both a mathematical optimization method and a computer programming method.",
        "A regular expression is a sequence of characters that specify a search pattern.",
        "Multithreading is the ability of a central processing unit to provide multiple threads.",
        "Garbage collection is a form of automatic memory management.",
        "A virtual machine is an emulation of a computer system.",
        "A container is a standard unit of software that packages up code and all its dependencies.",
        "Serverless computing is a cloud computing execution model.",
        "A microservice architecture arranges an application as a collection of loosely coupled services.",
        "REST is a software architectural style that defines a set of constraints.",
        "GraphQL is an open-source data query and manipulation language for APIs.",
        "SQL is a domain-specific language used in programming and designed for managing data.",
        "NoSQL database provides a mechanism for storage and retrieval of data.",
        "A cache is a hardware or software component that stores data so that future requests can be served faster.",
        "Latency is the time interval between the stimulation and response.",
        "Bandwidth is the maximum rate of data transfer across a given path.",
        "Encryption is the process of encoding information.",
        "Authentication is the act of proving an assertion, such as the identity of a computer system user.",
        "Authorization is the function of specifying access rights/privileges to resources.",
        "A firewall is a network security system that monitors and controls incoming and outgoing network traffic.",
        "An operating system is system software that manages computer hardware and software resources."
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
