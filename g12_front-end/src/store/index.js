import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: null,
      userId: '',
  },
  mutations: {
    set_token(state, token) {
      state.token = token;
      localStorage.token = token
    },
    del_token(state) {
      state.token = null;
      localStorage.removeItem('token')
    }
  },
  actions: {
  },
  modules: {
  }
})
