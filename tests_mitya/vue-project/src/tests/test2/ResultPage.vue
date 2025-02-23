<template>
    <div class="result-page">
      <h1>Тест завершён!</h1>
      <p>Ваш результат: {{ score }} правильных ответов из {{ answers.length }}  заданий. </p>
      <div v-if=" answers.length > 0">
        <button @click="toggleList" v-if="!showList"  >Показать результаты</button>
      <button @click="toggleList" v-else >Скрыть результаты</button>
      </div>
      <div class="result-list">
        <ol v-if="showList">
          <li v-for="(item, index) in answers" :key="index" class="result-item">
            {{ index  }}.  <p v-if="item[5] == correct" >Верно!</p>
            <p v-else >Неверно!</p> Задание: 
             <p :style="{color:  item[1]} ">{{ item[0] }}</p>
            <p :style="{color:  item[3]} ">{{ item[2] }}</p> 
            <p>Твой ответ: {{item[4] ? "Да" : "Нет"}}</p>
          </li> 
        </ol> 
      </div>
      
      <p v-if=" (score *100/answers.length) > 50 "  >Молодец!</p>
      <p v-else>Не расстраивайся! Пройди еще раз.</p>
      <button @click="resetTest">Пройти заново</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "ResultPage",
    props: ["score", "answers"],
    emits: ["reset"],
    data() {
      return {
        correct:true,
        showList:false,
      };
    },
    methods: {
      resetTest() {
        this.$emit("reset");
      },
      toggleList(){
        if (this.answers.length > 0 ) {
        this.showList = !this.showList;
        }
      }
    },
  };
  </script>
  
  <style scoped>
  .result-page {
    text-align: center;
    padding: 20px;
    counter-reset: section;
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
  /* background-color: #f0f0f0; */
  background-color: white;
  font-size: 24px;
  font-weight: bold;
  margin: 5px 0;
  padding: 8px;
  width: auto; 
  
  overflow: hidden;
  white-space: nowrap; 
  text-overflow: ellipsis; 
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.result-page ol li {
  list-style-position: inside; 
}

.game-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  gap: 20px;
  margin: 20px;
}
.word {
  font-size: 24px;
  font-weight: bold;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  min-width: 100px;
  text-align: center;
}
.buttons {
  margin-top: 20px;
}
button {
  font-size: 18px;
  margin: 10px;
  padding: 10px 20px;
}
.status {
  margin-top: 20px;
}
.game-over {
  margin-top: 30px;
}

.result-list {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
      list-style-type: none;
      padding: 0;
    }
   
    
    .result-item p {
      margin: 0;
      padding-right: 20px;
    }
    
    
    
    

</style>