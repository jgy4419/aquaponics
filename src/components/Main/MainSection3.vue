<template>
    <div class="contain">
        <div class="painting"/>
        <div class="inner">
            <div class="titleBox">
                <div class="box"/>
                <p class="greenTitle">내 손 안의 아쿠아포닉스. <br/>바로 시작해봐요!</p>
            </div>
            <div class="contentBox2">
                <div class="item" v-for="itemName, i in items.title.length" :key="i">
                    <p class="title">{{items.title[i]}}</p>
                    <router-link :to="items.url[i]">
                        <button class="btn">{{items.button[i]}}</button>
                    </router-link>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
export default {
    data(){
        return{
            items:{
                title: ['내 아쿠아 포닉스', '아쿠아포닉스 추천받기', '사이트 소개'],
                // 로그인 되면 회원가입 대신 마이페이지로 바꾸기
                button: ['보러가기', 'reference', 'About'],
                url: ['/mypage', '/reference', '/about']
            }
        }
    },
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    z-index: 2;
    width: 100vw;
    height: 800px;
    background-color: rgb(242, 242, 242);
    overflow: hidden;
    .painting{
        position: absolute;
        bottom: 0;
        right: -20%;
        transform: skewX(-30deg);
        width: 50vw;
        height: 50vh;
        background-color: #B4CFB0;
        // transform-origin: bottom, right;
    }
    .inner{
        position: relative;
        z-index: 10;
        width: 80vw;
        margin: auto;
        .titleBox{
            padding-top: 30px;
        }
        .contentBox2{
            opacity: 0;
            transform: translateY(100px);
            transition: 1s;
            width: 1000px;
            margin: auto;
            display: flex;
            margin-top: 10%;
            .item{
                position: relative;
                width: 30%;
                height: 300px;
                margin: 10px;
                border-radius: 20px;
                padding: 20px;
                background-color: #fff;
                .title{
                    font-size: 30px;
                    font-weight: 700;
                    color: #94B49F;
                }
                .btn{
                    position: absolute;
                    bottom: 0;
                    right: 0;
                    margin: 30px;
                    width: 150px;
                    height: 50px;
                    font-size: 20px;
                    border-radius: 10px;
                }
            }
            .item:nth-child(1){
                grid-row: 1 / 3;
            }
        }
        .contentBox2.event{
            opacity: 1;
            transform: translateY(0px);
        }
    }
    @media screen and (max-width: 900px){
        height: 1000px;
        .inner{
            .titleBox{
                .box{
                    width: 40px;
                    height: 40px;
                }
                .greenTitle{
                    font-size: 25px;
                }
            }
            .contentBox2{
                display: block;
                width: 100%;
                .item{
                    width: 90%;
                    height: 200px;
                    margin-top: 20px;
                    .title{
                        font-size: 20px;
                    }
                    .btn{
                        font-size: 16px;
                        width: 100px;
                        height: 50px;
                    }
                }
            }
        }
    }
}
</style>