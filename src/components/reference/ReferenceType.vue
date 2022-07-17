<template>
    <div class="reference-type-contain">
        <!-- props로 보낼 때 this. 붙여주기 -->
        <!-- 자식한테 state라는 메시지를 받으몀ㄴ modalState를 0으로 변경해달라는 뜻. -->
        <ReferenceDetail @state="modalState = 0" class="detailModal"
         v-if="modalState === 1" 
         :modalState="this.modalState"
         :name="this.modalData.name"
         :img="this.modalData.img"
         :description="this.modalData.description"
         :advantages="this.modalData.advantages"
         :disadvantages="this.modalData.disadvantages"
         :typeState="this.type.state"/>
         <!-- <ReferenceDetail/> -->
        <div class="typeState">
            <ul>
                <li class="stateBtn" v-for="data, i in type.modal.length" :key="i"
                @click="type.state = i">{{type.modal[i]}}</li>
            </ul>
        </div>
        <div class="systemData" v-if="type.state === 0">
            <div class="dataBox" @click="openModal(i, 0)" v-for="data, i in datas.system.length" :key="i"
            :style="{backgroundImage: `url(${datas.system[i].img})`}">
                <div class="backColor"/>
                <p class="dataTitle">{{datas.system[i].name}}</p>
            </div>
        </div>
        <div class="piscesData" v-if="type.state === 1">
            <div class="dataBox" @click="openModal(i, 1)" v-for="data, i in datas.pisces.length" :key="i"
            :style="{backgroundImage: `url(${datas.pisces[i].img})`}">
                <div class="backColor"/>
                <p class="dataTitle">{{datas.pisces[i].name}}</p>
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
            datas: [],
            modalState: 0,
            modalData: {
                name: '',
                img: '',
                description: '',
                advantages: '',
                disadvantages: ''
            },
            resModal: ''
        }
    },
    created(){
        this.datas = JSON.stringify(data);
        this.datas = JSON.parse(this.datas);
    },
    methods: {
        // 첫 번째 인자는 어디 클릭했는지 두 번째 인자는 구조 Modal에서 클릭했는지 물고기 Modal에서 클릭했는지 구분 시켜준다.
        openModal(index, open){
            // 모달 열어주고 클릭한 부분의 데이터를 this.modalData객체 안에 넣어준다.
            this.modalState = 1; 
            if(open === 0){
                // let propsValue = Object.values(this.datas.system[index]);
                // let propsKey = this.modalData;
                // console.log(propsKey);
                // console.log(Object.assign(propsKey, propsValue));
                // this.modalData = Object.assign(propsKey, propsValue);
                // Object.keys(this.modalData) = Object.values(this.datas.system)
                this.modalData.name = this.datas.system[index].name;
                this.modalData.img = this.datas.system[index].img;
                this.modalData.description = this.datas.system[index].description;
                this.modalData.advantages = this.datas.system[index].advantages;
                this.modalData.disadvantages = this.datas.system[index].disadvantages;
                console.log(this.modalData);
            }else if(open === 1){
                this.modalData.name = this.datas.pisces[index].name;
                this.modalData.img = this.datas.pisces[index].img;
                this.modalData.description = this.datas.pisces[index].description;
                console.log(this.modalData);
            }
        }
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
                    transition: .3s;
                    border-radius: 5px;
                    cursor: pointer;
                }
                li:hover{
                    background-color: #E5E3C9;
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