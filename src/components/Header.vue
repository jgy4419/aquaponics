<template>
    <div class="menuBox">
        <header>
            <div class="headerBox">
                <router-link to="/">
                    <p class="logo">로고</p>
                </router-link>
                <div class="menuListIcon" @click="hamburger()">
                    <div class="line" v-for="a in 3" :key="a"></div>
                </div>
            </div>
        </header>
        <div class="menu">
            <div class="inner">
                <ul>
                    <!-- li 버튼 누르면 메뉴에 이벤트 없어지도록 하기. -->
                    <router-link v-for="a, i in headerData.loginBefore.length" :key="i" 
                    :to="headerUrl.loginBefore[i]">
                        <li class="menuList">
                            {{headerData.loginBefore[i]}}
                        </li>
                    </router-link>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            headerData: {
                loginBefore: ['main', 'login', 'reference', 'about'],
                loginAfter: ['main', 'myPage', 'reference', 'about', 'logout']
            },
            headerUrl: {
                loginBefore: ['/', '/login', '/reference', '/about'],
                loginAfter: ['/', '/myPage', '/reference', '/about', '']
            }
        }
    },
    methods: {
        hamburger(){
            let line = document.querySelectorAll('.line');
            let menu = document.querySelector('.menu');
            let menuBox = document.querySelector('.menuBox');
            for(var i = 0; i < line.length; i++){
                line[i].classList.toggle('event');
            }
            // 햄버거 누르면 옆에 메뉴 생성해주기. + 배경 어둡게 해주기.
            menu.classList.toggle('event');
            menuBox.classList.toggle('event');
        },
    },
    watch: {
        '$route' (){
            document.querySelector('.menu').classList.remove('event');
            let line = document.querySelectorAll('.line');
            let menuBox = document.querySelector('.menuBox');
            for(var i = 0; i < line.length; i++){
                line[i].classList.remove('event');
                menuBox.classList.remove('event');
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.menuBox{
    position: relative;
    z-index: 2;
    overflow-x: hidden;
    header{
        width: 100vw;
        // height: 9vh;
        // background-color: rgb(215, 215, 215);
    .headerBox{
        margin: auto;
        padding-top: 25px;
        width: 80vw;
        display: flex;
        justify-content: space-between;
        .logo{
            position: relative;
            z-index: 100;
            font-size: 20px;
            font-weight: 700;
            color: #333;
        }
        // 햄버거 아이콘
        .menuListIcon{
            position: fixed;
            top: -8px;
            right: 10%;
            cursor: pointer;
            z-index: 1000;
            box-sizing: border-box;
            padding: 30px;
            width: 50px;
            height: 50px;
            .line{
                width: 30px;
                cursor: pointer;
                position: absolute;
                border-bottom: 5px solid #333;
            }
            .line:nth-child(2){
                margin-top: 10px;
            }
            .line:nth-child(3){
                animation-name: hamburgetBottom;
                margin-top: 20px;
            }
            .line.event:nth-child(1){
                animation-name: hamburgerTop;
                animation-duration: 1s;
                animation-fill-mode: forwards;
            }
            .line.event:nth-child(2){
                opacity: 0;
            }
            .line.event:nth-child(3){
                animation-name: hamburgerBottom;
                animation-fill-mode: forwards;
                animation-duration: 1s;
            }
            @keyframes hamburgerTop{
                0%{
                    
                    transform: rotate(0deg);
                }
                50%{
                    transform: translateY(10px);
                }
                100%{
                    transform: translateY(10px)rotateZ(50deg);
                }
            }
            @keyframes hamburgerBottom{
                0%{
                    transform: rotate(0deg);
                }
                50%{
                    transform: translateY(-10px);
                }
                100%{
                    transform: translateY(-10px) rotateZ(-50deg);
                    }
                }
            }
        }
    }
    .menu{
        position: fixed;
        margin-top: -48px;
        z-index: 2;
        opacity: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.7);
        transition: .7s;
        transform: translateX(400px);
        .inner{
            position: absolute;
            right: 0;
            background-color: #789395;
            width: 30%;
            height: 100vh;
            // margin: auto;
            ul{
                margin-left: 10%;
                .menuList{
                    transition: .3s;
                    margin-top: 80px;
                    font-size: 40px;
                    font-weight: 500;
                    color: #fff;
                    cursor: pointer;
                }
                .menuList:hover{
                    color: #E5E3C9;
                }
            }
        }
        @media screen and (max-width: 800px){
            .inner{
                width: 40%;
                ul{
                    .menuList{
                        font-size: 20px;
                    }
                }
            }
        }
    }
    .menu.event{
        z-index: 10;
        height: 100vh;
        opacity: 1;
        transform: translateX(0px);
    }
}
.menuBox.event{
    z-index: 1000;
}
</style>
