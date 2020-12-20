<template>
  <div class="home">
    <div class="css-1a4c3t1-Main e19xg79h1">
      <button class="btn btn-primary pull-right my-1 mx-3" @click.prevent="showPanel">
        회원가입
      </button>
      <slideout-panel></slideout-panel>
      <div class="background wallpaper eck1olp4 css-kfyg0z-Wallpaper">
        <div v-if="logined" class="css-16oxbml-WallpaperInner eck1olp7">
          <h3 class="css-c95cz3-WallpaperTitle eck1olp9">
            <span>영화 리뷰 및 추천을 무제한으로<br></span>
          </h3>
          <h4 class="css-n1qic-WallpaperSubTitle eck1olp8">매주 5백 여편의 신작이 업데이트 되며, 다양한 리뷰들이 있어요.</h4>
          <div class="css-16vrzn3-ButtonBlock eck1olp0">
            <button class="css-fhivc3-RoundedButtonLink eck1olp3" @click="handlelogin()">로그인 후 시작</button>
            <div v-show="!showlogin">
              <form @submit="login">
                <div class="login-box">
                  <div class="css-textbox">
                    <input type="text" id="username" placeholder="ID" v-model="username">
                  </div>
                  <div class="css-textbox">
                    <input type="password" id="password" placeholder="PASSWORD" v-model="password">
                  </div>
                  <button class="css-btn">로그인</button>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div v-else style="height: 10px;"> 
          <form @submit="changetoid">
            <fieldset style="position: relative;  display: inline-block;  padding: 0 0 0 40px;  background: #fff;  border: none;  border-radius: 5px;">
              <input class="search" style="color: #666;  z-index: 2;  border: 0 none; position: relative;  width: 600px;  height: 50px;  padding: 0;  display: inline-block;  float: left;" type="text" v-model="content" placeholder="영화 제목을 입력하세요.">
              <button class="searchbut" style="position: relative;  width: 100px;  height: 50px;  padding: 0;  display: inline-block;  float: left;"><i class="fa fa-search"></i></button>
            </fieldset>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Signup from '../components/Signup'
window.vue2PanelDebug = true;

export default {
  name: 'Home',
  props: {
    logined: Boolean,
  },
  data() {
    return {
      showlogin: 'true',
      showsignup: 'true',
      username: '',
      password: '',
      content: '',
      movieid: '',
      user: localStorage.getItem('username'),
    }
  },
  methods: {
    showPanel() {
      if (this.panelResult) {
        this.panelResult.show();
        return;
      }

      const panel = this.$showPanel({
        component: Signup,
        width: 500,
        cssClass: "panel-bd",
        openOn: 'right',
        props: {}
      });

      panel.promise
      .then(res => {
        console.log(res)
      });
    },
    handlelogin() {
      this.showlogin = !this.showlogin
    },
    handlesignup() {
      this.showsignup = !this.showsignup
    },
    login(event) {
      event.preventDefault()
      // axios로 서버에 로그인 요청 보낼거다!
      // 서버는 토큰을 응답으로 줄거고,
      // 나는 그 토큰을 어딘가에 저장한다(나중에 쓰려고)!
      axios({
        url:'http://127.0.0.1:8000/accounts/api-token-auth/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password,
        },
      }).then((res)=>{
        localStorage.setItem('jwt', res.data.token)
        localStorage.setItem('username', this.username)
        // App(부모)에다가 login 바꾸라고 요청
        this.$emit('login')
        this.handlelogin()
        this.$router.go(this.$router.currentRoute)
      }).catch((err)=>{
        console.error(err)
        alert('존재하지 않는 회원이거나 로그인 정보가 틀렸습니다.')
      })
    },
    logout() {
      this.$emit('logout')
    },
    getlogin() {
      this.$emit('login')
    }
  },
  created() {
  }
}
</script>

<style scoped type="text/css">
.panel-bd {
  background-color: gray;
}

.search:focus {  outline: 0 none; }

.search:focus + .searchbut {
  -webkit-transform: translate(0, 0);
      -ms-transform: translate(0, 0);
          transform: translate(0, 0);

  -webkit-transition-duration: 0.3s;
          transition-duration: 0.3s;
}

.search:focus + .searchbut .fa {
  -webkit-transform: translate(0px, 0);
      -ms-transform: translate(0px, 0);
          transform: translate(0px, 0);

  -webkit-transition-duration: 0.3s;
          transition-duration: 0.3s;
  color: #fff;
}

.searchbut {  
  z-index: 1;  width: 50px;  border: 0 none;  background: #ceb980;  cursor: pointer;  border-radius: 0 5px 5px 0;  
  -webkit-transform: translate(-50px, 0);
      -ms-transform: translate(-50px, 0);
          transform: translate(-50px, 0);

  -webkit-transition-duration: 0.3s;
          transition-duration: 0.3s;
}

