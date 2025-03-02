<template>
  <div class="memory-test" @click="handleClick">

    <div v-if="!testStarted" class="start-screen">
      <h2>Нажмите, чтобы начать тест</h2>
      <p>Это тест на краткосрочную память. Вам нужно будет отвечать на простые вопросы связанные с вашей жизнью или картинками из теста. </p>
    </div>

    <div v-else-if="currentQuestion <= totalQuestions && !testCompleted" class="test-container">
      <h2 class="question-count">Вопрос {{ currentQuestion }}/{{ totalQuestions }}</h2>

      <img :src="currentImage" alt="Вопрос о картинке" class="question-image" />
      <p>{{ currentQuestionText }}</p>

      <div class="options">
        <button
          v-for="(option, index) in currentOptions"
          :key="index"
          @click="checkAnswer(option)"
        >
          {{ option }}
        </button>
      </div>

    </div>

    <div v-if="testCompletedAndCallFunction" class="result">
      <h3>Тест завершен!</h3>
      <p>Вы правильно ответили на {{ score }} из {{ totalQuestions }} вопросов.</p>
      <button @click="restartTest">Пройти тест заново</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      testStarted: false,
      currentQuestion: 1,
      totalQuestions: 10,
      questions: [
        {
          text: "Помните какое сегодня число?",
          options: ["Да", "Нет"],
          answer: "Да",
          image: "https://trikky.ru/wp-content/blogs.dir/1/files/2024/05/11/i-23.jpeg",
        },
        {
          text: "Просто посмотрите на эту картинку.",
          options: ["Далее"],
          answer: "Далее",
          image: "https://image.jimcdn.com/app/cms/image/transf/none/path/s303186db9a6eac8a/backgroundarea/i24b4150e4347aa1f/version/1522171045/image.jpg",
        },
        {
          text: "Какое число было обведено на первой картинке?",
          options: ["3", "4", "5"],
          answer: "4",
          image: "https://pic.rutubelist.ru/video/21/62/216230a4acde4e677dc396832de6c50b.jpg",
        },
        {
          text: "Помните что Вы вчера ели на завтрак?",
          options: ["Да", "Нет"],
          answer: "Да",
          image: "https://i.pinimg.com/originals/a0/b9/03/a0b9032669a104ae3fb94fca5aace424.jpg",
        },
        {
          text: "Помните сколько у Вас двоюродных братьев и сестер?",
          options: ["Да", "Нет"],
          answer: "Да",
          image: "https://m.media-amazon.com/images/M/MV5BNTgzNGE1MTktNzAyZC00ZWYxLTljYTUtNDYxNDE1NGFiNzIzXkEyXkFqcGdeQXVyNDg4MjkzNDk@._V1_.jpg",
        },
        {
          text: "Была ли ложка на картинке с вопросом про завтрак?",
          options: ["Да", "Нет"],
          answer: "Нет",
          image: "https://pic.rutubelist.ru/video/21/62/216230a4acde4e677dc396832de6c50b.jpg",
        },
        {
          text: "Помните день рождение своего отца?",
          options: ["Да", "Нет"],
          answer: "Да",
          image: "https://sun9-40.userapi.com/impg/a2vuhBxQUt5-IGoI1i25rN9ZRgeQOcMvLJ0BhQ/7PHF_jv9A8g.jpg?size=1280x947&quality=95&sign=f87c039426a1802ea697ca8b12f41dbb&c_uniq_tag=amtE40_42hqpxK_noX4OfAJGb0z9L0gVAwBhcM",
        },
        {
          text: "Какого цвета была куртка на девушке по центру из вопроса про братьев и сестер?",
          options: ["Красная", "Зеленая", "Синяя"],
          answer: "Синяя",
          image: "https://pic.rutubelist.ru/video/21/62/216230a4acde4e677dc396832de6c50b.jpg",
        },
        {
          text: "На картинке с отцом на небе были облака?",
          options: ["Да, много", "Да, немного", "Нет"],
          answer: "Да, много",
          image: "https://pic.rutubelist.ru/video/21/62/216230a4acde4e677dc396832de6c50b.jpg",
        },
        {
          text: "Сколько бабочек было на второй картинке?",
          options: ["3", "4", "5"],
          answer: "3",
          image: "https://pic.rutubelist.ru/video/21/62/216230a4acde4e677dc396832de6c50b.jpg",
        },
      ],
      answers: [],
      options: [],
      score: 0,
      testCompleted: false,
      testId: 7
    };
  },
  computed: {
    currentQuestionText() {
      return this.questions[this.currentQuestion - 1].text;
    },
    currentOptions() {
      return this.questions[this.currentQuestion - 1].options;
    },
    currentImage() {
      return this.questions[this.currentQuestion - 1].image;
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
          "test": this.testId,
          "correct_answers": this.score,
          "time": null,
          "special_field": null
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
      }
    },
    checkAnswer(selectedOption) {
      const correctAnswer = this.questions[this.currentQuestion - 1].answer;
      if (selectedOption === correctAnswer) {
        this.score++;
      }

      if (this.currentQuestion < this.totalQuestions) {
        this.currentQuestion++;
      } else {
        this.testCompleted = true;
        this.$emit('test-complete', this.score);
      }
    },
    restartTest() {
      this.currentQuestion = 1;
      this.score = 0;
      this.testCompleted = false
      this.$emit('test-start');
    },
  },
};
</script>

<style>

.question-count{
  position: absolute;
  top: 90px;
}

.memory-test {
  height: 300px;
  max-width: 600px;
  text-align: center;
  margin-top: 100px;
}
.test-container{
  display: flex;
  flex-direction: column;
}

.question-image {
  max-width: 100%;
  margin-top: 250px;
}

.options button {
  margin: 10px;
  padding: 10px 20px;
  cursor: pointer;
}

.result {
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>