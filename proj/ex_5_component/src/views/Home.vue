<template>
  <div class="wrapper">
    <div class="navbar-wrapper">
      <Navbar />
    </div>
    <section v-if="isAuthenticated">
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
                :class="{ 'disabled-arrow': currentIndices.kostya <= 0 }"
                style="cursor: pointer"
              >
                <path d="M15 18l-6-6 6-6"></path>
              </svg>
            </div>
            <div class="carousel-wrapper">
              <div
                class="carousel-track"
                :style="{
                  transform: `translateX(${-(
                    currentIndices.kostya * 300 -
                    300
                  )}px)`,
                }"
              >
                <div
                  v-for="(test, index) in kostyaTests"
                  :key="`kostya-${index}`"
                  class="test-card"
                  :class="{
                    'main-card': index === currentIndices.kostya,
                    'side-card': index !== currentIndices.kostya,
                  }"
                >
                  <h3>{{ test.name }}</h3>
                  <img :src="test.preview" alt="Preview" class="preview-img" />
                  <p>{{ test.description }}</p>
                  <router-link :to="test.path" class="btn-modern"
                    >Перейти к тесту</router-link
                  >
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
                :class="{
                  'disabled-arrow':
                    currentIndices.kostya >= kostyaTests.length - 1,
                }"
                style="cursor: pointer"
              >
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
                :class="{ 'disabled-arrow': currentIndices.gleb <= 0 }"
                style="cursor: pointer"
              >
                <path d="M15 18l-6-6 6-6"></path>
              </svg>
            </div>
            <div class="carousel-wrapper">
              <div
                class="carousel-track"
                :style="{
                  transform: `translateX(${-(
                    currentIndices.gleb * 300 -
                    300
                  )}px)`,
                }"
              >
                <div
                  v-for="(test, index) in glebTests"
                  :key="`gleb-${index}`"
                  class="test-card"
                  :class="{
                    'main-card': index === currentIndices.gleb,
                    'side-card': index !== currentIndices.gleb,
                  }"
                >
                  <h3>{{ test.name }}</h3>
                  <img
                    :src="test.preview"
                    alt="Preview"
                    class="preview-img"
                    width="200"
                    height="93"
                  />
                  <p>{{ test.description }}</p>
                  <router-link :to="test.path" class="btn-modern"
                    >Перейти к тесту</router-link
                  >
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
                :class="{
                  'disabled-arrow': currentIndices.gleb >= glebTests.length - 1,
                }"
                style="cursor: pointer"
              >
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
                :class="{ 'disabled-arrow': currentIndices.ilya <= 0 }"
                style="cursor: pointer"
              >
                <path d="M15 18l-6-6 6-6"></path>
              </svg>
            </div>
            <div class="carousel-wrapper">
              <div
                class="carousel-track"
                :style="{
                  transform: `translateX(${-(
                    currentIndices.ilya * 300 -
                    300
                  )}px)`,
                }"
              >
                <div
                  v-for="(test, index) in ilyaTests"
                  :key="`ilya-${index}`"
                  class="test-card"
                  :class="{
                    'main-card': index === currentIndices.ilya,
                    'side-card': index !== currentIndices.ilya,
                  }"
                >
                  <h3>{{ test.name }}</h3>
                  <img :src="test.preview" alt="Preview" class="preview-img" />
                  <p>{{ test.description }}</p>
                  <router-link :to="test.path" class="btn-modern"
                    >Перейти к тесту</router-link
                  >
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
                :class="{
                  'disabled-arrow': currentIndices.ilya >= ilyaTests.length - 1,
                }"
                style="cursor: pointer"
              >
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
                :class="{ 'disabled-arrow': currentIndices.masha <= 0 }"
                style="cursor: pointer"
              >
                <path d="M15 18l-6-6 6-6"></path>
              </svg>
            </div>
            <div class="carousel-wrapper">
              <div
                class="carousel-track"
                :style="{
                  transform: `translateX(${-(
                    currentIndices.masha * 300 -
                    300
                  )}px)`,
                }"
              >
                <div
                  v-for="(test, index) in mashaTests"
                  :key="`masha-${index}`"
                  class="test-card"
                  :class="{
                    'main-card': index === currentIndices.masha,
                    'side-card': index !== currentIndices.masha,
                  }"
                >
                  <h3>{{ test.name }}</h3>
                  <img :src="test.preview" alt="Preview" class="preview-img" />
                  <p>{{ test.description }}</p>
                  <router-link :to="test.path" class="btn-modern"
                    >Перейти к тесту</router-link
                  >
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
                :class="{
                  'disabled-arrow':
                    currentIndices.masha >= mashaTests.length - 1,
                }"
                style="cursor: pointer"
              >
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
                :class="{ 'disabled-arrow': currentIndices.mitya <= 0 }"
                style="cursor: pointer"
              >
                <path d="M15 18l-6-6 6-6"></path>
              </svg>
            </div>
            <div class="carousel-wrapper">
              <div
                class="carousel-track"
                :style="{
                  transform: `translateX(${-(
                    currentIndices.mitya * 300 -
                    300
                  )}px)`,
                }"
              >
                <div
                  v-for="(test, index) in mityaTests"
                  :key="`mitya-${index}`"
                  class="test-card"
                  :class="{
                    'main-card': index === currentIndices.mitya,
                    'side-card': index !== currentIndices.mitya,
                  }"
                >
                  <h3>{{ test.name }}</h3>
                  <img :src="test.preview" alt="Preview" class="preview-img" />
                  <p>{{ test.description }}</p>
                  <router-link :to="test.path" class="btn-modern"
                    >Перейти к тесту</router-link
                  >
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
                :class="{
                  'disabled-arrow':
                    currentIndices.mitya >= mityaTests.length - 1,
                }"
                style="cursor: pointer"
              >
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
                :class="{ 'disabled-arrow': currentIndices.ksysha <= 0 }"
                style="cursor: pointer"
              >
                <path d="M15 18l-6-6 6-6"></path>
              </svg>
            </div>
            <div class="carousel-wrapper">
              <div
                class="carousel-track ks"
                :style="{
                  transform: `translateX(${-(
                    currentIndices.ksysha * 300 -
                    300
                  )}px)`,
                }"
              >
                <div
                  v-for="(test, index) in ksyshaTests"
                  :key="`ksysha-${index}`"
                  class="test-card"
                  :class="{
                    'main-card': index === currentIndices.ksysha,
                    'side-card': index !== currentIndices.ksysha,
                  }"
                >
                  <h3>{{ test.name }}</h3>
                  <img :src="test.preview" alt="Preview" class="preview-img" />
                  <p>{{ test.description }}</p>
                  <router-link :to="test.path" class="btn-modern"
                    >Перейти к тесту</router-link
                  >
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
                :class="{
                  'disabled-arrow':
                    currentIndices.ksysha >= ksyshaTests.length - 1,
                }"
                style="cursor: pointer"
              >
                <path d="M9 18l6-6-6-6"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section
      v-else
      class="d-flex justify-content-center align-items-center vh-100"
    >
      <h2>Для прохождения тестов требуется авторизация</h2>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/navbar/Navbar.vue";

