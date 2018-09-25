import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import Movies from '@/components/pages/Movies'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Movies',
      component: Movies
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})
