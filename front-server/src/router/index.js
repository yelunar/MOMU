import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import MusicArticleView from '@/views/MusicArticleView'
import CreateView from '@/views/CreateView'
import MusicCreateView from '@/views/MusicCreateView'
import UpdateView from '@/views/UpdateView'
import DetailView from '@/views/DetailView'
import MusicArticleDetailView from '@/views/MusicArticleDetailView'
import MovieView from '@/views/MovieView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import LogoutView from '@/views/LogoutView'
import AllMovieView from '@/views/AllMovieView'
import MovieDetailView from '@/views/MovieDetailView'
import MusicDetailView from '@/views/MusicDetailView'
import ProfileView from '@/views/ProfileView'
import AllMusicView from '@/views/AllMusicView'
import UserUpdateView from '@/views/UserUpdateView'
import searchView from '@/views/searchView'
import store from '@/store/index.js'
import NotFound from "@/views/NotFoundView.vue";

Vue.use(VueRouter)


const routes = [

  {
    path: "/notFound",
    name: "notFound",
    component: NotFound
  },

  {
    path: '/article/:movieid',
    name: 'ArticleView',
    component: ArticleView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }

  },

  {
    path: '/musicarticle/:musicid',
    name: 'MusicArticleView',
    component: MusicArticleView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/create/:movieid',
    name: 'CreateView',
    component: CreateView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },



  {
    path: '/musiccreate/:musicid',
    name: 'MusicCreateView',
    component: MusicCreateView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/update/:id',
    name: 'UpdateView',
    component: UpdateView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },


  {
    path: '/AllMovie',
    name: 'AllMovieView',
    component: AllMovieView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/searchView',
    name: 'searchView',
    component: searchView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/MovieDetailView/:movieid',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/MusicDetailView/:musicid',
    name: 'MusicDetailView',
    component: MusicDetailView
  },
  {
    path: '/ProfileView/:userid',
    name: 'ProfileView',
    component: ProfileView,

    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/userupdate',
    name: 'UserUpdateView',
    component: UserUpdateView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,

    // beforeEnter(to, from, next) {
    //   const islogin = store.getters.isLogin
    //   // console.log(islogin)
    //   if (islogin === true) {
    //     next({ name: 'MovieView' })
    //   } else {
    //     next()
    //   }
    // }
  },


  {
    path: '/logout',
    name: 'LogoutView',
    component: LogoutView
  },

  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/:id',
    name: 'MusicArticleDetailView',
    component: MusicArticleDetailView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: '/AllMusic',
    name: 'AllMusicView',
    component: AllMusicView,
    beforeEnter(to, from, next) {
      const islogin = store.getters.isLogin
      console.log(islogin)
      if (islogin === false) {
        alert('로그인이 필요한 서비스입니다')
        next({ name: 'LogInView' })
      } else {
        next()
      }
    }
  },

  {
    path: "/:pathMatch(.*)*",
    redirect: "/notFound"
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
