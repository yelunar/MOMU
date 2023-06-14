<template>
  <div class="entire1" style="padding-top: 3%">
    <input
      type="text"
      placeholder="이 리뷰 어때요? 한 마디 남겨주세요 :)"
      style="
        width: 80%;
        height: 9%;
        background-color: rgba(255, 255, 255, 0.826);
        padding-left: 1%;
      "
      @keyup.enter="CommentInput"
      v-model="content"
    />
    <button
      type="submit"
      value="logIn"
      class="CommentInput"
      style="
        color: white;
        border: none;
        height: 9%;
        width: 5%;
        border-radius: 10%;
        background-color: #198754;
      "
      @click.prevent="CommentInput"
    >
      제출
    </button>

    <!-- <ul v-for="comment in comments" :key="comment.id"><li>{{comment?.id}}번 댓글 {{comment?.content}}</li></ul> -->
    <div
      class=""
      style="position: absolute; left: 15%; width: 600px; height: 300px"
    >
      <CommentItem
        class="ms-1"
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
        @getcomment="CommentGet"
      />
    </div>
  </div>
</template>

<script>
import CommentItem from "@/components/CommentItem";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentList",
  props: {
    id: String,
  },
  components: {
    CommentItem,
  },
  data() {
    return {
      content: "",
      comments: null,
    };
  },
  created() {
    this.CommentGet();
  },
  methods: {
    CommentInput() {
      const content = this.content;
      const id = this.id;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/articles/${id}/comments/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log(res);
          this.CommentGet();
          this.content = "";
          // this.$router.push({name:'DetailView', params : {id:id}})
        })
        .catch((err) => {
          console.log(err);
        });
    },
    CommentGet() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.id}/comments/`,
      }).then((res) => {
        this.comments = res.data;
        // console.log(res.data);
      });
    },
  },
};
</script>

<style scoped>
.entire1 {
  padding: 0;
  width: 100%;
  height: 100vh;
  margin-top: 0%;
}

input {
  border-block-color: rgb(31, 172, 238);
}

/* * {
  position: absolute left 30%;
} */
</style>
