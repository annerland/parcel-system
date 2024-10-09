import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/home/home.vue';
import Layout from './components/ui/layout/Layout.vue';

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: Home },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;