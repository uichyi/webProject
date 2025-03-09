<script setup>
import { ref, watch } from "vue";
import Start from "./components/Start.vue";
import Game from "./components/Game.vue";
import TimerLine from "./components/TimerLine.vue";
import Results from "./components/Results.vue";
import axios from "axios";

const gameState = ref("start");
const gameDuration = ref(15);
const testId = 15;

const wpm = ref(0);
const changeWPM = (val) => {
  wpm.value = val;
};

const mistakenWords = ref([]);
const changeMistakenWords = (val) => {
  mistakenWords.value = val;
  console.log(mistakenWords.value);
};

const changeGameDuration = (value) => {
  gameDuration.value = value;
  console.log(gameDuration.value);
};

const changeState = (state) => {
  gameState.value = state;
};

let timerInterval;
const timer = ref(null);

async function saveTestResult() {
  const testResultData =
  {
    'user': localStorage.getItem('user_id'),
    "test": testId,
    "accuracy": wpm.value,
    "complete_time": gameDuration.value
  };
  console.log(testResultData)
  axios.post(
    '/test-results/create/',
    testResultData,
    {
      headers: {
        'Content-Type': 'application/json',
      },
    }
  ).then(response => {
    console.log('Результат теста сохранен:', response.data);
  }
  ).catch(error => {
    console.error('Ошибка при сохранении результата:', error);
  }
  );
}

watch(gameState, (newState) => {
  if (newState === "game") {
    if (timerInterval) {
      clearInterval(timerInterval);
    }

    timer.value = gameDuration.value;

    timerInterval = setInterval(() => {
      if (timer.value > 0) {
        timer.value -= 1;
      } else {
        gameState.value = "end";
        saveTestResult();
        clearInterval(timerInterval);
      }
    }, 1000);
  }
});
</script>

<template>
  <div id="app">
    <div class="navbarr">
      <RedButton />
    </div>
    <div v-if="gameState === 'start'">
      <Start @changeState="changeState" @changeGameDuration="changeGameDuration" :duration="gameDuration"></Start>
    </div>
    <div v-if="gameState === 'game'" class="col">
      <div class="panel">
        <TimerLine :timer="timer" :INIT_TIME="gameDuration"></TimerLine>
        <span>{{ timer }}</span>
      </div>

      <Game @changeWPM="changeWPM" @changeMistakenWords="changeMistakenWords" @changeState="changeState" :duration="gameDuration"></Game>
    </div>
    <div v-if="gameState === 'end'">
      <Results @changeState="changeState" :wpm="wpm" :mistakenWords="mistakenWords"></Results>
    </div>
  </div>

</template>

<script> 
import RedButton from "../../../navbar/Return.vue";
export default {
  components: {
    RedButton
  }
}
</script>

<style scoped>
#app {
  height: 100vh;
  width: 100vw;
  display: grid;
  grid-template-rows: auto 1fr;
  justify-content: center;
  align-items: center; 
}

.col {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

.panel {
  display: flex;
  align-items: center;
  gap: 1rem;
}
</style>