export default {
  data() {
    return {
      kostyaTests: [
        {
          name: "Пары эмодзи",
          path: "/test1",
          description: "Найдите пары одинаковых эмодзи за минуту",
          preview: "/static/previews/kostya/test1.png",
        },
        {
          name: "Направление стрелки",
          path: "/test2",
          description: "Определите направление стрелки на цветном фоне",
          preview: "/static/previews/kostya/test2.png",
        },
        {
          name: "Эмодзи друг за другом",
          path: "/test3",
          description: "Определите, поменялся ли эмодзи на новый",
          preview: "/static/previews/kostya/test3.png",
        },
        {
          name: "Сравнение чисел",
          path: "/test4",
          description: "Поставьте правильный знак между числами",
          preview: "/static/previews/kostya/test4.png",
        },
        {
          name: "Ближайший цвет",
          path: "/test5",
          description: "Определите оттенок какого цвета на экране",
          preview: "/static/previews/kostya/test5.png",
        },
      ],
      glebTests: [
        {
          name: "Цвет слова",
          path: "/attention-test",
          description: "Определи какого цвета слова на экране",
          preview: "/static/previews/gleb/attention.png",
        },
        {
          name: "Реакция нажатия",
          path: "/reaction-test",
          description: "Среагируй, когда цвет станет зеленым",
          preview: "/static/previews/gleb/reaction.png",
        },
        {
          name: "Краткосрочная память",
          path: "/memory-test",
          description: "Запоминай картинки и отвечай на вопросы",
          preview: "/static/previews/gleb/memory.png",
        },
        {
          name: "Поиск слов",
          path: "/text-selection-test",
          description: "Выдели слова из набора букв",
          preview: "/static/previews/gleb/text.png",
        },
        {
          name: "Сумма цифр",
          path: "/sum-digits-test",
          description: "Сложи все цифры в каждом ряду",
          preview: "/static/previews/gleb/sum.png",
        },
      ],
      ilyaTests: [
        {
          name: "Запомни места цифр",
          path: "/test1ilya",
          description:
            "Нажми на нужные квадраты в правильной последовательности",
          preview: "/static/previews/ilya/test1.png",
        },
        {
          name: "Особый цвет",
          path: "/test2ilya",
          description: "Найди квадрат с уникальным цветом",
          preview: "/static/previews/ilya/test2.png",
        },
        {
          name: "Особый символ",
          path: "/test3ilya",
          description: "Найди квадрат с уникальным символом",
          preview: "/static/previews/ilya/test3.png",
        },
        {
          name: "Скорость кликов",
          path: "/test4ilya",
          description: "Кликай как можно быстрее",
          preview: "/static/previews/ilya/test4.png",
        },
        {
          name: "Скорость печати",
          path: "/test5ilya",
          description: "Печатай слова как можно быстрее",
          preview: "/static/previews/ilya/test5.png",
        },
      ],
      mashaTests: [
        {
          name: "Название и цвет совпадают",
          path: "/rectangles",
          description: "Найди квадраты, у которых совпадают название и цвет",
          preview: "/static/previews/masha/rectangles.png",
        },
        {
          name: "Запомни 12 чисел",
          path: "/twelve-number-test",
          description: "Запомни в каких квадратах находятся числа",
          preview: "/static/previews/masha/twelve.png",
        },
        {
          name: "Числовой пазл",
          path: "/numbers-puzzle",
          description: "Определи, в каких квадратах лежат правильные числа",
          preview: "/static/previews/masha/puzzle.png",
        },
        {
          name: "Скорость реакции",
          path: "/reaction-speed",
          description: "Среагируй, когда цвет станет зеленым",
          preview: "/static/previews/masha/speed.png",
        },
        {
          name: "Тест Струпа",
          path: "/classical-stroop-test",
          description: "Найди слова, у которых совпадают название и их цвет",
          preview: "/static/previews/masha/stroop.png",
        },
      ],
      mityaTests: [
        {
          name: "Верно ли сравнение",
          path: "/test1mitya",
          description: "Определи верный ли стоит знак сравнения",
          preview: "/static/previews/mitya/test1.png",
        },
        {
          name: "Цвет соответствует слову",
          path: "/test2mitya",
          description: "Определи цвет слова соответствует ли слову внизу",
          preview: "/static/previews/mitya/test2.png",
        },
        {
          name: "Попади по квадрату",
          path: "/test3mitya",
          description: "Нажимайте на бежевый квадрат",
          preview: "/static/previews/mitya/test3.png",
        },
        {
          name: "Пятнашки",
          path: "/test4mitya",
          description: "Собери правильную картинку",
          preview: "/static/previews/mitya/test4.png",
        },
        {
          name: "Нужная сумма",
          path: "/test5mitya",
          description: "Отметьте числа, сумма которых равна нужной",
          preview: "/static/previews/mitya/test5.png",
        },
      ],
      ksyshaTests: [
        {
          name: "Простые вопросы",
          path: "/test1k",
          description: "Отвечайте на вопросы",
          preview: "/static/previews/ksysha/test1.png",
        },
        {
          name: "Нажми вовремя",
          path: "/test2k",
          description: "Нажми на кнопу, когда она появиться",
          preview: "/static/previews/ksysha/test2.png",
        },
        {
          name: "Цвет и слово совпадают",
          path: "/test3k",
          description: "Определите цвет слова",
          preview: "/static/previews/ksysha/test3.png",
        },
      ],
      currentIndices: {
        kostya: 0,
        gleb: 0,
        ilya: 0,
        masha: 0,
        mitya: 0,
        ksysha: 0,
      },
      isAuthenticated: false,
    };
  },
  created() {
    this.checkAuthStatus();
  },
  methods: {
    checkAuthStatus() {
      // Проверяем, есть ли user_id в localStorage
      this.isAuthenticated = !!localStorage.getItem("user_id");
    },
    navigateCarousel(group, direction) {
      const tests = {
        kostya: this.kostyaTests,
        gleb: this.glebTests,
        ilya: this.ilyaTests,
        masha: this.mashaTests,
        mitya: this.mityaTests,
        ksysha: this.ksyshaTests,
      };

      if (direction === "left" && this.currentIndices[group] > 0) {
        this.currentIndices[group]--;
      } else if (
        direction === "right" &&
        this.currentIndices[group] < tests[group].length - 1
      ) {
        this.currentIndices[group]++;
      }

      // Save the new index to localStorage
      localStorage.setItem(`carousel_${group}`, this.currentIndices[group]);
    },
    loadSavedIndices() {
      // Load saved indices from localStorage
      const groups = ["kostya", "gleb", "ilya", "masha", "mitya", "ksysha"];
      groups.forEach((group) => {
        const savedIndex = localStorage.getItem(`carousel_${group}`);
        if (savedIndex !== null) {
          // Ensure the saved index is within bounds
          const maxIndex = this[`${group}Tests`].length - 1;
          this.currentIndices[group] = Math.min(
            Math.max(parseInt(savedIndex), 0),
            maxIndex
          );
        }
      });
    },
  },
  mounted() {
    // Load saved indices when component mounts
    this.loadSavedIndices();
  },
  components: {
    Navbar,
  },
};
</script>

