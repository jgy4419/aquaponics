<template>
    <div class="contain">
        <div class="inner">
            <p class="close" @click="$emit('state')">X</p>
            <p class="title">조명 상태입니다.</p>
        </div>
        <div class="backColor"/>
    </div>    
</template>

<script>
export default {
    // emits: {
    //     'sensorModalState'
    // },
    props: {
        sensorModalState: Number
    },
    mounted(){
        // alert(this.sensorModalState);
    }
}
</script>

<style lang="scss" scoped>
.contain {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    .backColor {
        position: absolute;
        top: 0;
        width: 100%;
        height: 100%;
        background: rgba($color: #000000, $alpha: 0.5);
    }
    .inner {
        position: relative;
        top: 10%;
        margin-top: 20%;
        border-radius: 20px;
        z-index: 10;
        width: 70vw;
        height: 80vh;
        margin: auto;
        background-color: #fff;
        .close {
            position: absolute;
            cursor: pointer;
            top: 20px;
            right: 20px;
            font-size: 30px;
            font-weight: 700;
            color: #333;
        }
    }
}
</style>