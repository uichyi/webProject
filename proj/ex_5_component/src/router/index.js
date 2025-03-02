import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; // We'll create this next

// Existing imports (unchanged)
import Test1 from '../components/kostya/StartTest1.vue';
import Test2 from '../components/kostya/StartTest2.vue';
import Test3 from '../components/kostya/StartTest3.vue';
import Test4 from '../components/kostya/StartTest4.vue';
import Test5 from '../components/kostya/StartTest5.vue';
import AttentionTest from '../components/gleb/AttentionTest.vue';
import ReactionTest from '../components/gleb/ReactionTest.vue';
import MemoryTest from '../components/gleb/MemoryTest.vue';
import TextSelectionTest from '../components/gleb/TextSelectionTest.vue';
import SumDigitsTest from '../components/gleb/StartSumDigitsTest.vue';
import test1ilya from '../components/ilya/test_1_numbers/src/test1ilya.vue';
import test2ilya from '../components/ilya/test_2_unique_color/src/test2ilya.vue';
import test3ilya from '../components/ilya/test_3_extra_item/src/test3ilya.vue';
import test4ilya from '../components/ilya/test_4_clicks/src/test4ilya.vue';
import test5ilya from '../components/ilya/test_5_typing/src/test5ilya.vue';
import Rectangles from '../components/masha/Rectangles.vue';
import Twelve_number_test from '../components/masha/Twelve_number_test.vue';
import Numbers_puzzle from '../components/masha/Numbers_puzzle.vue';
import Reaction_speed from '../components/masha/Reaction_speed.vue';
import Classical_Stroop_Test from '../components/masha/Classical_Stroop_Test.vue';
import test1mitya from '../components/mitya/test1/test1mitya.vue';
import test2mitya from '../components/mitya/test2/test2mitya.vue';
import test3mitya from '../components/mitya/test3/test3mitya.vue';
import test4mitya from '../components/mitya/test4/test4mitya.vue';
import test5mitya from '../components/mitya/test5/test5mitya.vue';
import Test1k from '../components/ksysha/Test1k.vue';
import Test2k from '../components/ksysha/Test2k.vue';
import Test3k from '../components/ksysha/Test3k.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home }, // Home page route
    { path: '/test1', component: Test1 },
    { path: '/test2', component: Test2 },
    { path: '/test3', component: Test3 },
    { path: '/test4', component: Test4 },
    { path: '/test5', component: Test5 },
    { path: '/attention-test', component: AttentionTest },
    { path: '/reaction-test', component: ReactionTest },
    { path: '/memory-test', component: MemoryTest },
    { path: '/text-selection-test', component: TextSelectionTest },
    { path: '/sum-digits-test', component: SumDigitsTest },
    { path: '/test1ilya', component: test1ilya },
    { path: '/test2ilya', component: test2ilya },
    { path: '/test3ilya', component: test3ilya },
    { path: '/test4ilya', component: test4ilya },
    { path: '/test5ilya', component: test5ilya },
    { path: '/rectangles', component: Rectangles },
    { path: '/twelve-number-test', component: Twelve_number_test },
    { path: '/numbers-puzzle', component: Numbers_puzzle },
    { path: '/reaction-speed', component: Reaction_speed },
    { path: '/classical-stroop-test', component: Classical_Stroop_Test },
    { path: '/test1mitya', component: test1mitya },
    { path: '/test2mitya', component: test2mitya },
    { path: '/test3mitya', component: test3mitya },
    { path: '/test4mitya', component: test4mitya },
    { path: '/test5mitya', component: test5mitya },
    { path: '/test1k', component: Test1k },
    { path: '/test2k', component: Test2k },
    { path: '/test3k', component: Test3k },
  ],
});

export default router;