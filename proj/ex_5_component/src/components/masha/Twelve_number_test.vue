<script setup>
  import Timer_twelve_numbers from './Timer_twelve_numbers.vue'
</script>

<template>
    <h2 class='text-center mb-4'>Тест "Запоминание 12 чисел"</h2>
    <h4 v-if='time_finished != true' class='text-center'>Постарайтесь запомнить как можно больше из 12-ти чисел, которые вы видите ниже за 20 секунд.</h4>
    <h4 v-if='check == true' class='text-center'>Результат теста</h4>

    <div v-if='time_finished != true' class='d-flex justify-content-center mt-5'>
        <Timer_twelve_numbers ref="timer"/>
    </div>
    <div v-if='time_finished != true || check==true' >
        <div class='d-flex justify-content-center row'>
            <div class='col-lg-6 col-sm-12 mt-5'>
                <h5 class='text-center'>Исходная таблица</h5>
                <table class=''>
                    <tr v-for='tr in [0,4,8]'>
                        <td v-for='td in [0,1,2,3]'> <b>{{correct_data[td+tr]}}</b></td>
                    </tr>
                </table>
            </div>  
            <div v-if='check==true' class='col-lg-6 col-sm-12 mt-5'>  
                <h5 class='text-center'>Ваш ответ</h5>
                <table>
                    <tr v-for='tr in [0,4,8]'>
                        <td v-for='td in [0,1,2,3]' v-bind:id='td+tr' :style='{background: answ_color[td+tr]}'> <b>{{user_answer[td+tr]}}</b></td>
                    </tr>
                </table>
            </div>  
        </div>
        <div v-if='check==true' class='mt-4'>
            <h5>Вы смогли запомнить следующие числа:</h5>
            <h4><span v-for='ans in correct_answ.join(", ")'><b>{{ ans }}</b>  </span></h4> 
            <h5>Количество чисел c соблюдением последовательности: <b>{{corr_places_count}}</b></h5>
        </div>    
    </div>

    <h4 v-if='time_finished == true && check == false' class='text-center my-4'>Желательно разместить их в том порядке, в котором вы их видели, однако, ничего страшного, если порядок не будет соблюдён.</h4>
    <div v-if='time_finished == true && check == false' class='d-flex justify-content-center'>
        <table class='inp_table'>
            <tr v-for='tr in [0,4,8]'>
                <td v-for='td in [0,1,2,3]' style='font-size:100%'><input type='number' min=0 max=100 class='w-75 h-25' v-model='user_answer[td+tr]'/></td>
            </tr>
        </table>
    </div>
    <div class='d-flex justify-content-center'>
        <button v-if='time_finished == true && check == false' class='btn btn-primary mt-4' @click='checkAnswers'>Проверить ответы</button>
    </div>
    <p>{{checkTime}}</p>
</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                correct_data: [],
                user_answer: [],
                time_load: false,
                time_finished: false,
                check: false,
                answ_color: [],
                correct_answ: [],
                corr_places_count: 0,
                testId: 17
            };
        },
        created(){
            for (let i=0; i<12; i++){
                const num=Math.floor(Math.random()*100)
                this.correct_data.push(num)
            }
        },
        mounted(){
            this.time_load = true
        },
        computed:{
            checkTime(){
                if(this.time_load){
                    if (this.$refs.timer.timeLeftCount == 0){
                        this.time_finished = true
                        for(let i=0; i<12; i++){
                            this.user_answer.push(' ')
                            this.answ_color.push('white')
                        }
                    }   
                }
            },
            
        },
        methods: {
          async saveTestResult() {
              const testResultData = {
                'user': localStorage.getItem('user_id'),
                "test": this.testId,
                "number_correct_answers": this.correct_answ.length,
                "complete_time": 0,
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
            checkAnswers(){
               this.check = true
                for(let i=0; i<12; i++){
                    if(this.correct_data.includes(this.user_answer[i])){
                        this.correct_answ.push(this.user_answer[i])
                        this.correct_answ.sort()
                    }
                    if(this.user_answer[i] != ' ' && this.correct_data[i] == this.user_answer[i]){
                        this.answ_color[i] = '#a0e8a0'
                        this.corr_places_count++
                    }
                    else{
                        this.answ_color[i] = '#f0899d'
                    }
                }
                this.saveTestResult();
            }
        }
    }
</script>
<style scoped>
    table, th, td {
        margin-top: 30px;
        border: 2px solid #423189;
        font-size: 140%;
        text-align: center;
        margin:auto;
        color: #4B0082;
    }
    td{
        width: 120px;
        height: 140px;
    }
    h3,h5,h4 {
        color: #423189;
    }
    h2{
        color: #4B0082;
    }
</style>