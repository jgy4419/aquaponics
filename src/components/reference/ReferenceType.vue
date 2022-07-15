<template>
    <div class="reference-type-contain">
        <!-- props로 보낼 때 this. 붙여주기 -->
        <!-- 자식한테 state라는 메시지를 받으몀ㄴ modalState를 0으로 변경해달라는 뜻. -->
        <ReferenceDetail @state="modalState = 0" class="detailModal"
         v-if="modalState === 1" :modalState="this.modalState"/>
        <div class="typeState">
            <ul>
                <li v-for="data, i in type.modal.length" :key="i"
                @click="type.state = i">{{type.modal[i]}}</li>
            </ul>
        </div>
        <div class="systemData" v-if="type.state === 0">
            <div class="dataBox" @click="modalState = 1" v-for="data, i in systemData.name.length" :key="i"
            :style="{backgroundImage: `url(${systemData.imgUrl[i]}`}">
                <div class="backColor"/>
                <p class="dataTitle">{{systemData.name[i]}}</p>
            </div>
        </div>
        <div class="piscesData" v-if="type.state === 1">
            <div class="dataBox" @click="modalState = 1" v-for="data, i in piscesData.name.length" :key="i"
            :style="{backgroundImage: `url(${piscesData.imgUrl[i]}`}">
                <div class="backColor"/>
                <p class="dataTitle">{{piscesData.name[i]}}</p>
            </div>
        </div>
    </div>
</template>

<script>
// 자료실에 있는 데이터 불러오기.
import data from '../../referenceData.json';
import ReferenceDetail from './ReferenceDetail.vue';
export default {
    components:{
        ReferenceDetail,
    },
    data(){
        return{
            type: {
                state: 0,
                modal: ['구조', '물고기']
            },
            systemData:{
                name: [],
                description: [],
                imgUrl: []
            },
            piscesData:{
                name: [],
                description: [],
                imgUrl: []
            },
            modalState: 0,
        }
    },
    mounted(){
        console.log(data);
        for(let i = 0; i < data.system.length; i++){
            this.systemData.name.push(data.system[i].name);
            this.systemData.description.push(data.system[i].description);
            this.systemData.imgUrl.push(data.system[i].img);
        }
        for(let i = 0; i < data.pisces.length; i++){
            this.piscesData.name.push(data.pisces[i].name);
            this.piscesData.description.push(data.pisces[i].description);
            this.piscesData.imgUrl.push(data.pisces[i].img);
        }
        console.log(this.piscesData);
    }
}
</script>

<style lang="scss" scoped>
    .reference-type-contain{
        position: relative;
        z-index: 2;
        width: 80vw;
        height: 500px;
        .typeState{
            width: 100%;
            height: 100px;
            ul{
                display: flex;
                gap: 20px;
                li{
                    box-sizing: border-box;
                    text-align: center;
                    padding-top: 15px;
                    width: 90px;
                    height: 50px;
                    font-size: 20px;
                    font-weight: 700;
                    color: #fff;
                    background-color: #B4CFB0;
                    border-radius: 5px;
                    cursor: pointer;
                }
            }
        }
        .systemData, .piscesData{
            margin: auto;
            width: 90%;
            height: 700px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            text-align: center;
            // background-color: #333;
            .dataBox{
                position: relative;
                width: 400px;
                height: 300px;
                margin: 10px;
                // border: 1px solid #333;
                background-repeat: no-repeat;
                background-size: cover;
                cursor: pointer;
                .backColor{
                    transition: .2s;
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    background-color: #778574;
                    opacity: 0;
                }
                .dataTitle{
                    position: absolute; 
                    top: 40%;
                    width: 400px;
                    height: 300px;
                    color: #fff;
                    font-size: 30px;
                    opacity: 0;
                    transition: .6s;
                    transform: translateY(60px);
                }
            }
            .dataBox:hover{
                .backColor{
                    opacity: .95;
                }
                .dataTitle{
                    opacity: 1;
                    transform: translateY(0px);
                }
            }
        }
    }
</style>