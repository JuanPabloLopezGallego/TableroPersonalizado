import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Taller de dibujo",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════
# ESTILOS
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --bg: #f5f0e6;
        --paper: #ffffff;
        --ink: #14120e;
        --muted: #7a7468;
        --muted-2: #a8a196;
        --border: #e6dfd0;
        --accent: #ff5a36;
        --accent-soft: #fff0eb;
        --yellow: #ffd166;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif !important;
        color: var(--ink);
    }

    h1, h2, h3, h4, h5 {
        font-family: 'Instrument Serif', serif !important;
        font-weight: 600 !important;
        letter-spacing: -0.015em !important;
        color: var(--ink) !important;
    }

    /* ═══ FONDO CÁLIDO ═══ */
    .stApp {
        background-color: var(--bg) !important;
        background-image:
            radial-gradient(circle at 8% -5%, rgba(255, 90, 54, 0.08), transparent 40%),
            radial-gradient(circle at 92% 105%, rgba(255, 209, 102, 0.15), transparent 42%),
            repeating-linear-gradient(
                45deg,
                transparent 0 22px,
                rgba(20, 18, 14, 0.012) 22px 24px
            );
        background-attachment: fixed;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header[data-testid="stHeader"] { background: transparent; }

    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px !important;
    }

    /* ═══ SIDEBAR ═══ */
    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] * { color: var(--ink) !important; }
    [data-testid="stSidebar"] .block-container,
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem !important;
    }

    /* Marca superior del sidebar */
    .sb-brand {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding-bottom: 1.1rem;
        margin-bottom: 1.25rem;
        border-bottom: 1px solid var(--border);
    }
    .sb-brand-mark {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(135deg, #ff5a36, #ff8e53);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        box-shadow: 0 6px 16px rgba(255, 90, 54, 0.32);
        flex-shrink: 0;
    }
    .sb-brand-text .name {
        font-family: 'Instrument Serif', serif;
        font-weight: 700;
        font-size: 1.1rem;
        line-height: 1;
        color: var(--ink);
        letter-spacing: -0.01em;
    }
    .sb-brand-text .tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--muted);
        margin-top: 4px;
    }

    /* Secciones del sidebar */
    .sb-section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        font-weight: 600;
        color: var(--accent) !important;
        margin: 1.5rem 0 0.9rem 0;
        padding-bottom: 0.55rem;
        border-bottom: 1px dashed var(--border);
    }
    .sb-section:first-child { margin-top: 0; }
    .sb-section .num {
        background: var(--accent-soft);
        color: var(--accent);
        padding: 0.15rem 0.5rem;
        border-radius: 6px;
        font-size: 0.6rem;
        font-weight: 700;
    }

    /* Labels de widgets en sidebar */
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        font-size: 0.83rem !important;
        font-weight: 600 !important;
        color: #4c4740 !important;
        letter-spacing: 0.005em;
    }

    /* Sliders */
    [data-testid="stSidebar"] [data-baseweb="slider"] div[role="slider"] {
        background-color: var(--accent) !important;
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 4px rgba(255, 90, 54, 0.16) !important;
    }
    [data-testid="stSidebar"] [data-baseweb="slider"] > div > div > div {
        background: linear-gradient(90deg, var(--accent), #ff8e53) !important;
    }

    /* Selectbox */
    [data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background: #faf7f0 !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        color: var(--ink) !important;
        font-weight: 500 !important;
        transition: all 0.15s ease;
    }
    [data-testid="stSidebar"] div[data-baseweb="select"] > div:hover {
        border-color: var(--accent) !important;
    }
    [data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: var(--ink) !important;
    }

    /* Popovers (dropdowns abiertos) */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] [role="listbox"] {
        background-color: #ffffff !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        box-shadow: 0 12px 32px rgba(20, 18, 14, 0.14) !important;
    }
    div[data-baseweb="popover"] li,
    div[data-baseweb="popover"] [role="option"] {
        color: var(--ink) !important;
        font-weight: 500 !important;
    }
    div[data-baseweb="popover"] li:hover,
    div[data-baseweb="popover"] [aria-selected="true"] {
        background-color: var(--accent-soft) !important;
        color: var(--accent) !important;
    }

    /* ═══ HERO ═══ */
    .hero {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        gap: 2rem;
        padding-bottom: 1.5rem;
        margin-bottom: 1.75rem;
        border-bottom: 1px solid var(--border);
    }
    .hero-left { flex: 1; }
    .hero-kicker {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--accent);
        font-weight: 600;
        margin-bottom: 0.85rem;
    }
    .hero-kicker::before {
        content: '';
        display: inline-block;
        width: 22px;
        height: 2px;
        background: var(--accent);
    }
    .hero h1 {
        font-family: 'Instrument Serif', serif !important;
        font-size: 3rem !important;
        line-height: 1 !important;
        letter-spacing: -0.025em !important;
        font-weight: 600 !important;
        margin: 0 0 0.65rem 0 !important;
        color: var(--ink) !important;
    }
    .hero h1 em {
        font-style: italic;
        color: var(--accent);
        font-weight: 400;
    }
    .hero p {
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.55;
        margin: 0;
        max-width: 560px;
    }

    /* Chips de herramientas */
    .hero-chips {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        justify-content: flex-end;
    }
    .hero-chip {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 100px;
        padding: 0.45rem 0.85rem;
        font-size: 0.78rem;
        font-weight: 500;
        color: var(--ink);
        white-space: nowrap;
    }
    .hero-chip .dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--accent);
    }

    /* ═══ MARCO DEL LIENZO ═══ */
    .canvas-frame-label {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--muted);
        padding: 0 0.35rem 0.7rem 0.35rem;
    }
    .canvas-frame-label .size {
        color: var(--accent);
        font-weight: 600;
    }

    /* Container que envuelve el canvas */
    .st-key-canvas_wrap {
        background: #ffffff;
        border: 2px solid var(--ink);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 12px 12px 0 var(--accent);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }
    .st-key-canvas_wrap [data-testid="stCanvas"] {
        margin: 0 auto;
        border-radius: 12px;
        overflow: hidden;
    }
    .st-key-canvas_wrap canvas {
        border-radius: 12px !important;
        display: block;
    }

    /* ═══ TIPS AL PIE ═══ */
    .tips {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        margin-top: 2.5rem;
    }
    .tip {
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.1rem 1.2rem;
        transition: all 0.2s ease;
    }
    .tip:hover {
        border-color: var(--accent);
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(255, 90, 54, 0.10);
    }
    .tip-icon {
        font-size: 1.4rem;
        margin-bottom: 0.55rem;
        display: block;
    }
    .tip-title {
        font-family: 'Instrument Serif', serif;
        font-size: 1.05rem;
        font-weight: 600;
        margin: 0 0 0.3rem 0;
        color: var(--ink);
        letter-spacing: -0.01em;
    }
    .tip-text {
        font-size: 0.83rem;
        line-height: 1.5;
        color: var(--muted);
        margin: 0;
    }

    /* ═══ SCROLLBAR ═══ */
    ::-webkit-scrollbar { width: 10px; height: 10px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb {
        background: #d8cebc;
        border-radius: 10px;
        border: 2px solid var(--bg);
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent); }

    /* ═══ RESPONSIVE ═══ */
    @media (max-width: 900px) {
        .hero { flex-direction: column; align-items: flex-start; }
        .hero-chips { justify-content: flex-start; }
        .hero h1 { font-size: 2.2rem !important; }
        .tips { grid-template-columns: 1fr; }
        .st-key-canvas_wrap { padding: 1rem; box-shadow: 8px 8px 0 var(--accent); }
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
        <div class="sb-brand">
            <div class="sb-brand-mark">🎨</div>
            <div class="sb-brand-text">
                <div class="name">Taller de dibujo</div>
                <div class="tag">Studio · v1.0</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ─── Dimensiones ───
    st.markdown(
        '<div class="sb-section"><span class="num">01</span> Dimensiones del tablero</div>',
        unsafe_allow_html=True,
    )
    canvas_width = st.slider("Ancho", 300, 700, 500, 50)
    canvas_height = st.slider("Alto", 200, 600, 300, 50)

    # ─── Herramientas ───
    st.markdown(
        '<div class="sb-section"><span class="num">02</span> Herramientas de dibujo</div>',
        unsafe_allow_html=True,
    )
    drawing_mode = st.selectbox(
        "Herramienta",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    stroke_width = st.slider("Grosor de línea", 1, 30, 15)

    # ─── Colores ───
    st.markdown(
        '<div class="sb-section"><span class="num">03</span> Paleta de colores</div>',
        unsafe_allow_html=True,
    )
    stroke_color = st.color_picker("Color del trazo", "#FFFFFF")
    bg_color = st.color_picker("Color del lienzo", "#000000")


# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown("""
    <div class="hero">
        <div class="hero-left">
            <div class="hero-kicker">Lienzo interactivo · tiempo real</div>
            <h1>Tu <em>taller</em> de dibujo</h1>
            <p>Elige una herramienta, ajusta colores y empieza a crear. Todo lo que dibujes aparece al instante en el lienzo.</p>
        </div>
        <div class="hero-chips">
            <span class="hero-chip"><span class="dot"></span> 7 herramientas</span>
            <span class="hero-chip"><span class="dot"></span> Personalizable</span>
            <span class="hero-chip"><span class="dot"></span> Sin límites</span>
        </div>
    </div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# ETIQUETA DEL LIENZO
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
    <div class="canvas-frame-label">
        <span>📐 Lienzo activo</span>
        <span class="size">{canvas_width} × {canvas_height} px</span>
    </div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# LIENZO (misma funcionalidad)
# ═══════════════════════════════════════════════════════════════
with st.container(key="canvas_wrap"):
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
    )


# ═══════════════════════════════════════════════════════════════
# TIPS AL PIE
# ═══════════════════════════════════════════════════════════════
st.markdown("""
    <div class="tips">
        <div class="tip">
            <span class="tip-icon">🖌️</span>
            <h4 class="tip-title">Cambia de herramienta</h4>
            <p class="tip-text">Dibujo libre, líneas, rectángulos, círculos, polígonos y más. Todo desde el panel lateral.</p>
        </div>
        <div class="tip">
            <span class="tip-icon">🎨</span>
            <h4 class="tip-title">Personaliza los colores</h4>
            <p class="tip-text">Escoge el color del trazo y del fondo. Prueba combinaciones contrastantes para que tu obra resalte.</p>
        </div>
        <div class="tip">
            <span class="tip-icon">📏</span>
            <h4 class="tip-title">Ajusta el tamaño</h4>
            <p class="tip-text">Modifica el ancho y alto del lienzo según lo que quieras crear, y el grosor de la línea a tu gusto.</p>
        </div>
    </div>
""", unsafe_allow_html=True)
