import streamlit as st
import base64
from PIL import Image
import io

# Настройка страницы
st.set_page_config(page_title="Химия 10", layout="wide")

# Создаем изображения пробирок в base64
def create_test_tube_base64(color="#4ecdc4"):
    # Создаем простое изображение пробирки с помощью PIL
    img = Image.new('RGBA', (100, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Рисуем пробирку
    draw.rectangle([30, 50, 70, 180], fill=(200, 230, 255, 200), outline=(0, 102, 204, 255), width=3)
    draw.rectangle([40, 30, 60, 50], fill=(200, 230, 255, 200), outline=(0, 102, 204, 255), width=3)
    
    # Рисуем жидкость
    r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    draw.rectangle([31, 100, 69, 179], fill=(r, g, b, 180))
    
    # Сохраняем в base64
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Но лучше используем SVG для анимации
test_tube_svg = """
<svg width="100" height="200" viewBox="0 0 100 200">
    <!-- Пробирка -->
    <rect x="30" y="50" width="40" height="130" rx="5" fill="rgba(230,247,255,0.9)" stroke="#0066cc" stroke-width="2"/>
    <rect x="40" y="30" width="20" height="20" rx="5" fill="rgba(230,247,255,0.9)" stroke="#0066cc" stroke-width="2" stroke-bottom="none"/>
    
    <!-- Жидкость -->
    <rect id="liquid" x="31" y="100" width="38" height="80" rx="4" fill="{color}" opacity="0.8">
        <animate attributeName="height" values="80;90;80" dur="2s" repeatCount="indefinite"/>
    </rect>
    
    <!-- Пузырьки -->
    <circle cx="50" cy="170" r="3" fill="rgba(255,255,255,0.7)">
        <animate attributeName="cy" from="170" to="100" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" from="1" to="0" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="55" cy="160" r="2" fill="rgba(255,255,255,0.7)">
        <animate attributeName="cy" from="160" to="90" dur="2.5s" repeatCount="indefinite" begin="0.5s"/>
        <animate attributeName="opacity" from="1" to="0" dur="2.5s" repeatCount="indefinite" begin="0.5s"/>
    </circle>
</svg>
"""

# HTML с реальной анимацией пробирок
st.markdown("""
<style>
    .lab-animation {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 400px;
        background: linear-gradient(180deg, #2c3e50 0%, #1a1a2e 100%);
        border-radius: 20px;
        position: relative;
        overflow: hidden;
        margin: 30px 0;
    }
    
    .lab-table {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 80px;
        background: linear-gradient(to top, #3e2723, #5d4037);
        border-top: 10px solid #4e342e;
    }
    
    .tube-rack {
        position: absolute;
        bottom: 80px;
        width: 500px;
        height: 40px;
        background: #8d6e63;
        border-radius: 10px 10px 0 0;
        display: flex;
        justify-content: space-around;
        padding-top: 10px;
    }
    
    .tube-hole {
        width: 60px;
        height: 60px;
        background: #6d4c41;
        border-radius: 50%;
    }
    
    .tube-container {
        position: absolute;
        bottom: 140px;
        transition: all 1s ease;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.3));
    }
    
    .tube {
        width: 100px;
        height: 200px;
        position: relative;
        cursor: pointer;
        transition: transform 0.5s;
    }
    
    .tube:hover {
        transform: scale(1.05);
    }
    
    .tube-body {
        position: absolute;
        width: 40px;
        height: 130px;
        background: linear-gradient(90deg, rgba(255,255,255,0.8), rgba(255,255,255,0.6));
        border: 3px solid #1565c0;
        border-radius: 0 0 20px 20px;
        bottom: 0;
        left: 30px;
        overflow: hidden;
    }
    
    .tube-neck {
        position: absolute;
        width: 20px;
        height: 30px;
        background: linear-gradient(90deg, rgba(255,255,255,0.8), rgba(255,255,255,0.6));
        border: 3px solid #1565c0;
        border-bottom: none;
        border-radius: 10px 10px 0 0;
        bottom: 130px;
        left: 40px;
    }
    
    .tube-liquid {
        position: absolute;
        width: 100%;
        bottom: 0;
        border-radius: 0 0 17px 17px;
        transition: height 1s, background 0.5s;
    }
    
    .bubbles {
        position: absolute;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }
    
    .bubble {
        position: absolute;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 50%;
        animation: floatUp linear forwards;
    }
    
    @keyframes floatUp {
        to {
            transform: translateY(-100px);
            opacity: 0;
        }
    }
    
    .reaction-arrow {
        position: absolute;
        font-size: 60px;
        color: #ff9800;
        text-shadow: 0 0 20px #ff9800;
        z-index: 10;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }
    
    .chemical-formula {
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 32px;
        font-family: 'Courier New', monospace;
        color: #4fc3f7;
        background: rgba(0, 0, 0, 0.5);
        padding: 10px 20px;
        border-radius: 10px;
        z-index: 10;
        animation: glow 2s infinite;
    }
    
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #4fc3f7; }
        50% { text-shadow: 0 0 20px #4fc3f7; }
    }
    
    .control-panel {
        display: flex;
        gap: 10px;
        justify-content: center;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    
    .control-btn {
        padding: 12px 24px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s;
        min-width: 150px;
    }
    
    .control-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
</style>

<div class="lab-animation" id="labAnimation">
    <div class="lab-table"></div>
    <div class="tube-rack">
        <div class="tube-hole"></div>
        <div class="tube-hole"></div>
        <div class="tube-hole"></div>
    </div>
    
    <div class="chemical-formula" id="formulaDisplay">CH₄ + 2O₂ → CO₂ + 2H₂O</div>
    
    <!-- Левая пробирка -->
    <div class="tube-container" id="leftTube" style="left: 150px;">
        <div class="tube">
            <div class="tube-body">
                <div class="tube-liquid" id="leftLiquid" style="height: 80%; background: linear-gradient(to top, #4ecdc4, #26a69a);"></div>
            </div>
            <div class="tube-neck"></div>
        </div>
    </div>
    
    <!-- Стрелка реакции -->
    <div class="reaction-arrow" id="reactionArrow" style="left: 450px;">⚗️</div>
    
    <!-- Центральная пробирка -->
    <div class="tube-container" id="centerTube" style="left: 450px; opacity: 0;">
        <div class="tube">
            <div class="tube-body">
                <div class="tube-liquid" id="centerLiquid" style="height: 0%; background: linear-gradient(to top, #ff6b6b, #ee5a24);"></div>
            </div>
            <div class="tube-neck"></div>
        </div>
    </div>
    
    <!-- Правая пробирка -->
    <div class="tube-container" id="rightTube" style="left: 750px;">
        <div class="tube">
            <div class="tube-body">
                <div class="tube-liquid" id="rightLiquid" style="height: 80%; background: linear-gradient(to top, #45b7d1, #2e86de);"></div>
            </div>
            <div class="tube-neck"></div>
        </div>
    </div>
</div>

<script>
// Цвета для уроков
const lessonColors = {
    1: ['#4ecdc4', '#26a69a'],  // Алкандар
    2: ['#ff6b6b', '#ee5a24'],  // Алкендер
    3: ['#45b7d1', '#2e86de'],  // Алкиндер
    4: ['#96ceb4', '#66bb6a'],  // Спирттер
    5: ['#feca57', '#ffa502'],  // Фенолдар
    6: ['#ff9ff3', '#f368e0'],  // Альдегидтер
    7: ['#54a0ff', '#2e86de'],  // Кетондар
    8: ['#5f27cd', '#341f97'],  // Салыстыру
    9: ['#00d2d3', '#01a3a4'],  // Қышқылдар
    10: ['#ff9f43', '#ff7f00']  // Эфирлер
};

// Формулы для уроков
const lessonFormulas = {
    1: ['CH₄ + 2O₂ → CO₂ + 2H₂О', '2C₂H₆ + 7O₂ → 4CO₂ + 6H₂О'],
    2: ['C₂H₄ + H₂ → C₂H₆', 'CH₂=CH₂ + Br₂ → Br-CH₂-CH₂-Br'],
    3: ['2C₂H₂ + 5O₂ → 4CO₂ + 2H₂О', 'HC≡CH + 2H₂ → CH₃-CH₃'],
    4: ['CH₃OH + Na → CH₃ONa + ½H₂', 'C₂H₅OH + 3O₂ → 2CO₂ + 3H₂О'],
    5: ['C₆H₅OH + NaOH → C₆H₅ONa + H₂О', 'C₆H₅OH + 3Br₂ → C₆H₂Br₃OH + 3HBr'],
    6: ['HCHO + Ag₂O → HCOOH + 2Ag', 'CH₃CHO + 2[Ag(NH₃)₂]OH → CH₃COONH₄ + 2Ag + 3NH₃ + H₂О'],
    7: ['CH₃COCH₃ + H₂ → CH₃CHOHCH₃', '2CH₃COCH₃ → (CH₃)₂C=CHCOCH₃ + H₂О'],
    8: ['Алкан → Алкен → Алкин', 'sp³ → sp² → sp'],
    9: ['HCOOH + NaOH → HCOONa + H₂О', 'CH₃COOH + C₂H₅OH → CH₃COOC₂H₅ + H₂О'],
    10: ['CH₃COOH + CH₃OH → CH₃COOCH₃ + H₂О', 'RCOOH + R\'OH → RCOOR\' + H₂О']
};

let currentLesson = 1;
let isAnimating = false;

// Создаем пузырьки
function createBubbles(container, count = 10) {
    for (let i = 0; i < count; i++) {
        setTimeout(() => {
            const bubble = document.createElement('div');
            bubble.className = 'bubble';
            bubble.style.width = bubble.style.height = (Math.random() * 8 + 4) + 'px';
            bubble.style.left = Math.random() * 30 + 5 + 'px';
            bubble.style.bottom = '0';
            bubble.style.animationDuration = (Math.random() * 2 + 1) + 's';
            
            container.querySelector('.tube-body').appendChild(bubble);
            
            setTimeout(() => bubble.remove(), 3000);
        }, i * 100);
    }
}

// Запускаем реакцию
function startReaction() {
    if (isAnimating) return;
    isAnimating = true;
    
    const leftTube = document.getElementById('leftTube');
    const centerTube = document.getElementById('centerTube');
    const rightTube = document.getElementById('rightTube');
    const reactionArrow = document.getElementById('reactionArrow');
    const formulaDisplay = document.getElementById('formulaDisplay');
    
    const leftLiquid = document.getElementById('leftLiquid');
    const centerLiquid = document.getElementById('centerLiquid');
    const rightLiquid = document.getElementById('rightLiquid');
    
    // Обновляем формулу
    const formulas = lessonFormulas[currentLesson] || ['Химиялық реакция'];
    formulaDisplay.textContent = formulas[Math.floor(Math.random() * formulas.length)];
    
    // 1. Поднимаем пробирки
    leftTube.style.bottom = '240px';
    leftTube.style.transform = 'rotate(-30deg)';
    
    rightTube.style.bottom = '240px';
    rightTube.style.transform = 'rotate(30deg)';
    
    // 2. Наклоняем к центру и переливаем
    setTimeout(() => {
        leftTube.style.left = '350px';
        leftTube.style.transform = 'rotate(-60deg)';
        
        rightTube.style.left = '550px';
        rightTube.style.transform = 'rotate(60deg)';
        
        // Уменьшаем жидкость в боковых пробирках
        leftLiquid.style.height = '20%';
        rightLiquid.style.height = '20%';
        
        // Показываем центральную пробирку
        centerTube.style.opacity = '1';
        centerLiquid.style.height = '100%';
        
        // Создаем пузырьки в центральной пробирке
        createBubbles(centerTube, 20);
        
        // Анимируем стрелку
        reactionArrow.style.animation = 'pulse 0.3s infinite';
    }, 1000);
    
    // 3. Возвращаем на место
    setTimeout(() => {
        leftTube.style.bottom = '140px';
        leftTube.style.left = '150px';
        leftTube.style.transform = 'rotate(0deg)';
        
        rightTube.style.bottom = '140px';
        rightTube.style.left = '750px';
        rightTube.style.transform = 'rotate(0deg)';
        
        // Восстанавливаем жидкость
        setTimeout(() => {
            leftLiquid.style.height = '80%';
            rightLiquid.style.height = '80%';
            centerLiquid.style.height = '80%';
            
            // Меняем цвет центральной пробирки
            const colors = lessonColors[currentLesson] || ['#4ecdc4', '#26a69a'];
            centerLiquid.style.background = `linear-gradient(to top, ${colors[0]}, ${colors[1]})`;
            
            // Больше пузырьков
            createBubbles(centerTube, 15);
            
            // Сбрасываем анимацию стрелки
            reactionArrow.style.animation = '';
            
            isAnimating = false;
        }, 500);
    }, 2000);
}

// Меняем урок
function changeLesson(lessonId) {
    currentLesson = lessonId;
    const colors = lessonColors[lessonId] || ['#4ecdc4', '#26a69a'];
    
    // Меняем цвета всех пробирок
    document.getElementById('leftLiquid').style.background = 
        `linear-gradient(to top, ${colors[0]}, ${colors[1]})`;
    document.getElementById('rightLiquid').style.background = 
        `linear-gradient(to top, ${colors[0]}, ${colors[1]})`;
    
    // Обновляем формулу
    const formulas = lessonFormulas[lessonId] || ['Химиялық реакция'];
    document.getElementById('formulaDisplay').textContent = formulas[0];
    
    // Запускаем реакцию
    startReaction();
}

// Автоматическая анимация
setInterval(() => {
    if (!isAnimating) {
        startReaction();
    }
}, 8000);

// Инициализация
document.addEventListener('DOMContentLoaded', function() {
    // Создаем начальные пузырьки
    createBubbles(document.getElementById('leftTube'), 5);
    createBubbles(document.getElementById('rightTube'), 5);
    
    // Автозапуск через 2 секунды
    setTimeout(startReaction, 2000);
});
</script>
""", unsafe_allow_html=True)

# Заголовок
st.title("🧪 Органикалық химия - 10 сынып")
st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# Панель управления анимацией
st.markdown("### 🎮 Анимацияны басқару")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⚗️ Реакцияны бастау", use_container_width=True, key="start_reaction"):
        st.markdown("<script>startReaction();</script>", unsafe_allow_html=True)
        st.rerun()
with col2:
    if st.button("🔄 Пузырьки түсіру", use_container_width=True, key="add_bubbles"):
        st.markdown("""
        <script>
            createBubbles(document.getElementById('centerTube'), 20);
            createBubbles(document.getElementById('leftTube'), 10);
            createBubbles(document.getElementById('rightTube'), 10);
        </script>
        """, unsafe_allow_html=True)
        st.rerun()
with col3:
    lesson_num = st.selectbox("Сабақты таңдау", list(range(1, 11)), format_func=lambda x: f"Сабақ {x}")
    if st.button("🎨 Түстерді өзгерту", use_container_width=True, key="change_colors"):
        st.markdown(f"<script>changeLesson({lesson_num});</script>", unsafe_allow_html=True)
        st.rerun()

# 19 уроков (упрощенный список)
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
]

# Отображаем уроки
st.markdown("### 📚 Сабақтар тізімі")

cols = st.columns(5)
for idx, lesson in enumerate(lessons[:10]):
    with cols[idx % 5]:
        if st.button(
            f"{lesson['icon']}\n**{lesson['id']}. {lesson['title']}**",
            key=f"lesson_{lesson['id']}",
            use_container_width=True
        ):
            st.markdown(f"<script>changeLesson({lesson['id']});</script>", unsafe_allow_html=True)
            st.session_state.current_lesson = lesson['id']
            st.rerun()

# Показываем выбранный урок
if "current_lesson" in st.session_state:
    lesson_id = st.session_state.current_lesson
    lesson = lessons[lesson_id - 1] if lesson_id <= 10 else {"title": "Сабақ", "topic": "Тақырып"}
    st.markdown(f"## {lesson['icon']} Сабақ {lesson_id}: {lesson['title']}")
    st.markdown(f"**Тақырып:** {lesson['topic']}")

# Футер с информацией
st.markdown("---")
st.markdown("""
<div style="text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 25px; border-radius: 15px; color: white; margin-top: 30px;">
    <h3>🧬 Химиялық формулалар</h3>
    <div style="display: flex; justify-content: center; gap: 25px; flex-wrap: wrap; margin: 20px 0;">
        <div style="background: rgba(255,255,255,0.15); padding: 15px 25px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: 'Courier New', monospace; font-weight: bold;">CH₄</div>
            <div style="font-size: 14px; opacity: 0.9;">Метан</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 15px 25px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: 'Courier New', monospace; font-weight: bold;">C₂H₄</div>
            <div style="font-size: 14px; opacity: 0.9;">Этилен</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 15px 25px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: 'Courier New', monospace; font-weight: bold;">C₂H₅OH</div>
            <div style="font-size: 14px; opacity: 0.9;">Этанол</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 15px 25px; border-radius: 10px;">
            <div style="font-size: 28px; font-family: 'Courier New', monospace; font-weight: bold;">CH₃COOH</div>
            <div style="font-size: 14px; opacity: 0.9;">Сірке қышқылы</div>
        </div>
    </div>
    <p style="margin-top: 15px; opacity: 0.8; font-size: 14px;">
        Интерактивті химиялық анимация | Пробиркалар араласады | Нақты формулалар
    </p>
</div>
""", unsafe_allow_html=True)

# Дополнительная информация
with st.expander("ℹ️ Анимация туралы ақпарат"):
    st.write("""
    **Бұл анимацияда:**
    1. **3 пробирка** лабораториялық столда
    2. **Пробиркалар қозғалады** және араласады
    3. **Сұйықтықтар араласады** орталық пробиркаға
    4. **Көпіршіктер пайда болады** реакция кезінде
    5. **Химиялық формулалар** өзгереді
    6. **Әр сабақтың өзіндік түсі** бар
    
    **Басқару:**
    - **Реакцияны бастау** - пробиркаларды араластыру
    - **Пузырьки түсіру** - көпіршіктер қосу
    - **Түстерді өзгерту** - әр сабақтың түсіне ауысу
    
    Анимация әр 8 секунд сайын автоматты түрде қайталанады.
    """)

# Добавляем PIL для ImageDraw
try:
    from PIL import ImageDraw
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import ImageDraw
