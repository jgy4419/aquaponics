<template>
    <div class="contain">
        <div class="inner">
            <div class="titleBox">
                <div class="box"/>
                <div class="title">Aquaponics?</div>
            </div>
            <div class="contentBox">
                <!-- 마우스 올리면 border 생기고, text 왼쪽으로 20px 옮기기 -->
                <div v-for="itemText, i in items.itemText.length" :key="i" 
                class="item" @mouseover="itemIn()" @mouseout="itemOut()">
                    <img class="itemImage" :src="items.itemImage[i]" alt="메인이미지들">
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
    },
    methods: {
        itemIn(){
            // alert('in');
            this.hoverState = 1;
        },
        itemOut(){
                        // alert('out');
            this.hoverState = 0;
        }
    }
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    margin-top: 20px;
    width: 100vw;
    height: 100vh;
    // background-color: #333;
    .inner{
        width: 80vw;
        margin: auto;
        .titleBox{
            height: 100px;
            .box{
                position: absolute;
                width: 50px;
                height: 50px;
                background-color: #E5E3C9;
            }
            .title{
                position: absolute;
                top: 10px;
                margin-left: 20px;
                color: #94B49F;
                font-size: 50px;
                font-weight: 700;
            }
        }
        .contentBox{
            display: grid;
            grid-template-columns: 35vw 35vw;
            // grid-template-rows: 500px 500px;
            gap: 10%;
            width: 100%;
            height: 80vh;
            .item{
                height: 500px;
                opacity: 0;
                transition: .7s;
                transform: translateY(100px);
                border: 2px solid #B4CFB0;
                border-radius: 20px;
                .itemImage{
                    border-radius: 20px;
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
                opacity: 1;
                transform: translateY(0px);
            }
        }
    }
    @media screen and (max-width: 900px){
        .inner{
            .contentBox{
                .item{
                    height: 400px;
                    .itemText{
                        font-size: 16px;
                    }
                }
            }
        }
    }
    @media screen and (max-width: 768px){
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