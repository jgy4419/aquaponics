<template>
    <div class="contain">
        <div class="inner">
            <div style="height: 10px"/>
            <p class="title">농업의 새로운 재배 기술을 사용해<br/>물고기와 식물을 같이 키우고, 관찰하세요</p>
            <div class="domestic">
                <div class="left">
                    <!-- <h2 class="chartTitle">국내 현황</h2> -->
                    <img class="chartImage" src="../../Image/About/chartImg-removebg-preview.png" alt="차트">
                </div>
                <div class="right">
                    <div class="content">
                        <p class="boxTitle">{{box.title[0]}}</p>
                        <p class="boxContent">{{box.content[0]}}</p>
                    </div>
                    <div class="content">
                        <p class="boxTitle">{{box.title[1]}}</p>
                        <p class="boxContent"><span class="count">300</span>억원 + 매출</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import img from '../../Image/About/chartImg-removebg-preview.png'
export default {
    data(){
        return{
            box: {
                title: ['아쿠아포닉스 농법으로', '2019년 기준 국내에'],
                content: ['40여종 작물 재매']
            }
        }
    },
    mounted(){
        const count = document.querySelector('.count');
        let value = 0;
        let rafid;
        function render(){
            count.innerHTML = value;
            value += 3;
            rafid = requestAnimationFrame(render);
            if(value > 120){
                cancelAnimationFrame(rafid);
            }
        }
        render();
    },
    methods: {
    },
}
</script>

<style lang="scss" scoped>
.contain{
    width: 100vw;
    height: 100vh;
    min-height: 800px;
    margin-top: 15px;
    // background-color: #f4f3e9;
    background: linear-gradient(to top, #faf7db, #ffffff);
    color: #333;
    .inner{
        width: 80vw;
        margin: auto;
        .title{
            font-size: 50px;
            font-weight: 700;
            text-align: center;
            margin-top: 100px;

        }   
        .domestic{
            position: relative;
            margin-top: 10%;
            display: flex;
            justify-content: space-between;
            .left{
                .chartImage{
                    // width: 400px;
                    width: 30vw;
                    opacity: .3;
                }
            }
            .content{
                margin-top: 30px;
                font-weight: 700;
                .boxTitle{
                    font-size: 25px;
                    margin-bottom: 30px;
                }
                .boxContent{
                    font-size: 40px;
                }
            }
        }
        @media screen and (max-width: 1000px){
            .title{
                font-size: 40px;
            }
            .domestic{
                .content{
                    .boxTitle{
                        font-size: 20px;
                    }
                    .boxContent{
                        font-size: 30px;
                    }
                }
            }
        }
    }
}
@media screen and (max-width: 800px){
    .contain{
        height: 100vh;
        .inner{
            .title{
                font-size: 30px;
            }
            .domestic{
                display: block;
                text-align: center;
                .content{
                    .boxTitle{
                        font-size: 15px;
                    }
                    .boxContent{
                        font-size: 25px;
                    }
                }
            }
        }
    }
}
</style>