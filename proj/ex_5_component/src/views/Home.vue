<template>
    <div class="container mt-5 text-center">
      <h1 class="mb-4">Тесты</h1>
  
      <!-- Carousel of links with arrows -->
      <div class="d-flex align-items-center justify-content-center mb-4">
        <!-- Left Arrow -->
        <div class="arrow-left-container">
          <svg 
            @click="navigateTest('left')" 
            xmlns="http://www.w3.org/2000/svg" 
            width="40" 
            height="40" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            stroke-width="2" 
            stroke-linecap="round" 
            stroke-linejoin="round" 
            class="text-primary arrow-icon" 
            :class="{'disabled-arrow': currentTest <= 0}"
            style="cursor: pointer;">
            <path d="M15 18l-6-6 6-6"></path>
          </svg>
        </div>
  
        <!-- Test description and link -->
        <div class="mx-4">
          <p>Текущий тест: {{ currentTest + 1 }} из {{ tests.length }} ({{ selectedTest.name }})</p>
          <p>{{ selectedTest.description }}</p>
          <router-link 
            :to="selectedTest.path" 
            class="btn btn-primary">
            Перейти к тесту
          </router-link>
        </div>
  
        <!-- Right Arrow -->
        <div class="arrow-right-container">
          <svg 
            @click="navigateTest('right')" 
            xmlns="http://www.w3.org/2000/svg" 
            width="40" 
            height="40" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            stroke-width="2" 
            stroke-linecap="round" 
            stroke-linejoin="round" 
            class="text-primary arrow-icon" 
            :class="{'disabled-arrow': currentTest >= tests.length - 1}"
            style="cursor: pointer;">
            <path d="M9 18l6-6-6-6"></path>
          </svg>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tests: [
          { name: 'Test 1', path: '/test1', description: 'Перед вами набор эмодзи, в котором одинаковые только два. Найдите как можно больше пар таких эмодзи за минуту' },
          { name: 'Test 2', path: '/test2', description: 'Перед вами стрелка, которая смотрит вверх/вниз/влево/вправо и либо красный фон, либо синий. Вам необходимо за минуту определить как можно больше раз путь стрелки...' },
          { name: 'Test 3', path: '/test3', description: 'Описание теста 3' },
          { name: 'Test 4', path: '/test4', description: 'Описание теста 4' },
          { name: 'Test 5', path: '/test5', description: 'Описание теста 5' },
          { name: 'Attention Test', path: '/attention-test', description: 'Описание теста на внимание' },
          { name: 'Reaction Test', path: '/reaction-test', description: 'Описание теста на реакцию' },
          { name: 'Memory Test', path: '/memory-test', description: 'Описание теста на память' },
          { name: 'Text Selection Test', path: '/text-selection-test', description: 'Описание теста на выбор текста' },
          { name: 'Sum Digits Test', path: '/sum-digits-test', description: 'Описание теста на сумму цифр' },
          { name: 'Test 1 Ilya', path: '/test1ilya', description: 'Описание теста 1 от Ильи' },
          { name: 'Test 2 Ilya', path: '/test2ilya', description: 'Описание теста 2 от Ильи' },
          { name: 'Test 3 Ilya', path: '/test3ilya', description: 'Описание теста 3 от Ильи' },
          { name: 'Test 4 Ilya', path: '/test4ilya', description: 'Описание теста 4 от Ильи' },
          { name: 'Test 5 Ilya', path: '/test5ilya', description: 'Описание теста 5 от Ильи' },
          { name: 'Rectangles', path: '/rectangles', description: 'Описание теста на прямоугольники' },
          { name: 'Twelve Number Test', path: '/twelve-number-test', description: 'Описание теста на 12 чисел' },
          { name: 'Numbers Puzzle', path: '/numbers-puzzle', description: 'Описание головоломки с числами' },
          { name: 'Reaction Speed', path: '/reaction-speed', description: 'Описание теста на скорость реакции' },
          { name: 'Classical Stroop Test', path: '/classical-stroop-test', description: 'Описание классического теста Струпа' },
          { name: 'Test 1 Mitya', path: '/test1mitya', description: 'Описание теста 1 от Мити' },
          { name: 'Test 2 Mitya', path: '/test2mitya', description: 'Описание теста 2 от Мити' },
          { name: 'Test 3 Mitya', path: '/test3mitya', description: 'Описание теста 3 от Мити' },
          { name: 'Test 4 Mitya', path: '/test4mitya', description: 'Описание теста 4 от Мити' },
          { name: 'Test 5 Mitya', path: '/test5mitya', description: 'Описание теста 5 от Мити' },
          { name: 'Test 1 Ksysha', path: '/test1k', description: 'Описание теста 1 от Ксюши' },
          { name: 'Test 2 Ksysha', path: '/test2k', description: 'Описание теста 2 от Ксюши' },
          { name: 'Test 3 Ksysha', path: '/test3k', description: 'Описание теста 3 от Ксюши' },
        ],
        currentTest: 0,
      };
    },
    computed: {
      selectedTest() {
        return this.tests[this.currentTest];
      },
    },
    methods: {
      navigateTest(direction) {
        if (direction === 'left' && this.currentTest > 0) {
          this.currentTest--;
        } else if (direction === 'right' && this.currentTest < this.tests.length - 1) {
          this.currentTest++;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .arrow-left-container, .arrow-right-container {
    position: fixed;
    top: 50%;
    transform: translateY(-50%);
    z-index: 10;
  }
  
  .arrow-left-container {
    left: 0;
    padding: 10px;
    border-radius: 50%;
  }
  
  .arrow-right-container {
    right: 0;
    padding: 10px;
    border-radius: 50%;
  }
  
  .arrow-icon {
    width: 40px;
    height: 40px;
  }
  
  .disabled-arrow {
    opacity: 0.3;
    pointer-events: none;
  }
  </style>