<style scoped>
.wrapper {
  background: rgb(219, 240, 255);
  width: 100vw;
  height: 100%;
}
.navbar-wrapper {
  background: white;
  padding-block: 5px;
  border-bottom: 1px solid gray;
  padding-inline: 20%;
}
/* Локальные стили для Home.vue */
.carousel-section {
  padding: 40px;
  padding-bottom: 40px;
  position: relative;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.carousel-title {
  font-size: 2.5rem;
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
  display: flex;
  justify-content: center;
  width: 900px;
  position: relative;
  border-radius: 16px;
  background-color: #ffffff;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
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
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
  transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out,
    box-shadow 0.3s ease;
  margin: 0 15px;
}

.test-card:hover {
  box-shadow: 0 8px 35px rgba(0, 0, 0, 0.15);
  transform: translateY(-5px);
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
  border-radius: 12px;
  margin-bottom: 16px;
  border: 2px solid #f0f0f0;
}

.carousel-track .test-card:first-child {
  margin-left: 600px;
}
.carousel-track.ks .test-card:first-child {
  margin-left: 0;
}

.test-card h3 {
  font-size: 1.6rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 12px;
  transition: color 0.3s ease;
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
  box-shadow: 0 4px 15px rgba(107, 72, 255, 0.3);
}

.btn-modern:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(107, 72, 255, 0.5);
}

