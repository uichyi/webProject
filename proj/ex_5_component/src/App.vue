<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Общие стили для всего проекта */
body {
  font-family: 'Inter', sans-serif; /* Современный шрифт, можно заменить на другой */
  background: #f7f7fa; /* Мягкий серый фон */
  color: #1a1a1a;
  margin: 0;
  padding: 0;
}

h1, h2, h3 {
  font-weight: 700;
  color: #1a1a1a;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 32px;
}

h2 {
  font-size: 2rem;
}

p {
  font-size: 1rem;
  color: #666;
  line-height: 1.5;
}

.btn-modern {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, #6b48ff 0%, #8a3ffc 100%);
  color: #fff;
  font-weight: 600;
  text-decoration: none;
  border-radius: 8px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.btn-modern:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(107, 72, 255, 0.3);
  color: #fff;
}

.card {
  background: #ffffff;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  transition: box-shadow 0.3s ease;
}

.card:hover {
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
}
</style>