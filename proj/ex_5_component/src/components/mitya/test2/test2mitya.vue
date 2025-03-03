<template>
    <div id="app" class="app">
      <StartPage v-if="!isTesting && !isFinished" @start="startTest" />
      <TestPage
        v-if="isTesting"
        :firstWordColor="firstWordColor"
        :secondWordColor="secondWordColor"
        :firstWord="firstWord"
        :secondWord="secondWord"
        :timer="timer"
        @answer="checkAnswer"
      />
      <ResultPage v-if="isFinished" :score="score" :answers="answers" @reset="resetTest" />
    </div>
  </template>
  
  <script>
  import StartPage from "./StartPage.vue";
  import TestPage from "./TestPage.vue";
  import ResultPage from "./ResultPage.vue";
  import axios from "axios";
  
  export default {
    name: "App",
    components: {
      StartPage,
      TestPage,
      ResultPage,
    },
    data() {
      return { 
        isTesting: false, 
        isFinished: false, 
        firstWord: '',
        secondWord: '',
        firstWordColor: '',
        secondWordColor: '',
        colors: ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink', 'black'],
        words: ['красный', 'синий', 'зелёный', 'жёлтый', 'фиолетовый', 'оранжевый', 'коричневый', 'розовый', 'черный'],
        score: 0,
        timer: 10,
        interval: null,
        gameOver: false,
        answers: [],
        testId: 22
      };
    },
    methods: {
      generateTask() {
      const randomIndex1 = Math.floor(Math.random() * this.colors.length);
      const randomIndex2 = Math.floor(Math.random() * this.colors.length);

      this.firstWord = this.words[randomIndex1];
      this.firstWordColor = this.colors[randomIndex1];
      this.secondWord = this.words[randomIndex2];
      this.secondWordColor = this.colors[Math.floor(Math.random() * this.colors.length)];
    },
      startTest() {
        this.generateTask();
        this.timer = 10;
        this.score = 0;
        this.gameOver = false;
        this.answers = [],
        this.isTesting = true;
        this.isFinished = false;

        this.interval = setInterval(() => {
            this.timer--;
            if (this.timer <= 0) {
                clearInterval(this.interval);
                this.gameOver = true;
                this.isTesting = false;
                this.isFinished = true;
                this.saveTestResult()
            }
        }, 1000);
      },
      checkAnswer(isYes) {
      if (this.gameOver) return;
      const checkcolor = this.words.indexOf(this.firstWord);
      const colorofword = this.colors[checkcolor];
      const isCorrect =
        (colorofword === this.secondWordColor && isYes) ||
        (colorofword !== this.secondWordColor && !isYes);

      if (isCorrect) {
        this.score++;
      }
      this.answers.push([this.firstWord, this.firstWordColor, this.secondWord, this.secondWordColor, isYes, isCorrect])
      this.generateTask();
    },
      resetTest() {
        this.isTesting = false;
        this.isFinished = false;
        this.timeLeft = 60;
        this.score = 0;
        this.answers = [];
        
      },
      async saveTestResult() {
        const testResultData = {
          'user': localStorage.getItem('user_id'),
          "test": this.testId,
          "number_correct_answers": this.score,
          "number_all_answers": this.answers.length,
          "complete_time": 10,
          "accuracy": this.score / this.answers.length // Количество неправильных
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
      },
    },
  };
  </script>
  
  <style scoped>
  .app {
    text-align: center;
    font-family: Arial, sans-serif;
    padding: 20px;

    height: 100vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
  }
  </style>