<script setup>
  import Timer from './Timer.vue'
</script>
<template>
  <div class="text-center">
    <h2>Тест на основе эффекта Струпа</h2>
    <h5>Как можно скорее выберите из списка слов те слова, цвет которых совпадает с названием. </h5>
    <h5>Время на выполнение теста 1 минута</h5>
    <button @click="start_test" v-if='is_started==false && is_finished==false' class='btn btn-primary mt-3'>Начать тест</button>
  </div>
  <div v-if='is_finished' class='d-flex justify-content-center'>
    <div class="card mt-5 w-75">
      <div class="card-header text-center">
        <h4>Результат теста</h4>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"><h5><b>Время прохождения:</b> {{this.$refs.timer.timeUsed}} сек.</h5></li>
        <li class="list-group-item"><h5><b>Количество правильных выделенных цветов: </b>{{ find_corr_answ }}</h5></li>
        <li class="list-group-item"><h5><b>Количество ошибочно выделенных цветов: </b> {{ find_bad_answ }}</h5></li>
        <li class="list-group-item"><h5><b>Количество пропущенных цветов: </b> {{ count_corr_answ - find_corr_answ }} </h5></li>
        <li class="list-group-item"><h5><b>Количество совпадений:</b> {{ 30 - (count_corr_answ - find_corr_answ) - find_bad_answ  }}</h5></li>
      </ul>
    </div>
  </div> 
  <div v-if='is_finished' class='text-center'><button @click="start_test" class='btn btn-primary mt-3'>Начать заново</button></div> 
  <div class="text-center my-4"> 
    <Timer ref="timer" v-show="is_started"/>
    <div class="list">
      <div v-for="(dat, index) in data"
        :key="index"
        :id = "index"
        :style="{
          color: dat[2],
          width: '150px',
          height: '150px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          marginRight: '3%',
          marginLeft:'3%',
          marginTop:'1%',
          cursor: 'pointer',
          fontSize: '140%',
        }" @click='chooseCell(index)'>{{ dat[0] }}</div>
    </div>    
    
    <button v-if='is_started' @click="check_answ" class="btn btn-success">Готово</button>
    {{ check_time }}
  </div>  
</template>

<script>
export default {
  components: {
    Timer
  },
  data() {
    return {
      names: [['Зеленый','green'], ['Красный', 'red'], ['Жёлтый','yellow'], ['Синий','blue'], ['Фиолетовый','purple'],
      ['Черный','black'], ['Коричневый','brown'], ['Оранжевый','orange']],
      colors:['green', 'red','yellow','blue', 'purple','black','brown','orange'],
      data:[],
      count_corr_answ: 0,
      user_answs: [], 
      is_started: false,
      is_finished: false,
      find_corr_answ: 0,
      find_bad_answ: 0,
      time_load: false
    };
  },
  mounted(){
    this.time_load = true
  },
  computed:{
    check_time(){
      if(this.time_load){
        if(this.$refs.timer.timeLeftCount == 0 && this.is_started){
          this.check_answ()
        }
      }
    },
  },

  methods: {
    start_test(){
      this.is_started = true
      this.is_finished = false
      this.data=[]
      this.user_answs = []
      this.count_corr_answ = 0
      this.find_corr_answ = 0
      this.find_bad_answ = 0
      this.$refs.timer.resetTimer(60)

      for (let i=0; i<30; i++){
        if(document.getElementById(i)){
          document.getElementById(i).style.border = 'none'
        }
        const j = Math.floor(Math.random()*(this.names.length));
        const k = Math.floor(Math.random()*(this.colors.length));
        this.data.push([this.names[j][0], this.names[j][1], this.colors[k]])
        if (this.names[j][1] == this.colors[k]){
          this.count_corr_answ+=1
        }
      }
    },
    chooseCell(id){
      if(this.is_finished == false){
        if(this.user_answs.includes(id)){
          document.getElementById(id).style.border = 'none'
          this.user_answs.splice(this.user_answs.indexOf(id), 1)
        }
        else{
          document.getElementById(id).style.border = '5px solid #423189'
          this.user_answs.push(id)
        }
      }
    },
    check_answ(){
      this.is_started = false
      this.is_finished = true
      this.$refs.timer.stopTimer()
      for (let i=0; i<this.data.length; i++){
        if(this.data[i][1]==this.data[i][2]){
          if(this.user_answs.includes(i)){
            document.getElementById(i).style.border = '5px solid green'
            this.find_corr_answ++
          }
          else{
            document.getElementById(i).style.border = '5px solid yellow'
          }
        }
        else{
          if (this.user_answs.includes(i)){
            document.getElementById(i).style.border = '5px solid red'
            this.find_bad_answ+=1
          }
        }
      }
    }
  }
    
};



</script>

<style scoped>
  h2, h4{
    color: #4B0082;
  }
  h5{
    color: #9966CC;
    margin-top: 4px;
    margin-bottom: 4px;
  }
  .list{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>