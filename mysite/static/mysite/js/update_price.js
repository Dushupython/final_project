const vm = new Vue({
        el: '#app',
        data: {
          results: []
        },
        methods: {
    updatePosts: function () {
          axios.get('http://127.0.0.1:8000/get_data/').then(response =>{
        this.results = response.data;
        setTimeout(this.updatePosts, 2000);
      });
    }
  },
  created: function () {
    this.updatePosts();
  }
  })
