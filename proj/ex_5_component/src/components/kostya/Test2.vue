<template>
  <div class="container text-center">
    <div v-if="!gameOver">
      <div :style="{ backgroundColor }" class="text-center p-5 rounded mb-4">
        <h1 class="display-1">{{ currentSymbol }}</h1>
      </div>
      <div class="d-flex justify-content-center mb-3">
        <button v-for="direction in directions" :key="direction" class="btn btn-primary mx-2" @click="checkAnswer(direction)">
          {{ direction }}
        </button>
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
export default {
  data() {
    return {
      currentSymbol: '',
      score: 0,
      backgroundColor: '',
      directions: ['←', '→', '↑', '↓'],
      time: 60,
      timer: null,
      gameOver: false,
    };
  },
  methods: {
    generateNewSymbol() {
      const symbols = ['←', '→', '↑', '↓'];
      const backgrounds = ['blue', 'red'];
      
      this.currentSymbol = symbols[Math.floor(Math.random() * symbols.length)];
      this.backgroundColor = backgrounds[Math.floor(Math.random() * backgrounds.length)];
    },
    checkAnswer(selectedDirection) {
      const isBlueBackground = this.backgroundColor == 'blue';
      const isCorrect = (isBlueBackground && this.currentSymbol == selectedDirection) ||
                       (!isBlueBackground && (this.currentSymbol == this.viceVersa(selectedDirection)));

      if (isCorrect) {
        this.score++;
      } else {
        this.score--;
      }

      this.generateNewSymbol(); 
    },
    viceVersa(selectedDirection) {
      switch(selectedDirection){
        case '←': return '→';
        case '→': return '←';
        case '↑': return '↓';
        case '↓': return '↑';
      }
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
    }
  },
  mounted() {
    this.startTimer(); 
    this.generateNewSymbol();
  }
};
</script>