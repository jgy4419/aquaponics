<template>
    <div class="referenceModalContain">
        <div class="backColor"/>
        <div class="inner">
            <!-- 부모한테 state라는 메시지를 보내기 => ReferenceType.vue -->
            <p @click="$emit('state')" class="close">X</p>
            <h1 class="name">{{propsData.name}}</h1>
            <img :src="propsData.img" alt="받은 데이터 사진">

            <div class="description">
                <h2>설명</h2>
                <p v-for="description in propsData.description" :key="description" class="descriptionText">{{description}}</p>
            </div>
            <div class="pros-and-cons">
                <div class="advantages">
                    <h2>장점</h2>
                    <p class="advantagesText">{{propsData.advantages}}</p>
                </div>
                <div class="disadvantages">
                    <h2>단점</h2>
                    <p class="disadvantagesText">{{propsData.disadvantages}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    emits: [
        'modalState'
    ],
    data(){
        return{
            propsData: {},
        }
    },
    props: {
        typeState: Number,
        modalState: Number,
        datas: Array,
        dataIndex: Number
    },
    mounted(){
        if(this.typeState === 1){
            document.querySelector('.pros-and-cons').style.display = 'none';
            this.propsData = this.datas.pisces[this.dataIndex];
        }else if(this.typeState === 0){
            this.propsData = this.datas.system[this.dataIndex];
        }
    }
}
</script>

<style lang="scss" scoped>
    .referenceModalContain{
        position: fixed;
        z-index: 10;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        .backColor {
            position: absolute;
            width: 100%;
            height: 100%;
            background: rgba($color: #000, $alpha: .7);
        }
        .inner{
            position: absolute;
            overflow-y: scroll;
            width: 60vw;
            height: 80vh;
            background-color: #fff;
            border-radius: 20px;
            text-align: center;
            .close{
                position: absolute;
                top: 20px;
                right: 20px;
                font-size: 30px;
                font-weight: 700;
                cursor: pointer;
            }
            .name{
                margin-top: 30px;
                font-size: 30px;
            }
            img{
                width: 450px;
                height: 300px;
                margin-top: 20px;
                border-radius: 20px;
            }
            .description, .advantages, .disadvantages{
                margin: auto;
                width: 50%;
                height: 100px;
                h2{
                    text-align: left;
                    color: #333;
                    margin-top: 30px;
                }
                .descriptionText, .advantagesText, .disadvantagesText{
                    text-align: left;
                    margin-top: 10px;
                    font-size: 18px;
                    font-weight: 500;

                }
            }
        }
        @media screen and (max-width: 900px){
            .inner{
                width: 90%;
                .close{
                    font-size: 25px;
                }
                .name{
                    font-size: 20px;
                }
                img{
                    width: 80%;
                    height: 280px;
                }
                .description, .advantages, .disadvantages{
                    h2{
                        font-size: 20px;
                    }
                    .descriptionText, .advantagesText, .disadvantagesText{
                        font-size: 16px;
                    }
                }
            }
        }
    }
</style>