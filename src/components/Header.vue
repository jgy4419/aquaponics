<template>
    <header>
        <div class="inner">
            <ul class="headerBox">
                <router-link :to="headerUrl.loginBefore[i]" v-for="data, i in headerUrl.loginBefore.length" :key="i">
                    <li>
                        {{headerData.loginBefore[i]}}
                    </li>
                </router-link>
            </ul>
        </div>
    </header>
</template>

<script>
export default {
    data(){
        return{
            headerData: {
                loginBefore: ['main', 'login'],
                loginAfter: ['main', 'myPage', 'logout']
            },
            headerUrl: {
                loginBefore: ['/', '/login'],
                loginAfter: ['/', '/myPage', '']
            }
        }
    }
}
</script>

<style lang="scss" scoped>
header{
    position: relative;
    width: 100vw;
    height: 80px;
    background-color: #E5E3C9;
    .inner{
        position: absolute;
        margin: auto;
        width: 250px;
        right: 0;
        ul{
            padding: 13% 15%;
            display: flex;
            justify-content: space-between;
            li{
                font-size: 16px;
                font-weight: 700;
                cursor: pointer;
            }
        }
    }
}
</style>
