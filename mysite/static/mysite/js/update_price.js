new Vue({
    el: '#price',
    data:{
        price: []
    },
    created: function () {
        const vm = this;
        axios.get('http://127.0.0.1:8000/get_data/')
        .then(function (response) {
        console.log(response.data)
            })
    }
})