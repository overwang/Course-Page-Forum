<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card class="box-card">
          <div id="course-info" class="card-content">
            <div id="course-name">
              <h1>{{ courseInfo.name_zh }}</h1>
              <p>{{ courseInfo.name_en }}</p>
              <p>{{ courseInfo.semester }}</p>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="box-card">
          <div id="course-name">
            <h1>问题统计</h1>
            <p>问题数：{{ problemsNum }}</p>
            <p>标签数：{{ tagsNum }}</p>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-row>
      <el-card>
        <div class="block">
          <el-carousel height="300px">
            <el-carousel-item v-for="item in text" :key="item">
              <h1 class="small">{{ item }}</h1>
            </el-carousel-item>
          </el-carousel>
        </div>
      </el-card>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'GuideView',
  computed: {
    text() {
      if (this.$store.getters.allProblems.length === 0) {
        return ['暂时没有问题噢，点击左侧添加问题'];
      }
      return [
        '顶部可选择问题所属分类',
        '选择分类后可在左侧点击对应问题显示',
        '左侧顶部有查询框，可用来查询问题',
        '新建问题请点击左侧加号',
      ];
    },
    problemsNum() {
      return this.$store.state.problems.length;
    },
    tagsNum() {
      return this.$store.state.tags.length;
    },
    courseInfo() {
      document.title = `${this.$store.state.courseInfo.name_zh}-${this.$store.state.courseInfo.semester}-答疑平台`;
      return this.$store.state.courseInfo;
    },
  },
  beforeMount() {
    this.$store.commit({
      type: 'setCid',
      id: Number(this.$route.params.cid),
    });
    this.$store.dispatch('initProblems');
    this.$store.dispatch('getCourseInfo');
  },
};
</script>

<style scoped>
.el-carousel__item h1 {
  color: #475669;
  font-size: 20px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #effaff;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #ecf5ff;
}

.el-carousel__item {
  display: flex;
  justify-content: center;
  align-items: center;
}

#course-name {
  display: flex;
  flex-direction: column;
  height: 250px;
  justify-content: center;
  align-items: center;
}
#course-name > h1 {
  margin-bottom: 10px;
  font-size: 30px;
}

.box-card {
  height: 300px;
}

.text {
  font-size: 24px;
  font-weight: 500;
}
.el-row {
  margin-bottom: 20px;
}
.card-content {
}
</style>
