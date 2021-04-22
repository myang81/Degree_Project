import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: null,
    userId: '',
  },
  mutations: {
    set_token(state, datas) {
      state.token = datas[0];
      state.userId = datas[1]
      localStorage.token = datas[0]
      localStorage.userId = datas[1]
    },
    set_temporary_token(state, datas) {
      console.log(datas)
      // state.token = datas[0];
      // state.userId = datas[1]
    },
    del_token(state) {
      state.token = null;
      localStorage.removeItem('token')
      state.userId = null;
      localStorage.removeItem('userId')
    }
  },
  actions: {
  },
  modules: {
  }
})
