<template>
    <div class="contain">
        <div class="inner">
            <div class="titleBox">
                <div class="mainText">
                    <div class="title">Home<br/>Aquaponics</div>
                    <p class="serve">아쿠아포닉스를 집에서 키우고 관리하세요!</p>
                </div>
                <router-link to="/login">
                    <button class="btn">
                        시작하기
                    </button>   
                </router-link>
            </div>
            <img class="mainImg" :src="mainImage1" alt="메인사진">
        </div>
    </div>
</template>

<script>
// UI 참고 사이트 http://shimlee.co.kr/ 
import MainImage1 from '../../Image/Main/MainImage1.png'
export default {
    data(){
        return{
            mainImage1: MainImage1
        }
    }
}
</script>

<style lang="scss" scoped>
.contain{
    width: 100vw;
    height: 800px;
    .inner{
        position: relative;
        top: 15vh;
        width: 80%;
        height: 100%;
        margin: auto;
        display: flex;
        .titleBox{
            height: 60vh;
            .mainText{
                transition: 1s;
                transform: translateY(100px);
                opacity: 0;
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
            .mainText.event{
                opacity: 1;
                transform: translateY(0px);
            }
        }
        .btn{
            position: relative;
            z-index: 2;
            margin: 20% 0%;
            width: 120px;
            height: 60px;
            font-size: 20px;
            border-radius: 10px;
        }
        .mainImg{
            position: absolute;
            border-radius: 10px;
            opacity: 0;
            transform: translateX(120px);
            transition: 2s;
            right: 0;
        }
        .mainImg.event{
            opacity: 1;
            transform: translateX(0px);
        }
    }
}
@media screen and (max-width: 1000px){
    .contain{
        width: 100vw;
        height: 800px;
        background-image: url('../../Image/Main/MainImage1.png');
        background-repeat: no-repeat;
        background-size: cover;
        .inner{
            top: 0;
            .titleBox{
                margin: auto;
                text-align: center;
                .title{
                    font-size: 60px;
                }
                .serve{
                    font-size: 14px;
                }
            }
            .btn{
                width: 100px;
                height: 60px;
                font-size: 16px;
            }
            .mainImg{
                display: none;
            }
        }
    }
}
@media screen and (max-width: 365px){
    .contain{
        .inner{
            .title{
                font-size: 20px;
            }
            .serve{
                font-size: 12px;
            }
            .btn{
                width: 80px;
                height: 40px;
                font-size: 12px;
            }
        }
    }
}
</style>