<template>
  <div>
    <form @submit="signup">
        <input type="text" id="username" placeholder="아이디를 입력해주세요." v-model="username">
        <input type="text" id="email" placeholder="이메일을 입력해주세요." v-model="email">
        <input type="password" id="password" placeholder="비밀번호를 입력해주세요." v-model="password">
        <input 
        type="password" 
        id="passwordConfirmation" 
        v-model="passwordConfirmation"
        placeholder="비밀번호 확인"
        >
        <hr>
        <button class="btn btn-primary">Signup</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  methods: {
    data() {
      return {
        username: '',
        password: '',
        passwordConfirmation: '',
        email: '',
      }
    },
    closePanel() {
      this.$emit("closePanel", {});
    },
    signup(event) {
      event.preventDefault()
      // password, passwordConfirmation
      if (this.password !== this.passwordConfirmation){
        alert('비밀번호가 일치하지 않습니다!')
      }else{
        // 서버에 회원가입 요청!
        axios({
          url:'http://127.0.0.1:8000/accounts/signup/',
          method: 'POST',
          data: {
            username: this.username,
            password: this.password,
          },
        }).then((res)=>{
          console.log(res.data)
          this.$router.push('/')
          this.handlesignup()
          alert('가입되었습니다!')
        }).catch((err)=>{
          console.error(err)
          alert('동일한 id가 존재합니다.')
        })
      }
    },
  }
}
</script>

<style>

</style>