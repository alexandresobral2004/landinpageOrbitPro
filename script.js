/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
  navToggle = document.getElementById('nav-toggle'),
  navClose = document.getElementById('nav-close')

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if (navToggle) {
  navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu')
  })
}

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if (navClose) {
  navClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu')
  })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction() {
  const navMenu = document.getElementById('nav-menu')
  // When we click on each nav__link, we remove the show-menu class
  navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

function scrollActive() {
  const scrollY = window.pageYOffset

  sections.forEach(current => {
    const sectionHeight = current.offsetHeight
    const sectionTop = current.offsetTop - 50;
    const sectionId = current.getAttribute('id')

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
    } else {
      document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
    }
  })
}
window.addEventListener('scroll', scrollActive)

/*=============== CHANGE BACKGROUND HEADER ===============*/
function scrollHeader() {
  const nav = document.getElementById('header')
  // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
  if (this.scrollY >= 80) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/*=============== SHOW SCROLL UP ===============*/
function scrollUp() {
  const scrollUp = document.getElementById('scroll-up');
  // When the scroll is higher than 560 viewport height, add the show-scroll class to the a tag with the scroll-top class
  if (this.scrollY >= 560) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

/*=============== SMOOTH SCROLLING ===============*/
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const headerHeight = document.querySelector('.header').offsetHeight;
      const targetPosition = target.offsetTop - headerHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  });
});

/*=============== CONTACT FORM VALIDATION ===============*/
const contactForm = document.getElementById('contactForm');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const messageInput = document.getElementById('message');

// Function to show error message
function showError(input, message) {
  const formGroup = input.parentElement;

  // Remove existing error message
  const existingError = formGroup.querySelector('.error-message');
  if (existingError) {
    existingError.remove();
  }

  // Add error class to input
  input.classList.add('error');

  // Create and add error message
  const errorDiv = document.createElement('div');
  errorDiv.className = 'error-message';
  errorDiv.textContent = message;
  errorDiv.style.color = '#e74c3c';
  errorDiv.style.fontSize = '0.875rem';
  errorDiv.style.marginTop = '0.25rem';

  formGroup.appendChild(errorDiv);
}

// Function to clear error
function clearError(input) {
  const formGroup = input.parentElement;
  const errorMessage = formGroup.querySelector('.error-message');

  if (errorMessage) {
    errorMessage.remove();
  }

  input.classList.remove('error');
}

// Function to validate email
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Function to validate form
function validateForm() {
  let isValid = true;

  // Clear all previous errors
  [nameInput, emailInput, phoneInput, messageInput].forEach(input => {
    clearError(input);
  });

  // Validate name
  if (nameInput.value.trim() === '') {
    showError(nameInput, 'Nome é obrigatório');
    isValid = false;
  } else if (nameInput.value.trim().length < 2) {
    showError(nameInput, 'Nome deve ter pelo menos 2 caracteres');
    isValid = false;
  }

  // Validate email
  if (emailInput.value.trim() === '') {
    showError(emailInput, 'Email é obrigatório');
    isValid = false;
  } else if (!isValidEmail(emailInput.value.trim())) {
    showError(emailInput, 'Por favor, insira um email válido');
    isValid = false;
  }

  // Validate message
  if (messageInput.value.trim() === '') {
    showError(messageInput, 'Mensagem é obrigatória');
    isValid = false;
  } else if (messageInput.value.trim().length < 10) {
    showError(messageInput, 'Mensagem deve ter pelo menos 10 caracteres');
    isValid = false;
  }

  return isValid;
}

// Real-time validation
nameInput.addEventListener('blur', function () {
  if (this.value.trim() === '') {
    showError(this, 'Nome é obrigatório');
  } else if (this.value.trim().length < 2) {
    showError(this, 'Nome deve ter pelo menos 2 caracteres');
  } else {
    clearError(this);
  }
});

emailInput.addEventListener('blur', function () {
  if (this.value.trim() === '') {
    showError(this, 'Email é obrigatório');
  } else if (!isValidEmail(this.value.trim())) {
    showError(this, 'Por favor, insira um email válido');
  } else {
    clearError(this);
  }
});

messageInput.addEventListener('blur', function () {
  if (this.value.trim() === '') {
    showError(this, 'Mensagem é obrigatória');
  } else if (this.value.trim().length < 10) {
    showError(this, 'Mensagem deve ter pelo menos 10 caracteres');
  } else {
    clearError(this);
  }
});

