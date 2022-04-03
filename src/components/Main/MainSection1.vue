<template>
    <div class="contain">
        <div class="inner">
            
        </div>
    </div>
</template>

<script>
// 배경 이미지 => https://images.roa.ai/articles/2019/02/49151083_2380361025372621_1976658500691951616_n.jpg
export default {
    
}
</script>

<style lang="scss" scoped>
.contain{
    position: relative;
    z-index: 10;
    width: 100vw;
    height: 90vh;
    // background-image: url('https://images.roa.ai/articles/2019/02/49151083_2380361025372621_1976658500691951616_n.jpg');
    background-repeat: no-repeat;
    background-size: 100%;
    .inner{
        z-index: 10;
        position: absolute;
        left: 0;
        right: 0;
        margin: auto;
        width: 80%;
        background-color: #333;
    }
}
</style>