
import streamlit as st
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="John Dave G. Budionganon | Portfolio",
    page_icon="🎬",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background: #0b1018;
    color: #e8edf5;
    font-family: 'Poppins', sans-serif;
}

[data-testid="stSidebar"] {
    background: #111b2a;
    border-right: 1px solid #263c59;
}

[data-testid="stSidebar"] * {
    color: #e8edf5 !important;
}

h1, h2, h3 {
    font-family: 'Rajdhani', sans-serif !important;
    color: #55b8ff !important;
    font-weight: 700 !important;
}

p, li, label {
    color: #c5d0df;
}

.hero {
    background: linear-gradient(120deg, #152b45, #101722 75%);
    border: 1px solid #285078;
    border-radius: 18px;
    padding: 45px;
    margin-bottom: 25px;
}

.hero-tag {
    color: #55b8ff;
    letter-spacing: 4px;
    font-size: 11px;
    font-weight: 700;
}

.hero-name {
    font-family: 'Rajdhani', sans-serif;
    font-size: 46px;
    line-height: 1.1;
    color: #ffffff;
    font-weight: 700;
    margin-top: 15px;
}

.hero-desc {
    color: #c5d7e9;
    font-size: 14px;
    line-height: 1.9;
    max-width: 680px;
    margin-top: 18px;
}

.panel {
    background: #121e2c;
    border: 1px solid #263c59;
    border-radius: 14px;
    padding: 25px;
    margin-bottom: 18px;
}

.panel-tag {
    color: #55b8ff;
    letter-spacing: 3px;
    font-size: 10px;
    font-weight: 700;
}

.panel-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 25px;
    font-weight: 700;
    color: #ffffff;
    margin-top: 8px;
    margin-bottom: 12px;
}

.accent {
    color: #55b8ff;
    font-weight: 600;
}

.stButton > button {
    background: #218bd0;
    color: white;
    border: none;
    border-radius: 7px;
}

.stButton > button:hover {
    background: #55b8ff;
    color: #08111b;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ---------------- IMAGE FUNCTION ----------------
def show_image(filename, caption=None):
    image_path = IMAGE_DIR / filename

    if image_path.is_file():
        st.image(
            str(image_path),
            caption=caption,
            use_container_width=True
        )
    else:
        st.info(f"Add {filename} to your images folder to display it.")


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("# JDG.")
    st.caption("PERSONAL PORTFOLIO")
    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Home",
            "About Me",
            "Education",
            "Gaming",
            "Movies",
            "Mechanical Engineering"
        ]
    )

    st.markdown("---")
    st.caption("THINK BEYOND THE FRAME.")


# ---------------- HOME ----------------
if page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">A DIGITAL INTRODUCTION</div>
        <div class="hero-name">
            JOHN DAVE G.<br>BUDIONGANON
        </div>
        <p class="hero-desc">
            Welcome to my personal portfolio. This is a place where
            I share my interests, experiences, and academic journey.
            From exploring virtual worlds and enjoying cinematic stories
            to discovering the principles behind machines and technology,
            every interest gives me another way to learn and grow.
        </p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.3, 1])

    with left:
        st.markdown("## Beyond Entertainment and Technology")

        st.write("""
        I believe that the things we enjoy can reveal different sides
        of our personality. Gaming gives me the opportunity to explore
        challenges and interactive experiences, while watching movies
        lets me appreciate storytelling, creativity, and different
        perspectives.

        Alongside these interests, my journey in Mechanical Engineering
        allows me to explore how machines operate, how systems are
        designed, and how scientific ideas can be turned into practical
        solutions. These different experiences make learning and
        personal growth more interesting.
        """)

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">PERSONAL PHILOSOPHY</div>
            <div class="panel-title">Stay Curious. Keep Exploring.</div>
            There is always something new to discover, whether
            through an experience, a story, or an idea worth understanding.
        </div>
        """, unsafe_allow_html=True)

    with right:
        show_image("profile.jpg", "John Dave G. Budionganon")


# ---------------- ABOUT ME ----------------
elif page == "About Me":

    st.markdown("# ABOUT ME")
    st.caption("GETTING TO KNOW THE PERSON BEHIND THE SCREEN")

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">INTRODUCTION</div>
        <div class="panel-title">Different Interests, One Journey</div>

        My name is <span class="accent">John Dave G. Budionganon</span>.
        I enjoy spending my free time doing activities that entertain
        me while also allowing me to explore new ideas and experiences.
        Gaming and watching movies are two of my favorite hobbies because
        they offer different ways to enjoy stories, challenges, and
        creative worlds.

        I also value education and the opportunity to learn beyond
        what I already know. As a Mechanical Engineering student,
        I am gradually developing my understanding of machines,
        technology, and the engineering principles that influence
        many aspects of everyday life.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## My Interests")

    col1, col2 = st.columns(2)

    with col1:
        show_image("gaming.jpg", "Gaming")

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">HOBBY 01</div>
            <div class="panel-title">Gaming</div>
            Gaming is one of the ways I enjoy my free time.
            I like experiencing different game environments,
            taking on challenges, and discovering what makes
            each game unique. It is an activity that combines
            entertainment, strategy, and exploration.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        show_image("movies.jpg", "Watching movies")

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">HOBBY 02</div>
            <div class="panel-title">Watching Movies</div>
            Movies allow me to experience different stories,
            characters, and perspectives. I enjoy how a film
            can take viewers into another world, communicate
            emotions, and leave ideas worth thinking about
            even after the story ends.
        </div>
        """, unsafe_allow_html=True)


