<template>
    <div class="result-page">
      <h1>Тест завершён!</h1>
      <p>Ваш результат: {{ score }} правильных ответов из {{ all_expressions }} заданий. </p>
      <button @click="toggleList" v-if="!showList" >Показать результаты</button>
      <button @click="toggleList" v-else >Скрыть результаты</button>
      <button @click="resetTest">Пройти заново</button>
      <ol v-if="showList">
        <li v-for="(item, index) in expressions_answers" :key="index" :style="{ backgroundColor: item[1] ? 'green' : 'red' }" class="result-item">
          {{ item[0] }}
        </li> 
      </ol>
      
    </div>
  </template>
  
  <script>
  export default {
    name: "ResultPage",
    props: ["score", "expressions_answers", "all_expressions"],
    emits: ["reset"],
    data() {
      return {
        showList:false,
      };
    },
    methods: {
      resetTest() {
        this.$emit("reset");
      },
      toggleList(){
        this.showList = !this.showList;
      }
    },
  };
  </script>
  
  <style scoped>
  .result-page {
    text-align: center;
    padding: 20px;
  }
  button {
    margin: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  button:hover {
    background-color: #f0f0f0;
  }
  .result-item {
  background-color: #f0f0f0;
  margin: 5px 0;
  padding: 8px;
  width: auto; 
  max-width: 100px; 
  overflow: hidden;
  white-space: nowrap; 
  text-overflow: ellipsis; 
}

.result-page ol {
  margin-left: 600px;
}

.result-page ol li {
  list-style-position: inside; 
}

  </style>