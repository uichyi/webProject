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
        answers: []
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
    },
  };
  </script>
  
  <style>
  .app {
    text-align: center;
    font-family: Arial, sans-serif;
    padding: 20px;
  }
  </style>