# 🚀 Orbit PRO - Landing Page Streamlit

Uma landing page moderna e responsiva da Orbit PRO desenvolvida com Streamlit para fácil hospedagem no Streamlit Cloud.

## 🌐 Deploy no Streamlit Cloud

### Pré-requisitos

1. Conta no [Streamlit Cloud](https://streamlit.io/cloud)
2. Repositório GitHub com o projeto
3. Arquivos necessários no repositório

### Arquivos Essenciais para Deploy

```
📁 landingPageOrbit/
├── 📄 app.py              # Aplicação principal Streamlit
├── 📄 requirements.txt    # Dependências Python
├── 📁 .streamlit/         # Configurações do Streamlit
│   └── 📄 config.toml     # Tema e configurações
├── 📁 img/               # Imagens (opcional)
│   └── 📄 orbitPro.jpg   # Imagem hero
└── 📄 README_STREAMLIT.md # Este arquivo
```

### Passos para Deploy

1. **Faça push do projeto para o GitHub:**

   ```bash
   git add .
   git commit -m "Add Streamlit version"
   git push origin main
   ```

2. **Acesse [Streamlit Cloud](https://share.streamlit.io/)**

3. **Clique em "New app"**

4. **Configure a aplicação:**

   - Repository: `projetosAlexandre/task-list` (ou seu repo)
   - Branch: `main`
   - Main file path: `landingPageOrbit/app.py`
   - App URL: `orbit-pro` (ou outro nome desejado)

5. **Clique em "Deploy!"**

## 🎨 Características da Versão Streamlit

### ✅ Funcionalidades Implementadas

- **Design responsivo** adaptado para Streamlit
- **Cores da marca** Orbit PRO (#00BFFF, #333333)
- **Seções completas:** Hero, Sobre, Diferenciais, Serviços, Contato
- **Formulário de contato** funcional
- **Design visual animado** na seção About
- **Tipografia Poppins** via Google Fonts
- **Layout mobile-friendly**

### 🎯 Adaptações para Streamlit

- CSS customizado integrado
- Remoção de elementos nativos do Streamlit
- Layout em colunas responsivo
- Formulário interativo com validação
- Design system mantido

### 📱 Responsividade

- **Desktop:** Layout em colunas otimizado
- **Mobile:** Adaptação automática com media queries
- **Tablet:** Experiência intermediária balanceada

## 🛠️ Tecnologias Utilizadas

- **Streamlit** 1.28.0+ - Framework principal
- **Python** 3.8+ - Linguagem base
- **HTML/CSS** - Estilização customizada
- **Google Fonts** - Tipografia Poppins
- **Base64** - Encoding de imagens locais

## 🎨 Customizações CSS

### Tema Principal

```css
/* Cores da marca */
--primary-color: #00BFFF    /* Ciano Orbit PRO */
--secondary-color: #333333  /* Cinza escuro */
--background: #FFFFFF       /* Branco */
--background-alt: #F4F4F4   /* Cinza claro */
```

### Animações Mantidas

- **Float effect** na imagem hero
- **Orbit rotation** no design visual
- **Card hover effects** nos diferenciais e serviços

## 📧 Funcionalidades

### Formulário de Contato

- Campos: Nome*, Email*, Telefone, Empresa, Mensagem\*
- Validação front-end
- Feedback visual (sucesso/erro)
- Layout responsivo

### Seções Interativas

- **Hero:** Apresentação principal com CTA
- **Sobre:** História e experiência da empresa
- **Diferenciais:** 4 cards com pontos fortes
- **Serviços:** 5 frentes de atuação detalhadas
- **Contato:** Informações e formulário

## 🔧 Configurações do Streamlit

### Theme (config.toml)

```toml
[theme]
primaryColor = "#00BFFF"      # Azul Orbit PRO
backgroundColor = "#FFFFFF"    # Fundo branco
secondaryBackgroundColor = "#F4F4F4"  # Cinza claro
textColor = "#333333"         # Texto cinza escuro
font = "sans serif"           # Fonte sans-serif
```

### Server Settings

- **Headless mode:** Ativado para produção
- **CORS:** Desabilitado para simplicidade
- **Usage stats:** Desabilitado para privacidade

## 🚀 Como Executar Localmente

1. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Execute a aplicação:**

   ```bash
   streamlit run app.py
   ```

3. **Acesse no navegador:**
   ```
   http://localhost:8501
   ```

## 📈 Vantagens do Streamlit Cloud

- ✅ **Deploy gratuito** para projetos open source
- ✅ **Atualizações automáticas** via GitHub
- ✅ **Escalabilidade** automática
- ✅ **HTTPS** incluído
- ✅ **Domínio personalizado** disponível
- ✅ **Monitoramento** integrado

## 🔄 Comparação: HTML vs Streamlit

### Versão HTML Original

- Arquivo estático
- Hospedagem tradicional necessária
- JavaScript para interatividade
- Formulário requer backend

### Versão Streamlit

- Aplicação web interativa
- Deploy simplificado no Streamlit Cloud
- Python para lógica
- Formulário funcional integrado

## 📞 Suporte

Para questões sobre a implementação Streamlit:

- **Email:** orbitprosobral@gmail.com
- **Telefone:** (88) 99357 3809
- **Website:** www.orbitpro.com.br

---

**🎨 Orbit PRO - Transformando ideias em soluções com IA**
