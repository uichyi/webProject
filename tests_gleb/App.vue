<template>
  <div id="my-app">
    <h1>Когнитивные тесты</h1>

    <!-- Главное меню -->
    <div v-if="!currentTest" class="menu">
      <div
        v-for="(test, key) in tests"
        :key="key"
        class="menu-item"
        @click="selectTest(key)"
      >
        {{ test }}
      </div>
    </div>

    <!-- Таймер и выбранный тест -->
    <div v-else>
      <Timer ref="timer" />
      <component
        :is="currentTest"
        @test-complete="onTestComplete"
        @test-start="onTestStart"
      />
      <button @click="backToMenu" class="back-button">Вернуться в меню</button>
    </div>
  </div>
</template>

<script>
import Timer from './components/Timer.vue';
import AttentionTest from './components/AttentionTest.vue';
import ReactionTest from './components/ReactionTest.vue';
import MemoryTest from './components/MemoryTest.vue';
import TextSelectionTest from './components/TextSelectionTest.vue';
import SumDigitsTest from './components/SumDigitsTest.vue';

export default {
  components: {
    Timer,
    AttentionTest,
    ReactionTest,
    MemoryTest,
    TextSelectionTest,
    SumDigitsTest,
  },
  data() {
    return {
      currentTest: null,
      tests: {
        SumDigitsTest: 'Устный счет',
        AttentionTest: 'Внимание',
        ReactionTest: 'Реакция',
        MemoryTest: 'Память',
        TextSelectionTest: 'Выбор текста',
      },
    };
  },
  methods: {
    selectTest(testName) {
      this.currentTest = testName;
    },
    onTestComplete(score, total_test=10) {
      this.$refs.timer.stopTimer();
      const totalTime = this.$refs.timer.timeElapsed;
      alert(
        `Вы завершили тест за ${Math.floor(totalTime / 1000)} секунд. Ваш результат: ${score} из ${total_test}.`
      );
      this.backToMenu();
    },
    onTestStart() {
      this.$refs.timer.resetTimer();
      this.$refs.timer.startTimer();
    },
    backToMenu() {
      this.currentTest = null;
      this.$refs.timer.resetTimer();
    },
  },
};
</script>

<style>

#app{
  max-width: 4000px;
  display: flex;
  position: relative;
}

#my-app{
  width: 100%;
  box-sizing: border-box;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.menu {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  padding: 20px;
}

.menu-item {
  width: 150px;
  height: 150px;
  background-color: #f0f0f0;
  border: 2px solid #ccc;
  color: black;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.menu-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  background-color: #e0eaff;
  border-color: #6c91ff;
}

h1 {
  text-align: center;
  margin-bottom: 100px;
}

.back-button {
  left: 50%;
  margin-left: -85px;
  margin-top: 150px;
  background-color: #6c91ff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
  position: relative;
}

.back-button:hover {
  background-color: #5577cc;
}

.timer{
  margin-bottom: 50px;
}
</style>