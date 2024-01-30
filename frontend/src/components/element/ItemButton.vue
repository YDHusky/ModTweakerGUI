<script setup lang="ts">
import {ref} from "vue";

const item_url = ref("https://i.mcmod.cn/item/icon/128x128/0/1.png?v=16")
</script>

<template>
  <div class="item-button">
    <el-image :src="item_url" fit="cover"></el-image>
  </div>
</template>

<style>
.item-button{
  padding: 5px;
  width: 48px;
  height: 48px;
  border-radius: 5px;
  background-color: rgba(0, 0, 0, 0);
  .el-image{

    width: 100%;
    height: 100%;
    border-radius: 5px;
  }
}

</style>