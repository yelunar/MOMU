<template>

    <div class="card h-100">
      <img :src="this.result?.poster_path" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{this.result?.title}}</h5>
        <p class="card-text">asd</p>
      </div>
    </div>



</template>

<script>
export default {
    name:'searchResult',
    props:{
        result:Array,
    }
}
</script>

<style scoped>

</style>