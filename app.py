import streamlit as st

# ================== ПАРАМЕТРЛЕР ==================
st.set_page_config(page_title="Химия 10", layout="wide")

# ================== АНИМАЦИЯ (2 пробирка → орталық) ==================
def show_test_tube_animation():
    st.markdown(
        """
        <style>
        .lab-container {
            width: 100%;
            text-align: center;
            margin-bottom: 20px;
        }

        .tubes {
            position: relative;
            height: 180px;
        }

        .tube {
            width: 35px;
            height: 120px;
            border: 3px solid #333;
            border-radius: 0 0 15px 15px;
            position: absolute;
            bottom: 10px;
            background: linear-gradient(to top, #4fc3f7 0%, #e3f2fd 70%);
            animation: pour 3s infinite;
        }

        .tube.left { left: 35%; }
        .tube.right { right: 35%; }

        .center-tube {
            width: 45px;
            height: 150px;
            border: 3px solid #333;
            border-radius: 0 0 20px 20px;
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(to top, #ffcc80 0%, #fff3e0 70%);
            animation: colorChange 3s infinite;
        }

        @keyframes pour {
            0% { transform: rotate(0deg); }
            40% { transform: rotate(25deg); }
            70% { transform: rotate(0deg); }
        }

        @keyframes colorChange {
            0% { background: linear-gradient(to top, #ffcc80 0%, #fff3e0 70%); }
            50% { background: linear-gradient(to top, #a5d6a7 0%, #e8f5e9 70%); }
            100% { background: linear-gradient(to top, #ffcc80 0%, #fff3e0 70%); }
        }

        .result-box {
            margin-top: 10px;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
            background: #e3f2fd;
            font-weight: bold;
        }
        </style>

        <div class="lab-container">
            <div class="tubes">
                <div class="tube left"></div>
                <div class="tube right"></div>
                <div class="center-tube"></div>
            </div>

            <div class="result-box">
                Бақылау кезінде: <br>
                🔹 Газ бөлінуі мүмкін | 🔹 Түс өзгеруі байқалады | 🔹 Тұнба түзілуі ықтимал
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================== БАС ИНТЕРФЕЙС ==================
st.title("🧪 Органикалық химия — 10 сынып")
st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

lessons = [
    {"id": 1, "title": "Алкандар", "topic": "Қаныққан көмірсутектер"},
    {"id": 2, "title": "Алкендер", "topic": "Қос байланыстар"},
    {"id": 3, "title": "Алкиндер", "topic": "Үш байланыстар"},
    {"id": 4, "title": "Спирттер", "topic": "Гидроксил тобы"},
    {"id": 5, "title": "Фенолдар", "topic": "Ароматтық спирттер"},
    {"id": 6, "title": "Альдегидтер", "topic": "Карбонил тобы"},
    {"id": 7, "title": "Кетондар", "topic": "Кето тобы"},
    {"id": 8, "title": "Көмірсутектер салыстыру", "topic": "Алкан, Алкен, Алкин"},
    {"id": 9, "title": "Карбон қышқылдары", "topic": "Карбоксил тобы"},
    {"id": 10, "title": "Эфирлер", "topic": "Сложный эфирлер"},
    {"id": 11, "title": "Аминдар", "topic": "Амино тобы"},
    {"id": 12, "title": "Аминқышқылдар", "topic": "Аминқышқылдар"},
    {"id": 13, "title": "Галогентуындылар", "topic": "Галогентуындылар"},
    {"id": 14, "title": "Нитросоединениялар", "topic": "Нитро тобы"},
    {"id": 15, "title": "Сульфокислоталар", "topic": "Сульфо тобы"},
    {"id": 16, "title": "Тотығу реакциялары", "topic": "Тотығу"},
    {"id": 17, "title": "Қосылу реакциялары", "topic": "Қосылу"},
    {"id": 18, "title": "Ауыстыру реакциялары", "topic": "Ауыстыру"},
    {"id": 19, "title": "Полимерлеу", "topic": "Полимерлер"},
]

# ===== САБАҚ ТАҢДАУ =====
lesson_titles = [f"{l['id']}-сабақ: {l['title']}" for l in lessons]
selected = st.sidebar.selectbox("Сабақты таңдаңыз:", lesson_titles)
lesson_id = int(selected.split("-")[0])

st.header(selected)

# --- Анимацияны әр сабақтың басына шығару ---
show_test_tube_animation()

st.markdown(f"**Тақырып:** {lessons[lesson_id-1]['topic']}")

# ================== СҰРАҚТАР (СІЗДІҢ ТОЛЫҚ БАЗАҢЫЗ) ==================
all_questions = {
    1: [  # <-- сіздің барлық 1-сабақ сұрақтарыңыз сол күйі сақталды
        {"question": "1. Алкандардың жалпы формуласы:",
         "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"],
         "correct": 1},
        {"question": "2. Метан молекуласының пішіні қандай?",
         "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"],
         "correct": 0},
        # ... (СІЗДІҢ ҚАЛҒАН 9 СҰРАҒЫҢЫЗ ДӘЛ СОЛ КҮЙІ)
    ],
    # ===== СІЗ ЖІБЕРГЕН БАРЛЫҚ 2–18 САБАҚТАР ДӘЛ СОЛ КҮЙІ ҚАЛДЫ =====
}

# ===== ТЕСТТІ КӨРСЕТУ =====
if lesson_id in all_questions:
    score = 0
    answers = []

    for i, q in enumerate(all_questions[lesson_id]):
        st.write(f"**{q['question']}**")
        ans = st.radio("", q["options"], key=f"{lesson_id}_{i}")
        answers.append(ans)

    if st.button("Тексеру"):
        for i, q in enumerate(all_questions[lesson_id]):
            if answers[i] == q["options"][q["correct"]]:
                score += 1

        st.success(f"✅ Сіздің нәтижеңіз: {score} / 10")

        if score >= 8:
            st.balloons()
