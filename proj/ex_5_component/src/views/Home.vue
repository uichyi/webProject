<template>
  <Navbar />
    <div class="container mt-5 text-center">
      <h1 class="mb-4">Тесты</h1>
  
      <!-- Kostya's Carousel -->
      <div class="carousel-section mb-5">
        <h2 class="carousel-title">Тесты от Кости</h2>
        <div class="carousel-outer-wrapper">
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('kostya', 'left')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.kostya <= 0}"
              style="cursor: pointer;">
              <path d="M15 18l-6-6 6-6"></path>
            </svg>
          </div>
          <div class="carousel-wrapper">
            <div class="carousel-track" :style="{ transform: `translateX(${-(currentIndices.kostya * 300 - 300)}px)` }">
              <div v-for="(test, index) in kostyaTests" 
                   :key="`kostya-${index}`" 
                   class="test-card" 
                   :class="{ 'main-card': index === currentIndices.kostya, 'side-card': index !== currentIndices.kostya }">
                <h3>{{ test.name }}</h3>
                <img :src="test.preview" alt="Preview" class="preview-img" />
                <p>{{ test.description }}</p>
                <router-link v-if="index === currentIndices.kostya" :to="test.path" class="btn-modern">Перейти к тесту</router-link>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('kostya', 'right')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.kostya >= kostyaTests.length - 1}"
              style="cursor: pointer;">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </div>
        </div>
      </div>
  
      <!-- Gleb's Carousel -->
      <div class="carousel-section mb-5">
        <h2 class="carousel-title">Тесты от Глеба</h2>
        <div class="carousel-outer-wrapper">
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('gleb', 'left')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.gleb <= 0}"
              style="cursor: pointer;">
              <path d="M15 18l-6-6 6-6"></path>
            </svg>
          </div>
          <div class="carousel-wrapper">
            <div class="carousel-track" :style="{ transform: `translateX(${-(currentIndices.gleb * 300 - 300)}px)` }">
              <div v-for="(test, index) in glebTests" 
                   :key="`gleb-${index}`" 
                   class="test-card" 
                   :class="{ 'main-card': index === currentIndices.gleb, 'side-card': index !== currentIndices.gleb }">
                <h3>{{ test.name }}</h3>
                <img :src="test.preview" alt="Preview" class="preview-img" width="200" height="93"/>
                <p>{{ test.description }}</p>
                <router-link v-if="index === currentIndices.gleb" :to="test.path" class="btn-modern">Перейти к тесту</router-link>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('gleb', 'right')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.gleb >= glebTests.length - 1}"
              style="cursor: pointer;">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </div>
        </div>
      </div>
  
      <!-- Ilya's Carousel -->
      <div class="carousel-section mb-5">
        <h2 class="carousel-title">Тесты от Ильи</h2>
        <div class="carousel-outer-wrapper">
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('ilya', 'left')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.ilya <= 0}"
              style="cursor: pointer;">
              <path d="M15 18l-6-6 6-6"></path>
            </svg>
          </div>
          <div class="carousel-wrapper">
            <div class="carousel-track" :style="{ transform: `translateX(${-(currentIndices.ilya * 300 - 300)}px)` }">
              <div v-for="(test, index) in ilyaTests" 
                   :key="`ilya-${index}`" 
                   class="test-card" 
                   :class="{ 'main-card': index === currentIndices.ilya, 'side-card': index !== currentIndices.ilya }">
                <h3>{{ test.name }}</h3>
                <img :src="test.preview" alt="Preview" class="preview-img" />
                <p>{{ test.description }}</p>
                <router-link v-if="index === currentIndices.ilya" :to="test.path" class="btn-modern">Перейти к тесту</router-link>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('ilya', 'right')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.ilya >= ilyaTests.length - 1}"
              style="cursor: pointer;">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </div>
        </div>
      </div>
  
      <!-- Masha's Carousel -->
      <div class="carousel-section mb-5">
        <h2 class="carousel-title">Тесты от Маши</h2>
        <div class="carousel-outer-wrapper">
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('masha', 'left')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.masha <= 0}"
              style="cursor: pointer;">
              <path d="M15 18l-6-6 6-6"></path>
            </svg>
          </div>
          <div class="carousel-wrapper">
            <div class="carousel-track" :style="{ transform: `translateX(${-(currentIndices.masha * 300 - 300)}px)` }">
              <div v-for="(test, index) in mashaTests" 
                   :key="`masha-${index}`" 
                   class="test-card" 
                   :class="{ 'main-card': index === currentIndices.masha, 'side-card': index !== currentIndices.masha }">
                <h3>{{ test.name }}</h3>
                <img :src="test.preview" alt="Preview" class="preview-img" />
                <p>{{ test.description }}</p>
                <router-link v-if="index === currentIndices.masha" :to="test.path" class="btn-modern">Перейти к тесту</router-link>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('masha', 'right')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.masha >= mashaTests.length - 1}"
              style="cursor: pointer;">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </div>
        </div>
      </div>
  
      <!-- Mitya's Carousel -->
      <div class="carousel-section mb-5">
        <h2 class="carousel-title">Тесты от Мити</h2>
        <div class="carousel-outer-wrapper">
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('mitya', 'left')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.mitya <= 0}"
              style="cursor: pointer;">
              <path d="M15 18l-6-6 6-6"></path>
            </svg>
          </div>
          <div class="carousel-wrapper">
            <div class="carousel-track" :style="{ transform: `translateX(${-(currentIndices.mitya * 300 - 300)}px)` }">
              <div v-for="(test, index) in mityaTests" 
                   :key="`mitya-${index}`" 
                   class="test-card" 
                   :class="{ 'main-card': index === currentIndices.mitya, 'side-card': index !== currentIndices.mitya }">
                <h3>{{ test.name }}</h3>
                <img :src="test.preview" alt="Preview" class="preview-img" />
                <p>{{ test.description }}</p>
                <router-link v-if="index === currentIndices.mitya" :to="test.path" class="btn-modern">Перейти к тесту</router-link>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('mitya', 'right')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.mitya >= mityaTests.length - 1}"
              style="cursor: pointer;">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </div>
        </div>
      </div>
  
      <!-- Ksysha's Carousel -->
      <div class="carousel-section mb-5">
        <h2 class="carousel-title">Тесты от Ксюши</h2>
        <div class="carousel-outer-wrapper">
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('ksysha', 'left')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.ksysha <= 0}"
              style="cursor: pointer;">
              <path d="M15 18l-6-6 6-6"></path>
            </svg>
          </div>
          <div class="carousel-wrapper">
            <div class="carousel-track" :style="{ transform: `translateX(${-(currentIndices.ksysha * 300 - 300)}px)` }">
              <div v-for="(test, index) in ksyshaTests" 
                   :key="`ksysha-${index}`" 
                   class="test-card" 
                   :class="{ 'main-card': index === currentIndices.ksysha, 'side-card': index !== currentIndices.ksysha }">
                <h3>{{ test.name }}</h3>
                <img :src="test.preview" alt="Preview" class="preview-img" />
                <p>{{ test.description }}</p>
                <router-link v-if="index === currentIndices.ksysha" :to="test.path" class="btn-modern">Перейти к тесту</router-link>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <svg 
              @click="navigateCarousel('ksysha', 'right')" 
              xmlns="http://www.w3.org/2000/svg" 
              width="40" 
              height="40" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="2" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              class="arrow-icon" 
              :class="{'disabled-arrow': currentIndices.ksysha >= ksyshaTests.length - 1}"
              style="cursor: pointer;">
              <path d="M9 18l6-6-6-6"></path>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import Navbar from "../components/navbar/Navbar.vue";

