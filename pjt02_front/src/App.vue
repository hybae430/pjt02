<template>
  <div id="app">
    <router-view @logout="logout" @login="setLogin" :logined="logined"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      logined: false,
    }
  },
  methods: {
    setLogin() {
      this.logined = true
    },
    logout() {
      this.logined = false
      localStorage.removeItem('jwt')
      this.$router.push('/')
    },
    giveitem(data) {
      this.item = data
    }
  },
  created() {
    if (localStorage.getItem('jwt')) {
      this.logined = true
    }
  },
}
</script>

<style>
#app {
  font-family: Monaco, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.panel-1 {
  padding: 20px;
}
</style>
