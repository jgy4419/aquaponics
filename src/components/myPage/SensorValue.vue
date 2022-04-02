<template>
    <div class="contain">
        <br/>
        <h1>???님의 아쿠아포닉스 상태는?</h1>
        <br>
        <hr>
        <div class="inner">
            <div class="sensor"
            v-for="sensor, i in sensorList.length" :key="i">
                <h2>{{sensorList[i]}}</h2>
                <p>{{sensorValue[i]}}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            sensorList:['물고기 상태', '물 상태', '식물 상태'],
            sensorValue: [],
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
    }
}
</script>

<style lang="scss" scoped>
.contain{
    height: 100vh;
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
}
</style>