<template>
  <div class="entire">
    <p class="test"><span>페이지를 찾을 수 없습니다!</span></p>
    <img src="../final_logo.png" alt="" style="padding-left: 17%" />
  </div>
</template>

<script>
export default {};
</script>

<style>
.entire {
  background-color: black;
  height: 100vh;
  width: 100vw;
}

.test {
  display: inline-block;
  margin: 50px auto 0;
  /* padding: 15% 10% 5% 5%; */

  font-family: "Roboto", sans-serif;
  /* background: #fff; */
  font-size: 150px;
  font-weight: 700;
  text-align: center;
  cursor: pointer;
  user-select: none;
}

.test span {
  background: linear-gradient(to right, #fbcac9, #8ca6ce);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
