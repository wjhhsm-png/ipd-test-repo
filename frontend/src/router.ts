import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import Dashboard from './views/Dashboard.vue'
import Projects from './views/Projects.vue'
const router=createRouter({history:createWebHistory(),routes:[{path:'/',redirect:'/dashboard'},{path:'/login',component:Login},{path:'/dashboard',component:Dashboard},{path:'/projects',component:Projects}]})
export default router
