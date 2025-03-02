<template>
  <div class="attention-test" @click="handleClick">
    <div v-if="!testStarted" class="start-screen">
      <h2>Нажмите, чтобы начать тест</h2>
      <p>Это тест на внимательность. Вам нужно будет выбирать из предложенных вариантов слова правильно описывающие цвет слов на экране. </p>
    </div>

    <div v-else-if="currentTask <= totalTasks && !testCompleted">
      <h2>Задание {{ currentTask }}</h2>
      <div class="words">
        <span
          v-for="(word, index) in taskWords"
          :key="index"
          :style="{ color: word.color }"
          class="word"
        >
          {{ word.text }}
        </span>
      </div>
      <div class="options">
        <button
          v-for="(option, index) in options"
          :key="index"
          @click="checkAnswer(option)"
        >
          {{ option.join(', ') }}
        </button>
      </div>
      <div class="progress-bar">
        <div class="progress" :style="{ width: progress + '%' }"></div>
      </div>
    </div>

    <div v-if="testCompletedAndCallFunction" class="result">
      <h3>Тест завершен!</h3>
      <p>Вы правильно ответили на {{ score }} из {{ totalTasks }} вопросов.</p>
      <button @click="restartTest">Пройти тест заново</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      currentTask: 1,
      totalTasks: 10,
      words: ['Красный', 'Синий','Зеленый','Желтый','Белый'],
      colors: ['red', 'blue', 'green', 'yellow', 'white'],
      taskWords: [],
      correctAnswer: [],
      options: [],
      score: 0,
      testStarted: false,
      testCompleted: false,
      taskId: 6,
      testId: 6
    };
  },
  computed: {
    progress() {
      return (this.currentTask / this.totalTasks) * 100;
    },
    testCompletedAndCallFunction() {
      if (this.testCompleted) {
        this.saveTestResult();
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {
    async saveTestResult() {
      const testResultData =
        {
          'user': localStorage.getItem('user_id'),
          "test": this.testId,
          "number_correct_answers": this.score,
          "number_all_answers": this.totalTasks,
          "accuracy": this.score / this.totalTasks
        };
      console.log(testResultData)
        axios.post(
          'http://localhost:8000/api/test-results/create/',
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
    },
    handleClick() {
      if (!this.testStarted) {
        this.testStarted = true;
        this.$emit('test-start');
        this.generateTask();
      }
    },
    generateTask() {
      const wordsCount = this.currentTask;
      const words = [];
      const answer = [];
      for (let i = 0; i < wordsCount; i++) {
        const randomColorText = this.words[Math.floor(Math.random() * this.words.length)];
        const randomColorIndex = Math.floor(Math.random() * this.colors.length);
        const randomColor = this.colors[randomColorIndex];
        words.push({ text: randomColorText, color: randomColor });
        answer.push(this.words[randomColorIndex]);
      }
      this.taskWords = words;
      this.correctAnswer = answer;

      const options = [];
      const correctOption = [...answer];
      options.push(correctOption);

      while (options.length < 3) {
        const randomOption = []
        for(let i = 0; i < wordsCount; i++){
          randomOption.push(this.words[Math.floor(Math.random() * this.words.length)])
        }

        if (!options.some((opt) => JSON.stringify(opt) === JSON.stringify(randomOption))) {
          options.push(randomOption);
        }
      }

      this.options = options.sort(() => Math.random() - 0.5);
    },
    checkAnswer(selectedOption) {
      if (JSON.stringify(selectedOption) === JSON.stringify(this.correctAnswer)) {
        this.score++;
      }
      if (this.currentTask < this.totalTasks) {
        this.currentTask++;
        this.generateTask();
      } else {
        this.testCompleted = true;
        this.$emit('test-complete', this.score);
      }
    },
    restartTest() {
      this.currentTask = 1;
      this.score = 0;
      this.testCompleted = false
      this.generateTask();
      this.$emit('test-start');
    },
  },
};
</script>

<style scoped>
.attention-test {
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

.start-screen:hover {
  background-color: #e7f7e7; /* Hover effect */
}

.words {
  margin: 20px 0;
  display: flex;
  justify-content: center;
}

.word {
  font-size: 24px;
  margin: 0 10px;
}

.options button {
  margin: 10px;
  padding: 10px 20px;
  cursor: pointer;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.options button:hover {
  background-color: #45a049;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background: #ddd;
  margin-top: 20px;
  position: relative;
}

.progress {
  height: 100%;
  background: #4caf50;
  transition: width 0.3s;
}

.result {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  cursor: pointer;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}
</style>