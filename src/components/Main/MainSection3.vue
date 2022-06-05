<template>
    <div class="contain">
        <div class="inner">
            <div class="titleBox">
                <div class="box"/>
                <p class="greenTitle">내 손안의 아쿠아포닉스</p>
            </div>
            <div class="contentBox">
                <div class="item" v-for="itemName, i in items.title.length" :key="i">
                    <p class="title">{{items.title[i]}}</p>
                    <button class="btn">{{items.button[i]}}</button>
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
                title: ['사이트 상세', '시작하기', '나의 아쿠아포닉스'],
                button: ['보러가기', '회원가입', '마이페이지']
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    z-index: 10;
    width: 100vw;
    height: 800px;
    background-color: rgb(242, 242, 242);
    .inner{
        width: 80vw;
        margin: auto;
        .titleBox{
            padding-top: 30px;
        }
        .contentBox{
            width: 1000px;
            margin: auto;
            display: grid;
            margin-top: 10%;
            grid-template-columns: 400px 500px;
            grid-template-rows: 200px 200px;
            grid-gap: 10%;
            .item{
                position: relative;
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
    }
    @media screen and (max-width: 900px){
        height: 1000px;
        .inner{
            .contentBox{
                display: block;
                width: 100%;
                .item{
                    height: 200px;
                    margin-top: 20px;
                }
            }
        }
    }
}
</style>