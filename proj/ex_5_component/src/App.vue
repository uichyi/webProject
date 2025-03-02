<template>
  <div v-if="false">
    <!--<Log_in/>-->
    <!--<Sign_up/>-->
    <!--<User_information/>-->
  </div>
  <div v-else>
    <div id="app" class="container mt-5 text-center">
      <h1 class="mb-4">Тесты</h1>

      <!-- Layout with arrows and game -->
      <div class="d-flex align-items-center justify-content-center mb-4">
        
        <!-- Left Arrow (Fixed to the left of the screen) -->
        <div class="arrow-left-container">
          <svg 
            @click="navigateTest('left')" 
            xmlns="http://www.w3.org/2000/svg" 
            width="40" 
            height="40" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            stroke-width="2" 
            stroke-linecap="round" 
            stroke-linejoin="round" 
            class="text-primary arrow-icon" 
            :class="{'disabled-arrow': currentGame <= 0}"
            style="cursor: pointer;">
            <path d="M15 18l-6-6 6-6"></path>
          </svg>
        </div>

        <!-- Game -->
        <div class="mx-4">
          <p>Текущий тест: {{ currentGame + 1 }} из {{ tests.length }} ({{ selectedApp }})</p>

          <div v-if="selectedGame">
            <!-- Test Components -->
            <div v-if="selectedApp == 'test1'">
              <Test1 />
            </div>
            <div v-else-if="selectedApp == 'test2'">
              <Test2 />
            </div>
            <div v-else-if="selectedApp == 'test3'">
              <Test3 />
            </div>
            <div v-else-if="selectedApp == 'test4'">
              <Test4 />
            </div>
            <div v-else-if="selectedApp == 'test5'">
              <Test5 />
            </div>
            <div v-else-if="selectedApp == 'test6'">
              <AttentionTest />
            </div>
            <div v-else-if="selectedApp == 'test7'">
              <ReactionTest />
            </div>
            <div v-else-if="selectedApp == 'test8'">
              <MemoryTest />
            </div>
            <div v-else-if="selectedApp == 'test9'">
              <TextSelectionTest />
            </div>
            <div v-else-if="selectedApp == 'test10'">
              <SumDigitsTest />
            </div>
            <div v-else-if="selectedApp == 'test11'">
              <test1ilya />
            </div>
            <div v-else-if="selectedApp == 'test12'">
              <test2ilya />
            </div>
            <div v-else-if="selectedApp == 'test13'">
              <test3ilya />
            </div>
            <div v-else-if="selectedApp == 'test14'">
              <test4ilya />
            </div>
            <div v-else-if="selectedApp == 'test15'">
              <test5ilya />
            </div>
            <div v-else-if="selectedApp == 'test16'">
              <Rectangles />
            </div>
            <div v-else-if="selectedApp == 'test17'">
              <Twelve_number_test />
            </div>
            <div v-else-if="selectedApp == 'test18'">
              <Numbers_puzzle />
            </div>
            <div v-else-if="selectedApp == 'test19'">
              <Reaction_speed />
            </div>
            <div v-else-if="selectedApp == 'test20'">
              <Classical_Stroop_Test />
            </div>
            <div v-else-if="selectedApp == 'test21'">
              <test1mitya />
            </div>
            <div v-else-if="selectedApp == 'test22'">
              <test2mitya />
            </div>
            <div v-else-if="selectedApp == 'test23'">
              <test3mitya />
            </div>
            <div v-else-if="selectedApp == 'test24'">
              <test4mitya />
            </div>
            <div v-else-if="selectedApp == 'test25'">
              <test5mitya />
            </div>
            <div v-else-if="selectedApp == 'test26'">
              <Test1k />
            </div>
            <div v-else-if="selectedApp == 'test27'">
              <Test2k />
            </div>
            <div v-else-if="selectedApp == 'test28'">
              <Test3k />
            </div>
          </div>

          <div v-else-if="!selectedGame">
            <div v-if="selectedApp == 'test1'">
              <p>Перед вами набор эмодзи, в котором одинаковые только <b>два.</b> Найдите как можно больше пар таких эмодзи за минуту</p>
            </div>
            <div v-else-if="selectedApp == 'test2'">
              <p>Перед вами стрелка, которая смотрит вверх/вниз/влево/вправо и либо красный фон, либо синий. Вам необходимо за минуту определить как можно больше раз путь стрелки...</p>
            </div>
            <!-- Additional descriptions for other tests -->
            <button class="btn btn-primary" @click="startGame()">Начать игру</button>
          </div>
        </div>

        <!-- Right Arrow (Fixed to the right of the screen) -->
        <div class="arrow-right-container">
          <svg 
            @click="navigateTest('right')" 
            xmlns="http://www.w3.org/2000/svg" 
            width="40" 
            height="40" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="currentColor" 
            stroke-width="2" 
            stroke-linecap="round" 
            stroke-linejoin="round" 
            class="text-primary arrow-icon" 
            :class="{'disabled-arrow': currentGame >= tests.length - 1}"
            style="cursor: pointer;">
            <path d="M9 18l6-6-6-6"></path>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Test1 from './components/kostya/Test1.vue';