// Clear errors when user starts typing
[nameInput, emailInput, messageInput].forEach(input => {
  input.addEventListener('input', function () {
    if (this.classList.contains('error')) {
      clearError(this);
    }
  });
});

// Form submission
if (contactForm) {
  contactForm.addEventListener('submit', function (e) {
    e.preventDefault();

    if (validateForm()) {
      // Here you would normally send the form data to a server
      // For this demo, we'll show a success message
      showSuccessMessage();

      // Reset form
      contactForm.reset();
    }
  });
}

// Function to show success message
function showSuccessMessage() {
  // Create success message
  const successDiv = document.createElement('div');
  successDiv.className = 'success-message';
  successDiv.innerHTML = `
        <div style="
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #c3e6cb;
            text-align: center;
            font-weight: 500;
        ">
            ✅ Mensagem enviada com sucesso! Entraremos em contato em breve.
        </div>
    `;

  // Insert success message before the form
  const formContainer = contactForm.parentElement;
  formContainer.insertBefore(successDiv, contactForm);

  // Remove success message after 5 seconds
  setTimeout(() => {
    successDiv.remove();
  }, 5000);

  // Scroll to success message
  successDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/*=============== ANIMATION ON SCROLL ===============*/
// Simple animation observer for elements
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function (entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function () {
  // Elements to animate
  const animateElements = document.querySelectorAll(
    '.differential__card, .service__card, .contact__card, .about__content, .hero__content'
  );

  // Set initial state and observe
  animateElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });

  // Animate hero content immediately
  const heroContent = document.querySelector('.hero__content');
  if (heroContent) {
    setTimeout(() => {
      heroContent.style.opacity = '1';
      heroContent.style.transform = 'translateY(0)';
    }, 200);
  }
});

/*=============== FORM INPUT ANIMATIONS ===============*/
// Add focus animations to form inputs
document.querySelectorAll('.contact__form-input').forEach(input => {
  input.addEventListener('focus', function () {
    this.style.transform = 'scale(1.02)';
    this.style.transition = 'transform 0.2s ease';
  });

  input.addEventListener('blur', function () {
    this.style.transform = 'scale(1)';
  });
});

/*=============== BUTTON HOVER EFFECTS ===============*/
// Enhanced button interactions
document.querySelectorAll('.button').forEach(button => {
  button.addEventListener('mouseenter', function () {
    this.style.transform = 'translateY(-2px)';
  });

  button.addEventListener('mouseleave', function () {
    this.style.transform = 'translateY(0)';
  });
});

/*=============== LOADING ANIMATION ===============*/
// Add loading state to contact form button
const contactButton = document.querySelector('.contact__button');
if (contactButton) {
  contactForm.addEventListener('submit', function (e) {
    if (validateForm()) {
      // Show loading state
      const originalText = contactButton.textContent;
      contactButton.textContent = 'Enviando...';
      contactButton.disabled = true;
      contactButton.style.opacity = '0.7';

      // Simulate sending delay
      setTimeout(() => {
        contactButton.textContent = originalText;
        contactButton.disabled = false;
        contactButton.style.opacity = '1';
      }, 2000);
    }
  });
}

/*=============== MOBILE MENU ENHANCEMENTS ===============*/
// Close mobile menu when clicking outside
document.addEventListener('click', function (e) {
  const navMenu = document.getElementById('nav-menu');
  const navToggle = document.getElementById('nav-toggle');

  if (navMenu.classList.contains('show-menu') &&
    !navMenu.contains(e.target) &&
    !navToggle.contains(e.target)) {
    navMenu.classList.remove('show-menu');
  }
});

// Handle escape key to close mobile menu
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') {
    const navMenu = document.getElementById('nav-menu');
    if (navMenu.classList.contains('show-menu')) {
      navMenu.classList.remove('show-menu');
    }
  }
});

/*=============== CSS STYLES FOR FORM VALIDATION ===============*/
// Add CSS for form validation styles
const formValidationStyles = `
    .contact__form-input.error {
        border-color: #e74c3c;
        box-shadow: 0 0 10px rgba(231, 76, 60, 0.2);
    }
    
    .contact__form-input:focus {
        outline: none;
        border-color: var(--primary-color);
        box-shadow: 0 0 10px rgba(0, 191, 255, 0.2);
    }
    
    .contact__form-input.error:focus {
        border-color: #e74c3c;
        box-shadow: 0 0 10px rgba(231, 76, 60, 0.2);
    }
    
    .scroll-header {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
`;

// Inject validation styles
const styleSheet = document.createElement('style');
styleSheet.textContent = formValidationStyles;
document.head.appendChild(styleSheet);