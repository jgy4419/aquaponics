<template>
    <div class="contain">
        <div class="inner">
            <div class="titleBox">
                <div class="title">Home<br/>Aquaponics</div>
                <p class="serve">아쿠아포닉스를 집에서 키우고 관리하세요!</p>
                <router-link to="/login">
                    <button class="btn">
                        시작하기
                    </button>   
                </router-link>
            </div>
            <img class="mainImg" src="https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.daumcdn.net%2Fshophow%2Fp%2FP14086506296.jpg%3Fut%3D20210723101748" alt="메인사진">
        </div>
    </div>
</template>

<script>
// import Section1 from './MainSection1.vue'
export default {
    components: {
        // Section1,
    }
}
</script>

<style lang="scss" scoped>
.contain{
    width: 100vw;
    height: 90vh;
    .inner{
        position: relative;
        top: 15%;
        width: 70%;
        margin: auto;
        display: flex;
        .titleBox{
            height: 60vh;
            .title{
                color: transparent;
                background: linear-gradient(to right top, #94B49F, #ffffff);
                -webkit-background-clip: text;
                font-size: 80px;
                font-weight: 900;
                line-height: 7rem;
            }
            .serve{
                margin-top: 5%;
                font-size: 16px;
                font-weight: 700;
                color: rgb(185, 185, 185);
            }
        }
        .btn{
            margin: 20% 0%;
            width: 150px;
            height: 80px;
            font-size: 20px;
            border-radius: 10px;
        }
        .btn{
            color: #fff;
        }
        .mainImg{
            position: absolute;
            right: 0;
        }
    }
}
</style>