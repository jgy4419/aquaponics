<template>
  <Header/>
  <router-view></router-view>
</template>

<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header,
  }
}
</script>

<style lang="scss">
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

