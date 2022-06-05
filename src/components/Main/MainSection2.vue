<template>
    <div class="contain">
        <div class="backTexts">
            <p class="backText" v-for="backText in backText" :key="backText">{{backText}}</p>
        </div>
        <div class="inner">
            <div class="titleBox">
                <div class="box"/>
                <p class="greenTitle">Aquaponics?</p>
            </div>
            <div class="contentBox">
                <!-- 마우스 올리면 border 생기고, text 왼쪽으로 20px 옮기기 -->
                <div v-for="itemText, i in items.itemText.length" :key="i" 
                class="item" @mouseover="itemIn()" @mouseout="itemOut()">
                    <div class="itemImage" :style="{backgroundImage:`url('${items.itemImage[i]}')`}"/>
                    <div class="itemText">
                        {{items.itemText[i]}}
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
export default {
    data(){
        return{
            items: {
                itemImage: ['https://www.kamnews.co.kr/news/photo/202109/5335_10444_1742.jpg', 'https://images.roa.ai/articles/2019/02/49151083_2380361025372621_1976658500691951616_n.jpg', 
                'https://www.kamnews.co.kr/news/photo/202109/5335_10444_1742.jpg', 'https://images.roa.ai/articles/2019/02/49151083_2380361025372621_1976658500691951616_n.jpg'],
                itemText: ['설명 구구절ㄹ절절1', '설명 구구절ㄹ절절2', '설명 구구절ㄹ절절3', '설명 구구절ㄹ절절4'],
            },
            hoverState: 0,
            backText: ['#아쿠아포닉스를', '#집 안에서', '#애완동물처럼'],
        }
    },
    mounted(){
        let screenHeight = document.documentElement.scrollHeight;
        let item = document.querySelectorAll('.item');

        document.addEventListener('scroll', function(){
            let currentScrollValue = document.documentElement.scrollTop;
            if(currentScrollValue > screenHeight / 4){
                for(let i = 0; i < item.length; i++){
                    item[i].classList.add('event');
                }
            }else{
                for(let i = 0; i < item.length; i++){
                    item[i].classList.remove('event');
                }
            }
        })

        // const items = document.querySelectorAll('.item');
        // for(let i = 0; i < items.length; i++){
        //     items[i].addEventListener('mouseover', function(){
        //         // alert('test');
        //     })
        // }
    },
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    margin-top: 20px;
    width: 100vw;
    height: 1500px;
    .backTexts{
        position: absolute;
        top: 28%;
        line-height: 2;
        right: 0;
        .backText{
            font-size: 80px;
            font-weight: 500;
            color: rgb(220, 220, 220);
        }
    }
    .inner{
        width: 80vw;
        margin: auto;
        .contentBox{
            display: grid;
            grid-template-columns: 35vw 35vw;
            // grid-template-rows: 500px 500px;
            gap: 10%;
            width: 100%;
            height: 80vh;
            .item{
                width: 35vw;
                height: 500px;
                opacity: 0;
                transition: .7s;
                transform: translateY(100px);
                border-radius: 20px;
                box-shadow: 4px 12px 30px 6px rgb(231, 231, 231);
                .itemImage{
                    background-size: cover;
                    width: 100%;
                    height: 40%;
                }
                .itemText{
                    margin-top: 30px;
                    padding-left: 20px;
                    font-size: 20px;
                    font-weight: 500;
                    transition: .4s;
                }
            }
            .item:nth-child(2n){
                margin-top: 20%;
            }
            .item.event{
                opacity: .8;
                transform: translateY(0px);
            }
        }
    }
    @media screen and (max-width: 900px){
        .inner{
            .contentBox{
                .item{
                    width: 100%;
                    height: 400px;
                    .itemText{
                        font-size: 16px;
                    }
                }
            }
        }
    }
}
@media screen and (max-width: 768px){
    .contain{
        height: 1850px;
        .backTexts{
            display: none;
        }
        .inner{
            .contentBox{
                display: block;
                .item:nth-child(2n){
                    margin-top: 30px;
                }
                .item{
                    position: relative;
                    margin-top: 30px;
                    height: 400px;
                }
            }
        }
    }
}
</style>