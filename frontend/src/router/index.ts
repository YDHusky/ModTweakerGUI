import {createRouter, createWebHistory} from 'vue-router'
import MainLayout from "@/components/layout/MainLayout.vue";
import ModTweakerPage from "@/views/modTweaker/ModTweakerPage.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'MainLayout',
            component: MainLayout,
            children: [
                {
                    path: '',
                    name: 'ModTweakerPage',
                    component: ModTweakerPage
                }
            ]
        },

    ]
})

export default router
