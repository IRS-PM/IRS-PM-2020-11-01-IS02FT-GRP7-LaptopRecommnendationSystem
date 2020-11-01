import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Zh from "@/views/Zh";
import Zh2 from "@/views/Zh2";
import En from "@/views/En";
import En2 from "@/views/En2";
import Output from "@/components/Output";
import OutputEn from "@/components/OutputEn";
// import HelloWorld from "@/components/HelloWorld";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title: '电脑推荐',
        },
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
        meta: {
            title: 'About'
        }
    },
    {
        path: '/zh-cn-1',
        name: 'QuestionnaireCh',
        component: Zh,
        meta: {
            title: '电脑推荐系统',
        },
    },
    {
        path: '/zh-cn-2',
        name: 'QuestionnaireCh_2',
        component: Zh2,
        meta: {
            title: '电脑推荐系统'
        },
    },
    {
        path: '/en-1',
        name: 'QuestionnaireEn',
        component: En,
        meta: {
            title: 'Notebook Recommender',
        }
    },
    {
        path: '/en-2',
        name: 'QuestionnaireEn_2',
        component: En2,
        meta: {
            title: 'Notebook Recommender',
        }
    },
    {
        path: '/output',
        name: 'Output',
        component: Output,
        meta: {
            title: '推荐结果'
        },
    },
    {
        path: '/output-en',
        name: 'OutputEn',
        component: OutputEn,
        meta: {
            title: 'Result'
        },
    },

]


const router = new VueRouter({
    routes,
})

router.beforeEach((to, from, next) => {
    /* 路由发生变化修改页面title */
    if (to.meta.title) {
        document.title = to.meta.title
    }
    next()
})

export default router