export default {
    data() {
      return {
        kostyaTests: [
          { name: 'Test 1', path: '/test1', description: 'Найдите пары одинаковых эмодзи за минуту', preview: '/static/previews/kostya/test1.png' },
          { name: 'Test 2', path: '/test2', description: 'Определите путь стрелки на цветном фоне', preview: '/static/previews/kostya/test2.png' },
          { name: 'Test 3', path: '/test3', description: 'Описание теста 3', preview: '/static/previews/kostya/test3.png' },
          { name: 'Test 4', path: '/test4', description: 'Описание теста 4', preview: '/static/previews/kostya/test4.png' },
          { name: 'Test 5', path: '/test5', description: 'Описание теста 5', preview: '/static/previews/kostya/test5.png' },
        ],
        glebTests: [
          { name: 'Attention Test', path: '/attention-test', description: 'Тест на внимание', preview: '/static/previews/gleb/attention.png' },
          { name: 'Reaction Test', path: '/reaction-test', description: 'Тест на реакцию', preview: '/static/previews/gleb/reaction.png' },
          { name: 'Memory Test', path: '/memory-test', description: 'Тест на память', preview: '/static/previews/gleb/memory.png' },
          { name: 'Text Selection Test', path: '/text-selection-test', description: 'Тест на выбор текста', preview: '/static/previews/gleb/text.png' },
          { name: 'Sum Digits Test', path: '/sum-digits-test', description: 'Тест на сумму цифр', preview: '/static/previews/gleb/sum.png' },
        ],
        ilyaTests: [
          { name: 'Test 1 Ilya', path: '/test1ilya', description: 'Описание теста 1 от Ильи', preview: '/static/previews/ilya/test1.png' },
          { name: 'Test 2 Ilya', path: '/test2ilya', description: 'Описание теста 2 от Ильи', preview: '/static/previews/ilya/test2.png' },
          { name: 'Test 3 Ilya', path: '/test3ilya', description: 'Описание теста 3 от Ильи', preview: '/static/previews/ilya/test3.png' },
          { name: 'Test 4 Ilya', path: '/test4ilya', description: 'Описание теста 4 от Ильи', preview: '/static/previews/ilya/test4.png' },
          { name: 'Test 5 Ilya', path: '/test5ilya', description: 'Описание теста 5 от Ильи', preview: '/static/previews/ilya/test5.png' },
        ],
        mashaTests: [
          { name: 'Rectangles', path: '/rectangles', description: 'Тест на прямоугольники', preview: '/static/previews/masha/rectangles.png' },
          { name: 'Twelve Number Test', path: '/twelve-number-test', description: 'Тест на 12 чисел', preview: '/static/previews/masha/twelve.png' },
          { name: 'Numbers Puzzle', path: '/numbers-puzzle', description: 'Головоломка с числами', preview: '/static/previews/masha/puzzle.png' },
          { name: 'Reaction Speed', path: '/reaction-speed', description: 'Тест на скорость реакции', preview: '/static/previews/masha/speed.png' },
          { name: 'Classical Stroop Test', path: '/classical-stroop-test', description: 'Классический тест Струпа', preview: '/static/previews/masha/stroop.png' },
        ],
        mityaTests: [
          { name: 'Test 1 Mitya', path: '/test1mitya', description: 'Описание теста 1 от Мити', preview: '/static/previews/mitya/test1.png' },
          { name: 'Test 2 Mitya', path: '/test2mitya', description: 'Описание теста 2 от Мити', preview: '/static/previews/mitya/test2.png' },
          { name: 'Test 3 Mitya', path: '/test3mitya', description: 'Описание теста 3 от Мити', preview: '/static/previews/mitya/test3.png' },
          { name: 'Test 4 Mitya', path: '/test4mitya', description: 'Описание теста 4 от Мити', preview: '/static/previews/mitya/test4.png' },
          { name: 'Test 5 Mitya', path: '/test5mitya', description: 'Описание теста 5 от Мити', preview: '/static/previews/mitya/test5.png' },
        ],
        ksyshaTests: [
          { name: 'Test 1 Ksysha', path: '/test1k', description: 'Описание теста 1 от Ксюши', preview: '/static/previews/ksysha/test1.png' },
          { name: 'Test 2 Ksysha', path: '/test2k', description: 'Описание теста 2 от Ксюши', preview: '/static/previews/ksysha/test2.png' },
          { name: 'Test 3 Ksysha', path: '/test3k', description: 'Описание теста 3 от Ксюши', preview: '/static/previews/ksysha/test3.png' },
        ],
        currentIndices: {
          kostya: 0,
          gleb: 0,
          ilya: 0,
          masha: 0,
          mitya: 0,
          ksysha: 0,
        },
      };
    },
    methods: {
    navigateCarousel(group, direction) {
      const tests = {
        kostya: this.kostyaTests,
        gleb: this.glebTests,
        ilya: this.ilyaTests,
        masha: this.mashaTests,
        mitya: this.mityaTests,
        ksysha: this.ksyshaTests,
      };
      
      if (direction === 'left' && this.currentIndices[group] > 0) {
        this.currentIndices[group]--;
      } else if (direction === 'right' && this.currentIndices[group] < tests[group].length - 1) {
        this.currentIndices[group]++;
      }
      
      // Save the new index to localStorage
      localStorage.setItem(`carousel_${group}`, this.currentIndices[group]);
    },
    loadSavedIndices() {
      // Load saved indices from localStorage
      const groups = ['kostya', 'gleb', 'ilya', 'masha', 'mitya', 'ksysha'];
      groups.forEach(group => {
        const savedIndex = localStorage.getItem(`carousel_${group}`);
        if (savedIndex !== null) {
          // Ensure the saved index is within bounds
          const maxIndex = this[`${group}Tests`].length - 1;
          this.currentIndices[group] = Math.min(Math.max(parseInt(savedIndex), 0), maxIndex);
        }
      });
    }
  },
  mounted() {
    // Load saved indices when component mounts
    this.loadSavedIndices();
  },
  components: {
    Navbar,
  }
  };
  </script>
  
  <style scoped>
  /* Локальные стили для Home.vue */
  .carousel-section {
    padding-bottom: 40px;
    position: relative;
    background-color: #f9f9f9; /* Light background for better contrast */
    border-radius: 10px; /* Optional: Adds some roundness to the section */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Adds a light shadow to the section */
  }
  
  .carousel-title {
    font-size: 2.5rem; /* Slightly bigger title for more emphasis */
    font-weight: 700;
    color: #2b2b2b;
    margin-bottom: 32px;
    text-align: left;
  }
  
  .carousel-outer-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 1100px;
    margin: 0 auto;
  }
  
  .carousel-wrapper {
    overflow: hidden;
    width: 900px; /* 3 cards, each 300px */
    position: relative;
    border-radius: 16px;
    background-color: #ffffff; /* White background for the carousel container */
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); /* Adds a larger shadow to the carousel container */
  }
  
  .arrow-container {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px;
    z-index: 2;
  }
  
  .arrow-icon {
    width: 40px;
    height: 40px;
    color: #333;
    transition: color 0.3s ease, transform 0.3s ease;
  }
  
  .arrow-icon:hover {
    color: #6b48ff;
    transform: scale(1.1);
  }
  
  .disabled-arrow {
    opacity: 0.3;
    pointer-events: none;
  }
  
  .carousel-track {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  
  .test-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 24px;
    width: 300px;
    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1); /* Stronger shadow to make each card stand out more */
    flex-shrink: 0;
    transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out, box-shadow 0.3s ease;
    margin: 0 15px; /* Adds some space between the cards */
  }
  
  .test-card:hover {
    box-shadow: 0 8px 35px rgba(0, 0, 0, 0.15); /* Darker shadow on hover for better emphasis */
    transform: translateY(-5px); /* Slight movement on hover to give a lifted effect */
  }
  
  .main-card {
    transform: scale(1);
    opacity: 1;
    z-index: 1;
  }
  
  .side-card {
    transform: scale(0.85);
    opacity: 0.6;
  }
  
  .preview-img {
    width: 250px;
    height: 150px;
    /* object-fit: contain; */
    border-radius: 12px;
    margin-bottom: 16px;
    border: 2px solid #f0f0f0; /* Adds a subtle border around the images */
  }
  
  .test-card h3 {
    font-size: 1.6rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 12px;
    transition: color 0.3s ease; /* Adds a smooth transition for color */
  }
  
  .test-card p {
    font-size: 1rem;
    color: #777;
    line-height: 1.5;
    margin-bottom: 16px;
  }
  
  .btn-modern {
    display: inline-block;
    padding: 12px 24px;
    background: linear-gradient(135deg, #6b48ff 0%, #8a3ffc 100%);
    color: #fff;
    font-weight: 600;
    text-decoration: none;
    border-radius: 8px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 15px rgba(107, 72, 255, 0.3); /* Adds some shadow for a modern button */
  }
  
  .btn-modern:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(107, 72, 255, 0.5); /* Stronger shadow on hover */
  }
</style>
