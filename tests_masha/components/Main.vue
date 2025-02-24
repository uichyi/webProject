<script setup>
  import Rectangles from './Rectangles.vue'
  import Twelve_number_test from './Twelve_number_test.vue'
  import Numbers_puzzle from './Numbers_puzzle.vue'
  import Reaction_speed from './Reaction_speed.vue'
  import Classical_Stroop_Test from './Classical_Stroop_Test.vue'
</script> 

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light mb-5">
    <div class="container-fluid">
      <a class="navbar-brand">ТЕСТЫ</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link mx-3" aria-current="page" id='Classical_Stroop_Test' @click="choose_test('Classical_Stroop_Test')">Тест на основе эффекта Струпа</a>
          </li>  
          <li class="nav-item">
            <a class="nav-link mx-3" aria-current="page" id='Rectangles' @click="choose_test('Rectangles')">Тест Струпа</a>
          </li>
          <li class="nav-item">  
            <a class="nav-link mx-3" aria-current="page" id='Numbers_puzzle' @click="choose_test('Numbers_puzzle')">Числовой пазл</a>
          </li>
          <li class="nav-item">  
            <a class="nav-link mx-3" aria-current="page" id='Reaction_speed' @click="choose_test('Reaction_speed')">Тест-тренажер на скорость реакции</a>
          </li>
          <li class="nav-item">  
            <a class="nav-link mx-3" aria-current="page" id='Twelve_number_test' @click="choose_test('Twelve_number_test')">Запоминание 12 чисел</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <Rectangles v-if='is_chosen=="Rectangles"' />
  <Twelve_number_test v-if="is_chosen=='Twelve_number_test'"/>
  <Numbers_puzzle v-if="is_chosen=='Numbers_puzzle'"/> 
  <Reaction_speed v-if="is_chosen=='Reaction_speed'"/>
  <Classical_Stroop_Test v-if="is_chosen=='Classical_Stroop_Test'"/> 
</template>
<script>
  export default {
    data() {
      return {
        is_chosen: ''
      };
    },
    methods: {
      choose_test(name){
        if(this.is_chosen!='')
          document.getElementById(this.is_chosen).classList.remove('active');
        this.is_chosen = name
        document.getElementById(name).classList.add('active');
      }
    }        
  };
</script>    