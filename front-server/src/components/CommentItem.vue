<template>
  <div class="container mt-3">
    <div class="d-block">
      <div class="d-flex">
        <router-link
          :to="{ name: 'ProfileView', params: { userid: comment.username } }"
          class=""
          style="color: white; text-decoration: none"
        >
          {{ comment.nickname }}
        </router-link>
        <p v-if="!isEditing" class="ms-2" style="color: white">
          : {{ comment.content }}
        </p>
        <div class="ms-3">
          <div
            v-if="
              comment.username === this.$store.state.currentUser.username &&
              !isEditing
            "
          >
            <button
              class="mx-2 btn btn-sm btn-success waves-effect"
              @click="Switch"
            >
              수정
            </button>
            <button
              class="btn btn-sm btn-danger waves-effect"
              @click="deleteComment"
            >
              삭제
            </button>
          </div>
          <div v-if="isEditing">
            <input
              type="text"
              v-model="payload.content"
              @keyup.enter="Update"
            />
            <button
              class="mx-2 btn btn-sm btn-success waves-effect"
              @click="Update"
            >
              수정
            </button>
            |
            <button
              class="mx-2 btn btn-sm btn-secondary waves-effect"
              @click="Switch"
            >
              취소
            </button>
          </div>
        </div>

        <!-- <li>{{comment.id}}번 댓글 : {{comment.content}}  작성자 :{{comment.username}} -->
        <!-- <form @submit.prevent="deleteComment">
        <input type="submit" value="삭제">
      </form> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentItem",
  props: {
    comment: Object,
  },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.id,
        content: this.comment.content,
      },
    };
  },
  computed: {
    id() {
      return `str${this.comment.id}`;
    },
  },
  methods: {
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/comments/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$emit("getcomment");
          // console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Switch() {
      this.isEditing = !this.isEditing;
    },
    Update() {
      this.updateComment(this.payload);
      this.isEditing = false;
    },

    updateComment(data) {
      const content = data.content;
      // console.log(content);
      axios({
        method: "put",
        url: `${API_URL}/api/v1/comments/${data.commentPk}/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$emit("getcomment");
          // console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    CommentInput() {
      const content = this.comment.content;
      const id = this.comment.id;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/articles/${id}/comments/`,
        data: `${content}`,
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
  },
};
</script>

<style scoped>
.up {
  display: none;
}
input {
  border-block-color: red;
}
</style>
