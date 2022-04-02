<template>
    <header>
        <div class="headerBox">
            <p class="logo">로고</p>
            <div class="menu">
                <ul>
                    <li class="menuList" v-for="menu, i in headerData.loginBefore" :key="i">
                        <router-link :to="headerUrl.loginBefore[i]">
                            {{menu}}
                        </router-link>
                    </li>
                </ul>
            </div>
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
    width: 100vw;
    height: 70px;
    // background-color: rgb(215, 215, 215);
    .headerBox{
        margin: auto;
        padding-top: 25px;
        width: 90vw;
        display: flex;
        justify-content: space-between;
        .logo{
            font-size: 20px;
            font-weight: 700;
            color: #333;
        }
        .menu{
            width: 200px;
            ul{
                display: flex;
                justify-content: space-between;
                color: rgb(226, 226, 226);
                li a{
                    font-weight: 700;
                    color: rgb(172, 172, 172);
                }
                li a:hover{
                    color: #333;
                }
            }
        }
    }
}
</style>
