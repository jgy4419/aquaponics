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
                class="items">
                    <div class="itemImage" :style="{backgroundImage:`url('${items.itemImage[i]}')`}"/>
                    <h1 class="itemTitle">{{items.itemTitle[i]}}</h1>
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
                itemImage: ['https://www.kamnews.co.kr/news/photo/202109/5335_10444_1742.jpg', 'https://cdn.imweb.me/upload/S201712285a44c323cd4da/986098737d195.jpg', 
                'https://i.dailymail.co.uk/1s/2021/11/23/09/50856511-10230791-Cages_under_each_platform_could_be_used_to_keep_scallops_kelp_or-a-2_1637660062753.jpg', 'http://cms.arirang.co.kr/ACE5_Img/2021/04/20210426_16010845_86026.png'],
                itemTitle: ['# 아쿠아포닉스란?', '# 식물과 물고기에 어떻게 공존하나요?', '# 아쿠아포닉스 농법의 장점', '# 결론이 무엇인가요?'],
                itemText: ['아쿠아포닉스 농법은 논에서 물고기를 함께 키우거나, 연못에서 물고기를 키우고 그 물을 농업에 이용하는 방법으로 고대로부터 이어져온 농법이에요!',
                    '식물은 물고기에서 나오는 영양 성분이 가득한 물을먹고 자라고, 물고기는 식물이 정화해준 물을 먹고 살아요.', 
                    '아쿠아포닉스로 물고기 양식, 작물 재배를 한 번에 해결이 가능해요!', 
                    '자연적인 미생물 분해과정을 통해 물고기와 식물 모두 건강하게 자라는 지속 가능한 자연 선순환 방식의 농법이에요!'],
            },
            hoverState: 0,
            backText: ['#아쿠아포닉스를', '#집 안에서', '#애완동물처럼'],
        }
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
            position: relative;
            z-index: 2;
            margin-top: 10%;
            display: grid;
            grid-template-columns: 35vw 35vw;
            gap: 10%;
            width: 100%;
            height: 80vh;
            opacity: 0;
            transition: 1s;
            transform: translateY(100px);
            .items{
                opacity: .6;
                width: 35vw;
                height: 400px;
                border-radius: 20px;
                box-sizing: border-box;
                box-shadow: 4px 12px 30px 6px rgb(231, 231, 231);
                transition: .3s;
                .itemImage{
                    background-size: cover;
                    width: 100%;
                    height: 40%;
                }
                .itemTitle{
                    color: #94B49F;
                    padding: 20px;
                }
                .itemText{
                    color: #B4CFB0;
                    line-height: 1.6;
                    margin-top: 30px;
                    padding: 0px 20px;
                    font-size: 20px;
                    font-weight: 500;
                    transition: .4s;
                }
            }
            .items:nth-child(2n){
                margin-top: 20%;
            }
            .items:hover{
                opacity: 1;
                // transition: .1s;
            }
        }
        .contentBox.event{
            opacity: 1;
            transform: translateY(0px);
        }
    }
    @media screen and (max-width: 900px){
        .inner{
            .contentBox{
                .items{
                    width: 100%;
                    height: 400px;
                    .itemTitle{
                        font-size: 20px;
                    }
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
                .items:nth-child(2n){
                    margin-top: 30px;
                }
                .items{
                    position: relative;
                    margin-top: 30px;
                    width: 100%;
                    height: 400px;
                }
            }
        }
    }
}
</style>