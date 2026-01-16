import streamlit as st
import random
import time

# Настройка страницы
st.set_page_config(page_title="Химия 10", layout="wide")

# Заголовок
st.title("🧪 Органикалық химия - 10 сынып")
st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# CSS для анимации и стилей
st.markdown("""
<style>
    .test-tube-animation {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
        position: relative;
        margin: 20px 0;
    }
    
    .test-tube {
        width: 80px;
        height: 150px;
        background: linear-gradient(to bottom, #e6f7ff 0%, #b3e0ff 100%);
        border-radius: 0 0 40px 40px;
        position: relative;
        border: 3px solid #0066cc;
        z-index: 2;
    }
    
    .test-tube-neck {
        width: 30px;
        height: 50px;
        background: linear-gradient(to bottom, #e6f7ff 0%, #b3e0ff 100%);
        position: absolute;
        top: -50px;
        left: 25px;
        border: 3px solid #0066cc;
        border-bottom: none;
        border-radius: 20px 20px 0 0;
    }
    
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        border-radius: 0 0 37px 37px;
        transition: height 1s ease;
    }
    
    .bubble {
        position: absolute;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 50%;
        animation: floatUp 2s infinite ease-in-out;
    }
    
    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-100px); opacity: 0; }
    }
    
    .molecule {
        font-size: 24px;
        font-weight: bold;
        color: #0066cc;
        animation: rotate 4s infinite linear;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .formula-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .formula {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .reaction {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin: 20px 0;
    }
    
    .reaction-arrow {
        font-size: 30px;
        color: #ff6b6b;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    .lesson-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 15px;
        color: white;
        text-align: center;
        transition: transform 0.3s;
        border: none;
        cursor: pointer;
    }
    
    .lesson-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .lesson-number {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .lesson-title {
        font-size: 16px;
        margin-bottom: 5px;
    }
    
    .lesson-status {
        font-size: 12px;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Функция для создания анимации пробирки
def create_test_tube_animation(lesson_id):
    colors = ["#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57", "#ff9ff3", "#54a0ff", "#5f27cd"]
    color = colors[lesson_id % len(colors)]
    
    st.markdown(f"""
    <div class="test-tube-animation">
        <div class="molecule">⚛️</div>
        <div style="position: relative;">
            <div class="test-tube">
                <div class="liquid" style="height: {random.randint(30, 90)}%; background: {color};"></div>
            </div>
            <div class="test-tube-neck"></div>
        </div>
        <div class="molecule" style="animation-delay: 1s;">⚗️</div>
    </div>
    
    <script>
        // Создаем пузырьки
        function createBubbles() {{
            const container = document.querySelector('.test-tube-animation');
            for(let i = 0; i < 10; i++) {{
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                bubble.style.width = bubble.style.height = Math.random() * 15 + 5 + 'px';
                bubble.style.left = Math.random() * 70 + 5 + 'px';
                bubble.style.bottom = Math.random() * 50 + 'px';
                bubble.style.animationDelay = Math.random() * 2 + 's';
                bubble.style.animationDuration = Math.random() * 2 + 2 + 's';
                container.querySelector('.test-tube').appendChild(bubble);
            }}
        }}
        
        // Создаем молекулы
        function createMolecules() {{
            const container = document.querySelector('.test-tube-animation');
            const molecules = ['H₂O', 'CO₂', 'CH₄', 'C₂H₅OH', 'C₆H₆'];
            for(let i = 0; i < 3; i++) {{
                const mol = document.createElement('div');
                mol.className = 'molecule';
                mol.style.position = 'absolute';
                mol.style.left = Math.random() * 80 + 10 + '%';
                mol.style.top = Math.random() * 50 + 25 + '%';
                mol.style.fontSize = Math.random() * 20 + 16 + 'px';
                mol.style.opacity = 0.7;
                mol.textContent = molecules[{lesson_id - 1} % molecules.length];
                mol.style.animation = 'floatUp ' + (Math.random() * 3 + 3) + 's infinite ease-in-out';
                container.appendChild(mol);
            }}
        }}
        
        setTimeout(createBubbles, 100);
        setTimeout(createMolecules, 500);
    </script>
    """, unsafe_allow_html=True)

# Функция для отображения химических формул урока
def show_lesson_formulas(lesson_id):
    formulas = {
        1: ["CH₄", "C₂H₆", "C₃H₈", "C₄H₁₀", "CₙH₂ₙ₊₂"],
        2: ["C₂H₄", "C₃H₆", "C₄H₈", "CₙH₂ₙ", "CH₂=CH₂"],
        3: ["C₂H₂", "C₃H₄", "C₄H₆", "CₙH₂ₙ₋₂", "CH≡CH"],
        4: ["CH₃OH", "C₂H₅OH", "C₃H₇OH", "CH₂OH-CHOH-CH₂OH"],
        5: ["C₆H₅OH", "C₆H₄(OH)₂", "C₆H₃(OH)₃"],
        6: ["HCHO", "CH₃CHO", "C₂H₅CHO", "C₆H₅CHO"],
        7: ["CH₃COCH₃", "CH₃COC₂H₅", "C₆H₅COCH₃"],
        8: ["CH₄ → C₂H₄ → C₂H₂", "sp³ → sp² → sp"],
        9: ["HCOOH", "CH₃COOH", "C₆H₅COOH", "COOH-COOH"],
        10: ["CH₃COOCH₃", "CH₃COOC₂H₅", "HCOOCH₃"],
        11: ["CH₃NH₂", "(CH₃)₂NH", "(CH₃)₃N", "C₆H₅NH₂"],
        12: ["NH₂-CH₂-COOH", "NH₂-CH(CH₃)-COOH"],
        13: ["CH₃Cl", "C₂H₅Br", "C₆H₅Cl"],
        14: ["CH₃NO₂", "C₆H₅NO₂", "NO₂-CH₂-CH₃"],
        15: ["C₆H₅SO₃H", "CH₃SO₃H", "SO₃H"],
        16: ["R-CH₂OH → R-CHO", "R-CHO → R-COOH"],
        17: ["CH₂=CH₂ + H₂ → CH₃-CH₃", "HC≡CH + H₂O → CH₃CHO"],
        18: ["R-X + OH⁻ → R-OH", "C₆H₆ + HNO₃ → C₆H₅NO₂"],
        19: ["n CH₂=CH₂ → [-CH₂-CH₂-]ₙ", "n C₆H₅OH + n HCHO → Полимер"]
    }
    
    if lesson_id in formulas:
        st.markdown("<div class='formula-container'>", unsafe_allow_html=True)
        st.markdown("### 🧪 Сабақтың негізгі формулалары")
        
        cols = st.columns(min(len(formulas[lesson_id]), 5))
        for idx, formula in enumerate(formulas[lesson_id]):
            with cols[idx % len(cols)]:
                st.markdown(f"<div class='formula'>{formula}</div>", unsafe_allow_html=True)
        
        # Показываем пример реакции
        if lesson_id in [1, 2, 3, 4, 6, 7, 9]:
            st.markdown("<div class='reaction'>", unsafe_allow_html=True)
            if lesson_id == 1:
                st.markdown("<div class='formula'>CH₄ + 2O₂</div>", unsafe_allow_html=True)
                st.markdown("<div class='reaction-arrow'>→</div>", unsafe_allow_html=True)
                st.markdown("<div class='formula'>CO₂ + 2H₂O</div>", unsafe_allow_html=True)
            elif lesson_id == 2:
                st.markdown("<div class='formula'>CH₂=CH₂ + Br₂</div>", unsafe_allow_html=True)
                st.markdown("<div class='reaction-arrow'>→</div>", unsafe_allow_html=True)
                st.markdown("<div class='formula'>Br-CH₂-CH₂-Br</div>", unsafe_allow_html=True)
            elif lesson_id == 3:
                st.markdown("<div class='formula'>HC≡CH + 2H₂</div>", unsafe_allow_html=True)
                st.markdown("<div class='reaction-arrow'>→</div>", unsafe_allow_html=True)
                st.markdown("<div class='formula'>CH₃-CH₃</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# 19 уроков
lessons = [
    {"id": 1, "title": "Алкандар", "topic": "Қаныққан көмірсутектер", "icon": "⚗️"},
    {"id": 2, "title": "Алкендер", "topic": "Қос байланыстар", "icon": "🔗"},
    {"id": 3, "title": "Алкиндер", "topic": "Үш байланыстар", "icon": "⚡"},
    {"id": 4, "title": "Спирттер", "topic": "Гидроксил тобы", "icon": "🍷"},
    {"id": 5, "title": "Фенолдар", "topic": "Ароматтық спирттер", "icon": "🌹"},
    {"id": 6, "title": "Альдегидтер", "topic": "Карбонил тобы", "icon": "🎯"},
    {"id": 7, "title": "Кетондар", "topic": "Кето тобы", "icon": "🌀"},
    {"id": 8, "title": "Көмірсутектер салыстыру", "topic": "Алкан, Алкен, Алкин", "icon": "📊"},
    {"id": 9, "title": "Карбон қышқылдары", "topic": "Карбоксил тобы", "icon": "🧪"},
    {"id": 10, "title": "Эфирлер", "topic": "Сложный эфирлер", "icon": "⚖️"},
    {"id": 11, "title": "Аминдар", "topic": "Амино тобы", "icon": "🔬"},
    {"id": 12, "title": "Аминқышқылдар", "topic": "Аминқышқылдар", "icon": "🧬"},
    {"id": 13, "title": "Галогентуындылар", "topic": "Галогентуындылар", "icon": "☢️"},
    {"id": 14, "title": "Нитросоединениялар", "topic": "Нитро тобы", "icon": "💥"},
    {"id": 15, "title": "Сульфокислоталар", "topic": "Сульфо тобы", "icon": "🌪️"},
    {"id": 16, "title": "Тотығу реакциялары", "topic": "Тотығу", "icon": "🔥"},
    {"id": 17, "title": "Қосылу реакциялары", "topic": "Қосылу", "icon": "➕"},
    {"id": 18, "title": "Ауыстыру реакциялары", "topic": "Ауыстыру", "icon": "🔄"},
    {"id": 19, "title": "Полимерлеу", "topic": "Полимерлер", "icon": "🧵"},
]

# Инициализация состояния
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = None
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "test_completed" not in st.session_state:
    st.session_state.test_completed = {}
if "animation_state" not in st.session_state:
    st.session_state.animation_state = {}

# Главное меню с анимацией
st.write("### 📚 19 сабақты таңдаңыз:")

# Анимация на главной странице
if not st.session_state.current_lesson:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="test-tube-animation" style="height: 250px;">
            <div class="molecule" style="animation: floatUp 3s infinite ease-in-out;">CH₄</div>
            <div style="position: relative;">
                <div class="test-tube">
                    <div class="liquid" style="height: 70%; background: linear-gradient(to top, #4ecdc4, #44a08d);"></div>
                </div>
                <div class="test-tube-neck"></div>
            </div>
            <div class="molecule" style="animation: floatUp 4s infinite ease-in-out; animation-delay: 1s;">C₂H₆</div>
        </div>
        """, unsafe_allow_html=True)

