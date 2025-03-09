<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Тесты</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" v-if="!isAuthenticated">
            <router-link class="nav-link" to="/login">Войти</router-link>
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <router-link class="nav-link" to="/register">Зарегистрироваться</router-link>
          </li>
          <li class="nav-item" v-if="isAuthenticated">
            <button class="nav-link btn btn-link" @click="logout">Выйти</button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

  <script>
  export default {
    name: "Navbar",
    data() {
      return {
        isAuthenticated: false,
      };
    },
    created() {
      this.checkAuthStatus();
    },
    methods: {
      checkAuthStatus() {
        // Проверяем, есть ли user_id в localStorage
        this.isAuthenticated = !!localStorage.getItem('user_id');
      },
      logout() {
        // Удаляем user_id из localStorage
        localStorage.removeItem('user_id');
        this.isAuthenticated = false;
        // Перенаправление на главную страницу или страницу входа
        this.$router.push('/');
      },
    },
  };

  </script>

  <style scoped>
  .navbar-nav {
    gap: 1rem;
  }
  /* Custom purple button styling */
  .nav-item > .btn-purple {
    background-color: #6f42c1;  /* Purple color */
    color: white;
    border: none;
  }

  .nav-item > .btn-purple:hover {
    background-color: #5a2d99;  /* Darker purple on hover */
    color: white;
  }
  </style>
