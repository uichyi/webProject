<script setup>
  import Timer from './Timer.vue'
</script>
<template>
    <h2 class='text-center mb-4'>Тест "Числовой пазл"</h2>
    <div v-if='is_started == false' class='mx-5'>
        <h3 class='my-4'>Правила прохождения теста:</h3>
        <div>
            <h5>1. Нажимайте на ячейку в первом блоке куда хотите поставить число из второго блока</h5>
            <h5>2. Затем нажимайте на выбранное число из второго блока</h5>
            <h5>3. Это число переносится в первый блок и отмечается определенным цветом:</h5>
            <li class='my-1'><span style='background:#77d496'>Число находится в своей ячейке</span></li>
            <li class='my-1'><span style='background:#ffff7a'>Число находится не в своей ячейке. Это число присутствует либо в ряду, либо в колонке открытой ячейки</span></li>
            <li class='my-1'><span style='background:#ff4c5b'>Число находится не в своей ячейке. Этого числа нет ни в ряду, ни в колонке открытой ячейки</span></li>
        </div>
        <div>
            <button class='btn btn-primary mt-3 text-center' @click='startTest'>Начать</button>
        </div>
    </div>

    <Timer ref='timerPuzzle' class='text-center' v-show='is_started==true && is_finished==false'/>
    
    <div class='d-flex justify-content-center row' v-if='is_finished == false && is_started'>
        <div class='col-lg-6 col-sm-12 mt-5'>
            <table>
                <tr v-for='tr in [0,3,6]'>
                    <td v-for='td in [1,2,3]' :id='td+tr' @click='chooseCell(td+tr)'></td>
                </tr>    
            </table>
        </div>
        <div class='col-lg-6 col-sm-12 mt-5'>
            <table>
                <tr v-for='tr in [0,3,6]'>
                    <td v-for='td in [1,2,3]' :id='`id_${td+tr}`'  @click='chooseNumber(td+tr)'> <b>{{td+tr}}</b></td>
                </tr>    
            </table>
        </div>    
    </div>    
    <div v-if='is_finished' class="card" style="width: 50rem; margin:auto;">
        <div class="card-header text-center" style = 'background:#d5cede;'>
            <h3>Результат теста</h3>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item"><h5>Время выполнения: <b>{{$refs.timerPuzzle.timeUsedCount}}</b></h5></li>
            <li class="list-group-item"><h5>Количество верно расставленных квадратов: <b>{{guessed_nums.length}} / 9 </b></h5></li>
            <li class="list-group-item"><h5>Количество ошибок: <b>{{error_number}}</b></h5></li>
        </ul>
    </div>
    <div class='d-flex justify-content-center'>
        <button v-if='is_finished && level<3' class='btn btn-primary my-3' @click='nextLevel'>Продолжить</button>
    </div>
    <p v-if='time_load'>{{final}}</p>
</template>
<script>
    export default {
        components(){
            Timer
        },
        data() {
            return {
                hidden_numbers: [1,2,3,4,5,6,7,8,9],
                chosen_ceil_id: -1,
                guessed_nums: [],
                time_load: false,
                error_number: 0,
                is_finished: false,
                is_started: false,
                level: 1,
                time_levels: [80, 50, 30]
            };    
        },
        mounted(){
            this.time_load = true;
        },
        computed:{
            final(){
                console.log(this.hidden_numbers)
                if (this.guessed_nums.length == 9){
                    this.$refs.timerPuzzle.stopTimer()
                    this.is_finished = true
                }
               
                if (this.$refs.timerPuzzle.timeLeft == 0 && this.is_started){
                    this.is_finished = true
                }
                
            }            
        },
        methods: {
            startTest(){
                this.is_started = true;
                this.$refs.timerPuzzle.resetTimer(this.time_levels[this.level-1])
                this.hidden_numbers.sort(function(){ return 0.5-Math.random() });
            },
            nextLevel(){
                if (this.level<3){
                    this.level++
                    this.is_finished = false
                    this.error_number = 0
                    this.guessed_nums=[]
                    this.$refs.timerPuzzle.resetTimer(this.time_levels[this.level-1])
                    this.hidden_numbers.sort(function(){ return 0.5-Math.random() });
                }
            },
            chooseCell(id){
                if (this.chosen_ceil_id == -1 && this.guessed_nums.includes(this.hidden_numbers[id-1]) == false){
                    document.getElementById(id).style.border = '5px solid #423189'
                    this.chosen_ceil_id = id
                }    
            },
            chooseNumber(num){
                if (this.chosen_ceil_id != -1 && this.guessed_nums.includes(num) == false){
                    document.getElementById(this.chosen_ceil_id).innerHTML = num
                    document.getElementById(this.chosen_ceil_id).style.border = '1px solid #423189'
                    if(num == this.hidden_numbers[this.chosen_ceil_id-1]){
                        document.getElementById(this.chosen_ceil_id).style.background = '#77d496'
                        document.getElementById('id_'+num).style.background = '#d1d5de'
                        this.guessed_nums.push(num)
                    }
                    else if((this.chosen_ceil_id-1)%3 == this.hidden_numbers.indexOf(num)%3 ||
                    Math.floor((this.chosen_ceil_id-1)/3) == Math.floor(this.hidden_numbers.indexOf(num)/3)){
                        document.getElementById(this.chosen_ceil_id).style.background = '#ffff7a'
                    }
                    else{
                        document.getElementById(this.chosen_ceil_id).style.background = '#ff4c5b'
                        this.error_number++
                    }
                    this.chosen_ceil_id = -1
                }
            },
            
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