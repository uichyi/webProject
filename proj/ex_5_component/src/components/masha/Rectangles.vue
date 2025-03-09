
<script setup>
  import Timer from './Timer.vue'
</script>
<template>
  <div class="wrapper">
    <h2 class='text-center mb-4'>Тест Струпа</h2>
    <h4 v-if='is_finished == false' class='text-center'>Задание: найдите все квадраты, у которых цвет и надпись (название цвета) совпадают.</h4>
    <div v-if='is_finished == false' id='content'>
      <div class='text_container my-5'>
        <Timer ref="timer"/>
        <h5><b>Осталось найти:</b> {{correct_answ}}</h5>
        <h5><b>Уровень:</b> {{level}}</h5>
      </div>
        <p>{{next}}</p>
        <p>{{final}}</p>
        <div class="rectangles">
          <div
            v-for="(rectangle, index) in rectangles"
            :key="index"
            :id = "index"
            :style="{
              backgroundColor: rectangle.color,
              color: 'white',
              width: '100px',
              height: '100px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              margin: '10px',
              cursor: 'pointer'
            }"
            @click="checkMatch(rectangle, index)"
          >
            {{ rectangle.text }}
          </div>
    
      </div>
    </div>
    <div v-if='testCompletedAndCallFunction' class="card">
      <div class="card-header text-center">
        <h3>Результат теста</h3>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"><h5><b>Время прохождения:</b> {{ this.$refs.timer.timeUsedCount}} сек.</h5></li>
        <li class="list-group-item"><h5><b>Количество правильных ответов:</b> {{given_correct_answ}} / {{number_of_all_correct_answ}}</h5></li>
        <li class="list-group-item"><h5><b>Количество ошибок:</b> {{errors}} </h5></li>
      </ul>
    </div>
  </div>
  
</template>

<script>
import axios from "axios";

