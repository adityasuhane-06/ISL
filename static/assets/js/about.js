// About Page JavaScript

(function() {
  'use strict';

  // Counter Animation for Stats
  function animateCounter() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-target'));
      const duration = 2000; // 2 seconds
      const increment = target / (duration / 16); // 60fps
      let current = 0;
      
      const updateCounter = () => {
        current += increment;
        if (current < target) {
          counter.textContent = Math.ceil(current);
          requestAnimationFrame(updateCounter);
        } else {
          counter.textContent = target;
        }
      };
      
      updateCounter();
    });
  }

  // Intersection Observer for scroll animations
  function setupScrollAnimations() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          
          // Trigger counter animation when stats section is visible
          if (entry.target.classList.contains('stats-section')) {
            animateCounter();
          }
        }
      });
    }, observerOptions);

    // Observe feature cards
    document.querySelectorAll('.feature-card').forEach((card, index) => {
      card.style.animationDelay = `${index * 0.1}s`;
      observer.observe(card);
    });

    // Observe tech items
    document.querySelectorAll('.tech-item').forEach((item, index) => {
      item.style.animationDelay = `${index * 0.15}s`;
      observer.observe(item);
    });

    // Observe stats section
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
      observer.observe(statsSection);
    }
  }

  // Smooth scroll for anchor links
  function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }

  // Add parallax effect to hero section
  function setupParallax() {
    const hero = document.querySelector('.about-hero');
    if (!hero) return;

    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      if (hero) {
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
      }
    });
  }

  // Initialize page preloader
  function initPreloader() {
    const preloader = document.getElementById('js-preloader');
    if (preloader) {
      window.addEventListener('load', () => {
        preloader.classList.add('loaded');
      });
    }
  }

  // Add hover effect to feature cards
  function setupCardEffects() {
    document.querySelectorAll('.feature-card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
      });
      
      card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
      });
    });
  }

  // Initialize everything when DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    initPreloader();
    setupScrollAnimations();
    setupSmoothScroll();
    setupParallax();
    setupCardEffects();
  });

})();
