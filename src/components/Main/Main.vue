<template>
    <div class="contain">
        <!-- 이미지 사진 -->
        <!-- http://openimage.interpark.com/goods_image_big/6/0/2/7/8085846027_l.jpg -->
        <!-- 참고할 사이트 -->
        <!-- http://muplus.co.kr/2021_renewal/html/Main/main.html#none -->
        <div class="inner">
            <div class="titleBox">
                <div class="title">내 손 안의 <br/>아쿠아포닉스</div>
                <button class="btn">시작하기</button>
            </div>
            <img class="mainImg" src="https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.daumcdn.net%2Fshophow%2Fp%2FP14086506296.jpg%3Fut%3D20210723101748" alt="메인사진">
        </div>        

        <!-- <Section1/> -->
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
    // position: absolute;
    width: 100vw;
    height: 90vh;
    // background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd8zgQhWf09Wvwk2xEmU1C64c8K--6ZvsYWA&usqp=CAU');
    // background-repeat: no-repeat;
    // background-size: cover;
    .inner{
        position: relative;
        top: 5%;
        width: 70%;
        margin: auto;
        display: flex;
        .titleBox{
            // display: flex;
            // align-items: center;
            height: 60vh;
            .title{
                color: #333;
                font-size: 80px;
                font-weight: 900;
                line-height: 9rem;
            }
        }
        .btn{
            margin: 10% 10%;
            width: 150px;
            height: 80px;
            font-size: 20px;
            border-radius: 10px;
        }
        .mainImg{
            position: absolute;
            right: 0;
        }
    }
}
</style>