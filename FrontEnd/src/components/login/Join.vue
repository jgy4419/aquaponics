<template>
    <div>
        <div class="container">
            <div class="inner">
                <form action="/api/join" method="post" class="login" target="iframe1"> 
                    <p>회원가입</p>
                    <div>
                        <label for="input" class="labelName">이메일</label>
                        <input v-model="idInput" class="input" name="mail" type = "email" placeholder = 'ex) user@naver.com (필수)'>
                        <br/>
                        <button class="btn id" type="button" @click="idOverlap()">아이디 중복 검사</button>
                    </div>
                    <div v-for="value, i in value" :key="i">
                        <label for="input" class="labelName">{{label[i]}}</label>
                        <input class="input" :v-model="model[i]" :name="name[i]" :type = type[i] :placeholder = value>
                    </div>
                    <button class="btn nickname" type="button" @click="nicknameOverlap()">닉네임 중복 검사</button>
                    <br/><br/>
                    <div class="sex">
                        <label>성별을 선택해주세요.</label>
                        <select name="sex">
                            <option value="남">남</option>
                            <option value="여">여</option>
                        </select>
                    </div>
                    <input @click="loginCondition()" class="loginBtn" type="submit" value="회원가입"/>
                    <iframe id="iframe1" name="iframe1" style="display:none"></iframe>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return{
            name: ['password', 'rePassword', 'name', 'phonenumber', 'address', 'introduction', 'nickname'],
            label: ['비밀번호', '비밀번호 재확인', '이름', '전화번호', '주소', '자기소개', '닉네임'],
            value: ['비밀번호를 입력하세요 (필수)', '비밀번호를 한번 더 입력해주세요', '이름 (필수)', '전화번호 (필수)', '주소 (필수)', '자기소개', '닉네임(필수)'],
            type: ['password','password','text', 'tel', 'text', 'text', 'text'],
            checkId: false,
            checkNickname: false,
            idInput: '',
            model: ['paddword', 'rePassword', 'name', 'phonename', 'address', 'introduction', 'nicknameInput'],
            nicknameInput: '',
            grant: 0,

        }
    },
    methods: {
        // profileImg(input){
            /* 
                1. id(email)가 DB에 있는 것과 동일해야 됨.
                2. 비밀번호가 동일해야 됨.
                3. 필수부분이 다 채워져야 됨.f
            */
        loginCondition(){
            const inputs = document.querySelectorAll('.input');
            if(inputs[1].value !== inputs[2].value){
                alert('비밀번호가 다릅니다!');
                // (필수 부분이 비어있으면)
            // }else if(this.checkId === false || this.checkNickname === false){
            }else if(this.checkId === false || this.checkNickname === false){
                // id 유효성 검사가 되지 않으면
                alert('id나 닉네임 중복 검사를 다시 해주세요.');
            }else if(inputs[0].value == "" || inputs[1].value == "" || inputs[3].value == "" || inputs[4].value == "" || inputs[5].value == "" || inputs[7].value == ""){
                // 필수 input에 빈칸 유무
                alert('(필수) 부분이 비어있습니다!');
            }else{
                // 회원 가입을 성공하면, 입력된 정보들을 DB에 저장시켜주기.
                alert('환영합니다 오운완 입니다!');
                location.href = '/';
            }
        },
        idOverlap(){
            axios.post('/api/checkid', {mail: this.idInput})
            .then(res => {
                this.checkId = res.data.checkid; // true / false 유무
                if(this.checkId === false){
                    alert('아이디 비밀번호가 겹칩니다.');
                    this.checkId = false;
                }else if(this.checkId === true){
                    alert('사용할 수 있는 아이디입니다.');
                    this.checkId = true;
                }
            }).catch(err => console.log(err));
        },
        nicknameOverlap(){
            let inputValue = document.querySelectorAll('.input');
            axios.post('/api/checkNickname', {nickname: inputValue[7].value})
            .then(res => {
                this.checkNickname = res.data.checkNickname;
                if(this.checkNickname === false){
                    alert('닉네임이 겹칩니다!')
                    this.checkNickname = false;
                }else if(this.checkNickname === true){
                    alert('사용할 수 있는 닉네임입니다.');
                    this.checkNickname = true;
                }
            }).catch(err => console.log(err));
        }
    }
}
</script>

<style lang="scss" scoped>
.container{
    position: absolute;
    z-index: 100;
    margin: auto;
    top: 10%;
    left: 0;
    right: 0;
    width: 30vw;
    // border: 2px solid #333;
    border-radius: 10px;
    padding-bottom: 3%;
    .inner{
        width: 500px;
        color: #636363;
        p{
            font-size: 20px;
            font-weight: 700;
        }
        // .login{
            text-align: center;
            .btn.id, .btn.nickname{
                width: 150px;
                height: 40px;
                border-radius: 10px;
                // background-color
            }
            .labelName{
                // width: 100%;
                // padding-top: 10px;
                margin: 20px 0px 0px 100px;
                display: flex;
                // flex-direction: column;
            }
            input{
                font-size: 15px;
                width: 300px;
                height: 50px;
                border-radius: 10px;
                margin-top: 10px;
                border: 1px solid rgb(181, 181, 181);
                // border: 0;
                padding-left: 10px;
            }
            .loginBtn:hover{
                background-color: #94B49F;
                color: #fff;
            }
            .sex{
                margin: 10px auto;
                width: 200px;
                display: flex;
                justify-content: space-between;
            }
            .fileBox{
                width: 350px;
                margin: auto;
                display: flex;
                justify-content: space-between;
                font-size: 13px;
                text-align: end;
                label{
                    margin-top: 12px;
                }
                .file{
                    width: 200px;
                    border: 0;
                }
            }
            .priview{
                border-radius: 10px;
                width: 300px;
            }
            .loginBtn{
                background-color: #B4CFB0;
                color: #fcf3f3;
                font-weight: 900;
                box-sizing:content-box;
                border: 0px;
                transition: .3s;
                cursor: pointer;
            }
        // }
        .btn.id, .btn.nickname{
            margin: 20px 35% 0px 0px;
            font-weight: 700;
        }
    }
}
</style>