<template>
    <div class="contain">
        <div class="inner">
            <div class="btns">
                <button class="btn" 
                    @click="btnClick(i)"
                    v-for="btns, i in btnList" :key="i">
                    {{btns}}
                </button>
            </div>
            <div v-if="btnState === 0" class="graph">
                <ChartView class="chart"/>
            </div>
            <div v-if="btnState === 1" class="sensor">
                <Sensor class="abc"/>
            </div>
            <div v-if="btnState === 2"  class="watch">
                <video autoplay="true" id="videoElement"/>
            </div>
                
        </div>
    </div>
</template>

<script>
import ChartView from './ChartView.vue';
import Sensor from './SensorValue.vue';
export default {
    name: "line-chart",
    type: "line",
    components:{
        ChartView,
        Sensor
    },
    mounted(){
        var video = document.getElementById("videoElement");
        if (navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video.srcObject = stream;
            })
            .catch(function (error) {
                console.log(error);
            });
        }
    },
    data(){
        return{
            btnList: ['그래프', '센서값', '영상'],
            btnState: 0,
            chart: {
                data:{ 
                    labels: [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023], 
                    datasets: [ 
                        { 
                            label: "인원수", backgroundColor: "rgb(255,153,204, 0.5)", pointBackgroundColor: "hotpink", fill: true, tension: 0.1, borderColor: "hotpink", pointBorderColor: "hotpink", borderWidth: 1, pointBorderWidth: 1, 
                            data: [450, 300, 100, 1000, 750, 600, 900, 1500, 1200, 2000] 
                        } 
                    ] 
                }, 
                options: { 
                    plugins: { 
                        legend: { 
                            display: true, 
                            position: "left", 
                            labels: { 
                                boxWidth: 8, 
                                padding: 10, 
                                usePointStyle: true, 
                                pointStyle: "circle", 
                                font: { size: 14 } 
                            }, 
                        fullSize: true, 
                        align: "center" 
                        }, 
                            tooltip: { 
                                boxWidth: 15, 
                                bodyFont: { 
                                    size: 14 
                                } 
                            } 
                        }, 
                        scales: { 
                            x: { 
                                grid: { 
                                    display: false 
                                }, 
                                ticks: { 
                                    padding: 3 
                                } 
                            }, 
                        y: { 
                            ticks: { 
                                callback: (val) => { 
                                    return val !== 0 ? val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") : ""; 
                                }, 
                                    padding: 10 
                                }, 
                                grid: { 
                                    drawBorder: false, 
                                    color: "#323232", 
                                    lineWidth: 1 
                                } 
                            } 
                        }, 
                        responsive: true, 
                        maintainAspectRatio: false, 
                        animation: { duration: 5000 } 
                    } 
                } 
            }; 

    },
    methods: {
        btnClick(i){
            console.log(i);
            this.btnState = i;
        },
        // webCam(){
        //     var video = document.getElementById("#videoElement");
        //     video.addEventListener('')
    
        //     if (navigator.mediaDevices.getUserMedia) {
        //     navigator.mediaDevices.getUserMedia({ video: true })
        //         .then(function (stream) {
        //         video.srcObject = stream;
        //         })
        //         .catch(function (error) {
        //         console.log(error);
        //         });
        //     }
        // }
    }
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    z-index: 1;
    width: 100vw;
    .inner{
        margin: auto;
        width: 70%;
        .btns{
            display: flex;    
        }
        .sensor{
            .abc{
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
    }
    
}
</style>