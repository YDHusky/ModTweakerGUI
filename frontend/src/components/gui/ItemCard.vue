<script setup lang="ts">

import ItemButton from "@/components/element/ItemButton.vue";
import {ref} from "vue";
let data = ref('')
</script>

<template>
  <div class="item-card-warp">
    <div class="item-card-search">
      <input v-model="data"/>
    </div>
    <div class="item-card-list">
      <ItemButton v-for="i in 45"></ItemButton>
    </div>
  </div>
</template>

<style scoped>
.item-card-warp {
  width: 597px;
  height: 418px;
  background-size: 100% 100%;
  background-image: url("@/assets/gui/item_card.png");
  .item-card-search{
    width: 265px;
    margin-left: 250px;
    input{
      width: 100%;
      margin: 12px auto auto auto;
      height: 35px;
      background-color: rgba(0,0,0,0);
      border: none;
      outline: none;
      color: white;
      font-size: 20px;
    }
  }
  .item-card-list{
    width: 100%;
    padding-left: 27px;
    margin-top: 9px;
    padding-right: 54px;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    .item-button{
      margin: 3px;
    }
  }
}
</style>