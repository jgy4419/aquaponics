<template>
    <div class="contain">
        <div class="inner">
            <img src="https://www.canceranswer.co.kr/news/photo/202109/3045_4820_1253.jpg" alt="이미지">
            <ul>
                <li class="name">
                    {{intro[0]}} : {{introduction.names}}
                </li>
                <li class="introduction">
                    {{intro[1]}} : {{introduction.intro}}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        introduction: Object,
    },
    data(){
        return{
            intro: ['이름', '소개글']
        }
    },
}
</script>

<style lang="scss" scoped>
.contain{
    width: 100vw;
    // height: 90vh;
    .inner{
        margin: auto;
        width: 70%;
        display: flex;
        align-items: center;
        // margin-top: 6%;
        img{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 5px solid rgb(241, 240, 240);
            margin-right: 5%;
        }
        .name{
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 10%;
        }
        .introduction{
            font-size: 25px;
            font-weight: 500;
        }
    }
}
@media screen and (max-width: 768px){
    .contain{
        .inner{
            display: block;
            text-align: center;
            img{
                width: 100px;
                height: 100px;
            }
            .name{
                margin-top: 20px;
                font-size: 30px;
            }
            .introduction{
                margin-top: -20px;
                font-size: 20px;
            }
        }
    }
}
</style>