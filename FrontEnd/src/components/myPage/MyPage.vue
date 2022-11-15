<template>
    <div class="contain">
        <Section1 class="section1" :introduction="introduction"/>
        <Section2 class="section2"/>
    </div>
</template>

<script>
import Section1 from './MyPageSection1.vue'
import Section2 from './MyPageSection2.vue'

// import axios from 'axios';
export default {
    components: {
        Section1,
        Section2,
    },
    data(){
        return{
            introduction: {
                names: '아쿠',
                intro: '안녕하세요 저는 아쿠 입니다.',   
            }
        }
    },
    mounted(){
        // axios.get('http://localhost:8800/user')
        // .then(res => {
        //     console.log(res.data[0].name);
        //     this.introduction.names = res.data[0].name;
        //     this.introduction.intro = res.data[0].introduction;
        // })
        // .catch(err => {
        //     console.log(err);
        // })
    },
}
</script>

<style lang="scss" scoped>
.contain{
    .section1{
        margin-top: 5%;
    }
    .section2{
        margin-top: 5%;
    }
}
</style>