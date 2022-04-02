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
                <p>{{sensor.sensor1}}</p>
            </div>
            <!-- <div class="sensor">
                {{sensor.sensor1}}
            </div>
            <div class="sensor">
                {{sensor.sensor2}}
            </div>
            <div class="sensor">
                {{sensor.sensor3}}
            </div> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            sensorList:['물고기 상태', '물 상태', '식물 상태'],
            sensor: {
                sensor1: '',
                sensor2: '',
                sensor3: '',
            }
        }
    },
    mounted(){
        // 특정 유저 센서 데이터 test 파일
        axios.get('http://localhost:8800/sensor')
        .then(res => {
            console.log(res.data[0].sensor1);
            this.sensor.sensor1 = res.data[0].sensor1;
            this.sensor.sensor2 = res.data[0].sensor2;
            this.sensor.sensor3 = res.data[0].author;
        })
        .catch(err => {
            console.log(err);
        })
    }
}
</script>

<style lang="scss" scoped>
.contain{
    width: 70vw;
    .inner{
        display: flex;
        flex-wrap: wrap;
        .sensor{
            width: 30%;
            height: 200px;
            border: 1px solid #333;
        }
    }
}
</style>