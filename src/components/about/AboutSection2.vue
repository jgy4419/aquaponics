<template>
    <div class="contain">
        <div class="inner">
            <p class="smallTitle">This site</p>
            <h1 class="title">다양한 센서 데이터로 <br/>실시간으로 아쿠아포닉스를 확인해요.</h1>
            <div class="contentBox">
                <div class="content">
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            content: {

            }
        }
    }    
}
</script>

<style lang="scss" scoped>
.contain {
    width: 100vw;
    height: 100vh;
    .inner {
        width: 1100px;
        margin: auto;
        .smallTitle{
            color: #94B49F;
            font-size: 20px;
            font-weight: 700;
        }
        .title{
            line-height: 1.6;
            font-size: 40px;
            margin-top: 20px;
        }
    }
}
</style>