import echarts from 'echarts'
import china from 'china/china.json'  //此处填上面内容创建的china.json文件的路径
Vue.prototype.$echarts = echarts
echarts.registerMap('china', china)
