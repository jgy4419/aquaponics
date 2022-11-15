<template>
    <div class="contain">
        <div class="inner">
            <div v-if="btnState === 0" class="sensor">
                <Sensor class="sensorInner"/>
            </div>
            <div v-if="btnState === 1" class="sensor">
                <Sensor class="sensorInner"/>
            </div>
        </div>
    </div>
</template>

<script>
// import ChartView from './ChartView.vue';
import Sensor from './SensorValue.vue';
// import Chart from './ChartView.vue';
// import Camera from './Camera.vue';
export default {
    name: "line-chart",
    type: "line",
    components:{
        Sensor,
    },
    data(){
        return{
            btnList: ['그래프', '센서값'],
            btnState: 0,
        }
    },
    methods: {
        btnClick(i){
            console.log(i);
            this.btnState = i;
        },
    }
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    z-index: 2;
    margin: auto;
    width: 100vw;
    min-height: 1200px;
    .inner{
        margin: auto;
        width: 70%;
        .btns{
            display: flex;    
        }
        .sensor{
            .sensorInner{
                width: 100%;
            }
        }
        .btn{
            width: 100px;
            height: 50px;
            font-size: 16px;
            font-weight: 700;
            margin-right: 10px;
            border-radius: 5px;
        }
        @media screen and (max-width: 768px){
            .btn{
                width: 80px;
                height: 40px;
                font-size: 12px;
            }
        }
    }
}
</style>