.fa-search {  
  font-size: 1.4rem;  color: #29abe2;  z-index: 3;  top: 25%; 
  -webkit-transform: translate(-190px, 0); 
      -ms-transform: translate(-190px, 0);
          transform: translate(-190px, 0);

  -webkit-transition-duration: 0.3s;
          transition-duration: 0.3s;

  -webkit-transition: all 0.1s ease-in-out;
          transition: all 0.1s ease-in-out;
}

.css-urf8br-Self {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
  height: 100%;
  padding: 0px 0 0;
}
.css-1a4c3t1-Main {
  -webkit-flex: 1;
  -ms-flex: 1;
  flex: 1;
  background: #141517;
}
.css-kfyg0z-Wallpaper {
  height: 100vh;
  display: flex;
  position: relative;
  flex-direction: column;
  -webkit-box-pack: center;
  justify-content: center;
}
*, ::before, ::after {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}
.css-16oxbml-WallpaperInner {
  position: relative;
  z-index: 100;
  text-align: center;
}
.css-c95cz3-WallpaperTitle {
  color: #fff;
  font-size: 3.4722222222222223vw;
  font-weight: 400;
  -webkit-letter-spacing: -0.24305555555555555vw;
  -moz-letter-spacing: -0.24305555555555555vw;
  -ms-letter-spacing: -0.24305555555555555vw;
  letter-spacing: -0.24305555555555555vw;
  line-height: 4.375vw;
  white-space: pre-wrap;
  margin-bottom: 1.1111111111111112vw;
}
.css-n1qic-WallpaperSubTitle {
  color: #fff;
  font-size: 1.5277777777777777vw;
  font-weight: 400;
  -webkit-letter-spacing: -0.04861111111111111vw;
  -moz-letter-spacing: -0.04861111111111111vw;
  -ms-letter-spacing: -0.04861111111111111vw;
  letter-spacing: -0.04861111111111111vw;
  line-height: 2.2916666666666665vw;
  margin-bottom: 3.75vw;
  opacity: 0.65;
}
.css-16vrzn3-ButtonBlock {
  text-align: center;
}
.css-fhivc3-RoundedButtonLink {
  display: inline-block;
  background-color: #F82F62;
  color: #FFFFFF;
  font-size: 15px;
  font-weight: 700;
  -webkit-letter-spacing: -0.1px;
  -moz-letter-spacing: -0.1px;
  -ms-letter-spacing: -0.1px;
  letter-spacing: -0.1px;
  line-height: 51px;
  text-align: center;
  width: 100%;
  height: 52px;
  border-radius: 40px;
  font-size: 1.3888888888888888vw;
  font-weight: 700;
  -webkit-letter-spacing: -0.0625vw;
  -moz-letter-spacing: -0.0625vw;
  -ms-letter-spacing: -0.0625vw;
  letter-spacing: -0.0625vw;
  line-height: 4.166666666666666vw;
  width: auto;
  min-width: 13.125vw;
  height: 4.166666666666666vw;
  padding: 0 1.5625vw;
  border-radius: 2.083333333333333vw;
}
.background {
  background-image: url("https://an2-img.amz.wtchn.net/image/v1/watcha/image/upload/v1598871938/uvkdbogisjyrkec9uogn.webp");
}
.css-115xuao-StyledGnb {
  position: fixed;
  top: 0px;
  z-index: 500;
  font-size: 14px;
  -webkit-letter-spacing: -0.4px;
  -moz-letter-spacing: -0.4px;
  -ms-letter-spacing: -0.4px;
  letter-spacing: -0.4px;
  width: 100%;
  height: 72px;
  padding: 0 4%;
}
.css-nbgvz1-StyledInvisibleSubLinkList {
  position: absolute;
  bottom: 0;
  left: -3260px;
  visibility: hidden;
}
.css-q6083p-StyledLogo {
    position: relative;
    z-index: 10001;
    float: left;
    background: url('/logo.png');
    background-size: 99px 40px;
    width: 99px;
    height: 72px;
}
.css-1sjcvs8-StyledRightNav {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  position: relative;
  right: -11px;
  float: right;
}
.css-ey2scv-StyledRightNavButtonLink {
  display: inline-block;
  background-color: #121218;
  color: #FFFFFF;
  font-size: 14px;
  font-weight: 700;
  -webkit-letter-spacing: -0.4px;
  -moz-letter-spacing: -0.4px;
  -ms-letter-spacing: -0.4px;
  letter-spacing: -0.4px;
  line-height: 21px;
  width: 100%;
  padding: 10px 14px;
  border-radius: 4px;
  background: #fff;
  color: #121218;
  font-size: 13px;
  font-weight: 700;
  -webkit-letter-spacing: -0.3px;
  -moz-letter-spacing: -0.3px;
  -ms-letter-spacing: -0.3px;
  letter-spacing: -0.3px;
  padding: 5px 18px 6px;
  border-radius: 40px;
  margin: 23px 0 0;
  border:1px solid black;
}

