<template>
    <div class="contain">
        <div class="inner">
            <div class="contentBox1">
                <div class="mainTitle1">
                    <p class="smallTitle">Technology</p>
                    <h1 class="title">적용된 기술</h1>
                </div>
                <div class="contentInner1">
                    <ul>
                        <li class="content1" v-for="title, i in content1.contentBox1Title.length" :key="i">
                            <h2 class="boxTitle1">{{content1.contentBox1Title[i]}}</h2>
                            <p class="boxContent1">{{content1.contentBox1Content[i]}}</p>
                            <hr>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="contentBox2">
                <div class="mainTitle">
                    <p class="smallTitle">Main Function</p>
                    <h1 class="title">주요 기능</h1>
                </div>
                <div class="contentInner2">
                    <ul>
                        <li class="content2" v-for="title, i in content2.contentBox2Title.length" :key="i">
                            <div class="text">
                                <h2 class="boxTitle2">{{content2.contentBox2Title[i]}}</h2>
                                <p class="boxContent2">{{content2.contentBox2Content[i]}}</p>
                            </div>
                            <img class="contentImg" :src="content2.contentBox2Image[i]" alt="이미지">
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            content1: {
                contentBox1Title: ['플랫폼 시각화', '센서 데이터 분석', 'AI 자동화'],
                contentBox1Content: [
                    'Web을 통해 시각화된 센서 데이터를 확인하게 합니다.',
                    '센서들을 통해 입력받은 값을 분석합니다.',
                    '분석된 데이터들을 이용하여 자동으로 시스템을 적용시킵니다.'
                ]
            },
            content2: {
                contentBox2Title: ['데이터 시각화', '자동 조절'],
                contentBox2Content: [
                    '샌서에서 입력받은 값을 시각화하여 웹으로 모니터링이 가능합니다.',
                    '센서에서 받은 값을 바탕으로 수질 및 조도를 조절할 수 있습니다.'
                ],
                contentBox2Image: [
                    'https://i0.wp.com/iphoneislam.com/wp-content/uploads/2020/07/best_gardening_apps.jpg?fit=590%2C357&ssl=1',
                    'https://cdn.imweb.me/upload/S2020110674261a25e9da9/724b36cb78aa9.jpg'
                ]
            }
        }
    },
    mounted(){
        let screenHeight = document.documentElement.scrollHeight;
        document.addEventListener("scroll", () => {
            let currentScrollValue = document.documentElement.scrollTop;
            let content1 = document.querySelectorAll(".content1");
            let contentImg = document.querySelectorAll('.contentImg');
            let content2Text = document.querySelectorAll('.text');

            if(currentScrollValue > screenHeight / 5){
                document.querySelector('.mainTitle1').classList.add('event');
                content1.forEach((e) => {
                    e.classList.add('event');
                })
            }
            for(let i = 0; i < contentImg.length; i++){
                if(currentScrollValue > screenHeight / 2.5 && currentScrollValue < screenHeight / 1.8){
                    setTimeout(() => {
                        contentImg[0].classList.add('event');
                    }, 1000);
                    content2Text[0].classList.add('event');
                }else if(currentScrollValue > screenHeight / 1.7){
                    setTimeout(() => {
                        contentImg[1].classList.add('event');
                    }, 1000);
                    content2Text[1].classList.add('event');
                }
            }
        })
    }
}
</script>

<style lang="scss" scoped>
.contain {
    width: 100vw;
    height: 100vh;
    min-height: 650px;
    background-color: rgb(248, 248, 248);
    .inner {
        position: relative;
        top: 10%;
        width: 80vw;
        margin: auto;
        color: #333;
        .contentBox1, .contentBox2{
            position: relative;
            height: 100vh;
            min-height: 600px;
            .mainTitle1{
                opacity: 0;
                transition: 1.5s; 
            }
            .mainTitle1.event{
                opacity: 1;
            }
            .smallTitle{
                color: #94B49F;
                font-size: 20px;
                font-weight: 700;
            }
            .title{
                font-size: 50px;
                margin-top: 20px;
            }
            .contentInner1{
                position: absolute;
                margin-top: -4%;
                right: 0;
                .content1{
                    opacity: 0;
                    margin-top: 30px;
                    transform: translateX(150px);
                    font-weight: 700;
                    .boxTitle1{
                        font-size: 40px;
                        margin-bottom: 30px;
                    }
                    .boxContent1{
                        font-size: 16px;
                        margin-bottom: 20px;
                        color: rgb(144, 143, 143);
                    }
                }
                .content1:nth-child(1){
                    transition: 1s;
                    margin-top: 0;
                }
                .content1:nth-child(2){
                    transition: 1.3s;
                }
                .content1:nth-child(3){
                    transition: 1.5s;
                }
                .content1.event{
                    transform: translateX(0px);
                    opacity: 1;
                }
            }
            .contentInner2{
                .content2{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-top: 10%;
                    .text{
                        opacity: 0;
                        transition: 1.3s;
                        transform: translateY(50px);
                        .boxTitle2{
                            font-size: 40px;
                            font-weight: 700;
                            margin-bottom: 30px;
                        }
                        .boxContent2{
                            width: 300px;
                            font-size: 20px;
                            font-weight: 500;
                            line-height: 1.6;
                            color: rgb(144, 143, 143);
                        }
                    }
                    .text.event{
                        opacity: 1;
                        transform: translateY(0px);
                    }
                    .contentImg{
                        opacity: 0;
                        transition: 1s;
                        transform: translateX(120px);
                        width: 50%;
                        border-radius: 20px;
                    }
                    .contentImg.event{
                        opacity: 1;
                        transform: translateX(0px);
                    }
                }
                .content2:nth-child(1){
                    position: relative;
                    .content2{
                        .text:nth-child(1){
                            position: absolute;
                            right: 0;
                        }
                    }
                }
            }
        }
    }
    @media screen and (max-width: 800px){
        height: 90vh;
        .inner{
            .contentBox1{
                text-align: center;
                .smallTitle{
                    font-size: 15px;
                }
                .title{
                    font-size: 30px;
                }
                .contentInner1{
                    width: 100%;
                    .content1{
                        .boxTitle1{
                            margin-top: 10%;
                            font-size: 25px;
                        }
                        .boxContent1{
                            font-size: 13px;
                        }
                        hr{
                            width: 300px;
                            margin: auto;
                        }
                    }
                }
            }
            .contentBox2{
                text-align: center;
                .smallTitle{
                    font-size: 15px;
                }
                .title{
                        font-size: 30px;
                    }
                .contentInner2{
                    .content2{
                        display: block;
                        text-align: center;
                        .text{
                            .boxTitle2{
                                font-size: 25px;
                            }
                            .boxContent2{
                                font-size: 13px;
                                width: 100%;
                            }
                        }
                        .contentImg{
                            width: 100%;
                            margin-top: 5%;
                        }
                    }
                }
            }
        }
    }
}
</style>