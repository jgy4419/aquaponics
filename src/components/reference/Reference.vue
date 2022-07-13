<template>
    <div class="referenceContain" style="margin-top: 30px">
        <div class="inner">
            <section class="sectionHead">
                <p class="subTitle">Reference</p>
                <h1 class="mainTitle">자료실</h1>
                <hr/>
                <div class="description">
                    <p>
                        처음 아쿠아포닉스를 키우시는 분들이 어떤 구조로 만들면 좋을지, 또는 어떤 어류를 같이 키워야 좋은지를
                        알 수 있는 자료들이 있는 페이지입니다.
                    </p> 
                </div>
            </section>
            <ReferenceType/>
        </div>
    </div>    
</template>

<script>
import ReferenceType from './ReferenceType.vue';
export default {
    components: {
        ReferenceType
    }
}
</script>

<style lang="scss" scoped>
.referenceContain{
    position: relative;
    width: 100vw;
    height: 100vh;
    .inner{
        width: 80vw;
        margin: auto;
        .sectionHead{
            height: 300px;
            .subTitle{
                font-size: 18px;
                font-weight: 700;
                line-height: 2em;
                color: #94B49F;
            }
            .mainTitle{
                font-size: 50px;
                font-weight: 700;
                color: #333;
                margin-bottom: 10px;
            }
            hr{
                border: 1px solid rgb(216, 216, 216);
            }
            .description{
                width: 50vw;
                margin: auto;
                p{
                    margin-top: 30px;
                    line-height: 1.5em;
                    font-size: 25px;
                    font-weight: 600;
                    color: #333;
                }
            }
        }
    }
}
</style>