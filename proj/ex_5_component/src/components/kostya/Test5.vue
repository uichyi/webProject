<template>
  <div class="container text-center">
    <div v-if="!gameOver">
      <div class="color-display" :style="{'background-color': displayedColor}"></div>
      <div class="d-flex justify-content-center mb-3">
        <button class="btn btn-danger mx-2" @click="checkAnswer('red')">Красный</button>
        <button class="btn btn-success mx-2" @click="checkAnswer('green')">Зеленый</button>
        <button class="btn btn-primary mx-2" @click="checkAnswer('blue')">Синий</button>
      </div>
      <div class="my-2">Счет: {{ score }}</div>
      <div class="my-2">Осталось {{ time }} секунд</div>
    </div>
    <div v-else>
      <h2>Игра окончена, Счет: {{ score }}</h2>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      displayedColor: '',
      red: 0,
      green: 0,
      blue: 0,
      score: 0,
      time: 60,
      timer: null,
      gameOver: false,
      testId: 5
    };
  },
  methods: {
    generateColor() {
      do {
        this.red = Math.floor(Math.random() * 256);
        this.green = Math.floor(Math.random() * 256);
        this.blue = Math.floor(Math.random() * 256);
      } while (Math.abs(this.red - this.green) < 40 && Math.abs(this.green - this.blue) < 40 && Math.abs(this.red - this.red) < 40); 
      this.displayedColor = `rgb(${this.red}, ${this.green}, ${this.blue})`;
    },
    checkAnswer(selectedColor) {
      let maxColorValue = Math.max(this.red, this.green, this.blue);
      let correctColor;

      switch (maxColorValue) {
        case this.red: correctColor = 'red'; break;
        case this.green: correctColor = 'green'; break;
        case this.blue: correctColor = 'blue'; break;
      } 

      if (selectedColor == correctColor) {
        this.score++;
      } else {
        this.score--;
      }

      this.generateColor();
    },
    startTimer() {
      this.timer = setInterval(() => {
        this.time--;
        if (this.time <= 0) {
          this.stopGame();
        }
      }, 1000);
    },
    stopGame() {
      this.gameOver = true;
      clearInterval(this.timer);
      this.saveTestResult();
    },
    async saveTestResult() {
      const testResultData = {
        'user': localStorage.getItem('user_id'),
        "test": this.testId,
        "number_correct_answers": this.score,
        "complete_time": 60,
      };
      console.log(testResultData);

      try {
        const response = await axios.post(
          '/test-results/create/',
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
  mounted() {
    this.startTimer();
    this.generateColor();
  },
};
</script>

<style>
.color-display {
  width: 200px;
  height: 200px;
  margin: 20px auto;
  border: 2px solid #000;
}
</style>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f9f9f9;
}
</style>