# 3 колонки для уроков
cols = st.columns(3)
for idx, lesson in enumerate(lessons):
    with cols[idx % 3]:
        lesson_id = lesson["id"]
        if lesson_id in st.session_state.test_completed:
            score = st.session_state.test_completed[lesson_id]
            status_color = "🟢" if score >= 8 else "🟡" if score >= 6 else "🔴"
            status = f"{status_color} {score}/10"
            button_text = f"{lesson['icon']} **{lesson_id}. {lesson['title']}**\n{status}"
        else:
            button_text = f"{lesson['icon']} **{lesson_id}. {lesson['title']}**\n📝 Тест берілмеген"
        
        if st.button(button_text, key=f"btn_{lesson_id}", use_container_width=True):
            st.session_state.current_lesson = lesson_id
            # Инициализируем состояние анимации для урока
            if lesson_id not in st.session_state.animation_state:
                st.session_state.animation_state[lesson_id] = {
                    "liquid_level": random.randint(30, 90),
                    "color": f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}",
                    "bubbles": random.randint(5, 15)
                }
            st.rerun()

# Если урок выбран
if st.session_state.current_lesson:
    lesson_id = st.session_state.current_lesson
    lesson = lessons[lesson_id-1]
    
    st.markdown("---")
    
    # Создаем две колонки: слева анимация, справа информация
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Анимация пробирки для урока
        create_test_tube_animation(lesson_id)
        
        # Кнопки для взаимодействия с анимацией
        st.write("### 🎮 Анимацияны басқару")
        
        if st.button("🧪 Құйып көру", key="pour"):
            if lesson_id in st.session_state.animation_state:
                st.session_state.animation_state[lesson_id]["liquid_level"] = min(
                    95, st.session_state.animation_state[lesson_id]["liquid_level"] + 20
                )
            st.rerun()
        
        if st.button("💨 Көбік түсіру", key="bubbles"):
            if lesson_id in st.session_state.animation_state:
                st.session_state.animation_state[lesson_id]["bubbles"] += 5
            st.rerun()
        
        if st.button("🎨 Түсін өзгерту", key="color"):
            if lesson_id in st.session_state.animation_state:
                colors = ["#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57", "#ff9ff3", "#54a0ff", "#5f27cd"]
                st.session_state.animation_state[lesson_id]["color"] = random.choice(colors)
            st.rerun()
    
    with col2:
        st.write(f"## {lesson['icon']} Сабақ {lesson_id}: {lesson['title']}")
        st.write(f"**Тақырып:** {lesson['topic']}")
        
        # Химические формулы урока
        show_lesson_formulas(lesson_id)
        
        # Тест
        st.write("### ✅ Тест (10 сұрақ)")

