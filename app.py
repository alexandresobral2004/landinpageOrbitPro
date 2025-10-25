import streamlit as st
import base64
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Orbit PRO - Soluções em IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Função para carregar CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Função para carregar imagem e converter para base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Função para exibir imagem local
def get_img_with_href(local_img_path, target_width="100%"):
    img_format = Path(local_img_path).suffix
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <img src="data:image/{img_format[1:]};base64,{bin_str}" 
             style="width: {target_width}; height: auto; border-radius: 1rem; 
                    box-shadow: 0 8px 30px rgba(0, 191, 255, 0.3);
                    animation: float 6s ease-in-out infinite;">
    '''
    return html_code

# CSS customizado para o Streamlit
streamlit_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stException {display: none;}
    .stAlert {display: none;}
    
    /* Hide debug elements */
    .st-emotion-cache-brzme7 {display: none !important;}
    pre[class*="st-emotion-cache"] {display: none !important;}
    div[data-testid="stException"] {display: none !important;}
    
    /* Main container */
    .main > div {
        padding-top: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #FFFFFF 0%, #F4F4F4 100%);
        padding: 4rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        color: #333333;
        margin-bottom: 1rem;
    }
    
    .hero-description {
        font-family: 'Poppins', sans-serif;
        font-size: 1.25rem;
        color: #555555;
        line-height: 1.6;
        margin-bottom: 2rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Sections */
    .section {
        padding: 3rem 2rem;
    }
    
    .section-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 600;
        color: #333333;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .about-section {
        background-color: #F4F4F4;
    }
    
    /* Cards */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 191, 255, 0.15);
    }
    
    .card-icon {
        font-size: 2.5rem;
        color: #00BFFF;
        margin-bottom: 1rem;
    }
    
    .card-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #333333;
        margin-bottom: 1rem;
    }
    
    .card-description {
        font-family: 'Poppins', sans-serif;
        color: #555555;
        line-height: 1.6;
    }
    
    /* Contact section */
    .contact-section {
        background-color: #FFFFFF;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    .contact-info {
        background: #F4F4F4;
        padding: 2rem;
        border-radius: 1rem;
        margin: 2rem 0;
    }
    
    /* Button */
    .custom-button {
        background-color: #00BFFF;
        color: white;
        padding: 1rem 2rem;
        border-radius: 0.5rem;
        border: none;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 1.1rem;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .custom-button:hover {
        background-color: #0099CC;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 191, 255, 0.3);
    }
    
    /* Orbit design */
    .orbit-design {
        width: 220px;
        height: 220px;
        position: relative;
        margin: 0 auto;
        background: linear-gradient(135deg, #00BFFF 0%, #0099CC 100%);
        border-radius: 50%;
        box-shadow: 0 8px 30px rgba(0, 191, 255, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        animation: rotateOrbit 20s linear infinite;
    }
    
    .orbit-logo {
        background: rgba(255, 255, 255, 0.95);
        padding: 8px 16px;
        border-radius: 20px;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #333333;
    }
    
    .orbit-pro {
        color: #00BFFF;
        font-weight: 700;
    }
    
    @keyframes rotateOrbit {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title { font-size: 2rem; }
        .hero-description { font-size: 1rem; }
        .section { padding: 2rem 1rem; }
        .orbit-design { width: 180px; height: 180px; }
    }
    </style>
"""

def main():
    # Aplicar CSS customizado
    st.markdown(streamlit_style, unsafe_allow_html=True)
    
    # Hide any potential debug or error elements
    st.markdown("""
        <style>
        .stException, .stAlert, .stError {
            display: none !important;
        }
        pre[class*="st-emotion-cache"] {
            display: none !important;
        }
        div[class*="st-emotion-cache"] pre {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header com logo
    st.markdown("""
        <div style="background: white; padding: 1rem 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 1rem; font-family: 'Poppins', sans-serif;">
                    <div style="font-size: 2.2rem; font-weight: 600; color: #333333;">
                        Orbit <span style="color: #00BFFF; font-weight: 700;">PRO</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #666; padding-left: 1rem; border-left: 2px solid #00BFFF; font-weight: 500;">
                        Soluções em IA
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div class="hero-section">
                <h1 class="hero-title">Soluções em IA</h1>
                <p class="hero-description">
                    Se sua empresa busca inovar com inteligência, conte com a Orbit PRO para transformar dados em decisões, processos em automações e ideias em soluções.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Verificar se a imagem existe
        img_path = "img/orbitPro.jpg"
        if Path(img_path).exists():
            st.markdown(f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 100%; padding: 2rem;">
                    {get_img_with_href(img_path, "250px")}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="display: flex; justify-content: center; align-items: center; height: 250px;">
                    <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #00BFFF, #0099CC); 
                               border-radius: 50%; display: flex; align-items: center; justify-content: center;
                               color: white; font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 1.5rem;">
                        Orbit PRO
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # Seção Sobre
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Sobre a Orbit PRO</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <div style="padding: 2rem;">
                <p style="font-family: 'Poppins', sans-serif; color: #555555; line-height: 1.8; margin-bottom: 1.5rem; font-size: 1.1rem;">
                    Com mais de 20 anos de experiência nas áreas de computação, desenvolvimento de sistemas e treinamento de usuários, a Orbit PRO se consolidou como referência em soluções tecnológicas inovadoras.
                </p>
                <p style="font-family: 'Poppins', sans-serif; color: #555555; line-height: 1.8; font-size: 1.1rem;">
                    Nossa equipe multidisciplinar alia conhecimento técnico profundo à capacidade de entender e transformar os desafios dos nossos clientes em resultados concretos.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%; padding: 2rem;">
                <div class="orbit-design">
                    <div class="orbit-logo">
                        Orbit <span class="orbit-pro">PRO</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Diferenciais
    st.markdown('<h2 class="section-title">Diferenciais Orbit PRO</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    diferenciais = [
        ("🎓", "Equipe Experiente", "Equipe experiente com sólida formação acadêmica e atuação prática em projetos reais."),
        ("✅", "Abordagem Personalizada", "Abordagem personalizada, focada nas necessidades específicas de cada cliente."),
        ("🚀", "Compromisso com Resultados", "Compromisso com resultados, com entregas ágeis e acompanhamento contínuo."),
        ("🧠", "Atualização Constante", "Atualização constante, acompanhando as tendências e evoluções da Inteligência Artificial.")
    ]
    
    cols = [col1, col2, col3, col4]
    
    for i, (icon, title, desc) in enumerate(diferenciais):
        with cols[i]:
            st.markdown(f"""
                <div class="card">
                    <div class="card-icon">{icon}</div>
                    <h3 class="card-title">{title}</h3>
                    <p class="card-description">{desc}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # Serviços
    st.markdown('<div class="section" style="background-color: #F4F4F4;">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Nossas Frentes de Atuação</h2>', unsafe_allow_html=True)
    
    servicos = [
        ("🧠", "Consultoria em Inteligência Artificial", "A Orbit PRO oferece serviços especializados em Inteligência Artificial, com foco em aplicações práticas que impulsionam negócios e otimizam processos."),
        ("🤖", "Desenvolvimento de Agentes Inteligentes e Bots", "Criação de assistentes virtuais personalizados, bots para redes sociais e integração com WhatsApp, Instagram, Facebook e Telegram."),
        ("📱", "Aplicações Web e Mobile com IA", "Integração de modelos de IA em sistemas web e aplicativos móveis, com soluções para recomendação de conteúdo e análise de sentimentos."),
        ("📊", "Análise de Dados e Inteligência de Negócio", "Coleta, tratamento e visualização de dados com técnicas de machine learning para previsão de demanda e segmentação de clientes."),
        ("🎓", "Treinamento Corporativo em IA", "Capacitação de equipes para uso estratégico de ferramentas de IA, workshops práticos e formação técnica em Python e Machine Learning.")
    ]
    
    for i in range(0, len(servicos), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            icon, title, desc = servicos[i]
            st.markdown(f"""
                <div class="card">
                    <div class="card-icon">{icon}</div>
                    <h3 class="card-title">{title}</h3>
                    <p class="card-description">{desc}</p>
                </div>
            """, unsafe_allow_html=True)
        
        if i + 1 < len(servicos):
            with col2:
                icon, title, desc = servicos[i + 1]
                st.markdown(f"""
                    <div class="card">
                        <div class="card-icon">{icon}</div>
                        <h3 class="card-title">{title}</h3>
                        <p class="card-description">{desc}</p>
                    </div>
                """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contato
    st.markdown('<div class="contact-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Vamos Conversar?</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="contact-info">
                <div style="font-size: 2rem; color: #00BFFF; margin-bottom: 1rem;">📧</div>
                <h3 style="font-family: 'Poppins', sans-serif; color: #333333; margin-bottom: 0.5rem;">Email</h3>
                <p style="color: #555555;">orbitprosobral@gmail.com</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="contact-info">
                <div style="font-size: 2rem; color: #00BFFF; margin-bottom: 1rem;">📞</div>
                <h3 style="font-family: 'Poppins', sans-serif; color: #333333; margin-bottom: 0.5rem;">Telefone</h3>
                <p style="color: #555555;">(88) 99357 3809</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="contact-info">
                <div style="font-size: 2rem; color: #00BFFF; margin-bottom: 1rem;">🌐</div>
                <h3 style="font-family: 'Poppins', sans-serif; color: #333333; margin-bottom: 0.5rem;">Website</h3>
                <p style="color: #555555;">https://orbitpro.streamlit.app/</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Formulário de contato
    st.markdown('<h3 style="text-align: center; margin: 2rem 0; font-family: \'Poppins\', sans-serif; color: #333333;">Entre em Contato</h3>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Nome *", placeholder="Seu nome completo")
            email = st.text_input("Email *", placeholder="seu@email.com")
        
        with col2:
            telefone = st.text_input("Telefone", placeholder="(XX) XXXXX-XXXX")
            empresa = st.text_input("Empresa", placeholder="Nome da sua empresa")
        
        mensagem = st.text_area("Mensagem *", placeholder="Descreva como podemos ajudar você...", height=100)
        
        submitted = st.form_submit_button("Enviar Mensagem", use_container_width=True)
        
        if submitted:
            if nome and email and mensagem:
                st.success("✅ Mensagem enviada com sucesso! Entraremos em contato em breve.")
            else:
                st.error("❌ Por favor, preencha todos os campos obrigatórios (*).")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div style="background: #333333; color: white; padding: 2rem; text-align: center; margin-top: 2rem;">
            <div style="font-family: 'Poppins', sans-serif; font-size: 1.2rem; margin-bottom: 1rem;">
                Orbit <span style="color: #00BFFF; font-weight: 700;">PRO</span>
            </div>
            <p style="color: #CCCCCC; margin: 0;">
                © 2025 Orbit PRO. Todos os direitos reservados. | https://orbitpro.streamlit.app/
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()