# ---------------- EDUCATION ----------------
elif page == "Education":

    st.markdown("# EDUCATIONAL BACKGROUND")
    st.caption("THE FOUNDATION OF MY CONTINUOUS LEARNING JOURNEY")

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">SENIOR HIGH SCHOOL</div>
        <div class="panel-title">Tabon M. Estrella National High School</div>

        My senior high school experience at Tabon M. Estrella
        National High School was an important part of my academic
        development. It provided opportunities to gain knowledge,
        develop essential skills, interact with different people,
        and prepare for the next stage of my education.

        The experiences I gained during this period became part
        of the foundation that I continue to build on as a college student.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">COLLEGE EDUCATION</div>
        <div class="panel-title">North Eastern Mindanao State University</div>

        **Program: Bachelor of Science in Mechanical Engineering**

        Continuing my studies at North Eastern Mindanao State
        University represents a new chapter filled with learning,
        challenges, and opportunities. As a Mechanical Engineering
        student, I am introduced to concepts involving mathematics,
        physics, design, and mechanical systems.

        This academic path encourages me to become more analytical,
        patient, and creative when approaching problems. It also
        helps me understand how engineering knowledge can be
        applied to machines, equipment, and technologies that
        contribute to everyday life.
    </div>
    """, unsafe_allow_html=True)


# ---------------- GAMING ----------------
elif page == "Gaming":

    st.markdown("# THE WORLD OF GAMING")
    st.caption("CHALLENGES, STRATEGY, AND VIRTUAL EXPERIENCES")

    left, right = st.columns([1, 1])

    with left:
        show_image("gaming.jpg", "Exploring virtual worlds")

    with right:
        st.markdown("""
        <div class="panel">
            <div class="panel-tag">HOBBY 01</div>
            <div class="panel-title">More Than Just Playing</div>

            Gaming is one of my favorite ways to spend my free time.
            I enjoy how games can offer different experiences,
            from exploring imaginative environments to completing
            objectives and overcoming challenging situations.

            What makes gaming interesting to me is that every game
            has its own style, mechanics, and experience. Some require
            careful decisions, while others focus on exploration
            and storytelling. It is a hobby that keeps me entertained
            and gives me something different to experience whenever
            I play.
        </div>
        """, unsafe_allow_html=True)


# ---------------- MOVIES ----------------
elif page == "Movies":

    st.markdown("# THE ART OF CINEMA")
    st.caption("EVERY FILM HAS A STORY WORTH EXPERIENCING")

    left, right = st.columns([1, 1])

    with left:
        show_image("movies.jpg", "Stories brought to life")

    with right:
        st.markdown("""
        <div class="panel">
            <div class="panel-tag">HOBBY 02</div>
            <div class="panel-title">A Different World in Every Film</div>

            Watching movies is another activity I genuinely enjoy.
            I appreciate how films bring together storytelling,
            visuals, sound, and performances to create experiences
            that can entertain, inspire, and make people think.

            Every movie offers something different. Some take viewers
            on exciting adventures, while others explore meaningful
            situations and human experiences. I enjoy discovering
            these different stories and seeing how each film presents
            its own perspective on the world.
        </div>
        """, unsafe_allow_html=True)


# ---------------- MECHANICAL ENGINEERING ----------------
elif page == "Mechanical Engineering":

    st.markdown("# MECHANICAL ENGINEERING")
    st.caption("WHERE SCIENCE, DESIGN, AND INNOVATION COME TOGETHER")

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">MY COLLEGE PROGRAM</div>
        <div class="panel-title">Bachelor of Science in Mechanical Engineering</div>

        Mechanical Engineering is a field that focuses on understanding,
        designing, developing, and improving machines and mechanical
        systems. It combines mathematics, physics, creativity, and
        technical knowledge to help solve problems and create
        practical solutions.

        As a student of this program at North Eastern Mindanao
        State University, I have the opportunity to learn about
        the principles behind how machines operate, how different
        components interact, and how engineering designs are
        transformed into useful applications.

        This course challenges me to develop logical thinking,
        patience, accuracy, and problem-solving skills. It also
        encourages me to look beyond how things appear and understand
        the processes and mechanisms that make them function.

        My goal is to continue learning, improve my technical abilities,
        and prepare myself for future opportunities where I can apply
        engineering knowledge to real-world challenges.
    </div>
    """, unsafe_allow_html=True)

    show_image("engineering.jpg", "Discovering the world of engineering")


# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:20px;">
    <p style="color:#55b8ff; font-family:'Rajdhani'; font-size:24px; font-weight:700;">
        JOHN DAVE G. BUDIONGANON
    </p>
    <p style="color:#8293a8; font-size:11px; letter-spacing:2px;">
        PERSONAL PORTFOLIO | BUILT WITH STREAMLIT
    </p>
</div>
""", unsafe_allow_html=True)
