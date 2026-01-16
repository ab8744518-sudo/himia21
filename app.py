import streamlit as st

# Әр сабаққа өз түсі (19 сабақ)
lesson_colors = {
    1: ("#00c8ff", "#00c8ff", "#9d00ff"),   # Алкандар
    2: ("#00ff7f", "#00ff7f", "#1e90ff"),   # Алкендер
    3: ("#ffd700", "#ffd700", "#ff4500"),   # Алкиндер
    4: ("#87cefa", "#87cefa", "#4682b4"),   # Спирттер
    5: ("#ff69b4", "#ff69b4", "#8b008b"),   # Фенолдар
    6: ("#ffa500", "#ffa500", "#ff0000"),   # Альдегидтер
    7: ("#adff2f", "#adff2f", "#006400"),   # Кетондар
    8: ("#40e0d0", "#40e0d0", "#00008b"),   # Көмірсутектер салыстыру
    9: ("#ffdead", "#ffdead", "#cd853f"),   # Карбон қышқылдары
    10: ("#f0e68c", "#f0e68c", "#daa520"),  # Эфирлер
    11: ("#dda0dd", "#dda0dd", "#800080"),  # Аминдар
    12: ("#98fb98", "#98fb98", "#228b22"),  # Аминқышқылдар
    13: ("#afeeee", "#afeeee", "#2f4f4f"),  # Галогентуындылар
    14: ("#fffacd", "#fffacd", "#b8860b"),  # Нитросоединениялар
    15: ("#e6e6fa", "#e6e6fa", "#483d8b"),  # Сульфокислоталар
    16: ("#ffb6c1", "#ffb6c1", "#dc143c"),  # Тотығу
    17: ("#90ee90", "#90ee90", "#006400"),  # Қосылу
    18: ("#add8e6", "#add8e6", "#000080"),  # Ауыстыру
    19: ("#ff6347", "#ff6347", "#8b0000"),  # Полимерлеу
}

def show_tubes(lesson_id):
    left, right, center = lesson_colors.get(lesson_id, ("#00c8ff","#00c8ff","#9d00ff"))

    st.markdown(f"""
    <style>
    .lab-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 120px;
        margin: 40px 0;
    }}

    .test-tube {{
        width: 60px;
        height: 180px;
        border: 3px solid white;
        border-radius: 0 0 20px 20px;
        position: relative;
        background: rgba(255,255,255,0.1);
        overflow: hidden;
    }}

    .liquid {{
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 60%;
        animation: pour 2s infinite ease-in-out;
    }}

    .left .liquid {{ background: {left}; animation-delay: 0s; }}
    .right .liquid {{ background: {right}; animation-delay: 1s; }}
    .center .liquid {{ background: {center}; height: 30%; }}

    @keyframes pour {{
        0% {{ height: 60%; }}
        50% {{ height: 10%; }}
        100% {{ height: 60%; }}
    }}
    </style>

    <div class="lab-container">
      <div class="test-tube left"><div class="liquid"></div></div>
      <div class="test-tube center"><div class="liquid"></div></div>
      <div class="test-tube right"><div class="liquid"></div></div>
    </div>
    """, unsafe_allow_html=True)
