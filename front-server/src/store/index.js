import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersisterdState from 'vuex-persistedstate'


Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"
const PersisterdState = createPersisterdState({
  paths: ['/AllMusic',

  ],

  reducer: state => ({
    token: state.token,
    users: state.users,
    currentUser: state.currentUser,
    allmovies: state.allmovies,
    music: state.music,
    newmovie: state.newmovie,

  })
})

export default new Vuex.Store({
  plugins: [
    PersisterdState,
    // createPersisterdState()
  ],
  state: {
    articles: [
    ],
    article: { title: "", content: "" },
    token: null,
    movie: [],
    users: [],
    currentUser: '',
    allmovies: [],
    // 팔로잉
    followings: [],
    // 팔로워
    followers: [],
    likeuser: [],
    profile: [],
    moviedetail: [],
    music: [],
    musicdetail: [],
    videoid: null,
    allgenre_dict: {
      '🧐 지적 호기심 충전!': '다큐멘터리',
      '🌟 그냥 심심할 때 킬링타임': '코미디',
      '😭 펑펑 울고 싶을 때': '가족',
      '🎭 미스터리': '미스터리',
      '💑 두근두근 설레고 싶을 때': '멜로/로맨스',
      '🦼 뒤통수가 후끈 반전 스릴러': '스릴러',
      '💥 스트레스 뻥 뚫어버리기': '어드벤처',
      '🗽 미국 서부로 떠나보자': '서부극(웨스턴)',
      '🔫 색다른 전쟁영화 한 편 어때요?': '전쟁',
      '🪐 현실과는 다른 또다른 세계': '판타지',
      '🚦 상상력 풀가동': 'SF',
      '😬 손에 땀을 쥐게 하는 긴장감': '액션',
      '💐 예술의 아름다움': '공연',
      '🌈 영상미 뿜뿜하는 영화': '뮤지컬',
      '🎴 사극아 이리오너라': '사극',
      '🎰 혹시 나도 프로파일러?!': '범죄',
      '👩🏻‍🦰 다양한 사람들의 이야기': '드라마',
      '😱 무서운게 딱 좋아': '공포(호러)',
      '🏫 하이틴 시절이 생각나는': '애니메이션',
      '🍀 무엇을 골라야 할지 모르겠다면?': '기타',
    },
    allgenre: ['🧐 지적 호기심 충전!',
      '🌟 그냥 심심할 때 킬링타임',
      '😭 펑펑 울고 싶을 때',
      '🎭 미스터리',
      '💑 두근두근 설레고 싶을 때',
      '🦼 뒤통수가 후끈 반전 스릴러',
      '💥 스트레스 뻥 뚫어버리기',
      '🗽 미국 서부로 떠나보자',
      '🔫 색다른 전쟁영화 한 편 어때요?',
      '🪐 현실과는 다른 또다른 세계',
      '🚦 상상력 풀가동',
      '😬 손에 땀을 쥐게 하는 긴장감',
      '💐 예술의 아름다움',
      '🌈 영상미 뿜뿜하는 영화',
      '🎴 사극아 이리오너라',
      '🎰 혹시 나도 프로파일러?!',
      '👩🏻‍🦰 다양한 사람들의 이야기',
      '😱 무서운게 딱 좋아',
      '🏫 하이틴 시절이 생각나는',
      '🍀 무엇을 골라야 할지 모르겠다면?'],

    musicgenre_dict: {
      '🤹🏻‍♀️ 둠칫둠칫 춤추고 싶을 때': '댄스/팝',
      '🎤 요즘 대세인 팝송은?': '팝',
      '☔ 감성에 젖고 싶을 때': '발라드',
      '😎 도전! 쇼미더머니': '랩/힙합',
      '🤍 새벽 감성 모음': '인디',
      '💫 일상에서 쌓인 스트레스를 날려줄': '락/메탈',
      '🎆 느낌있는 알앤비': '알앤비/소울',
      '🚘 운전하면서 잠이 확~! 깨고 싶을 때': '트로트',
      '🌁 출퇴근할 때 듣는': '포크/어쿠스틱'

    },

    musicgenre: [
      '🤹🏻‍♀️ 둠칫둠칫 춤추고 싶을 때',
      '🎤 요즘 대세인 팝송은?',
      '☔ 감성에 젖고 싶을 때',
      '😎 도전! 쇼미더머니',
      '🤍 새벽 감성 모음',
      '💫 일상에서 쌓인 스트레스를 날려줄',
      '🎆 느낌있는 알앤비',
      '🚘 운전하면서 잠이 확~! 깨고 싶을 때',
      '🌁 출퇴근할 때 듣는'

    ]
  },
  getters: {
    articles: (state) => state.articles,
    article: (state) => state.article,
    token: (state) => state.token,
    isLogin(state) {
      return state.token ? true : false
    },
    followings: (state) => state.followings,
    followers: (state) => state.followers,
    profile: (state) => state.profile,
    allmovies: (state) => state.allmovies,
    moviedetail: (state) => state.moviedetail,
    newmovie: (state) => state.movie,
    music: (state) => state.music,
    musicdetail: (state) => state.musicdetail,
    currentUser: (state) => state.currentUser,
    article_movie: (state) => state.article?.article_movie,
    article_music: (state) => state.article?.article_music,
    videoid: (state) => `https://www.youtube.com/embed/${state.videoid}`

  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GETARTICLEDETAIL(state, article) {
      state.article = article
      // console.log(13, state.article)
    },
    SIGN_UP(state, token) {
      state.token = token
      // console.log(token)
    },
    SAVE_TOKEN(state, token) {

      state.token = token
      // console.log(state.token, 123)
      router.push({ name: 'MovieView' })
    },
    MOVIE(state, movies) {
      state.movie = movies
    },
    ALLMOVIES(state, allmovies) {
      state.allmovies = allmovies
    },
    SET_CURRENT_USER(state, user) {
      // console.log(123)
      // console.log(user)
      localStorage.setItem("currentUser", user)
      state.currentUser = user
    },
    LIKEUSERS(state, payload) {
      state.likeuser = payload
      // console.log(state.likeuser)
    },
    SET_ARTICLE: (state, article) => (state.article = article),
    FOLLOWCNT(state, payload) {
      state.followings = payload.followings
      state.followers = payload.followers
    },
    GETPROFILE(state, payload) {
      // console.log(payload)
      state.profile = payload
    },
    SET_MOVIE(state, movie) {
      // console.log(movie)
      state.moviedetail = movie
    },
    MUSIC(state, music) {
      // console.log(music)
      state.music = music
    },
    SET_MUSIC(state, music) {
      state.musicdetail = music
    },
    YOUTUBE(state, videoid) {
      state.videoid = videoid
    }
  },
  actions: {
    getArticles(context, movieid) {
      // console.log(context.state.token)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${movieid}/movie_articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMusicArticles(context, musicid) {
      console.log(context.state.token)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${musicid}/music_articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getArticleDetail(context, articlepk) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${articlepk}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('GETARTICLEDETAIL', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      // console.log(payload)
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          // console.log(res.data.key)
          // context.commit('SIGN_UP', res.data.key)
          // const payload = {'key':res.data.key, username}
          context.commit('SAVE_TOKEN', res.data.key)
          context.dispatch("CurrentUser", username)
        })
        .catch(err => alert(err.data.error))
    },
    CurrentUser(context, username) {
      // console.log(123456)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/profile/${username}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, 123456)
          context.commit('SET_CURRENT_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      console.log(payload)
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          // console.log(res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
          localStorage.setItem("token", res.data.key)
          context.dispatch("CurrentUser", username)
        })
        .catch( ()=> alert('로그인에 실패했습니다')  )
    },
    logout(context) {
      context.commit('SAVE_TOKEN', '')
      localStorage.setItem("token", '')
      // alert('로그아웃되었습니다')
      localStorage.setItem("currentUser", '')
      context.commit('SET_CURRENT_USER', '')
      console.log('로그아웃')
      this.router.push({ name: "LoginView" })

    },
    movie(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/newmovie/`,
        // headers : {
        //   Authorization: `Token ${this.state.token}`
        // }
      })
        .then((res) => {
          context.commit('MOVIE', res.data)
        })
    },
    allmovies(context) {
      console.log('allmovie')
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(789)
          // console.log(res.data)
          context.commit('ALLMOVIES', res.data)
        })
        .catch((err => {
          console.log(err)
        })
        )
    },
    getmoviedetail(context, moviepk) {
      console.log(moviepk)
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movie/${moviepk}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('SET_MOVIE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    music(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/music/`,
        // headers: {
        //   Authorization: `Token ${this.state.token}`
        // }
      }).then((res) => {
        // console.log(res);
        context.commit('MUSIC', res.data)
      });
    },
    getmusicdetail(context, musicpk) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/music/${musicpk}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('SET_MUSIC', res.data)
          context.dispatch('searchToApp', res.data.title)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    searchToApp(context, title) {
      // console.log(title)
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: 'AIzaSyCcq6OHCc0tn6GB08nUsm8Dns_21qEvUvQ',
          // AIzaSyA9nD2LNL5jGSXHNJkjcYYIWGCtOZXL7IQ
          // AIzaSyCcq6OHCc0tn6GB08nUsm8Dns_21qEvUvQ
          // AIzaSyDCMeoOGb715FWGfCVv6UWkTUubYVpwDgI
          // AIzaSyASFEFz85zISjCsdhKc9pcln3rk-Nkvp90
          // AIzaSyBus7l-m1RyzfGFq9gs_tjWaL5UNf1OfC0



          part: 'snippet',
          type: 'video',
          q: `${title} MV`
        },
      })
        .then(res => {
          // console.log(789)
          context.commit('YOUTUBE', res.data.items[0].id.videoId)
          // imgsrc = res.data.items[0].id.videoId
          console.log(res.data.items[0].id.videoId, 123)
        })
        .catch(err => {
          console.log(err)
        })
    },

    likeArticle(context, articlePk) {
      console.log(articlePk)
      axios({
        method: "post",
        url: `${API_URL}/api/v1/like/${articlePk}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          // console.log(res.data, 123)
          context.commit('SET_ARTICLE', res.data)

        })
    },
    likeMovie(context, movieid) {
      console.log(movieid)
      axios({
        method: "post",
        url: `${API_URL}/api/v2/movie/like/${movieid}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          // console.log(res.data)
          context.commit('SET_MOVIE', res.data)
          // context.dispatch("allmovies");
        })
    },
    likeMusic(context, musicid) {
      axios({
        method: "post",
        url: `${API_URL}/api/v2/music/like/${musicid}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(res => {
          // console.log(res.data)
          context.commit('SET_MUSIC', res.data)
        })
    },
    follow(context, payload) {
      // console.log(payload)
      const username = payload.username
      // console.log(username, 123)
      axios({
        method: "post",
        url: `${API_URL}/api/v1/accounts/follow/${username}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then(() => {
          // console.log(res)
          context.dispatch('getprofile', username)
        })
    },
    getfollows(context, username) {
      console.log(username)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/profile/${username}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(res)
          const payload = { 'followers': res.data.followers, 'followings': res.data.followings }
          context.commit('FOLLOWCNT', payload)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getprofile(context, username) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/profile/${username}/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
        .then((res) => {
          // console.log(res, 123456)
          context.commit('GETPROFILE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getUser(context, username) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/accounts/profile/${username}`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(res => {
          context.commit('GET_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})


