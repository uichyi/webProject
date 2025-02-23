<script setup>
import { ref, computed } from 'vue'
import test1 from './tests/test1/App.vue'
import test2 from './tests/test2/App.vue'
import test3 from './tests/test3/App.vue'
import test4 from './tests/test4/App.vue'
import test5 from './tests/test5/App.vue'

const routes = {
  '/first-test': test1,
  '/second-test': test2,
  '/third-test': test3,
  '/fourth-test': test4,
  '/fifth-test': test5,
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/first-test'] || NotFound
})
</script>

<template>
  <div id="home">
    <a href="#/first-test">Первый тест</a> |
    <a href="#/second-test">Второй тест</a> |
    <a href="#/third-test">Третий тест</a> |
    <a href="#/fourth-test">Четвертый тест</a> |
    <a href="#/fifth-test">Пятый тест</a>
    <component :is="currentView" />
  </div>
</template>


<script>
export default {
  name: "Home",
};
</script>

<style scoped>
#home {
  text-align: center;
  margin: 0 auto;
  padding: 10px;
}

#home button {
  display: block;
  margin: 0 auto;
  margin-bottom: 10px;
}
</style>