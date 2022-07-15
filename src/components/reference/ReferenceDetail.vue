<template>
    <div class="referenceModalContain">
        <div class="backColor"/>
        <div class="inner">
            <!-- 부모한테 state라는 메시지를 보내기 => ReferenceType.vue -->
            <p @click="$emit('state')" class="close">X</p>
            <h1 class="name">{{name}}</h1>
            <img :src="this.img" alt="받은 데이터 사진">
            <div class="description">
                <h2>설명</h2>
                <p class="descriptionText">{{description}}</p>
            </div>
            <div class="advantages">
                <h2>장점</h2>
                <p class="advantagesText">상업적 규모에 적합. 식물과 물고기에서 많은 수확이 가능.</p>
            </div>
            <div class="disadvantages">
                <h2>단점</h2>
                <p class="disadvantagesText">고형물을 걸러내는 필터가 필요하고 열매 없는 잎채소만 재배가능.</p>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    emits: [
        'modalState'
    ],
    props: {
        modalState: Number,
        name: String,
        img: String,
        description: String
    },
}
</script>

<style lang="scss" scoped>
    .referenceModalContain{
        position: fixed;
        z-index: 1;
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
    }
</style>