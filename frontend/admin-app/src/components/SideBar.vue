<template>
  <div class="list">
    <div v-for="item in list" :key="item.name">
      <router-link :to="item.link" class="link">
        <el-card class="list-item"
          :class="$route.name === item.link ? 'is-always-shadow active' : ''"
          align="center" shadow="hover">
            {{ item.name }}
        </el-card>
      </router-link>
    </div>
    <div>
      <el-card class="list-item"
        align="center" shadow="hover">
          <a :href="`/course/${$route.params.cid}/home`" target="blank" :underline="false">
            课程主页
          </a>
      </el-card>
      <el-card class="list-item"
        align="center" shadow="hover">
          <a :href="`/proans/course/${$route.params.cid}`" target="blank"
            :underline="false">
            答疑系统
          </a>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
  data() {
    return {
      list: [
        {
          name: '助教管理',
          link: 'assistants',
        },
        {
          name: '学生管理',
          link: 'students',
        },
        {
          name: '课程简介',
          link: 'intro',
        },
        {
          name: '课程公告',
          link: 'announce',
        },
        {
          name: '课程日历',
          link: 'schedule',
        },
      ],
      current: this.$route.name,
    };
  },
  methods: {
    testRouter() {
      console.log(this.$route);
    },
  },
};
</script>

<style scoped>
.list {
  width: 200px;
  margin-right: 30px;
  margin-top:20px;
}
.active {
  background-color: #ecf5ff;
  color: #409eff;
}
.list-item {
  margin-bottom: 25px;
}
.list-item :hover {
  background: rgba(250, 250, 250, .8);
}
.link {
  text-decoration: none;
  color: #303133;
}
a {
  text-decoration: none;
  color: #303133;
}
a :hover :active{
  color: #409eff;
}
</style>
