def interactive_tubes(reaction_text, color):
    html_code = f"""
    <html>
    <head>
    <style>
    .container {{
        text-align: center;
        width: 100%;
    }}

    .tubes {{
        display: flex;
        justify-content: center;
        gap: 80px;
        margin-bottom: 20px;
        align-items: flex-end;
    }}

    .tube {{
        width: 55px;
        height: 180px;
        border: 3px solid #222;
        border-radius: 0 0 22px 22px;
        background: linear-gradient(to top, #b3e5fc 0%, #e3f2fd 70%);
        position: relative;
        overflow: hidden;
        box-shadow: inset 0px 0px 8px rgba(0,0,0,0.2);
        transition: transform 1s;
    }}

    .center {{
        background: linear-gradient(to top, #ffcc80 0%, #fff3e0 70%);
        transition: background 1.5s;
    }}

    /* Молекулалар (кішкентай шарлар) */
    .molecule {{
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: rgba(0, 0, 0, 0.6);
        animation: float 2.5s infinite ease-in-out;
    }}

    .m1 {{ left: 15px; top: 90px; animation-delay: 0s; }}
    .m2 {{ left: 30px; top: 60px; animation-delay: 0.5s; }}
    .m3 {{ left: 20px; top: 120px; animation-delay: 1s; }}
    .m4 {{ left: 25px; top: 40px; animation-delay: 1.5s; }}

    @keyframes float {{
        0% {{ transform: translateY(0); opacity: 0.6; }}
        50% {{ transform: translateY(-12px); opacity: 1; }}
        100% {{ transform: translateY(0); opacity: 0.6; }}
    }}

    .pour-left {{ transform: rotate(22deg) translateX(12px); }}
    .pour-right {{ transform: rotate(-22deg) translateX(-12px); }}

    .buttons {{
        margin-top: 10px;
    }}

    button {{
        padding: 10px 16px;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        background: #1976d2;
        color: white;
        cursor: pointer;
        margin: 5px;
    }}

    button:hover {{ background: #0d47a1; }}

    .result {{
        padding: 15px;
        border-radius: 12px;
        background: {color};
        font-size: 20px;
        font-weight: bold;
        margin-top: 15px;
        display: none;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }}
    </style>
    </head>

    <body>
    <div class="container">

        <h3>🧪 Виртуалды реакция моделі</h3>

        <div class="tubes">
            <div id="left" class="tube">
                <div class="molecule m1"></div>
                <div class="molecule m2"></div>
            </div>

            <div id="center" class="tube center">
                <div class="molecule m3"></div>
                <div class="molecule m4"></div>
            </div>

            <div id="right" class="tube">
                <div class="molecule m1"></div>
                <div class="molecule m2"></div>
            </div>
        </div>

        <div class="buttons">
            <button onclick="pour()">▶️ Құюды бастау</button>
            <button onclick="showResult()">🔬 Реакцияны көрсету</button>
        </div>

        <div id="res" class="result">{reaction_text}</div>

    </div>

    <script>
    function pour() {{
        document.getElementById("left").classList.toggle("pour-left");
        document.getElementById("right").classList.toggle("pour-right");
    }}

    function showResult() {{
        document.getElementById("center").style.background =
            "linear-gradient(to top, {color} 0%, #ffffff 70%)";

        document.getElementById("res").style.display = "block";
    }}
    </script>
    </body>
    </html>
    """
    components.html(html_code, height=420)
