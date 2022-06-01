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
            <img class="mainImg" src="https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.daumcdn.net%2Fshophow%2Fp%2FP14086506296.jpg%3Fut%3D20210723101748" alt="메인사진">
        </div>
    </div>
</template>

<script>
export default {
    mounted(){
        setTimeout(() => {
            let mainText = document.querySelector('.mainText');
            let mainImg = document.querySelector(".mainImg");   
            mainText.classList.add('event');
            mainImg.classList.add("event");
        }, 300);
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
        background-image: url('https://shop3.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop3.daumcdn.net%2Fshophow%2Fp%2FP14086506296.jpg%3Fut%3D20210723101748');
        background-repeat: no-repeat;
        background-size: cover;
        .inner{
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