import Test2 from './components/kostya/Test2.vue';
import Test3 from './components/kostya/Test3.vue';
import Test4 from './components/kostya/Test4.vue';
import Test5 from './components/kostya/Test5.vue';

import AttentionTest from './components/gleb/AttentionTest.vue';
import ReactionTest from './components/gleb/ReactionTest.vue';
import MemoryTest from './components/gleb/MemoryTest.vue';
import TextSelectionTest from './components/gleb/TextSelectionTest.vue';
import SumDigitsTest from './components/gleb/SumDigitsTest.vue';

import test1ilya from './components/ilya/test_1_numbers/src/test1ilya.vue';
import test2ilya from './components/ilya/test_2_unique_color/src/test2ilya.vue';
import test3ilya from './components/ilya/test_3_extra_item/src/test3ilya.vue';
import test4ilya from './components/ilya/test_4_clicks/src/test4ilya.vue';
import test5ilya from './components/ilya/test_5_typing/src/test5ilya.vue';

import Rectangles from './components/masha/Rectangles.vue';
import Twelve_number_test from './components/masha/Twelve_number_test.vue';
import Numbers_puzzle from './components/masha/Numbers_puzzle.vue';
import Reaction_speed from './components/masha/Reaction_speed.vue';
import Classical_Stroop_Test from './components/masha/Classical_Stroop_Test.vue';

import test1mitya from './components/mitya/test1/test1mitya.vue';
import test2mitya from './components/mitya/test2/test2mitya.vue';
import test3mitya from './components/mitya/test3/test3mitya.vue';
import test4mitya from './components/mitya/test4/test4mitya.vue';
import test5mitya from './components/mitya/test5/test5mitya.vue';

import Test1k from './components/ksysha/Test1k.vue';
import Test2k from './components/ksysha/Test2k.vue';
import Test3k from './components/ksysha/Test3k.vue';

export default {
  components: {
    Test1,
    Test2,
    Test3,
    Test4,
    Test5,
    AttentionTest,
    ReactionTest,
    MemoryTest,
    TextSelectionTest,
    SumDigitsTest,
    test1ilya,
    test2ilya,
    test3ilya,
    test4ilya,
    test5ilya,
    Rectangles,
    Twelve_number_test,
    Numbers_puzzle,
    Reaction_speed,
    Classical_Stroop_Test,
    test1mitya,
    test2mitya,
    test3mitya,
    test4mitya,
    test5mitya,
    Test1k,
    Test2k,
    Test3k
  },
  data() {
    return {
      tests: [
        'test1', 'test2', 'test3', 'test4', 'test5',
        'test6', 'test7', 'test8', 'test9', 'test10',
        'test11', 'test12', 'test13', 'test14', 'test15',
        'test16', 'test17', 'test18', 'test19', 'test20',
        'test21', 'test22', 'test23', 'test24', 'test25',
        'test26', 'test27', 'test28',
      ],
      selectedApp: 'test1',
      selectedGame: false,
      currentGame: 0, // Initialize counter
    };
  },
  methods: {
    selectApp(app) {
      this.selectedApp = app;
      this.selectedGame = false;
    },
    startGame() {
      this.selectedGame = true;
    },
    navigateTest(direction) {
      if (direction === 'left' && this.currentGame > 0) {
        this.currentGame--;
      } else if (direction === 'right' && this.currentGame < this.tests.length - 1) {
        this.currentGame++;
      }
      this.selectedApp = this.tests[this.currentGame]; // Update the selected test based on currentGame index
      this.selectedGame = false;
    }
  }
};
</script>

<style scoped>
.arrow-left-container, .arrow-right-container {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}

.arrow-left-container {
  left: 0;
  padding: 10px;
  border-radius: 50%;
}

.arrow-right-container {
  right: 0;
  padding: 10px;
  border-radius: 50%;
}

.arrow-icon {
  width: 40px;
  height: 40px;
}

.disabled-arrow {
  opacity: 0.3;
  pointer-events: none;
}
</style>
