<template>
  <div>
    <el-container>
      <el-header>
        <teacher-header></teacher-header>
      </el-header>
      <el-main style="overflow-y: hidden;">
        <el-row type="flex" justify="center">
          <el-col :xs="24" :sm="24" :md="22" :lg="22" :xl="22" >
            <teacher-content></teacher-content>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import TeacherHeader from '@/views/teacher/TeacherHeader.vue';
import TeacherContent from '@/views/teacher/TeacherContent.vue';

export default {
  name: 'TeacherView',
  components: {
    TeacherHeader,
    TeacherContent,
  },
};
</script>

<style scoped>

.el-header {
  padding: 0 !important;
  border-bottom: 1px solid #eeeeee;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

</style>
