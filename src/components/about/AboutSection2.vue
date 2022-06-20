<template>
    <div class="contain">
        <div class="inner">
            <div class="contentBox1">
                <div class="mainTitle1">
                    <p class="smallTitle">Technology</p>
                    <h1 class="title">적용된 기술</h1>
                </div>
                <div class="contentInner1">
                    <div class="content1" v-for="title, i in content1.contentBox1Title.length" :key="i">
                        <h2 class="boxTitle1">{{content1.contentBox1Title[i]}}</h2>
                        <p class="boxContent1">{{content1.contentBox1Content[i]}}</p>
                        <hr>
                    </div>
                </div>
            </div>
            <div class="contentBox2">
                <div class="content2">
                    
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
                contentBox2Title: ['자동 조절', '데이터 시각화'],
                contentBox2Content: [
                    '샌서에서 입력받은 값을 시각화하여 웹으로 모니터링 가능합니다.',
                    '센서에서 입력받은 값을 시각화하여 웹으로 모니터링할 수 있게 합니다.'
                ]
            }
        }
    },
    mounted(){
        let screenHeight = document.documentElement.scrollHeight;

        document.addEventListener("scroll", () => {
            let currentScrollValue = document.documentElement.scrollTop;
            let content1 = document.querySelectorAll(".content1");
            if(currentScrollValue > screenHeight / 2.5){
                document.querySelector('.mainTitle1').classList.add('event');
                content1.forEach((e) => {
                    e.classList.add('event');
                })
            }
        })
    }
}
</script>

<style lang="scss" scoped>
.contain {
    width: 100vw;
    height: 100vh;
    .inner {
        position: relative;
        top: 10%;
        width: 1100px;
        margin: auto;
        color: #333;
        .contentBox1{
            position: relative;
            display: flex;
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
                line-height: 1.6;
                font-size: 50px;
                margin-top: 20px;
            }
            .contentInner1{
                position: absolute;
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
                    transform: translateX(9px);
                    opacity: 1;
                }
            }
        }
        .contentBox2{
            
        }
    }
}
</style>