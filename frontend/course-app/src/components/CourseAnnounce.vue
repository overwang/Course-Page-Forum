<template>
  <div class="course-announcement">
    <!-- This is CourseAnnounce view. -->
    <el-scrollbar>
      <div v-if="announces && announces.length > 0"
        shadow="always" class="announcement-card">
        <el-row :gutter="20" style="width: 100%">
          <el-col :span="6">
            <div class="announcement-info">
              <h3 class="announcement-title">{{ announces[0].title }}</h3>
              <div class="announcement-publish-info">
                发布者：{{ announces[0].author.name || announces[0].author.nickname }}
              </div>
              <div class="announcement-publish-info">
                发布时间：{{ (new Date(announces[0].create_datetime))
                  .toLocaleString('zh-CN', { hour12: false }) }}
              </div>
            </div>
          </el-col>
          <el-col :span="18">
            <div class="announcement-content">
              {{ announces[0].content }}
            </div>
          </el-col>
        </el-row>
      </div>
      <div v-else>
        <el-card class="box-card" shadow="hover">
        暂时还没有公告哦～
        </el-card>
      </div>
      <div v-if="announces && announces.length > 1"
        :class="{'announcements-panel-active': this.isActive,
        'announcements-panel-close': !this.isActive}"
        :style="(isActive) ? 'height:' + (announces.length - 1) * 93 + 'px' : ''">
        <div v-show="isActive" v-for="item in announces.slice(1)" :key="item.title"
          shadow="always" class="announcement-card">
          <el-row :gutter="20" style="width: 100%">
            <el-col :span="6">
              <div class="announcement-info">
                <h3 class="announcement-title">{{ item.title }}</h3>
                <div class="announcement-publish-info">
                  发布者：{{ item.author.name || announces[0].author.nickname }}
                </div>
                <div class="announcement-publish-info">
                  发布时间：{{ (new Date(item.create_datetime))
                    .toLocaleString('zh-CN', { hour12: false }) }}
                </div>
              </div>
            </el-col>
            <el-col :span="18">
              <div class="announcement-content">
                {{ item.content }}
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-scrollbar>
    <el-button v-if="announces && announces.length > 1"
      @click="onClick" class="btn-more">
      <i :class="isActive ? 'el-icon-caret-top' : 'el-icon-caret-bottom'"></i>
      <span>{{ btnMassage }}</span>
    </el-button>
  </div>
</template>

<script>
export default {
  name: 'CourseAnnounce',
  props: {
    allinfo: {},
  },
  data() {
    return {
      isActive: false,
      btnMassage: 'More',
    };
  },
  methods: {
    onClick() {
      if (this.isActive === false) {
        this.isActive = true;
        this.btnMassage = 'Pack up';
      } else {
        this.isActive = false;
        this.btnMassage = 'More';
      }
    },
  },
  computed: {
    announces() {
      const announces = [];
      if (this.allinfo.announces !== undefined) {
        this.allinfo.announces.forEach((announce) => {
          announces.push(announce);
        });
      }
      announces.sort((a, b) => {
        if (a.create_datetime > b.create_datetime) {
          return -1;
        }
        if (a.create_datetime < b.create_datetime) {
          return 1;
        }
        return 0;
      });
      return announces;
    },
  },
};
</script>

<style scoped>

.el-scrollbar .el-scrollbar__wrap {
  max-height: 20em;
  overflow-x:hidden;
}

.el-scrollbar__wrap .el-scrollbar__view {
  height: 100%;
}

.course-announcement {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border: 1px solid #EBEEF5;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
}

.btn-more {
  width: 100%;
  margin: 0;
  background-color: #f9fafc;
  border: 0px;
}

.announcements-panel-active {
  margin: 0;
  width: 100%;
  transition: height .8s;
}

.announcements-panel-close {
  margin: 0;
  width: 100%;
  height: 0em;
  transition: height .8s;
}

.announcement-info {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 30px;
  width: 250px;
}

.more-announcements-header {
  font-weight:700;
  margin-left: 1em;
}

.announcement-card {
  margin: 2em 1em 0 1em;
  height: auto;
  display: flex;
  flex-direction: row;
  border-bottom: 1px solid #EBEEF5;
}

.announcement-title {
  margin: 0 1em;
}

.announcement-publish-info {
 font-weight:200;
 font-size: 14px;
 display: flex;
}

.announcement-content {
  display: flex;
  font-size: 1em;
  margin: 0 1em;
  padding-bottom: 2em;
}

</style>