export default {
  components: {
    Timer
  },
  data() {
    return {
      origins:[{ color: 'blue', textColor: 'blue', text: 'Синий' },
        { color: 'red', textColor: 'red', text: 'Красный' },
        { color: 'green', textColor: 'yellow', text: 'Желтый' },
        { color: 'yellow', textColor: 'green', text: 'Зеленый' },
        { color: 'black', textColor: 'black', text: 'Черный' },
        { color: 'red', textColor: 'blue', text: 'Синий' },
        { color: 'blue', textColor: 'red', text: 'Красный' },
        { color: 'black', textColor: 'purple', text: 'Фиолетовый' },
        { color: 'yellow', textColor: 'black', text: 'Черный' },
        { color: 'orange', textColor: 'orange', text: 'Оранжевый' },
        { color: 'blue', textColor: 'white', text: 'Белый' },
        { color: 'pink', textColor: 'red', text: 'Красный' },
        { color: 'yellow', textColor: 'yellow', text: 'Желтый' },
        { color: 'yellow', textColor: 'green', text: 'Зеленый' },
        { color: 'purple', textColor: 'orange', text: 'Оранжевый' },
        { color: 'blue', textColor: 'blue', text: 'Синий' },
        { color: 'red', textColor: 'red', text: 'Красный' },
        { color: 'green', textColor: 'yellow', text: 'Желтый' },
        { color: 'yellow', textColor: 'green', text: 'Зеленый' },
        { color: 'purple', textColor: 'black', text: 'Черный' },
        { color: 'pink', textColor: 'pink', text: 'Розовый' },
        { color: 'blue', textColor: 'blue', text: 'Синий' },
        { color: 'purple', textColor: 'purple', text: 'Фиолетовый' },
        { color: 'red', textColor: 'yellow', text: 'Желтый' },
        { color: 'green', textColor: 'green', text: 'Зеленый' },
        { color: 'pink', textColor: 'black', text: 'Черный' }],
      matchCount: 0,
      errors: 0,
      correct_answ: 2,
      rectangles: [{ color: 'blue', textColor: 'blue', text: 'Синий' },
        { color: 'green', textColor: 'yellow', text: 'Желтый' },
        { color: 'red', textColor: 'red', text: 'Красный' },
        { color: 'yellow', textColor: 'green', text: 'Зеленый' },
        { color: 'purple', textColor: 'black', text: 'Черный' }
      ],
      hidden:[],
      error_divs:[],
      level:1,
      number_of_levels:5,
      number_of_all_correct_answ:2,
      given_correct_answ: 0,
      time_load: false,
      is_finished: false,
      testId: 16
    };
  },
  mounted(){
    this.time_load = true
  },
  computed:{
    testCompletedAndCallFunction() {
      if (this.is_finished) {
        this.saveTestResult();
        return true;
      } else {
        return false;
      }
    },
    next(){
      if (this.correct_answ == 0 && this.level<this.number_of_levels){
        this.level++
        for (let i=0; i<this.hidden.length; i++){
          const rec = document.getElementById(this.hidden[i])
          rec.style.visibility='visible'
        }
        for (let i=0; i<this.error_divs.length; i++){
          const rec = document.getElementById(this.error_divs[i])
          rec.style.border='none'
          rec.style.opacity = '1'
        }

        this.rectangles=[]
  
        for (let i=0;i<this.level*5;i++){
          const j=Math.floor(Math.random()*(this.origins.length));
          this.rectangles.push(this.origins[j])
          if (this.origins[j].color == this.origins[j].textColor){
            this.correct_answ+=1
          }
        }
        this.number_of_all_correct_answ+=this.correct_answ
      }
      else if(this.correct_answ == 0 && this.level==this.number_of_levels)
        this.level++
    },
    final(){
      if (this.level==this.number_of_levels+1){
        this.$refs.timer.stopTimer()
        this.is_finished = true
      }
      if (this.time_load){
        if (this.$refs.timer.timeLeftCount == 0){
            this.is_finished = true
            if (this.level < this.number_of_levels){
              for (let lev=this.level+1; lev<this.number_of_levels+1; lev++){
                for (let i=0;i<lev*5;i++){
                  const j=Math.floor(Math.random()*(this.origins.length));
                  if (this.origins[j].color == this.origins[j].textColor){
                    this.number_of_all_correct_answ+=1
                  }
                }
                        
              }    
            }
        }
      }
        
    }
  },
  methods: {
    async saveTestResult() {
      const testResultData = {
        'user': localStorage.getItem('user_id'),
        "test": this.testId,
        "number_correct_answers": this.given_correct_answ,
        "number_all_answers": this.given_correct_answ + this.errors,
        "complete_time": this.$refs.timer.timeUsedCount,
        "accuracy": Number(((this.given_correct_answ + this.errors) / this.number_of_all_correct_answ).toFixed(2))
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
    checkMatch(rectangle, index) {
      if (rectangle.color === rectangle.textColor) {
        this.matchCount++;
        // this.rectangles.splice(index,1);
        const rec = document.getElementById(index)
        rec.style.visibility = 'hidden'
        this.correct_answ--
        this.hidden.push(index)
        this.given_correct_answ++
      }
      else{
        const rec = document.getElementById(index)
        if (rec.style.opacity != '0.5'){  
          this.error_divs.push(index)  
          rec.style.border='3px solid red'
          rec.style.opacity = '0.5'
          this.errors++
        }

      }
    },
  },

};



</script>

<style scoped>
  .wrapper {
    /* height: 100vh; */
    display: flex;
    justify-content: center;
    flex-direction: column;
  }

  .rectangles {
    display: flex;
    flex-wrap: wrap;
    margin-left: 25%;
    margin-right: 25%;
  }
  h5{
    color: #9966CC;
    margin-top: 4px;
    margin-bottom: 4px;
  }
  h2{
    color: #423189;
  }
  h3{
    color: #423189;
  }
  .text_container{
    margin:auto;
  }
  #content{
    align-content: center;
  }
  .text_container{
    margin-left: 25%;
    margin-right: 25%;
  }
</style>