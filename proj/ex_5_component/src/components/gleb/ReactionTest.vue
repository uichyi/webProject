<template>
  <div class="test-container" @click="handleClick">
    <div v-if="!testStarted" class="start-screen">
      <h2>Нажмите, чтобы начать тест</h2>
      <p>Вам предстоит выполнить 5 попыток. Реагируйте как можно быстрее, когда круг станет зеленым!</p>
    </div>
    <div v-else-if="currentAttempt <= totalAttempts" class="circle-container">
      <div
        :class="['circle', isGreen ? 'green' : 'red']"
      ></div>
    </div>
    <div v-else class="result-screen">
      <h2>Тест завершен!</h2>
      <p>Ваше среднее время реакции: {{ averageReactionTime }} мс</p>
      <button @click="restartTest">Пройти заново</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      testStarted: false,
      isGreen: false,
      currentAttempt: 1,
      totalAttempts: 5,
      reactionTimes: [],
      timeoutId: null,
      startTime: 0,
      testId: 7,
    };
  },
  computed: {
    averageReactionTime() {
      if (this.reactionTimes.length === 0) return 0;
      const sum = this.reactionTimes.reduce((a, b) => a + b, 0);
      return (sum / this.reactionTimes.length).toFixed(2);
    },
  },
  methods: {
    startTest() {
      this.testStarted = true;
      this.startNextAttempt();
    },
    startNextAttempt() {
      this.isGreen = false;

      const randomDelay = Math.floor(Math.random() * 2000) + 1000; // 1-3 секунды
      this.timeoutId = setTimeout(() => {
        this.isGreen = true;
        this.startTime = performance.now();
      }, randomDelay);
    },
    handleClick() {
      if (!this.testStarted) {
        this.startTest();
      } else if (this.isGreen) {
        const reactionTime = performance.now() - this.startTime;
        this.reactionTimes.push(reactionTime);

        if (this.currentAttempt < this.totalAttempts) {
          this.currentAttempt++;
          this.startNextAttempt();
        } else {
          this.currentAttempt++;
          clearTimeout(this.timeoutId);
          this.saveTestResult(); // Вызов функции сохранения результата
        }
      } else {
        alert('Подождите, пока круг станет зеленым!');
        clearTimeout(this.timeoutId);
        this.startNextAttempt();
      }
    },
    restartTest() {
      this.testStarted = false;
      this.currentAttempt = 1;
      this.reactionTimes = [];
      this.isGreen = false;
    },
    async saveTestResult() {
      const testResultData = {
        'user': localStorage.getItem('user_id'),
        "test": this.testId,
        "accuracy": this.averageReactionTime,
      };
      console.log(testResultData);

      try {
        const response = await axios.post(
          'http://localhost:8000/api/test-results/create/',
          testResultData,
          {
            headers: { 'Content-Type': 'application/json' }
          }
        );
        console.log('Результат теста сохранен:', response.data);
      } catch (error) {
        console.error('Ошибка при сохранении результата:', error);
      }
    }
  },
};
</script>

<style scoped>
.timer{
  display: none;
}

.test-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100vh; /* Make sure the content fills the screen */
  width: 100vw;
  background-color: #0000003f;
}

.start-screen {
  /* max-width: 600px; */

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  border: 2px solid #4caf50;
  background-color: #f4f4f4;
  cursor: pointer; /* Indicating it's clickable */
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: all 0.3s;
}

.circle-container {
  position: relative;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: red;
  transition: background-color 0.2s;
}

.circle.green {
  background-color: green;
}

.result-screen {
  text-align: center;
}

button {
  padding: 10px 20px;
  margin-top: 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>