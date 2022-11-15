<template>
    <div class="contain">
        <br/>
        <p class="title"><span class="user-name">아쿠</span>님의 아쿠아포닉스 상태는?</p>
        <br>
        <hr>
        <div class="inner">
            <div :class="waterState === 1 ? 'sensor humidity_state' : 'humidity_state_blue'">
                <h2>물 상태</h2>
                <p>{{waterState === 1 ? '적당합니다!' : '물을 보충해주세요!'}}</p>
            </div>
            <div :class="ledState === 0 ? 'sensor on' : 'sensor off'"
              @click="ledStateFunc()">
                <h2>LED {{ledState === 0 ? 'OFF' : 'ON'}}</h2>
            </div>
            <div class="use_chart_sensor">
                <p class="title">온/습도, 조도</p>
                <p class="sub_title">최근 7일 내 상태만 불러옵니다.</p>
                <Chart/>
            </div>
        </div>
    </div>
</template>

<script>
import Chart from './ChartView.vue';
import axios from 'axios';
export default {
    components: {
        Chart
    },
    data(){
        return{
            sensorList:['온/습도 상태', '물 상태'],
            sensorValue: [],
            sensorModalState: 0,
            ledState: 0,
            waterState: 0
        }
    },
    async mounted(){
        // setInterval(async () => {
            await axios.get(`http://127.0.0.1:5000/water`)
            .then(res => {
            this.waterState = res.data[res.data.length-1];
            console.log(res.data);
            }).catch(error => console.log(error));
        // }, 100000);
    },
    methods: {
        async ledStateFunc(){
            if(this.ledState === 0){
                axios.get(`http://127.0.0.1:5000/ledON`)
                .then(res => {
                    console.log([res.data]);
                }).catch(error => console.log(error));
            }
            else if(this.ledState === 1){
                axios.get(`http://127.0.0.1:5000/ledOFF`)
                .then(res => {
                    console.log([res.data]);
                }).catch(error => console.log(error));
            }
            this.ledState === 0 ? this.ledState = 1 : this.ledState = 0;
            //if(this.ledState === 0){
            //    await axios.get(`http://127.0.0.1:5000/ledON`)
            //    .then(res => {
            //        this.waterState = res.data[res.data.length-1];
            //        console.log(res.data);
            //    }).catch(error => console.log(error));
            //}
            //else if(this.ledState === 1){
            //    await axios.get(`http://127.0.0.1:5000/ledOFF`)
            //    .then(res => {
            //        this.waterState = res.data[res.data.length-1];
            //        console.log(res.data);
            //    }).catch(error => console.log(error));
            //}
            //this.ledState === 0 ? this.ledState = 1 : this.ledState = 0;

       }
    }
}
</script>

<style lang="scss" scoped>
.contain{
    height: 100vh;
    .title{
        font-size: 30px;
        font-weight: 700;
        .user-name{
            color: rgb(102, 206, 128);
        }
    }
    .inner{
        display: flex;
        flex-wrap: wrap;
        .sensor{
            color: #333;
            width: 30%;
            height: 200px;
            box-sizing: border-box;
            border-radius: 10px;
            margin: 5% 3% 0% 0%;
            padding: 20px;
            box-shadow: 4px 12px 30px 6px rgb(231, 231, 231);
            transition: .2s;
            cursor: pointer;
            .humidity_state, .humidity_state_blue{
                margin-top: 10px;
                font-size: 14px;
                font-weight: 600;
                font-size: #333;
                color: #333;
                width: 30%;
                height: 200px;
                box-sizing: border-box;
                border-radius: 10px;
                margin: 5% 3% 0% 0%;
                padding: 20px;
                box-shadow: 4px 12px 30px 6px rgb(231, 231, 231);
                transition: .2s;
                cursor: pointer;
            }
            .humidity_state_blue{
                background-color: rgb(151, 164, 233);
                color: #fff;
            }
        }
        .sensor .off{
            color: #fff;
            background-color: rgb(250, 150, 150);
        }
        .sensor:hover{
            transform: translateY(-10px);
        }
        .use_chart_sensor{
            margin-top: 10%;
            .title{
                text-align: center;
                font-size: 30px;
                font-weight: 700;
            }
            .sub_title{
                text-align: center;
                margin-top: 20px;
                font-size: 20px;
                font-weight: 600;
                color: grey;
            }
        }
    }
    @media screen and (max-width: 768px){
        .title{
            font-size: 20px;
        }
        .inner{
            display: block;
            .sensor{
                width: 100%;
                height: 150px;
                font-size: 14px;
            }
        }
    }
}
</style>    