# ОСТАВЛЯЮ ВАШИ ВОПРОСЫ БЕЗ ИЗМЕНЕНИЙ (они остаются в коде как были)
# Здесь должен остаться весь ваш словарь all_questions из предыдущего кода
# Для экономии места я покажу только структуру:

# ВОПРОСЫ ДЛЯ ВСЕХ 19 УРОКОВ (ваш оригинальный код остается здесь)
all_questions = {
    1: [
        {"question": "1. Алкандардың жалпы формуласы:", 
         "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], 
         "correct": 1},
        # ... остальные 9 вопросов для урока 1
    ],
    2: [
        # ... вопросы для урока 2
    ],
    # ... и так до 19
}

# Продолжение кода для отображения теста (остается без изменений)
if st.session_state.current_lesson:
    lesson_id = st.session_state.current_lesson
    
    if lesson_id in all_questions:
        questions = all_questions[lesson_id]
        
        # Проверяем, завершен ли тест
        if lesson_id in st.session_state.test_completed:
            score = st.session_state.test_completed[lesson_id]
            
            # Анимация для завершенного теста
            st.balloons()
            st.success(f"### 🎉 Тест аяқталды! Нәтиже: {score}/10")
            
            # Показываем правильные ответы
            for i, q in enumerate(questions):
                with st.expander(f"Сұрақ {i+1}: {q['question']}"):
                    correct_answer = q['options'][q['correct']]
                    st.info(f"**Дұрыс жауап:** {correct_answer}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Тестті қайта тапсыру", use_container_width=True):
                    st.session_state.test_completed.pop(lesson_id, None)
                    st.session_state.answers.pop(lesson_id, None)
                    st.rerun()
            with col2:
                if st.button("📊 Келесі тестке өту", use_container_width=True):
                    next_lesson = lesson_id + 1 if lesson_id < 19 else 1
                    st.session_state.current_lesson = next_lesson
                    st.rerun()
        else:
            # Тестирование
            user_answers = st.session_state.answers.get(lesson_id, {})
            score = 0
            
            for i, q in enumerate(questions):
                st.write(f"**{i+1}. {q['question']}**")
                
                # Если уже отвечали
                if i in user_answers:
                    user_answer_index = user_answers[i]
                    user_answer = q['options'][user_answer_index]
                    is_correct = (user_answer_index == q['correct'])
                    
                    if is_correct:
                        st.success(f"✓ Сіздің жауабыңыз: {user_answer}")
                        score += 1
                    else:
                        st.error(f"✗ Сіздің жауабыңыз: {user_answer}")
                        correct_answer = q['options'][q['correct']]
                        st.info(f"✓ Дұрыс жауап: {correct_answer}")
                else:
                    # Выбор ответа
                    user_choice = st.radio(
                        f"Жауап {i+1}",
                        q["options"],
                        key=f"radio_{lesson_id}_{i}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    
                    if user_choice:
                        selected_index = q["options"].index(user_choice)
                        if lesson_id not in st.session_state.answers:
                            st.session_state.answers[lesson_id] = {}
                        st.session_state.answers[lesson_id][i] = selected_index
                        st.rerun()
                
                st.write("---")
            
            # Кнопка завершения теста
            if len(user_answers) == len(questions):
                percentage = (score / len(questions)) * 100
                
                # Показываем предварительный результат
                st.write(f"### 📈 Алдын ала нәтиже: {score}/{len(questions)} ({percentage:.1f}%)")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Тестті аяқтау", type="primary", use_container_width=True):
                        st.session_state.test_completed[lesson_id] = score
                        st.balloons()
                        st.rerun()
                
                with col2:
                    if st.button("🔄 Жауаптарды өзгерту", type="secondary", use_container_width=True):
                        st.session_state.answers[lesson_id] = {}
                        st.rerun()

# Кнопка назад
if st.session_state.current_lesson and st.button("← Басты бетке қайту", use_container_width=True):
    st.session_state.current_lesson = None
    st.rerun()

# Общая статистика
st.markdown("---")
st.write("### 📊 Жалпы статистика")

completed_count = len(st.session_state.test_completed)
if completed_count > 0:
    total_score = sum(st.session_state.test_completed.values())
    max_score = completed_count * 10
    overall_percentage = (total_score / max_score) * 100
    
    # Прогресс бар
    st.progress(overall_percentage / 100)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("✅ Өтілген сабақтар", f"{completed_count}/19")
    with col2:
        st.metric("📊 Орташа балл", f"{total_score/completed_count:.1f}/10")
    with col3:
        st.metric("🌟 Жалпы ұпай", f"{total_score}/{max_score}")
    
    # Достижения
    if completed_count == 19:
        st.success("🏆 Тамаша! Сіз барлық сабақтарды өттіңіз!")
    elif completed_count >= 10:
        st.info(f"📚 Жақсы жұмыс! Сіз {completed_count} сабақты өттіңіз")
else:
    st.info("📝 Сіз әлі ешқандай тест тапсырған жоқсыз")

# Футер с формулами
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
    <h3>🧬 Органикалық химияның негізгі формулалары</h3>
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 15px;">
        <div class="formula">CH₄ - Метан</div>
        <div class="formula">C₂H₄ - Этилен</div>
        <div class="formula">C₂H₂ - Ацетилен</div>
        <div class="formula">C₂H₅OH - Этанол</div>
        <div class="formula">CH₃COOH - Сірке қышқылы</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("*Барлығы: 19 сабақ × 10 сұрақ = 190 сұрақ*")
