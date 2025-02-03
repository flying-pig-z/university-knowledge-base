<meta name="referrer" content="no-referrer"/>

## 一.前端MVVC
前端的 MVVM 模式（Model-View-ViewModel）是一种软件架构设计模式，用于分离前端应用程序中的数据逻辑和用户界面。它主要通过 **Model（模型）、View（视图）和 ViewModel（视图模型）**三者之间的协作来实现数据与视图的双向绑定，简化界面更新和用户交互。以下是各部分的定义和作用：

**1.Model（模型）**: 负责处理与应用程序业务逻辑相关的数据部分。它包括应用程序的核心数据和状态，通常从服务器获取或存储在本地。Model 不关心用户界面，只负责处理业务逻辑。

相当于Vue中的script标签

**2.View（视图）**: 负责展示数据，即用户界面部分。它仅仅是 Model 数据的表现形式，不包含业务逻辑。前端的 View 通常是页面，通过绑定的数据动态展示 Model 的状态。

就相当于Vue中的<template>和<style>

**3.ViewModel（视图模型）**: 充当 View 和 Model 之间的中介，它负责处理用户交互逻辑并将其转化为对 Model 的更新，同时将 Model 的变化同步到 View。ViewModel 是关键部分，它通过双向数据绑定使 Model 和 View 保持同步，避免手动更新视图。

**MVVM的特点:**

+ **双向数据绑定**: View 和 ViewModel 之间的数据是双向绑定的，一个修改就会影响另一个。就拿Vue举例，template中数据的修改会影响script中数据的修改。
+ **分离关注点**: MVVM 模式将界面和业务逻辑解耦，降低了代码复杂性，使得代码更具可维护性和可扩展性。
+ **响应式更新**: 当 Model 发生变化时，View 会自动更新，不需要手动操作 DOM。

## 二.Vue中的script
一般为如下格式：

```plain
<script>
    export default {
      data() {
        return {
          count: 0
        };
      },
      methods: {
        increment() {
          this.count++;
        }
      }
    };
</script>
```

### 1.export default
+ **用途**: 将这个 Vue 组件的定义作为默认导出，允许其他文件导入它。
+ **意义**: export default的作用是将这个完整的 Vue 组件导出，供其他模块（如主应用或其他组件）使用。当其他模块引入这个文件时，不需要使用大括号（{}），可以直接指定一个名称来使用这个组件。

```plain
import Register from "../pages/Register";
```

### 2.data函数
+ data 函数的作用是定义并初始化组件的状态数据。
+ 这个函数在组件实例化时被调用，返回的对象会被合并到组件实例中，成为响应式数据。
+ script中可以使用 this 可以访问这些数据。template中使用v-model之类的指令将便签中的数据与data中的变量绑定。

### 3.methods和computed
methods通常与事件绑定（如点击事件）搭配使用，主要用于执行操作。

而computed是基于组件的响应式数据，自动更新并缓存计算结果，适合处理依赖数据的派生状态。

简单来说，methods是**主动执行**的函数，而computed是**被动计算**的属性，只有在依赖的数据变化时才会重新计算。

**一般我们有某个时间的时候，就根据事件进入methods或computed代码块处理，然后利用data中的双向数据绑定的特性，获取数据进行对应的处理，然后修改数据或样式来完成原来页面的渲染更改。**

## 三.Vue中的template
相当于html，可以直接引入其他组件

## 四.Vue中的style
相当于css，一般组件化化开发的时候（比如使用elementUI），会加上scoped解决样式冲突

默认情况写在组件中的样式会 **全局生效** → 因此很容易造成多个组件之间的样式冲突问题。

1. **全局样式**: 默认组件中的样式会作用到全局，任何一个组件中都会受到此样式的影响
2. **局部样式**: 可以给组件加上**scoped** 属性,可以**让样式只作用于当前组件**

## 五.main.js
```plain
import Vue from 'vue' 
import App from './App.vue' 
import VueRouter from 'vue-router' 
import router from './router' 
import ElementUI from 'element-ui' 
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false Vue.use(ElementUI) Vue.use(VueRouter) 
new Vue({   
    render: h => h(App),  
    router, 
}).$mount('#app')
```

这个 `main.js` 文件是 Vue.js 项目中的入口文件，主要用于初始化和配置整个应用。

### 1.引入依赖
```plain
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
```

+ Vue: 引入Vue框架，核心的JavaScript框架，驱动整个应用的逻辑和界面渲染。
+ App.vue: 根组件，它是Vue应用的起点，通常包含整个应用的布局和结构。
+ VueRouter: 引入 vue-router 用于管理路由，即页面之间的导航和切换。
+ router: 从 ./router 中导入自定义的路由配置，管理不同 URL 对应的组件。
+ ElementUI: 引入Element UI组件库
+ theme-chalk/index.css: Element UI 的默认主题样式文件，用于为组件提供样式。

### 2.关闭生产模式的提示
```plain
Vue.config.productionTip = false
```

这行代码会关闭 Vue 在生产环境中的提示信息，避免在生产环境中显示不必要的警告。

### 3.安装插件
```plain
Vue.use(ElementUI)
Vue.use(VueRouter)
```

Vue.use(ElementUI): 注册 Element UI，使其全局可用，方便在各个组件中使用 Element UI 提供的 UI 组件。 

Vue.use(VueRouter): 注册 VueRouter，用于管理应用的路由。

### 4.创建 Vue 实例
```plain
new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
```

+ render: h => h(App): 渲染 App.vue 组件作为整个应用的根组件。
+ router: 将之前导入的路由配置关联到 Vue 实例中，使应用具备路由功能。
+ .$mount('#app'): 挂载 Vue 实例到 #app DOM 元素上，整个应用会在这个元素内渲染。

**总结**： 这个 main.js 文件是 Vue 项目启动的核心配置文件，负责引入 Vue 框架、路由配置和 UI 库（Element UI），并通过根组件 App.vue 渲染整个应用。

## 六.定义路由--index.js
```plain
import VueRouter from "vue-router";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Home from "../pages/Home";
import HomePart from "../components/HomePart";
import Student from "../components/Student";
import RollCall from "../components/RollCall";
import Question from "../components/Question";
export default new VueRouter({
    mode: 'history',
    routes: [{
        path: '/login',
        component: Login
    },
    {
        path: '/register',
        component: Register
    },
    {
        path: '/',
        component: Home,
        children: [
            {
                path: 'home',
                component: HomePart
            },
            {
                path: 'student',
                component: Student
            },
            {
                path: 'roll-call',
                component: RollCall
            },
            {
                path: '/question',
                name: 'question',
                component: Question, // 这是你的组件
            }

        ],
        redirect: '/home'

    }
    ]
})
```

