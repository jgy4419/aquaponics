<template>
    <div>
        <div class="container">
            <div class="inner">
                <form action="/searchid" method="post" class="login"> 
                    <p>비밀번호 찾기</p>
                    <div v-for="value, i in value" :key="i">
                        <input :type = type[i] :placeholder = value>
                    </div>
                    <input class="loginBtn btn" type="submit" value="찾기">
                </form>
                <ul class="loginList">
                        <li v-for="loginList, i in loginList" :key="i">
                            <router-link :to = route[i]>
                                {{loginList}}
                            </router-link>
                        </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            value: ['아이디를 입력하세요', '이름', 'Email', '휴대폰 번호'],
            type: ['text', 'text', 'email', 'tel'],
            loginList: ['로그인', '회원가입', '아이디 찾기'],
            route: ['/login', '/login/Join', '/login/SearchId']
        }
    }
}
</script>

<style lang="scss" scoped>
.container{
    position: absolute;
    margin: auto;
    top: 20%;
    left: 0;
    right: 0;
    width: 40vw;
    // border: 2px solid #333;
    border-radius: 10px;
    padding-bottom: 3%;
    .inner{
        color: #636363;
        p{
            font-size: 20px;
            font-weight: 700;
        }
        .login{
            text-align: center;
            input{
                font-size: 15px;
                width: 300px;
                height: 50px;
                border-radius: 10px;
                margin-top: 10px;
                border: 2px solid rgb(181, 181, 181);
                padding-left: 10px;
            }
        }
        .loginList{
            margin-top: 30px;
            display: flex;
            justify-content: space-between;
            cursor: pointer;
        }
    }
}
</style>