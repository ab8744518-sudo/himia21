import streamlit as st
import random

# Настройка страницы
st.set_page_config(page_title="Химия 10", layout="wide")

# CSS для полной анимации
st.markdown("""
<style>
    /* Контейнер для анимации */
    .lab-animation {
        width: 100%;
        height: 300px;
        position: relative;
        margin: 30px 0;
        overflow: hidden;
        background: linear-gradient(180deg, #1a237e 0%, #283593 50%, #3949ab 100%);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Лабораторный стол */
    .lab-table {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 80px;
        background: linear-gradient(to top, #5d4037, #795548);
        border-top: 5px solid #4e342e;
    }
    
    /* Стойка для пробирок */
    .test-tube-rack {
        position: absolute;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        width: 400px;
        height: 50px;
        background: #8d6e63;
        border-radius: 10px 10px 0 0;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 0 20px;
    }
    
    /* Отверстия в стойке */
    .rack-hole {
        width: 70px;
        height: 70px;
        background: #6d4c41;
        border-radius: 50%;
        position: relative;
        z-index: 1;
    }
    
    /* Пробирка */
    .test-tube {
        width: 50px;
        height: 150px;
        position: absolute;
        bottom: 130px;
        transition: all 1s cubic-bezier(0.4, 0, 0.2, 1);
        z-index: 2;
        cursor: pointer;
    }
    
    .tube-body {
        width: 100%;
        height: 120px;
        background: linear-gradient(to right, rgba(255,255,255,0.9), rgba(255,255,255,0.7));
        border-radius: 10px 10px 25px 25px;
        border: 3px solid #1565c0;
        position: relative;
        overflow: hidden;
    }
    
    .tube-neck {
        width: 30px;
        height: 30px;
        background: linear-gradient(to right, rgba(255,255,255,0.9), rgba(255,255,255,0.7));
        position: absolute;
        top: -30px;
        left: 10px;
        border: 3px solid #1565c0;
        border-bottom: none;
        border-radius: 15px 15px 0 0;
    }
    
    /* Жидкость в пробирке */
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        border-radius: 0 0 22px 22px;
        transition: height 1s ease, background 0.5s ease;
    }
    
    /* Бурлящая жидкость */
    .bubbling-liquid {
        animation: bubble 2s infinite;
    }
    
    @keyframes bubble {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    /* Пузырьки */
    .bubble {
        position: absolute;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        animation: floatUp linear infinite;
    }
    
    @keyframes floatUp {
        to { transform: translateY(-150px); opacity: 0; }
    }
    
    /* Стрелка реакции */
    .reaction-arrow {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        font-size: 60px;
        color: #ff9800;
        text-shadow: 0 0 20px #ff9800;
        animation: pulse 1.5s infinite;
        z-index: 3;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 0.5; transform: translate(-50%, -50%) scale(1.2); }
    }
    
    /* Анимированная реакция */
    .reaction-flash {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(255,152,0,0.8) 0%, rgba(255,152,0,0) 70%);
        border-radius: 50%;
        animation: flash 0.5s;
        z-index: 1;
    }
    
    @keyframes flash {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
        100% { transform: translate(-50%, -50%) scale(2); opacity: 0; }
    }
    
    /* Дым/пар */
    .smoke {
        position: absolute;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        animation: smokeFloat 4s infinite;
    }
    
    @keyframes smokeFloat {
        0% { transform: translateY(0) scale(1); opacity: 0; }
        20% { opacity: 0.8; }
        100% { transform: translateY(-200px) scale(2); opacity: 0; }
    }
    
    /* Молекулы */
    .molecule {
        position: absolute;
        font-size: 20px;
        font-weight: bold;
        color: #e3f2fd;
        text-shadow: 0 0 10px #2196f3;
        animation: moleculeFloat 6s infinite linear;
    }
    
    @keyframes moleculeFloat {
        0% { transform: translateY(100px) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
    
    /* Кнопки управления */
    .control-panel {
        display: flex;
        gap: 10px;
        margin: 20px 0;
        justify-content: center;
    }
    
    .control-btn {
        padding: 12px 24px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .control-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    /* Информационная панель */
    .info-panel {
        background: rgba(30, 30, 60, 0.9);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        border-left: 5px solid #4ecdc4;
    }
    
    /* Карточки уроков */
    .lesson-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
        transition: all 0.3s;
        margin: 10px 0;
        border: none;
        cursor: pointer;
    }
    
    .lesson-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# JavaScript для интерактивной анимации
animation_js = """
<script>
// Цвета для разных уроков
const lessonColors = {
    1: '#4ecdc4', 2: '#ff6b6b', 3: '#45b7d1', 4: '#96ceb4', 5: '#feca57',
    6: '#ff9ff3', 7: '#54a0ff', 8: '#5f27cd', 9: '#00d2d3', 10: '#ff9f43',
    11: '#341f97', 12: '#01a3a4', 13: '#8395a7', 14: '#ee5a24', 15: '#a29bfe',
    16: '#fd79a8', 17: '#00cec9', 18: '#6c5ce7', 19: '#fdcb6e'
};

// Формулы для разных уроков
const lessonFormulas = {
    1: ['CH₄', 'C₂H₆', 'C₃H₈'],
    2: ['C₂H₄', 'C₃H₆'],
    3: ['C₂H₂', 'C₃H₄'],
    4: ['CH₃OH', 'C₂H₅OH'],
    5: ['C₆H₅OH'],
    6: ['HCHO', 'CH₃CHO'],
    7: ['CH₃COCH₃'],
    8: ['CH₄ → C₂H₄ → C₂H₂'],
    9: ['HCOOH', 'CH₃COOH'],
    10: ['CH₃COOCH₃'],
    11: ['CH₃NH₂'],
    12: ['NH₂-CH₂-COOH'],
    13: ['CH₃Cl'],
    14: ['CH₃NO₂'],
    15: ['C₆H₅SO₃H'],
    16: ['R-CH₂OH → R-CHO'],
    17: ['CH₂=CH₂ + H₂'],
    18: ['R-X → R-OH'],
    19: ['nCH₂=CH₂ → полимер']
};

let currentLesson = 1;
let animationActive = false;

// Создаем анимацию
function createLabAnimation() {
    const container = document.getElementById('labAnimation');
    if (!container) return;
    
    container.innerHTML = '';
    
    // Создаем лабораторный стол
    const table = document.createElement('div');
    table.className = 'lab-table';
    container.appendChild(table);
    
    // Создаем стойку для пробирок
    const rack = document.createElement('div');
    rack.className = 'test-tube-rack';
    
    // Создаем отверстия в стойке
    for (let i = 0; i < 3; i++) {
        const hole = document.createElement('div');
        hole.className = 'rack-hole';
        rack.appendChild(hole);
    }
    container.appendChild(rack);
    
    // Создаем левую пробирку
    createTestTube(container, 'leftTube', 100, '#4ecdc4');
    
    // Создаем центральную пробирку
    createTestTube(container, 'centerTube', 400, '#ff6b6b', 0.5);
    
    // Создаем правую пробирку
    createTestTube(container, 'rightTube', 700, '#45b7d1');
    
    // Создаем стрелку реакции
    const arrow = document.createElement('div');
    arrow.className = 'reaction-arrow';
    arrow.innerHTML = '⚗️';
    arrow.id = 'reactionArrow';
    container.appendChild(arrow);
    
    // Создаем информационную панель
    const infoPanel = document.createElement('div');
    infoPanel.className = 'info-panel';
    infoPanel.innerHTML = `
        <div style="text-align: center;">
            <h3 style="color: #4ecdc4; margin: 0;">🧪 Химиялық реакция</h3>
            <p style="color: white; margin: 10px 0;" id="reactionText">Пробиркаларды араластыру үшін түймені басыңыз</p>
            <div style="font-size: 24px; font-family: monospace; color: #ffeb3b;" id="formulaDisplay">CH₄</div>
        </div>
    `;
    container.appendChild(infoPanel);
    
    // Добавляем плавающие молекулы
    for (let i = 0; i < 5; i++) {
        createMolecule(container);
    }
}

// Создаем пробирку
function createTestTube(container, id, left, color, opacity = 1) {
    const tube = document.createElement('div');
    tube.id = id;
    tube.className = 'test-tube';
    tube.style.left = left + 'px';
    tube.style.opacity = opacity;
    
    const tubeBody = document.createElement('div');
    tubeBody.className = 'tube-body';
    
    const liquid = document.createElement('div');
    liquid.className = 'liquid bubbling-liquid';
    liquid.id = id + 'Liquid';
    liquid.style.height = '80%';
    liquid.style.background = `linear-gradient(to top, ${color}80, ${color})`;
    
    const tubeNeck = document.createElement('div');
    tubeNeck.className = 'tube-neck';
    
    tubeBody.appendChild(liquid);
    tube.appendChild(tubeBody);
    tube.appendChild(tubeNeck);
    container.appendChild(tube);
    
    // Добавляем пузырьки
    addBubbles(liquid);
    
    return tube;
}

// Добавляем пузырьки
function addBubbles(container) {
    for (let i = 0; i < 8; i++) {
        setTimeout(() => {
            const bubble = document.createElement('div');
            bubble.className = 'bubble';
            bubble.style.width = bubble.style.height = (Math.random() * 8 + 4) + 'px';
            bubble.style.left = Math.random() * 40 + 5 + 'px';
            bubble.style.bottom = '0';
            bubble.style.animationDuration = (Math.random() * 2 + 1) + 's';
            bubble.style.animationDelay = (Math.random() * 1) + 's';
            container.appendChild(bubble);
            
            // Удаляем пузырек после анимации
            setTimeout(() => bubble.remove(), 3000);
        }, i * 300);
    }
}

// Создаем молекулу
function createMolecule(container) {
    const molecule = document.createElement('div');
    molecule.className = 'molecule';
    molecule.innerHTML = ['CH₄', 'C₂H₆', 'C₃H₈', 'H₂O', 'CO₂', 'O₂'][Math.floor(Math.random() * 6)];
    molecule.style.left = Math.random() * 90 + 5 + '%';
    molecule.style.animationDuration = (Math.random() * 4 + 3) + 's';
    molecule.style.animationDelay = Math.random() * 2 + 's';
    container.appendChild(molecule);
}

// Запускаем реакцию
function startReaction() {
    if (animationActive) return;
    animationActive = true;
    
    const leftTube = document.getElementById('leftTube');
    const centerTube = document.getElementById('centerTube');
    const rightTube = document.getElementById('rightTube');
    const reactionArrow = document.getElementById('reactionArrow');
    const formulaDisplay = document.getElementById('formulaDisplay');
    const reactionText = document.getElementById('reactionText');
    
    // Меняем формулу
    const formulas = lessonFormulas[currentLesson] || ['CH₄'];
    formulaDisplay.textContent = formulas[Math.floor(Math.random() * formulas.length)];
    reactionText.textContent = 'Реакция жүруде...';
    reactionText.style.color = '#ff9800';
    
    // 1. Поднимаем боковые пробирки
    leftTube.style.bottom = '230px';
    leftTube.style.transform = 'rotate(-30deg)';
    
    rightTube.style.bottom = '230px';
    rightTube.style.transform = 'rotate(30deg)';
    
    // 2. Наклоняем к центру
    setTimeout(() => {
        leftTube.style.left = '250px';
        leftTube.style.transform = 'rotate(-60deg)';
        
        rightTube.style.left = '550px';
        rightTube.style.transform = 'rotate(60deg)';
        
        // Уменьшаем жидкость в боковых пробирках
        document.getElementById('leftTubeLiquid').style.height = '20%';
        document.getElementById('rightTubeLiquid').style.height = '20%';
        
        // Увеличиваем жидкость в центральной
        document.getElementById('centerTubeLiquid').style.height = '100%';
        
        // Анимация стрелки
        reactionArrow.style.animation = 'pulse 0.3s infinite';
        
        // Создаем вспышку
        createFlash();
    }, 1000);
    
    // 3. Возвращаем на место
    setTimeout(() => {
        leftTube.style.bottom = '130px';
        leftTube.style.left = '100px';
        leftTube.style.transform = 'rotate(0deg)';
        
        rightTube.style.bottom = '130px';
        rightTube.style.left = '700px';
        rightTube.style.transform = 'rotate(0deg)';
        
        // Восстанавливаем жидкость
        setTimeout(() => {
            document.getElementById('leftTubeLiquid').style.height = '80%';
            document.getElementById('rightTubeLiquid').style.height = '80%';
            document.getElementById('centerTubeLiquid').style.height = '80%';
            
            // Много пузырьков
            addBubbles(document.getElementById('centerTubeLiquid'));
            addBubbles(document.getElementById('centerTubeLiquid'));
            
            // Меняем цвет центральной пробирки
            const colors = ['#4ecdc4', '#ff6b6b', '#45b7d1', '#96ceb4', '#feca57'];
            const newColor = colors[Math.floor(Math.random() * colors.length)];
            document.getElementById('centerTubeLiquid').style.background = 
                `linear-gradient(to top, ${newColor}80, ${newColor})`;
            
            // Обновляем текст
            reactionText.textContent = 'Реакция аяқталды!';
            reactionText.style.color = '#4caf50';
            
            // Сбрасываем анимацию стрелки
            reactionArrow.style.animation = '';
            
            animationActive = false;
        }, 500);
    }, 2000);
}

// Создаем вспышку реакции
function createFlash() {
    const container = document.getElementById('labAnimation');
    const flash = document.createElement('div');
    flash.className = 'reaction-flash';
    container.appendChild(flash);
    
    setTimeout(() => flash.remove(), 500);
}

// Создаем дым
function createSmoke() {
    const container = document.getElementById('labAnimation');
    for (let i = 0; i < 10; i++) {
        setTimeout(() => {
            const smoke = document.createElement('div');
            smoke.className = 'smoke';
            smoke.style.width = smoke.style.height = (Math.random() * 30 + 20) + 'px';
            smoke.style.left = Math.random() * 80 + 10 + '%';
            smoke.style.bottom = '150px';
            smoke.style.animationDuration = (Math.random() * 2 + 2) + 's';
            container.appendChild(smoke);
            
            setTimeout(() => smoke.remove(), 4000);
        }, i * 200);
    }
}

// Инициализация
document.addEventListener('DOMContentLoaded', function() {
    createLabAnimation();
    
    // Обновляем каждые 10 секунд
    setInterval(() => {
        if (!animationActive) {
            startReaction();
            createSmoke();
        }
    }, 10000);
});

// Функция для смены урока
function changeLesson(lessonId) {
    currentLesson = lessonId;
    const color = lessonColors[lessonId] || '#4ecdc4';
    
    // Меняем цвет жидкостей
    const liquids = document.querySelectorAll('.liquid');
    liquids.forEach(liquid => {
        liquid.style.background = `linear-gradient(to top, ${color}80, ${color})`;
    });
    
    // Обновляем формулу
    const formulas = lessonFormulas[lessonId] || ['CH₄'];
    document.getElementById('formulaDisplay').textContent = formulas[0];
    
    // Запускаем реакцию
    startReaction();
}
</script>
"""

# Инициализация состояния
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = None

# Заголовок
st.title("🧪 Органикалық химия - 10 сынып")
st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# Главная анимация
st.markdown('<div id="labAnimation" class="lab-animation"></div>', unsafe_allow_html=True)

# Добавляем JavaScript
st.markdown(animation_js, unsafe_allow_html=True)

# Панель управления
st.markdown("### 🎮 Анимацияны басқару")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("⚗️ Реакцияны бастау", use_container_width=True):
        st.markdown("<script>startReaction(); createSmoke();</script>", unsafe_allow_html=True)
        st.rerun()
with col2:
    if st.button("💨 Дым түсіру", use_container_width=True):
        st.markdown("<script>createSmoke();</script>", unsafe_allow_html=True)
        st.rerun()
with col3:
    if st.button("🔄 Пробиркаларды қайта орнату", use_container_width=True):
        st.markdown("<script>createLabAnimation();</script>", unsafe_allow_html=True)
        st.rerun()
with col4:
    if st.button("🎨 Түстерді өзгерту", use_container_width=True):
        st.markdown("<script>changeLesson(Math.floor(Math.random() * 19) + 1);</script>", unsafe_allow_html=True)
        st.rerun()

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

# Меню уроков
st.markdown("### 📚 19 сабақты таңдаңыз:")

cols = st.columns(3)
for idx, lesson in enumerate(lessons):
    with cols[idx % 3]:
        if st.button(
            f"{lesson['icon']} **{lesson['id']}. {lesson['title']}**\n{lesson['topic']}",
            key=f"btn_{lesson['id']}",
            use_container_width=True
        ):
            st.session_state.current_lesson = lesson['id']
            st.markdown(f"<script>changeLesson({lesson['id']});</script>", unsafe_allow_html=True)
            st.rerun()

# Показываем выбранный урок
if st.session_state.current_lesson:
    lesson = lessons[st.session_state.current_lesson - 1]
    st.markdown(f"## {lesson['icon']} Сабақ {lesson['id']}: {lesson['title']}")
    st.markdown(f"**Тақырып:** {lesson['topic']}")
    
    # Здесь будет тест (ваш существующий код)

# Футер
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #1a237e 0%, #3949ab 100%); 
            border-radius: 15px; color: white; margin-top: 30px;">
    <h3>🧬 Органикалық химияның негізгі формулалары</h3>
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 15px;">
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: monospace;">CH₄</div>
            <div>Метан</div>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: monospace;">C₂H₄</div>
            <div>Этилен</div>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: monospace;">C₂H₂</div>
            <div>Ацетилен</div>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: monospace;">C₂H₅OH</div>
            <div>Этанол</div>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: monospace;">CH₃COOH</div>
            <div>Сірке қышқылы</div>
        </div>
    </div>
    <p style="margin-top: 20px; opacity: 0.9;">19 сабақ | 190 сұрақ | Интерактивті анимация</p>
</div>
""", unsafe_allow_html=True)