.trans-left {
  cursor:pointer;
  animation-name: moving;
  animation-duration: 17s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}

@keyframes moving {
  0% {
transform:translate(0,0);
  }
  100% {
transform:translate(-270rem,0);
-webkit-transform:translate(-270rem,0);
  }
}

.trans-left:hover {
  animation-play-state: paused;
}

.css-textbox {
  width: 100%;
  overflow: hidden;
  font-size: 20px;
  padding: 8px 0;
  margin: 8px 0;
  border-bottom: 1px solid white;
}

.css-textbox input{
  border: none;
  outline: none;
  background: none;
  color: white;
  font-size: 18px;
  width: 80%;
  float: left;
  margin: 0 10px;
  }

.login-box{
  width: 16rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 80%);
  color: white;
}

.signup-box{
  width: 16rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 50%);
  color: white;
}
.css-textbox input::placeholder{
  color: grey;
  font-weight: 500;
}
.css-signup-btn {
  width: 70%;
  background: none;
  border: 2px solid #F82F62;
  color: white;
  padding: 5px;
  font-size: 18px;
  cursor: pointer;
  margin: 12px 0;
}
.css-btn {
  width: 100%;
  background: none;
  border: 2px solid #F82F62;
  color: white;
  padding: 5px;
  font-size: 18px;
  cursor: pointer;
  margin: 12px 0;
}
.slideout-panel-open{overflow:hidden}
.slideout-panel{display:block;transition:opacity .15s}
.slideout-panel .slideout-panel-bg{position:fixed;z-index:1000;top:0;left:0;width:100%;height:100%;background-color:rgba(0,0,0,.5);transition:opacity .3s ease;overflow-y:hidden;z-index:100}
.slideout-panel .slideout-panel-bg.transparent{background-color:transparent}
.slideout-panel .slideout-panel-bg.fadeIn-enter{opacity:0}
.slideout-panel .slideout-panel-bg.fadeIn-enter-to,.slideout-panel .slideout-panel-bg.fadeIn-leave{opacity:1}
.slideout-panel .slideout-panel-bg.fadeIn-leave-to{opacity:0}
.slideout-panel .slideout-panel-bg.fadeIn-leave-active{transition-delay:.4s}
.slideout-panel .slideout-wrapper{position:static}
.slideout-panel .slideout-wrapper .slideout{height:100%;position:fixed;top:0;bottom:0;background:#fff;transition-timing-function:cubic-bezier(.215,.61,.355,1);transition-duration:.6s;overflow-y:auto;transition-delay:.4s}
.slideout-panel .slideout-wrapper .slideout.open-on-left{right:auto;left:0}
.slideout-panel .slideout-wrapper .slideout.open-on-left.slideIn-enter{transform:translateX(-100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-left.slideIn-enter-to,.slideout-panel .slideout-wrapper .slideout.open-on-left.slideIn-leave{transform:translateX(0)}
.slideout-panel .slideout-wrapper .slideout.open-on-left.slideIn-leave-to{transform:translateX(-100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-left.slideIn-leave-active{transition-delay:0}
.slideout-panel .slideout-wrapper .slideout.open-on-top{right:0;left:0;bottom:auto;top:0}
.slideout-panel .slideout-wrapper .slideout.open-on-top.slideIn-enter{transform:translateY(-100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-top.slideIn-enter-to,.slideout-panel .slideout-wrapper .slideout.open-on-top.slideIn-leave{transform:translateY(0)}
.slideout-panel .slideout-wrapper .slideout.open-on-top.slideIn-leave-to{transform:translateY(-100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-top.slideIn-leave-active{transition-delay:0}
.slideout-panel .slideout-wrapper .slideout.open-on-bottom{right:0;left:0;bottom:0;top:auto}
.slideout-panel .slideout-wrapper .slideout.open-on-bottom.slideIn-enter{transform:translateY(100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-bottom.slideIn-enter-to,.slideout-panel .slideout-wrapper .slideout.open-on-bottom.slideIn-leave{transform:translateY(0)}
.slideout-panel .slideout-wrapper .slideout.open-on-bottom.slideIn-leave-to{transform:translateY(100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-bottom.slideIn-leave-active{transition-delay:0}
.slideout-panel .slideout-wrapper .slideout.open-on-right{right:0;left:auto}
.slideout-panel .slideout-wrapper .slideout.open-on-right.slideIn-enter{transform:translateX(100%)}
.slideout-panel .slideout-wrapper .slideout.open-on-right.slideIn-enter-to,.slideout-panel .slideout-wrapper .slideout.open-on-right.slideIn-leave{transform:translateX(0)}
.slideout-panel .slideout-wrapper .slideout.open-on-right.slideIn-leave-to{transform:translateX(100%)}
</style>