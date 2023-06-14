<template>
  <div>
    
    <h1>LOGOUT 되었습니다</h1>


  </div>
</template>

<script>
export default {
    name : 'LogOutView',
    methods : {
      logout() {
        // console.log(123)
          this.$store.dispatch('logout')
      }
    },
    created() {
      // console.log(123)
        this.logout()
        // this.$router.push({name:'LogInView'})
    }
}
</script>

<style scoped>

</style>