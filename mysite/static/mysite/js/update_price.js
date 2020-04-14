new Vue({
    el: '#price',
    created: function () {
        const vm = this;
        axios.get('/get_data/')
        .then(function (response) {
        console.log(response.data)
            })
    }
})