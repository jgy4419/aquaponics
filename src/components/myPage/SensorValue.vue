<template>
    <div class="contain">
        <br/>
        <p class="title">???님의 아쿠아포닉스 상태는?</p>
        <br>
        <hr>
        <div class="inner">
            <div class="sensor" @click="modalOpen()"
            v-for="sensor, i in sensorList.length" :key="i">
                <h2>{{sensorList[i]}}</h2>
                <p>{{sensorValue[i]}}</p>
            </div>
        </div>
        <SensorDetail 
        :sensorModalState="this.sensorModalState" 
        @state="sensorModalState = 0"
        v-if="sensorModalState === 1"/>
    </div>
</template>

<script>
import axios from 'axios';
import SensorDetail from './SensorDetail.vue';
export default {
    components: {
        SensorDetail,
    },
    data(){
        return{
            sensorList:['물고기 상태', '물 상태', '식물 상태'],
            sensorValue: [],
            sensorModalState: 0,
        }
    },
    mounted(){
        // 특정 유저 센서 데이터 test 파일
        axios.get('http://localhost:8800/sensor')
        .then(res => {
            console.log(res.data[0].sensor1);
            for(let i = 0; i < res.data.length; i++){
                this.sensorValue.push(res.data[0].sensor1);
                this.sensorValue.push(res.data[0].sensor2);
                this.sensorValue.push(res.data[0].author);
            }
            console.log('!!',this.sensorValue);
        })
        .catch(err => {
            console.log(err);
        })
    },
    methods: {
        modalOpen(){
            this.sensorModalState = 1
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
    }
    .inner{
        display: flex;
        flex-wrap: wrap;
        .sensor{
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
        .sensor:hover{
            transform: translateY(-10px);
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