/* Медиа-запрос для ширины менее 800px */
@media (max-width: 800px) {
  .carousel-wrapper {
    width: 100%;
    box-shadow: none; /* Убираем тень для более чистого вида */
  }

  .carousel-track {
    flex-direction: column; /* Переключаем в колонку */
    align-items: center;
    transform: none !important; /* Отключаем трансформацию */
    transition: none; /* Убираем анимацию */
  }

  .test-card {
    width: 100%; /* Полная ширина карточки */
    max-width: 300px; /* Ограничиваем максимальную ширину */
    margin: 15px 0; /* Вертикальные отступы вместо горизонтальных */
    transform: none; /* Отключаем масштабирование */
    opacity: 1; /* Все карточки полностью видимы */
  }

  .main-card,
  .side-card {
    transform: none; /* Убираем различия между главной и боковыми карточками */
    opacity: 1;
  }

  .arrow-container {
    display: none; /* Скрываем стрелки, так как карусель не нужна */
  }

  .carousel-track .test-card:first-child {
    margin-left: 0; /* Убираем отступ для первой карточки */
  }

  .carousel-outer-wrapper {
    flex-direction: column; /* Убеждаемся, что внешний контейнер тоже в колонке */
  }

  .carousel-section {
    padding: 20px; /* Уменьшаем отступы для мобильных устройств */
  }

  .carousel-title {
    font-size: 2rem; /* Уменьшаем размер заголовка */
    text-align: center; /* Центрируем заголовок */
  }
}
</style>
