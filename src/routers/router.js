import {createWebHistory, createRouter} from "vue-router";
// 메인 페이지
import Main from '../components/Main/Main'

// 로그인 페이지
import Login from '../components/login/Login';
import Join from '../components/login/Join';
import SearchId from '../components/login/SearchId';
import searchPw from '../components/login/SearchPw';
import About from '../components/about/About'

// 마이페이지 
import MyPage from '../components/myPage/MyPage'


const routes = [
    {
        path: "/",
        component: Main
    },
    {
        path: "/login",
        component: Login
    },
    {
        path: "/login/join",
        component: Join
    },
    {
        path: "/login/searchid",
        component: SearchId
    },
    {
        path: "/login/searchpw",
        component: searchPw
    },
    {
        path: "/MyPage",
        component: MyPage
    },
    {
        path: "/about",
        component: About
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;