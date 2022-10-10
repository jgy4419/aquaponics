<template>
  <Menu/>
  <router-view></router-view>
</template>

<script>
import Menu from './components/Header.vue'

export default {
  name  : 'App',
  mounted(){
    window.addEventListener('scroll', () => {
      
    })
  },
  components: {
    Menu,
  }
}
</script>

<style lang="scss">
.titleBox{
  .box{
      position: absolute;
      width: 50px;
      height: 50px;
      background-color: #E5E3C9;
      // transform: rotate(45deg);
  }
  .greenTitle{
      position: relative;
      top: 10px;
      margin-left: 20px;
      color: #94B49F;
      font-size: 50px;
      font-weight: 700;
  }
  @media screen and (max-width: 900px){
    .greenTitle{
      font-size: 35px;
    }   
  }
}
.btn{
  background-color: #B4CFB0;
  color: #fcf3f3;
  font-weight: 900;
  box-sizing:content-box;
  border: 0px;
  transition: .3s;
  cursor: pointer;
}
.btn:hover{
  background-color: #94B49F;
  color: #fff;
}
</style>

