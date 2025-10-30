// Community Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
  // Initialize all features
  initPreloader();
  setupScrollAnimations();
  setupCounterAnimations();
  setupGalleryModal();
  setupSmoothScroll();
  setupEventRegistration();
});

// Preloader
function initPreloader() {
  const preloader = document.getElementById('js-preloader');
  if (preloader) {
    window.addEventListener('load', function() {
      setTimeout(function() {
        preloader.style.opacity = '0';
        setTimeout(function() {
          preloader.style.display = 'none';
        }, 500);
      }, 800);
    });
  }
}

// Scroll Reveal Animations
function setupScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        
        // Trigger counter animation when stats section is visible
        if (entry.target.classList.contains('stat-card')) {
          const statNumber = entry.target.querySelector('.stat-number');
          if (statNumber && !statNumber.classList.contains('counted')) {
            animateCounter(statNumber);
            statNumber.classList.add('counted');
          }
        }
      }
    });
  }, observerOptions);

  // Observe all sections and cards
  const elements = document.querySelectorAll('.stat-card, .gallery-item, .testimonial-card, .event-card');
  elements.forEach(el => {
    el.classList.add('scroll-reveal');
    observer.observe(el);
  });
}

// Counter Animation
function animateCounter(element) {
  const target = parseInt(element.getAttribute('data-target'));
  const duration = 2000; // 2 seconds
  const increment = target / (duration / 16); // 60 FPS
  let current = 0;

  const updateCounter = () => {
    current += increment;
    if (current < target) {
      element.textContent = Math.floor(current).toLocaleString();
      requestAnimationFrame(updateCounter);
    } else {
      element.textContent = target.toLocaleString();
    }
  };

  updateCounter();
}

// Setup counter animations for stats
function setupCounterAnimations() {
  const statNumbers = document.querySelectorAll('.stat-number');
  
  const observerOptions = {
    threshold: 0.5
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
        animateCounter(entry.target);
        entry.target.classList.add('counted');
      }
    });
  }, observerOptions);

  statNumbers.forEach(stat => observer.observe(stat));
}

// Gallery Modal/Lightbox
function setupGalleryModal() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  
  galleryItems.forEach(item => {
    item.addEventListener('click', function() {
      const img = this.querySelector('img');
      const content = this.querySelector('.gallery-content');
      
      // Create modal
      const modal = document.createElement('div');
      modal.className = 'gallery-modal';
      modal.innerHTML = `
        <div class="gallery-modal-content">
          <span class="gallery-modal-close">&times;</span>
          <img src="${img.src}" alt="${img.alt}">
          <div class="gallery-modal-info">
            <h3>${content.querySelector('h4').textContent}</h3>
            <p>${content.querySelector('p').textContent}</p>
          </div>
        </div>
      `;
      
      document.body.appendChild(modal);
      
      // Add styles dynamically
      if (!document.getElementById('gallery-modal-styles')) {
        const style = document.createElement('style');
        style.id = 'gallery-modal-styles';
        style.innerHTML = `
          .gallery-modal {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.95);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            animation: fadeIn 0.3s ease;
          }
          .gallery-modal-content {
            max-width: 900px;
            width: 100%;
            position: relative;
            animation: slideUp 0.4s ease;
          }
          .gallery-modal-content img {
            width: 100%;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
          }
          .gallery-modal-close {
            position: absolute;
            top: -40px;
            right: 0;
            font-size: 40px;
            color: white;
            cursor: pointer;
            transition: transform 0.3s ease;
          }
          .gallery-modal-close:hover {
            transform: rotate(90deg);
          }
          .gallery-modal-info {
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-top: 20px;
            text-align: center;
          }
          .gallery-modal-info h3 {
            font-size: 28px;
            font-weight: 700;
            color: #764ba2;
            margin-bottom: 10px;
          }
          .gallery-modal-info p {
            font-size: 18px;
            color: #666;
          }
          @keyframes slideUp {
            from {
              opacity: 0;
              transform: translateY(30px);
            }
            to {
              opacity: 1;
              transform: translateY(0);
            }
          }
        `;
        document.head.appendChild(style);
      }
      
      // Close modal
      setTimeout(() => {
        modal.style.opacity = '1';
      }, 10);
      
      const closeBtn = modal.querySelector('.gallery-modal-close');
      closeBtn.addEventListener('click', function() {
        modal.style.opacity = '0';
        setTimeout(() => {
          modal.remove();
        }, 300);
      });
      
      modal.addEventListener('click', function(e) {
        if (e.target === modal) {
          modal.style.opacity = '0';
          setTimeout(() => {
            modal.remove();
          }, 300);
        }
      });
    });
  });
}

// Smooth Scrolling
function setupSmoothScroll() {
  const links = document.querySelectorAll('a[href^="#"]');
  
  links.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#' && href !== '#!') {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
}

// Event Registration
function setupEventRegistration() {
  const eventBtns = document.querySelectorAll('.event-btn');
  
  eventBtns.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Show confirmation message
      const originalText = this.textContent;
      this.textContent = 'Registered! ✓';
      this.style.background = '#28a745';
      this.style.pointerEvents = 'none';
      
      // Show notification
      showNotification('Successfully registered for the event!');
      
      // Reset after 3 seconds
      setTimeout(() => {
        this.textContent = originalText;
        this.style.background = '';
        this.style.pointerEvents = '';
      }, 3000);
    });
  });
}

// Notification System
function showNotification(message) {
  const notification = document.createElement('div');
  notification.className = 'custom-notification';
  notification.textContent = message;
  
  // Add styles dynamically
  if (!document.getElementById('notification-styles')) {
    const style = document.createElement('style');
    style.id = 'notification-styles';
    style.innerHTML = `
      .custom-notification {
        position: fixed;
        top: 100px;
        right: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px 30px;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        z-index: 9999;
        animation: slideInRight 0.4s ease, slideOutRight 0.4s ease 2.6s;
        font-weight: 600;
      }
      @keyframes slideInRight {
        from {
          transform: translateX(400px);
          opacity: 0;
        }
        to {
          transform: translateX(0);
          opacity: 1;
        }
      }
      @keyframes slideOutRight {
        from {
          transform: translateX(0);
          opacity: 1;
        }
        to {
          transform: translateX(400px);
          opacity: 0;
        }
      }
    `;
    document.head.appendChild(style);
  }
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.remove();
  }, 3000);
}

// Parallax Effect for Hero
window.addEventListener('scroll', function() {
  const hero = document.querySelector('.community-hero');
  if (hero) {
    const scrolled = window.pageYOffset;
    const rate = scrolled * 0.5;
    hero.style.transform = 'translateY(' + rate + 'px)';
  }
});

// Add hover effects to stat cards
const statCards = document.querySelectorAll('.stat-card');
statCards.forEach(card => {
  card.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-10px) scale(1.05)';
  });
  
  card.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0) scale(1)';
  });
});

// Testimonial Card Effects
const testimonialCards = document.querySelectorAll('.testimonial-card');
testimonialCards.forEach(card => {
  card.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-10px) rotate(2deg)';
  });
  
  card.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0) rotate(0deg)';
  });
});

// Log page load
console.log('Community page loaded successfully!');
console.log('Join our vibrant Sign Sarthi community!');
